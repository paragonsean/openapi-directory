

# GoogleCloudMlV1XraiAttribution

Attributes credit by computing the XRAI taking advantage of the model's fully differentiable structure. Refer to this paper for more details: https://arxiv.org/abs/1906.02825 Currently only implemented for models with natural image inputs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numIntegralSteps** | **Integer** | Number of steps for approximating the path integral. A good value to start is 50 and gradually increase until the sum to diff property is met within the desired error range. |  [optional] |



