

# PatchJobInstanceDetails

Patch details for a VM instance. For more information about reviewing VM instance details, see [Listing all VM instance details for a specific patch job](https://cloud.google.com/compute/docs/os-patch-management/manage-patch-jobs#list-instance-details).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attemptCount** | **String** | The number of times the agent that the agent attempts to apply the patch. |  [optional] |
|**failureReason** | **String** | If the patch fails, this field provides the reason. |  [optional] |
|**instanceSystemId** | **String** | The unique identifier for the instance. This identifier is defined by the server. |  [optional] |
|**name** | **String** | The instance name in the form &#x60;projects/_*_/zones/_*_/instances/_*&#x60; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of instance patch. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PATCH_STATE_UNSPECIFIED | &quot;PATCH_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| NOTIFIED | &quot;NOTIFIED&quot; |
| STARTED | &quot;STARTED&quot; |
| DOWNLOADING_PATCHES | &quot;DOWNLOADING_PATCHES&quot; |
| APPLYING_PATCHES | &quot;APPLYING_PATCHES&quot; |
| REBOOTING | &quot;REBOOTING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| SUCCEEDED_REBOOT_REQUIRED | &quot;SUCCEEDED_REBOOT_REQUIRED&quot; |
| FAILED | &quot;FAILED&quot; |
| ACKED | &quot;ACKED&quot; |
| TIMED_OUT | &quot;TIMED_OUT&quot; |
| RUNNING_PRE_PATCH_STEP | &quot;RUNNING_PRE_PATCH_STEP&quot; |
| RUNNING_POST_PATCH_STEP | &quot;RUNNING_POST_PATCH_STEP&quot; |
| NO_AGENT_DETECTED | &quot;NO_AGENT_DETECTED&quot; |



