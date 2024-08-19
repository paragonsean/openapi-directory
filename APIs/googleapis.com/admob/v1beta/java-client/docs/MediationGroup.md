

# MediationGroup

Describes an AdMob mediation group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | User provided name for the mediation group. The maximum length allowed is 120 characters. |  [optional] |
|**mediationAbExperimentState** | [**MediationAbExperimentStateEnum**](#MediationAbExperimentStateEnum) | Output only. The state of the mediation a/b experiment that belongs to this mediation group. |  [optional] [readonly] |
|**mediationGroupId** | **String** | The ID of the mediation group. Example: \&quot;0123456789\&quot;. This is a read only property. |  [optional] |
|**mediationGroupLines** | [**Map&lt;String, MediationGroupMediationGroupLine&gt;**](MediationGroupMediationGroupLine.md) | The mediation lines used for serving for this mediation group. Key is the ID of the mediation group line. For creation, use distinct negative values as placeholder. |  [optional] |
|**name** | **String** | Resource name for this mediation group. Format is: accounts/{publisher_id}/mediationGroups/{mediation_group_id} Example: accounts/pub-9876543210987654/mediationGroups/0123456789 |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The status of the mediation group. Only enabled mediation groups will be served. |  [optional] |
|**targeting** | [**MediationGroupTargeting**](MediationGroupTargeting.md) |  |  [optional] |



## Enum: MediationAbExperimentStateEnum

| Name | Value |
|---- | -----|
| EXPERIMENT_STATE_UNSPECIFIED | &quot;EXPERIMENT_STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| NOT_RUNNING | &quot;NOT_RUNNING&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



