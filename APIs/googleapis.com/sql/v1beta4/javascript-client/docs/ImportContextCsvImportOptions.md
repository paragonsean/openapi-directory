# CloudSqlAdminApi.ImportContextCsvImportOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **[String]** | The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data. | [optional] 
**escapeCharacter** | **String** | Specifies the character that should appear before a data character that needs to be escaped. | [optional] 
**fieldsTerminatedBy** | **String** | Specifies the character that separates columns within each row (line) of the file. | [optional] 
**linesTerminatedBy** | **String** | This is used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values. | [optional] 
**quoteCharacter** | **String** | Specifies the quoting character to be used when a data value is quoted. | [optional] 
**table** | **String** | The table to which CSV data is imported. | [optional] 


