

# GoogleCloudHealthcareV1DicomBigQueryDestination

The BigQuery table where the server writes the output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**force** | **Boolean** | Use &#x60;write_disposition&#x60; instead. If &#x60;write_disposition&#x60; is specified, this parameter is ignored. force&#x3D;false is equivalent to write_disposition&#x3D;WRITE_EMPTY and force&#x3D;true is equivalent to write_disposition&#x3D;WRITE_TRUNCATE. |  [optional] |
|**tableUri** | **String** | BigQuery URI to a table, up to 2000 characters long, in the format &#x60;bq://projectId.bqDatasetId.tableId&#x60; |  [optional] |
|**writeDisposition** | [**WriteDispositionEnum**](#WriteDispositionEnum) | Determines whether the existing table in the destination is to be overwritten or appended to. If a write_disposition is specified, the &#x60;force&#x60; parameter is ignored. |  [optional] |



## Enum: WriteDispositionEnum

| Name | Value |
|---- | -----|
| DISPOSITION_UNSPECIFIED | &quot;WRITE_DISPOSITION_UNSPECIFIED&quot; |
| EMPTY | &quot;WRITE_EMPTY&quot; |
| TRUNCATE | &quot;WRITE_TRUNCATE&quot; |
| APPEND | &quot;WRITE_APPEND&quot; |



