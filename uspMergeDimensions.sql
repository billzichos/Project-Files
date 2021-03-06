USE [COPTDW]
GO
/****** Object:  StoredProcedure [dbo].[uspMergeDimensions]    Script Date: 01/14/2015 08:54:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROC [dbo].[uspMergeDimensions] 
	(@tableName varchar(128),
	 @altKey1 varchar(128),
	 @altKey2 varchar(128),
	 @altKey3 varchar(128),
	 @sourceServer varchar(128),
	 @sourceDb varchar(128))
AS

BEGIN



/*--------------------------------------------------------------------------------------------------------------
BASED ON THE INPUTS, FIND THE NON-KEY AND NON-AUDIT RELATED FIELDS.  APPLY SOME FORMATTING TO THE FIELDS AND 
SAVE IN VARIABLES
----------------------------------------------------------------------------------------------------------------*/

DECLARE @insertFields varchar(max)
DECLARE @updateFields varchar(max)
DECLARE @updateSearchCondition varchar(max)

SELECT
 @insertFields = IsNull(@insertFields + ', ', '') + '[' + COLUMN_NAME + ']',
 @updateFields = ISNULL(@updateFields + ', ', '') + 'T.[' + COLUMN_NAME + '] = S.[' + COLUMN_NAME + ']',
 @updateSearchCondition = ISNULL(@updateSearchCondition + ' OR ', '') + 'T.[' + COLUMN_NAME + '] <> S.[' + COLUMN_NAME + ']'
FROM information_schema.columns
WHERE TABLE_NAME = @tableName
AND COLUMN_NAME <> 'CreatedBy'
AND COLUMN_NAME <> 'CreatedDT'
AND COLUMN_NAME <> 'UpdatedBy'
AND COLUMN_NAME <> 'UpdatedDT'
AND COLUMN_NAME NOT IN (SELECT name FROM sys.columns WHERE is_identity = 1 AND OBJECT_NAME(object_id) = @tableName)



/*----------------------------------------------------------------------------------------------------------------
USING THE INPUTS TO THE STORED PROCEDURE, PLUS THE VARIABLES COLLECTED IN PREVIOUS STEP, START BUILDING THE SQL
STATEMENT WITH PLACEHOLDERS.
------------------------------------------------------------------------------------------------------------------*/

DECLARE @SQL varchar(max)

SET @SQL =
	'
	MERGE [test-sql1].[COPTDW].dbo.<TARGET_TABLE> AS T
		USING <SOURCE_SERVER>.<SOURCE_DB>.dbo.vwCOPTDW_<SOURCE_TABLE> AS S
		ON (<ALT_KEYSTRING>)
		 WHEN MATCHED
			AND (<CLAUSE_SEARCH_CONDITION>)
			THEN UPDATE SET <UPDATE_FIELDS>, T.UpdatedBy = ''<ETL_NAME>'', T.UpdatedDT = GetDate()
		  WHEN NOT MATCHED BY TARGET
			THEN INSERT (<INSERT_FIELDS>, CreatedBy, CreatedDT) VALUES (<INSERT_FIELDS>, ''<ETL_NAME>'', GetDate())
		  WHEN NOT MATCHED BY SOURCE
			THEN UPDATE SET T.isActiveFlag = 0, T.UpdatedBy = ''<ETL_NAME>'', T.UpdatedDT = GetDate();
	'



/*---------------------------------------------------------------------------------------------------------
BUILD THE ALTERNATE KEY STRING DEPENDING ON THE INPUT VALUES
---------------------------------------------------------------------------------------------------------*/
DECLARE @altString varchar(max)

BEGIN
IF ISNULL(@altKey1, '') = ''
	SET @altString = @altString
ELSE
	SET @altString = 'T.' + @altKey1 + ' = S.' + @altKey1 + ' AND '
END

BEGIN
IF ISNULL(@altKey2, '') = ''
	SET @altString = @altString
ELSE
	SET @altString = @altString + 'T.' + @altKey2 + ' = S.' + @altKey2 + ' AND '
END

BEGIN
IF ISNULL(@altKey3, '') = ''
	SET @altString = @altString
ELSE
	SET @altString = @altString + 'T.' + @altKey3 + ' = S.' + @altKey3
END

BEGIN
IF RIGHT(RTRIM(@altString), 4) = ' AND'
	SET @altString = SUBSTRING(@altString,1,LEN(@altString)-4)
END



/*---------------------------------------------------------------------------------------------------------
REPLACE THE PLACEHOLDERS WITH ACTUAL VALUES IN PREPARATION FOR EXECUTING THE SQL STATEMENT.
----------------------------------------------------------------------------------------------------------*/

SET @SQL = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(@SQL, '<TARGET_TABLE>', IsNull(@tableName,'')), '<SOURCE_SERVER>', IsNull(@sourceServer,'')), '<SOURCE_DB>', IsNull(@sourceDb, '')), '<SOURCE_TABLE>', IsNull(@tableName,'')), '<ALT_KEYSTRING>', IsNull(@altString,'')), '<ETL_NAME>', IsNull(@tableName,'') + ' ETL'), '<UPDATE_FIELDS>', IsNull(@updateFields,'')), '<INSERT_FIELDS>', IsNull(@insertFields,'')), '<CLAUSE_SEARCH_CONDITION>', ISNULL(@updateSearchCondition,''))



/*--------------------------------------------------------------------------------------------
EXECUTE THE SQL STATEMENT
*/--------------------------------------------------------------------------------------------

EXEC (@SQL)
--print(@SQL)

END

--execute dbo.uspMergeDimensions 'LeaseDim', 'LeaseCode', NULL, AltKey3, '[test-sql1]', '[INSIGHT_X]'
--EXEC dbo.uspMergeDimensions 'VendorDim', 'VndrCode', NULL, NULL, '[test-sql1]', '[EtlStage]'
--EXEC dbo.uspMergeDimensions 'FinancialProjectDim', 'FinProjectCode', NULL, NULL, '[test-sql1]', '[EtlStage]'
--EXEC dbo.uspMergeDimensions 'DimJob', 'CTIJobCode', NULL, NULL, '[test-sql1]', '[ETLStage]'