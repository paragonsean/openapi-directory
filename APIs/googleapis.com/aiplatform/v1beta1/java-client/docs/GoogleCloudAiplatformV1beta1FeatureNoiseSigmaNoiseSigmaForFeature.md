

# GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature

Noise sigma for a single feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the input feature for which noise sigma is provided. The features are defined in explanation metadata inputs. |  [optional] |
|**sigma** | **Float** | This represents the standard deviation of the Gaussian kernel that will be used to add noise to the feature prior to computing gradients. Similar to noise_sigma but represents the noise added to the current feature. Defaults to 0.1. |  [optional] |



