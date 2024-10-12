# BigQueryApi.BigLakeConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionId** | **String** | Required. The connection specifying the credentials to be used to read and write to external storage, such as Cloud Storage. The connection_id can have the form \&quot;&lt;project\\_id&gt;.&lt;location\\_id&gt;.&lt;connection\\_id&gt;\&quot; or \&quot;projects/&lt;project\\_id&gt;/locations/&lt;location\\_id&gt;/connections/&lt;connection\\_id&gt;\&quot;. | [optional] 
**fileFormat** | **String** | Required. The file format the table data is stored in. | [optional] 
**storageUri** | **String** | Required. The fully qualified location prefix of the external folder where table data is stored. The &#39;*&#39; wildcard character is not allowed. The URI should be in the format \&quot;gs://bucket/path_to_table/\&quot; | [optional] 
**tableFormat** | **String** | Required. The table format the metadata only snapshots are stored in. | [optional] 



## Enum: FileFormatEnum


* `FILE_FORMAT_UNSPECIFIED` (value: `"FILE_FORMAT_UNSPECIFIED"`)

* `PARQUET` (value: `"PARQUET"`)





## Enum: TableFormatEnum


* `TABLE_FORMAT_UNSPECIFIED` (value: `"TABLE_FORMAT_UNSPECIFIED"`)

* `ICEBERG` (value: `"ICEBERG"`)




