

# GoogleCloudMlV1IntegratedGradientsAttribution

Attributes credit by computing the Aumann-Shapley value taking advantage of the model's fully differentiable structure. Refer to this paper for more details: https://arxiv.org/abs/1703.01365

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numIntegralSteps** | **Integer** | Number of steps for approximating the path integral. A good value to start is 50 and gradually increase until the sum to diff property is met within the desired error range. |  [optional] |



