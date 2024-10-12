# ServiceBusManagementClient.CaptureDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**Destination**](Destination.md) |  | [optional] 
**enabled** | **Boolean** | A value that indicates whether capture description is enabled.  | [optional] 
**encoding** | **String** | Enumerates the possible values for the encoding format of capture description. | [optional] 
**intervalInSeconds** | **Number** | The time window allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds | [optional] 
**sizeLimitInBytes** | **Number** | The size window defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 and 524288000 bytes | [optional] 



## Enum: EncodingEnum


* `Avro` (value: `"Avro"`)

* `AvroDeflate` (value: `"AvroDeflate"`)




