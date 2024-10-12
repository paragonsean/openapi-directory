

# GoogleCloudMlV1Trial

A message representing a trial.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Output only. The identifier of the client that originally requested this trial. |  [optional] [readonly] |
|**endTime** | **String** | Output only. Time at which the trial&#39;s status changed to COMPLETED. |  [optional] [readonly] |
|**finalMeasurement** | [**GoogleCloudMlV1Measurement**](GoogleCloudMlV1Measurement.md) |  |  [optional] |
|**infeasibleReason** | **String** | Output only. A human readable string describing why the trial is infeasible. This should only be set if trial_infeasible is true. |  [optional] [readonly] |
|**measurements** | [**List&lt;GoogleCloudMlV1Measurement&gt;**](GoogleCloudMlV1Measurement.md) | A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_time). These are used for early stopping computations. |  [optional] |
|**name** | **String** | Output only. Name of the trial assigned by the service. |  [optional] [readonly] |
|**parameters** | [**List&lt;GoogleCloudMlV1TrialParameter&gt;**](GoogleCloudMlV1TrialParameter.md) | The parameters of the trial. |  [optional] |
|**startTime** | **String** | Output only. Time at which the trial was started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The detailed state of a trial. |  [optional] |
|**trialInfeasible** | **Boolean** | Output only. If true, the parameters in this trial are not attempted again. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| STOPPING | &quot;STOPPING&quot; |



