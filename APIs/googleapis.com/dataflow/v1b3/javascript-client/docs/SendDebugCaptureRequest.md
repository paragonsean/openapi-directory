# DataflowApi.SendDebugCaptureRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**componentId** | **String** | The internal component id for which debug information is sent. | [optional] 
**data** | **String** | The encoded debug information. | [optional] 
**dataFormat** | **String** | Format for the data field above (id&#x3D;5). | [optional] 
**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id. | [optional] 
**workerId** | **String** | The worker id, i.e., VM hostname. | [optional] 



## Enum: DataFormatEnum


* `DATA_FORMAT_UNSPECIFIED` (value: `"DATA_FORMAT_UNSPECIFIED"`)

* `RAW` (value: `"RAW"`)

* `JSON` (value: `"JSON"`)

* `ZLIB` (value: `"ZLIB"`)

* `BROTLI` (value: `"BROTLI"`)




