

# CaptureDescription

Properties to configure capture description for eventhub

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**Destination**](Destination.md) |  |  [optional] |
|**enabled** | **Boolean** | A value that indicates whether capture description is enabled.  |  [optional] |
|**encoding** | [**EncodingEnum**](#EncodingEnum) | Enumerates the possible values for the encoding format of capture description. |  [optional] |
|**intervalInSeconds** | **Integer** | The time window allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds |  [optional] |
|**sizeLimitInBytes** | **Integer** | The size window defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 and 524288000 bytes |  [optional] |



## Enum: EncodingEnum

| Name | Value |
|---- | -----|
| AVRO | &quot;Avro&quot; |
| AVRO_DEFLATE | &quot;AvroDeflate&quot; |



