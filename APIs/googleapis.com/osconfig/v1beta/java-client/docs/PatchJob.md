

# PatchJob

A high level representation of a patch job that is either in progress or has completed. Instance details are not included in the job. To paginate through instance details, use `ListPatchJobInstanceDetails`. For more information about patch jobs, see [Creating patch jobs](https://cloud.google.com/compute/docs/os-patch-management/create-patch-job).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Time this patch job was created. |  [optional] |
|**description** | **String** | Description of the patch job. Length of the description is limited to 1024 characters. |  [optional] |
|**displayName** | **String** | Display name for this patch job. This is not a unique identifier. |  [optional] |
|**dryRun** | **Boolean** | If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance. |  [optional] |
|**duration** | **String** | Duration of the patch job. After the duration ends, the patch job times out. |  [optional] |
|**errorMessage** | **String** | If this patch job failed, this message provides information about the failure. |  [optional] |
|**instanceDetailsSummary** | [**PatchJobInstanceDetailsSummary**](PatchJobInstanceDetailsSummary.md) |  |  [optional] |
|**instanceFilter** | [**PatchInstanceFilter**](PatchInstanceFilter.md) |  |  [optional] |
|**name** | **String** | Unique identifier for this patch job in the form &#x60;projects/_*_/patchJobs/_*&#x60; |  [optional] |
|**patchConfig** | [**PatchConfig**](PatchConfig.md) |  |  [optional] |
|**patchDeployment** | **String** | Output only. Name of the patch deployment that created this patch job. |  [optional] [readonly] |
|**percentComplete** | **Double** | Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete. |  [optional] |
|**rollout** | [**PatchRollout**](PatchRollout.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the PatchJob. |  [optional] |
|**updateTime** | **String** | Last time this patch job was updated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| STARTED | &quot;STARTED&quot; |
| INSTANCE_LOOKUP | &quot;INSTANCE_LOOKUP&quot; |
| PATCHING | &quot;PATCHING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| COMPLETED_WITH_ERRORS | &quot;COMPLETED_WITH_ERRORS&quot; |
| CANCELED | &quot;CANCELED&quot; |
| TIMED_OUT | &quot;TIMED_OUT&quot; |



