

# GcsDestinationConfig

Google Cloud Storage destination configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avroFileFormat** | **Object** | AVRO file format configuration. |  [optional] |
|**fileRotationInterval** | **String** | The maximum duration for which new events are added before a file is closed and a new file is created. Values within the range of 15-60 seconds are allowed. |  [optional] |
|**fileRotationMb** | **Integer** | The maximum file size to be saved in the bucket. |  [optional] |
|**jsonFileFormat** | [**JsonFileFormat**](JsonFileFormat.md) |  |  [optional] |
|**path** | **String** | Path inside the Cloud Storage bucket to write data to. |  [optional] |



