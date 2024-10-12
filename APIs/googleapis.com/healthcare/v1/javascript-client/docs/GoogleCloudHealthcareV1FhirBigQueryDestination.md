# CloudHealthcareApi.GoogleCloudHealthcareV1FhirBigQueryDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasetUri** | **String** | BigQuery URI to an existing dataset, up to 2000 characters long, in the format &#x60;bq://projectId.bqDatasetId&#x60;. | [optional] 
**force** | **Boolean** | If this flag is &#x60;TRUE&#x60;, all tables are deleted from the dataset before the new exported tables are written. If the flag is not set and the destination dataset contains tables, the export call returns an error. If &#x60;write_disposition&#x60; is specified, this parameter is ignored. force&#x3D;false is equivalent to write_disposition&#x3D;WRITE_EMPTY and force&#x3D;true is equivalent to write_disposition&#x3D;WRITE_TRUNCATE. | [optional] 
**schemaConfig** | [**SchemaConfig**](SchemaConfig.md) |  | [optional] 
**writeDisposition** | **String** | Determines if existing data in the destination dataset is overwritten, appended to, or not written if the tables contain data. If a write_disposition is specified, the &#x60;force&#x60; parameter is ignored. | [optional] 



## Enum: WriteDispositionEnum


* `DISPOSITION_UNSPECIFIED` (value: `"WRITE_DISPOSITION_UNSPECIFIED"`)

* `EMPTY` (value: `"WRITE_EMPTY"`)

* `TRUNCATE` (value: `"WRITE_TRUNCATE"`)

* `APPEND` (value: `"WRITE_APPEND"`)




