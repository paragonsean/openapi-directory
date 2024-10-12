# OsConfigApi.PatchJobInstanceDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attemptCount** | **String** | The number of times the agent that the agent attempts to apply the patch. | [optional] 
**failureReason** | **String** | If the patch fails, this field provides the reason. | [optional] 
**instanceSystemId** | **String** | The unique identifier for the instance. This identifier is defined by the server. | [optional] 
**name** | **String** | The instance name in the form &#x60;projects/_*_/zones/_*_/instances/_*&#x60; | [optional] 
**state** | **String** | Current state of instance patch. | [optional] 



## Enum: StateEnum


* `PATCH_STATE_UNSPECIFIED` (value: `"PATCH_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `NOTIFIED` (value: `"NOTIFIED"`)

* `STARTED` (value: `"STARTED"`)

* `DOWNLOADING_PATCHES` (value: `"DOWNLOADING_PATCHES"`)

* `APPLYING_PATCHES` (value: `"APPLYING_PATCHES"`)

* `REBOOTING` (value: `"REBOOTING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `SUCCEEDED_REBOOT_REQUIRED` (value: `"SUCCEEDED_REBOOT_REQUIRED"`)

* `FAILED` (value: `"FAILED"`)

* `ACKED` (value: `"ACKED"`)

* `TIMED_OUT` (value: `"TIMED_OUT"`)

* `RUNNING_PRE_PATCH_STEP` (value: `"RUNNING_PRE_PATCH_STEP"`)

* `RUNNING_POST_PATCH_STEP` (value: `"RUNNING_POST_PATCH_STEP"`)

* `NO_AGENT_DETECTED` (value: `"NO_AGENT_DETECTED"`)




