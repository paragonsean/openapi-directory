

# PatchJobInstanceDetailsSummary

A summary of the current patch state across all instances that this patch job affects. Contains counts of instances in different states. These states map to `InstancePatchState`. List patch job instance details to see the specific states of each instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ackedInstanceCount** | **String** | Number of instances that have acked and will start shortly. |  [optional] |
|**applyingPatchesInstanceCount** | **String** | Number of instances that are applying patches. |  [optional] |
|**downloadingPatchesInstanceCount** | **String** | Number of instances that are downloading patches. |  [optional] |
|**failedInstanceCount** | **String** | Number of instances that failed. |  [optional] |
|**inactiveInstanceCount** | **String** | Number of instances that are inactive. |  [optional] |
|**noAgentDetectedInstanceCount** | **String** | Number of instances that do not appear to be running the agent. Check to ensure that the agent is installed, running, and able to communicate with the service. |  [optional] |
|**notifiedInstanceCount** | **String** | Number of instances notified about patch job. |  [optional] |
|**pendingInstanceCount** | **String** | Number of instances pending patch job. |  [optional] |
|**postPatchStepInstanceCount** | **String** | Number of instances that are running the post-patch step. |  [optional] |
|**prePatchStepInstanceCount** | **String** | Number of instances that are running the pre-patch step. |  [optional] |
|**rebootingInstanceCount** | **String** | Number of instances rebooting. |  [optional] |
|**startedInstanceCount** | **String** | Number of instances that have started. |  [optional] |
|**succeededInstanceCount** | **String** | Number of instances that have completed successfully. |  [optional] |
|**succeededRebootRequiredInstanceCount** | **String** | Number of instances that require reboot. |  [optional] |
|**timedOutInstanceCount** | **String** | Number of instances that exceeded the time out while applying the patch. |  [optional] |



