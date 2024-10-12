# NetworkConnectivityApi.Warnings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Output only. A warning code, if applicable. | [optional] [readonly] 
**data** | **{String: String}** | Output only. Metadata about this warning in key: value format. The key should provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be scope and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement. | [optional] [readonly] 
**warningMessage** | **String** | Output only. A human-readable description of the warning code. | [optional] [readonly] 



## Enum: CodeEnum


* `WARNING_UNSPECIFIED` (value: `"WARNING_UNSPECIFIED"`)

* `RESOURCE_NOT_ACTIVE` (value: `"RESOURCE_NOT_ACTIVE"`)

* `RESOURCE_BEING_MODIFIED` (value: `"RESOURCE_BEING_MODIFIED"`)




