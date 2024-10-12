# CloudDeployApi.AutomationRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanceRolloutOperation** | [**AdvanceRolloutOperation**](AdvanceRolloutOperation.md) |  | [optional] 
**automationId** | **String** | Output only. The ID of the automation that initiated the operation. | [optional] [readonly] 
**automationSnapshot** | [**Automation**](Automation.md) |  | [optional] 
**createTime** | **String** | Output only. Time at which the &#x60;AutomationRun&#x60; was created. | [optional] [readonly] 
**etag** | **String** | Output only. The weak etag of the &#x60;AutomationRun&#x60; resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] [readonly] 
**expireTime** | **String** | Output only. Time the &#x60;AutomationRun&#x60; expires. An &#x60;AutomationRun&#x60; expires after 14 days from its creation date. | [optional] [readonly] 
**name** | **String** | Output only. Name of the &#x60;AutomationRun&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}&#x60;. | [optional] [readonly] 
**promoteReleaseOperation** | [**PromoteReleaseOperation**](PromoteReleaseOperation.md) |  | [optional] 
**repairRolloutOperation** | [**RepairRolloutOperation**](RepairRolloutOperation.md) |  | [optional] 
**ruleId** | **String** | Output only. The ID of the automation rule that initiated the operation. | [optional] [readonly] 
**serviceAccount** | **String** | Output only. Email address of the user-managed IAM service account that performs the operations against Cloud Deploy resources. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the &#x60;AutomationRun&#x60;. | [optional] [readonly] 
**stateDescription** | **String** | Output only. Explains the current state of the &#x60;AutomationRun&#x60;. Present only when an explanation is needed. | [optional] [readonly] 
**targetId** | **String** | Output only. The ID of the target that represents the promotion stage that initiates the &#x60;AutomationRun&#x60;. The value of this field is the last segment of a target name. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time at which the automationRun was updated. | [optional] [readonly] 
**waitUntilTime** | **String** | Output only. Earliest time the &#x60;AutomationRun&#x60; will attempt to resume. Wait-time is configured by &#x60;wait&#x60; in automation rule. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `FAILED` (value: `"FAILED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `PENDING` (value: `"PENDING"`)

* `ABORTED` (value: `"ABORTED"`)




