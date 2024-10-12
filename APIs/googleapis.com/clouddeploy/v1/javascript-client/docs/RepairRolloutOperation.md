# CloudDeployApi.RepairRolloutOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentRepairModeIndex** | **String** | Output only. The index of the current repair action in the repair sequence. | [optional] [readonly] 
**jobId** | **String** | Output only. The job ID for the Job to repair. | [optional] [readonly] 
**phaseId** | **String** | Output only. The phase ID of the phase that includes the job being repaired. | [optional] [readonly] 
**repairPhases** | [**[RepairPhase]**](RepairPhase.md) | Output only. Records of the repair attempts. Each repair phase may have multiple retry attempts or single rollback attempt. | [optional] [readonly] 
**rollout** | **String** | Output only. The name of the rollout that initiates the &#x60;AutomationRun&#x60;. | [optional] [readonly] 


