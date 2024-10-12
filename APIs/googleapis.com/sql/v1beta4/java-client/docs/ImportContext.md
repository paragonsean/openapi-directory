

# ImportContext

Database instance import context.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bakImportOptions** | [**ImportContextBakImportOptions**](ImportContextBakImportOptions.md) |  |  [optional] |
|**csvImportOptions** | [**ImportContextCsvImportOptions**](ImportContextCsvImportOptions.md) |  |  [optional] |
|**database** | **String** | The target database for the import. If &#x60;fileType&#x60; is &#x60;SQL&#x60;, this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. If &#x60;fileType&#x60; is &#x60;CSV&#x60;, one database must be specified. |  [optional] |
|**fileType** | [**FileTypeEnum**](#FileTypeEnum) | The file type for the specified uri. * &#x60;SQL&#x60;: The file contains SQL statements. * &#x60;CSV&#x60;: The file contains CSV data. * &#x60;BAK&#x60;: The file contains backup data for a SQL Server instance. |  [optional] |
|**importUser** | **String** | The PostgreSQL user for this import operation. PostgreSQL instances only. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#importContext&#x60;. |  [optional] |
|**uri** | **String** | Path to the import file in Cloud Storage, in the form &#x60;gs://bucketName/fileName&#x60;. Compressed gzip files (.gz) are supported when &#x60;fileType&#x60; is &#x60;SQL&#x60;. The instance must have write permissions to the bucket and read access to the file. |  [optional] |



## Enum: FileTypeEnum

| Name | Value |
|---- | -----|
| SQL_FILE_TYPE_UNSPECIFIED | &quot;SQL_FILE_TYPE_UNSPECIFIED&quot; |
| SQL | &quot;SQL&quot; |
| CSV | &quot;CSV&quot; |
| BAK | &quot;BAK&quot; |



