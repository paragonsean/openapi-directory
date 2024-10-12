# CloudSqlAdminApi.ExportContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bakExportOptions** | [**ExportContextBakExportOptions**](ExportContextBakExportOptions.md) |  | [optional] 
**csvExportOptions** | [**ExportContextCsvExportOptions**](ExportContextCsvExportOptions.md) |  | [optional] 
**databases** | **[String]** | Databases to be exported. &#x60;MySQL instances:&#x60; If &#x60;fileType&#x60; is &#x60;SQL&#x60; and no database is specified, all databases are exported, except for the &#x60;mysql&#x60; system database. If &#x60;fileType&#x60; is &#x60;CSV&#x60;, you can specify one database, either by using this property or by using the &#x60;csvExportOptions.selectQuery&#x60; property, which takes precedence over this property. &#x60;PostgreSQL instances:&#x60; You must specify one database to be exported. If &#x60;fileType&#x60; is &#x60;CSV&#x60;, this database must match the one specified in the &#x60;csvExportOptions.selectQuery&#x60; property. &#x60;SQL Server instances:&#x60; You must specify one database to be exported, and the &#x60;fileType&#x60; must be &#x60;BAK&#x60;. | [optional] 
**fileType** | **String** | The file type for the specified uri. | [optional] 
**kind** | **String** | This is always &#x60;sql#exportContext&#x60;. | [optional] 
**offload** | **Boolean** | Option for export offload. | [optional] 
**sqlExportOptions** | [**ExportContextSqlExportOptions**](ExportContextSqlExportOptions.md) |  | [optional] 
**uri** | **String** | The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form &#x60;gs://bucketName/fileName&#x60;. If the file already exists, the request succeeds, but the operation fails. If &#x60;fileType&#x60; is &#x60;SQL&#x60; and the filename ends with .gz, the contents are compressed. | [optional] 



## Enum: FileTypeEnum


* `SQL_FILE_TYPE_UNSPECIFIED` (value: `"SQL_FILE_TYPE_UNSPECIFIED"`)

* `SQL` (value: `"SQL"`)

* `CSV` (value: `"CSV"`)

* `BAK` (value: `"BAK"`)




