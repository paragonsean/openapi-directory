

# SendDebugCaptureRequest

Request to send encoded debug information. Next ID: 8

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**componentId** | **String** | The internal component id for which debug information is sent. |  [optional] |
|**data** | **String** | The encoded debug information. |  [optional] |
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | Format for the data field above (id&#x3D;5). |  [optional] |
|**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id. |  [optional] |
|**workerId** | **String** | The worker id, i.e., VM hostname. |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| DATA_FORMAT_UNSPECIFIED | &quot;DATA_FORMAT_UNSPECIFIED&quot; |
| RAW | &quot;RAW&quot; |
| JSON | &quot;JSON&quot; |
| ZLIB | &quot;ZLIB&quot; |
| BROTLI | &quot;BROTLI&quot; |



