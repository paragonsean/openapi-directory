

# ImageResult

Result of evaluating one image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowlistResult** | [**AllowlistResult**](AllowlistResult.md) |  |  [optional] |
|**checkSetResult** | [**CheckSetResult**](CheckSetResult.md) |  |  [optional] |
|**explanation** | **String** | Explanation of this image result. Only populated if no check sets were evaluated. |  [optional] |
|**imageUri** | **String** | Image URI from the request. |  [optional] |
|**verdict** | [**VerdictEnum**](#VerdictEnum) | The result of evaluating this image. |  [optional] |



## Enum: VerdictEnum

| Name | Value |
|---- | -----|
| IMAGE_VERDICT_UNSPECIFIED | &quot;IMAGE_VERDICT_UNSPECIFIED&quot; |
| CONFORMANT | &quot;CONFORMANT&quot; |
| NON_CONFORMANT | &quot;NON_CONFORMANT&quot; |
| ERROR | &quot;ERROR&quot; |



