

# AutomationRolloutMetadata

AutomationRolloutMetadata contains Automation-related actions that were performed on a rollout.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advanceAutomationRuns** | **List&lt;String&gt;** | Output only. The IDs of the AutomationRuns initiated by an advance rollout rule. |  [optional] [readonly] |
|**currentRepairAutomationRun** | **String** | Output only. The current AutomationRun repairing the rollout. |  [optional] [readonly] |
|**promoteAutomationRun** | **String** | Output only. The ID of the AutomationRun initiated by a promote release rule. |  [optional] [readonly] |
|**repairAutomationRuns** | **List&lt;String&gt;** | Output only. The IDs of the AutomationRuns initiated by a repair rollout rule. |  [optional] [readonly] |



