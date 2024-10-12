

# GooglePrivacyDlpV2InfoTypeLikelihood

Configuration for setting a minimum likelihood per infotype. Used to customize the minimum likelihood level for specific infotypes in the request. For example, use this if you want to lower the precision for PERSON_NAME without lowering the precision for the other infotypes in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**infoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  |  [optional] |
|**minLikelihood** | [**MinLikelihoodEnum**](#MinLikelihoodEnum) | Only returns findings equal to or above this threshold. This field is required or else the configuration fails. |  [optional] |



## Enum: MinLikelihoodEnum

| Name | Value |
|---- | -----|
| LIKELIHOOD_UNSPECIFIED | &quot;LIKELIHOOD_UNSPECIFIED&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



