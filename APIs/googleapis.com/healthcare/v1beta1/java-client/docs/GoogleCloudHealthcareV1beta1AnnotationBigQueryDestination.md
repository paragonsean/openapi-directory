

# GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination

The BigQuery table for export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**force** | **Boolean** | Use &#x60;write_disposition&#x60; instead. If &#x60;write_disposition&#x60; is specified, this parameter is ignored. force&#x3D;false is equivalent to write_disposition&#x3D;WRITE_EMPTY and force&#x3D;true is equivalent to write_disposition&#x3D;WRITE_TRUNCATE. |  [optional] |
|**schemaType** | [**SchemaTypeEnum**](#SchemaTypeEnum) | Specifies the schema format to export. |  [optional] |
|**tableUri** | **String** | BigQuery URI to a table, up to 2000 characters long, must be of the form bq://projectId.bqDatasetId.tableId. |  [optional] |
|**writeDisposition** | [**WriteDispositionEnum**](#WriteDispositionEnum) | Determines if existing data in the destination dataset is overwritten, appended to, or not written if the tables contain data. If a write_disposition is specified, the &#x60;force&#x60; parameter is ignored. |  [optional] |



## Enum: SchemaTypeEnum

| Name | Value |
|---- | -----|
| SCHEMA_TYPE_UNSPECIFIED | &quot;SCHEMA_TYPE_UNSPECIFIED&quot; |
| SIMPLE | &quot;SIMPLE&quot; |



## Enum: WriteDispositionEnum

| Name | Value |
|---- | -----|
| DISPOSITION_UNSPECIFIED | &quot;WRITE_DISPOSITION_UNSPECIFIED&quot; |
| EMPTY | &quot;WRITE_EMPTY&quot; |
| TRUNCATE | &quot;WRITE_TRUNCATE&quot; |
| APPEND | &quot;WRITE_APPEND&quot; |



