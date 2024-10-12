# OsConfigApi.PatchDeployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. | [optional] [readonly] 
**description** | **String** | Optional. Description of the patch deployment. Length of the description is limited to 1024 characters. | [optional] 
**duration** | **String** | Optional. Duration of the patch. After the duration ends, the patch times out. | [optional] 
**instanceFilter** | [**PatchInstanceFilter**](PatchInstanceFilter.md) |  | [optional] 
**lastExecuteTime** | **String** | Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. | [optional] [readonly] 
**name** | **String** | Unique name for the patch deployment resource in a project. The patch deployment name is in the form: &#x60;projects/{project_id}/patchDeployments/{patch_deployment_id}&#x60;. This field is ignored when you create a new patch deployment. | [optional] 
**oneTimeSchedule** | [**OneTimeSchedule**](OneTimeSchedule.md) |  | [optional] 
**patchConfig** | [**PatchConfig**](PatchConfig.md) |  | [optional] 
**recurringSchedule** | [**RecurringSchedule**](RecurringSchedule.md) |  | [optional] 
**rollout** | [**PatchRollout**](PatchRollout.md) |  | [optional] 
**state** | **String** | Output only. Current state of the patch deployment. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `PAUSED` (value: `"PAUSED"`)




