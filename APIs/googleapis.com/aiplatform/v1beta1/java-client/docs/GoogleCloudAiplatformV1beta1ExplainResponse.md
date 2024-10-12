

# GoogleCloudAiplatformV1beta1ExplainResponse

Response message for PredictionService.Explain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**concurrentExplanations** | [**Map&lt;String, GoogleCloudAiplatformV1beta1ExplainResponseConcurrentExplanation&gt;**](GoogleCloudAiplatformV1beta1ExplainResponseConcurrentExplanation.md) | This field stores the results of the explanations run in parallel with The default explanation strategy/method. |  [optional] |
|**deployedModelId** | **String** | ID of the Endpoint&#39;s DeployedModel that served this explanation. |  [optional] |
|**explanations** | [**List&lt;GoogleCloudAiplatformV1beta1Explanation&gt;**](GoogleCloudAiplatformV1beta1Explanation.md) | The explanations of the Model&#39;s PredictResponse.predictions. It has the same number of elements as instances to be explained. |  [optional] |
|**predictions** | **List&lt;Object&gt;** | The predictions that are the output of the predictions call. Same as PredictResponse.predictions. |  [optional] |



