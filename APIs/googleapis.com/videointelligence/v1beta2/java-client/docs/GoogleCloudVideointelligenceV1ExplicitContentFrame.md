

# GoogleCloudVideointelligenceV1ExplicitContentFrame

Video frame level annotation results for explicit content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pornographyLikelihood** | [**PornographyLikelihoodEnum**](#PornographyLikelihoodEnum) | Likelihood of the pornography content.. |  [optional] |
|**timeOffset** | **String** | Time-offset, relative to the beginning of the video, corresponding to the video frame for this location. |  [optional] |



## Enum: PornographyLikelihoodEnum

| Name | Value |
|---- | -----|
| LIKELIHOOD_UNSPECIFIED | &quot;LIKELIHOOD_UNSPECIFIED&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



