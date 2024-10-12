# OsConfigApi.PatchJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Time this patch job was created. | [optional] 
**description** | **String** | Description of the patch job. Length of the description is limited to 1024 characters. | [optional] 
**displayName** | **String** | Display name for this patch job. This is not a unique identifier. | [optional] 
**dryRun** | **Boolean** | If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance. | [optional] 
**duration** | **String** | Duration of the patch job. After the duration ends, the patch job times out. | [optional] 
**errorMessage** | **String** | If this patch job failed, this message provides information about the failure. | [optional] 
**instanceDetailsSummary** | [**PatchJobInstanceDetailsSummary**](PatchJobInstanceDetailsSummary.md) |  | [optional] 
**instanceFilter** | [**PatchInstanceFilter**](PatchInstanceFilter.md) |  | [optional] 
**name** | **String** | Unique identifier for this patch job in the form &#x60;projects/_*_/patchJobs/_*&#x60; | [optional] 
**patchConfig** | [**PatchConfig**](PatchConfig.md) |  | [optional] 
**patchDeployment** | **String** | Output only. Name of the patch deployment that created this patch job. | [optional] [readonly] 
**percentComplete** | **Number** | Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete. | [optional] 
**rollout** | [**PatchRollout**](PatchRollout.md) |  | [optional] 
**state** | **String** | The current state of the PatchJob. | [optional] 
**updateTime** | **String** | Last time this patch job was updated. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `STARTED` (value: `"STARTED"`)

* `INSTANCE_LOOKUP` (value: `"INSTANCE_LOOKUP"`)

* `PATCHING` (value: `"PATCHING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `COMPLETED_WITH_ERRORS` (value: `"COMPLETED_WITH_ERRORS"`)

* `CANCELED` (value: `"CANCELED"`)

* `TIMED_OUT` (value: `"TIMED_OUT"`)




