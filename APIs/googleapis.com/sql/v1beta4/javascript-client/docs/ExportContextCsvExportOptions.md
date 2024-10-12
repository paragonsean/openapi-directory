# CloudSqlAdminApi.ExportContextCsvExportOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escapeCharacter** | **String** | Specifies the character that should appear before a data character that needs to be escaped. | [optional] 
**fieldsTerminatedBy** | **String** | Specifies the character that separates columns within each row (line) of the file. | [optional] 
**linesTerminatedBy** | **String** | This is used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values. | [optional] 
**quoteCharacter** | **String** | Specifies the quoting character to be used when a data value is quoted. | [optional] 
**selectQuery** | **String** | The select query used to extract the data. | [optional] 


