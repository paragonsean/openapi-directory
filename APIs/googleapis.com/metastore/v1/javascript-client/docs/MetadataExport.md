# DataprocMetastoreApi.MetadataExport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseDumpType** | **String** | Output only. The type of the database dump. | [optional] [readonly] 
**destinationGcsUri** | **String** | Output only. A Cloud Storage URI of a folder that metadata are exported to, in the form of gs:////, where is automatically generated. | [optional] [readonly] 
**endTime** | **String** | Output only. The time when the export ended. | [optional] [readonly] 
**startTime** | **String** | Output only. The time when the export started. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the export. | [optional] [readonly] 



## Enum: DatabaseDumpTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `MYSQL` (value: `"MYSQL"`)

* `AVRO` (value: `"AVRO"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




