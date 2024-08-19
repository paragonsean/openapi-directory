

# MediationAbExperiment

The mediation A/B experiment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controlMediationLines** | [**List&lt;MediationAbExperimentExperimentMediationLine&gt;**](MediationAbExperimentExperimentMediationLine.md) | Output only. The experiment mediation lines for control. They are inherited from the parent mediation group. It is an output only field. |  [optional] [readonly] |
|**displayName** | **String** | The display name for the mediation A/B experiment. |  [optional] |
|**endTime** | **String** | Output only. The time at which the experiment was ended or target to end (in UTC). |  [optional] [readonly] |
|**experimentId** | **String** | Output only. Unique identifier for the mediation A/B experiment. It is an output only property. |  [optional] [readonly] |
|**mediationGroupId** | **String** | Output only. The mediation group id this experiment belongs to. This can be used for filtering the experiments in the list experiments API. |  [optional] [readonly] |
|**name** | **String** | Resource name for this experiment. The format is accounts/{publisher_id}/ mediationGroups/{mediation_group_id}/mediationAbExperiment/ {mediation_group_experiment_id}. For example: accounts/pub-9876543210987654/mediationGroups/0123456789/ mediationAbExperiment/12345 |  [optional] |
|**startTime** | **String** | Output only. The time at which the experiment was started (in UTC). |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the experiment. It is an output only field. |  [optional] [readonly] |
|**treatmentMediationLines** | [**List&lt;MediationAbExperimentExperimentMediationLine&gt;**](MediationAbExperimentExperimentMediationLine.md) | The experiment mediation lines created for the treatment. They will be used for serving when the experiment status is RUNNING. |  [optional] |
|**treatmentTrafficPercentage** | **String** | The percentage of the mediation A/B experiment traffic that will be send to the treatment (variant B). The remainder is sent to the control (variant A). The percentage is expressed as an integer in the inclusive range of [1,99]. See https://support.google.com/admob/answer/9572326 for details. |  [optional] |
|**variantLeader** | [**VariantLeaderEnum**](#VariantLeaderEnum) | Output only. The variant leader for the experiment according to some key metrics. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| EXPERIMENT_STATE_UNSPECIFIED | &quot;EXPERIMENT_STATE_UNSPECIFIED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| ENDED | &quot;ENDED&quot; |



## Enum: VariantLeaderEnum

| Name | Value |
|---- | -----|
| VARIANT_LEADER_UNSPECIFIED | &quot;VARIANT_LEADER_UNSPECIFIED&quot; |
| CONTROL | &quot;CONTROL&quot; |
| TREATMENT | &quot;TREATMENT&quot; |
| INSUFFICIENT_DATA | &quot;INSUFFICIENT_DATA&quot; |
| TOO_EARLY_TO_CALL | &quot;TOO_EARLY_TO_CALL&quot; |
| NO_VARIANT_LEADER | &quot;NO_VARIANT_LEADER&quot; |



