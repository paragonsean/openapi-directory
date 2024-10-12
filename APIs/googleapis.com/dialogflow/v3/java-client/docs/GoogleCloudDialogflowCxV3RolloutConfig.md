

# GoogleCloudDialogflowCxV3RolloutConfig

The configuration for auto rollout.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureCondition** | **String** | The conditions that are used to evaluate the failure of a rollout step. If not specified, no rollout steps will fail. E.g. \&quot;containment_rate &lt; 10% OR average_turn_count &lt; 3\&quot;. See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). |  [optional] |
|**rolloutCondition** | **String** | The conditions that are used to evaluate the success of a rollout step. If not specified, all rollout steps will proceed to the next one unless failure conditions are met. E.g. \&quot;containment_rate &gt; 60% AND callback_rate &lt; 20%\&quot;. See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). |  [optional] |
|**rolloutSteps** | [**List&lt;GoogleCloudDialogflowCxV3RolloutConfigRolloutStep&gt;**](GoogleCloudDialogflowCxV3RolloutConfigRolloutStep.md) | Steps to roll out a flow version. Steps should be sorted by percentage in ascending order. |  [optional] |



