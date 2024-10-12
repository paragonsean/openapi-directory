# DatastreamApi.GcsDestinationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avroFileFormat** | **Object** | AVRO file format configuration. | [optional] 
**fileRotationInterval** | **String** | The maximum duration for which new events are added before a file is closed and a new file is created. | [optional] 
**fileRotationMb** | **Number** | The maximum file size to be saved in the bucket. | [optional] 
**gcsFileFormat** | **String** | File format that data should be written in. Deprecated field (b/169501737) - use file_format instead. | [optional] 
**jsonFileFormat** | [**JsonFileFormat**](JsonFileFormat.md) |  | [optional] 
**path** | **String** | Path inside the Cloud Storage bucket to write data to. | [optional] 



## Enum: GcsFileFormatEnum


* `GCS_FILE_FORMAT_UNSPECIFIED` (value: `"GCS_FILE_FORMAT_UNSPECIFIED"`)

* `AVRO` (value: `"AVRO"`)




