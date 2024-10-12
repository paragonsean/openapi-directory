

# GoogleCloudHealthcareV1beta1FhirBigQueryDestination

The configuration for exporting to BigQuery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetUri** | **String** | BigQuery URI to an existing dataset, up to 2000 characters long, in the format &#x60;bq://projectId.bqDatasetId&#x60;. |  [optional] |
|**force** | **Boolean** | Use &#x60;write_disposition&#x60; instead. If &#x60;write_disposition&#x60; is specified, this parameter is ignored. force&#x3D;false is equivalent to write_disposition&#x3D;WRITE_EMPTY and force&#x3D;true is equivalent to write_disposition&#x3D;WRITE_TRUNCATE. |  [optional] |
|**schemaConfig** | [**SchemaConfig**](SchemaConfig.md) |  |  [optional] |
|**writeDisposition** | [**WriteDispositionEnum**](#WriteDispositionEnum) | Determines if existing data in the destination dataset is overwritten, appended to, or not written if the tables contain data. If a write_disposition is specified, the &#x60;force&#x60; parameter is ignored. |  [optional] |



## Enum: WriteDispositionEnum

| Name | Value |
|---- | -----|
| DISPOSITION_UNSPECIFIED | &quot;WRITE_DISPOSITION_UNSPECIFIED&quot; |
| EMPTY | &quot;WRITE_EMPTY&quot; |
| TRUNCATE | &quot;WRITE_TRUNCATE&quot; |
| APPEND | &quot;WRITE_APPEND&quot; |



