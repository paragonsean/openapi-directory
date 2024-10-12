# OsConfigApi.OSPolicyAssignmentRollout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruptionBudget** | [**FixedOrPercent**](FixedOrPercent.md) |  | [optional] 
**minWaitDuration** | **String** | Required. This determines the minimum duration of time to wait after the configuration changes are applied through the current rollout. A VM continues to count towards the &#x60;disruption_budget&#x60; at least until this duration of time has passed after configuration changes are applied. | [optional] 


