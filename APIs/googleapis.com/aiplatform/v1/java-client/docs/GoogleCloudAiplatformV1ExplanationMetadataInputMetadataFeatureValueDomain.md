

# GoogleCloudAiplatformV1ExplanationMetadataInputMetadataFeatureValueDomain

Domain details of the input feature value. Provides numeric information about the feature, such as its range (min, max). If the feature has been pre-processed, for example with z-scoring, then it provides information about how to recover the original feature. For example, if the input feature is an image and it has been pre-processed to obtain 0-mean and stddev = 1 values, then original_mean, and original_stddev refer to the mean and stddev of the original feature (e.g. image tensor) from which input feature (with mean = 0 and stddev = 1) was obtained.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxValue** | **Float** | The maximum permissible value for this feature. |  [optional] |
|**minValue** | **Float** | The minimum permissible value for this feature. |  [optional] |
|**originalMean** | **Float** | If this input feature has been normalized to a mean value of 0, the original_mean specifies the mean value of the domain prior to normalization. |  [optional] |
|**originalStddev** | **Float** | If this input feature has been normalized to a standard deviation of 1.0, the original_stddev specifies the standard deviation of the domain prior to normalization. |  [optional] |



