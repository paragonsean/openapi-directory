

# GoogleCloudAiplatformV1beta1XraiAttribution

An explanation method that redistributes Integrated Gradients attributions to segmented regions, taking advantage of the model's fully differentiable structure. Refer to this paper for more details: https://arxiv.org/abs/1906.02825 Supported only by image Models.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blurBaselineConfig** | [**GoogleCloudAiplatformV1beta1BlurBaselineConfig**](GoogleCloudAiplatformV1beta1BlurBaselineConfig.md) |  |  [optional] |
|**smoothGradConfig** | [**GoogleCloudAiplatformV1beta1SmoothGradConfig**](GoogleCloudAiplatformV1beta1SmoothGradConfig.md) |  |  [optional] |
|**stepCount** | **Integer** | Required. The number of steps for approximating the path integral. A good value to start is 50 and gradually increase until the sum to diff property is met within the desired error range. Valid range of its value is [1, 100], inclusively. |  [optional] |



