

# GoogleCloudAiplatformV1IntegratedGradientsAttribution

An attribution method that computes the Aumann-Shapley value taking advantage of the model's fully differentiable structure. Refer to this paper for more details: https://arxiv.org/abs/1703.01365

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blurBaselineConfig** | [**GoogleCloudAiplatformV1BlurBaselineConfig**](GoogleCloudAiplatformV1BlurBaselineConfig.md) |  |  [optional] |
|**smoothGradConfig** | [**GoogleCloudAiplatformV1SmoothGradConfig**](GoogleCloudAiplatformV1SmoothGradConfig.md) |  |  [optional] |
|**stepCount** | **Integer** | Required. The number of steps for approximating the path integral. A good value to start is 50 and gradually increase until the sum to diff property is within the desired error range. Valid range of its value is [1, 100], inclusively. |  [optional] |



