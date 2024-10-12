# AgcoApi.BuildSystemSharedDTOActivityRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityRunID** | **Number** | The identifier for the ActivityRun | [optional] 
**endDate** | **Date** | Read Only. The UTC date and time when the activity completed | [optional] 
**jobActivityID** | **Number** | Read Only. The ID of the Job Activity that defines this activity run | [optional] 
**jobRunID** | **Number** | Read Only. The ID of the JobRun under which this ActivityRun is executing | [optional] 
**parameters** | [**[BuildSystemSharedDTOParameterValue]**](BuildSystemSharedDTOParameterValue.md) | The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated. | [optional] [readonly] 
**startDate** | **Date** | Read Only. The UTC date and time when the activity started | [optional] 
**status** | [**BuildSystemSharedDTOActivityRunStatus**](BuildSystemSharedDTOActivityRunStatus.md) |  | 
**steps** | [**[BuildSystemSharedDTOActivityStep]**](BuildSystemSharedDTOActivityStep.md) | Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep | [optional] [readonly] 


