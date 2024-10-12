

# GoogleCloudAiplatformV1beta1TrialContext

Next ID: 3

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human-readable field which can store a description of this context. This will become part of the resulting Trial&#39;s description field. |  [optional] |
|**parameters** | [**List&lt;GoogleCloudAiplatformV1beta1TrialParameter&gt;**](GoogleCloudAiplatformV1beta1TrialParameter.md) | If/when a Trial is generated or selected from this Context, its Parameters will match any parameters specified here. (I.e. if this context specifies parameter name:&#39;a&#39; int_value:3, then a resulting Trial will have int_value:3 for its parameter named &#39;a&#39;.) Note that we first attempt to match existing REQUESTED Trials with contexts, and if there are no matches, we generate suggestions in the subspace defined by the parameters specified here. NOTE: a Context without any Parameters matches the entire feasible search space. |  [optional] |



