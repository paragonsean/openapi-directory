

# GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig

Additional config specs for a Media Recommendation engine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**optimizationObjective** | **String** | The optimization objective. e.g., &#x60;cvr&#x60;. This field together with optimization_objective describe engine metadata to use to control engine training and serving. Currently supported values: &#x60;ctr&#x60;, &#x60;cvr&#x60;. If not specified, we choose default based on engine type. Default depends on type of recommendation: &#x60;recommended-for-you&#x60; &#x3D;&gt; &#x60;ctr&#x60; &#x60;others-you-may-like&#x60; &#x3D;&gt; &#x60;ctr&#x60; |  [optional] |
|**optimizationObjectiveConfig** | [**GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig**](GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig.md) |  |  [optional] |
|**trainingState** | [**TrainingStateEnum**](#TrainingStateEnum) | The training state that the engine is in (e.g. &#x60;TRAINING&#x60; or &#x60;PAUSED&#x60;). Since part of the cost of running the service is frequency of training - this can be used to determine when to train engine in order to control cost. If not specified: the default value for &#x60;CreateEngine&#x60; method is &#x60;TRAINING&#x60;. The default value for &#x60;UpdateEngine&#x60; method is to keep the state the same as before. |  [optional] |
|**type** | **String** | Required. The type of engine. e.g., &#x60;recommended-for-you&#x60;. This field together with optimization_objective describe engine metadata to use to control engine training and serving. Currently supported values: &#x60;recommended-for-you&#x60;, &#x60;others-you-may-like&#x60;, &#x60;more-like-this&#x60;, &#x60;most-popular-items&#x60;. |  [optional] |



## Enum: TrainingStateEnum

| Name | Value |
|---- | -----|
| TRAINING_STATE_UNSPECIFIED | &quot;TRAINING_STATE_UNSPECIFIED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| TRAINING | &quot;TRAINING&quot; |



