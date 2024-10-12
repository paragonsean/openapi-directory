# VertexAiApi.GoogleCloudAiplatformV1beta1SmoothGradConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featureNoiseSigma** | [**GoogleCloudAiplatformV1beta1FeatureNoiseSigma**](GoogleCloudAiplatformV1beta1FeatureNoiseSigma.md) |  | [optional] 
**noiseSigma** | **Number** | This is a single float value and will be used to add noise to all the features. Use this field when all features are normalized to have the same distribution: scale to range [0, 1], [-1, 1] or z-scoring, where features are normalized to have 0-mean and 1-variance. Learn more about [normalization](https://developers.google.com/machine-learning/data-prep/transform/normalization). For best results the recommended value is about 10% - 20% of the standard deviation of the input feature. Refer to section 3.2 of the SmoothGrad paper: https://arxiv.org/pdf/1706.03825.pdf. Defaults to 0.1. If the distribution is different per feature, set feature_noise_sigma instead for each feature. | [optional] 
**noisySampleCount** | **Number** | The number of gradient samples to use for approximation. The higher this number, the more accurate the gradient is, but the runtime complexity increases by this factor as well. Valid range of its value is [1, 50]. Defaults to 3. | [optional] 


