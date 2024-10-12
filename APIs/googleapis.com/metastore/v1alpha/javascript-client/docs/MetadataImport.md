# DataprocMetastoreApi.MetadataImport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the metadata import was started. | [optional] [readonly] 
**databaseDump** | [**DatabaseDump**](DatabaseDump.md) |  | [optional] 
**description** | **String** | The description of the metadata import. | [optional] 
**endTime** | **String** | Output only. The time when the metadata import finished. | [optional] [readonly] 
**name** | **String** | Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}. | [optional] 
**state** | **String** | Output only. The current state of the metadata import. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the metadata import was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `UPDATING` (value: `"UPDATING"`)

* `FAILED` (value: `"FAILED"`)




