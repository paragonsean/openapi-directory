

# DownloadModelResponse

The response for downloading a model to device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadUri** | **String** | Output only. A download URI for the model/zip file. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The time that the download URI link expires. If the link has expired, the REST call must be repeated. |  [optional] [readonly] |
|**modelFormat** | [**ModelFormatEnum**](#ModelFormatEnum) | Output only. The format of the model being downloaded. |  [optional] [readonly] |
|**sizeBytes** | **String** | Output only. The size of the file(s), if this information is available. |  [optional] [readonly] |



## Enum: ModelFormatEnum

| Name | Value |
|---- | -----|
| MODEL_FORMAT_UNSPECIFIED | &quot;MODEL_FORMAT_UNSPECIFIED&quot; |
| TFLITE | &quot;TFLITE&quot; |



