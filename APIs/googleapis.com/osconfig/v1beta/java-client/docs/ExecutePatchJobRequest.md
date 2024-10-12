

# ExecutePatchJobRequest

A request message to initiate patching across Compute Engine instances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the patch job. Length of the description is limited to 1024 characters. |  [optional] |
|**displayName** | **String** | Display name for this patch job. This does not have to be unique. |  [optional] |
|**dryRun** | **Boolean** | If this patch is a dry-run only, instances are contacted but will do nothing. |  [optional] |
|**duration** | **String** | Duration of the patch job. After the duration ends, the patch job times out. |  [optional] |
|**instanceFilter** | [**PatchInstanceFilter**](PatchInstanceFilter.md) |  |  [optional] |
|**patchConfig** | [**PatchConfig**](PatchConfig.md) |  |  [optional] |
|**rollout** | [**PatchRollout**](PatchRollout.md) |  |  [optional] |



