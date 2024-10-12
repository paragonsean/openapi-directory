

# LiveOutputProperties

The JSON object that contains the properties required to create a Live Output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveWindowLength** | **String** | ISO 8601 timespan duration of the archive window length. This is duration that customer want to retain the recorded content. |  |
|**assetName** | **String** | The asset name. |  |
|**created** | **OffsetDateTime** | The exact time the Live Output was created. |  [optional] [readonly] |
|**description** | **String** | The description of the Live Output. |  [optional] |
|**hls** | [**Hls**](Hls.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | The exact time the Live Output was last modified. |  [optional] [readonly] |
|**manifestName** | **String** | The manifest file name.  If not provided, the service will generate one automatically. |  [optional] |
|**outputSnapTime** | **Long** | The output snapshot time. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the Live Output. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | The resource state of the Live Output. |  [optional] [readonly] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| RUNNING | &quot;Running&quot; |
| DELETING | &quot;Deleting&quot; |



