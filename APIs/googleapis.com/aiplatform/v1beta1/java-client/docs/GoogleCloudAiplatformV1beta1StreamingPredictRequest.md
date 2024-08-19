

# GoogleCloudAiplatformV1beta1StreamingPredictRequest

Request message for PredictionService.StreamingPredict. The first message must contain endpoint field and optionally input. The subsequent messages must contain input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputs** | [**List&lt;GoogleCloudAiplatformV1beta1Tensor&gt;**](GoogleCloudAiplatformV1beta1Tensor.md) | The prediction input. |  [optional] |
|**parameters** | [**GoogleCloudAiplatformV1beta1Tensor**](GoogleCloudAiplatformV1beta1Tensor.md) |  |  [optional] |



