# AdMobApi.MediationGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | User provided name for the mediation group. The maximum length allowed is 120 characters. | [optional] 
**mediationAbExperimentState** | **String** | Output only. The state of the mediation a/b experiment that belongs to this mediation group. | [optional] [readonly] 
**mediationGroupId** | **String** | The ID of the mediation group. Example: \&quot;0123456789\&quot;. This is a read only property. | [optional] 
**mediationGroupLines** | [**{String: MediationGroupMediationGroupLine}**](MediationGroupMediationGroupLine.md) | The mediation lines used for serving for this mediation group. Key is the ID of the mediation group line. For creation, use distinct negative values as placeholder. | [optional] 
**name** | **String** | Resource name for this mediation group. Format is: accounts/{publisher_id}/mediationGroups/{mediation_group_id} Example: accounts/pub-9876543210987654/mediationGroups/0123456789 | [optional] 
**state** | **String** | The status of the mediation group. Only enabled mediation groups will be served. | [optional] 
**targeting** | [**MediationGroupTargeting**](MediationGroupTargeting.md) |  | [optional] 



## Enum: MediationAbExperimentStateEnum


* `EXPERIMENT_STATE_UNSPECIFIED` (value: `"EXPERIMENT_STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `NOT_RUNNING` (value: `"NOT_RUNNING"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




