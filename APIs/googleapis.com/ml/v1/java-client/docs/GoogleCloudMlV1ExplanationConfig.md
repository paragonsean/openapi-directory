

# GoogleCloudMlV1ExplanationConfig

Message holding configuration options for explaining model predictions. There are three feature attribution methods supported for TensorFlow models: integrated gradients, sampled Shapley, and XRAI. [Learn more about feature attributions.](/ai-platform/prediction/docs/ai-explanations/overview)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**integratedGradientsAttribution** | [**GoogleCloudMlV1IntegratedGradientsAttribution**](GoogleCloudMlV1IntegratedGradientsAttribution.md) |  |  [optional] |
|**sampledShapleyAttribution** | [**GoogleCloudMlV1SampledShapleyAttribution**](GoogleCloudMlV1SampledShapleyAttribution.md) |  |  [optional] |
|**xraiAttribution** | [**GoogleCloudMlV1XraiAttribution**](GoogleCloudMlV1XraiAttribution.md) |  |  [optional] |



