# BinaryAuthorizationApi.ImageResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowlistResult** | [**AllowlistResult**](AllowlistResult.md) |  | [optional] 
**checkSetResult** | [**CheckSetResult**](CheckSetResult.md) |  | [optional] 
**explanation** | **String** | Explanation of this image result. Only populated if no check sets were evaluated. | [optional] 
**imageUri** | **String** | Image URI from the request. | [optional] 
**verdict** | **String** | The result of evaluating this image. | [optional] 



## Enum: VerdictEnum


* `IMAGE_VERDICT_UNSPECIFIED` (value: `"IMAGE_VERDICT_UNSPECIFIED"`)

* `CONFORMANT` (value: `"CONFORMANT"`)

* `NON_CONFORMANT` (value: `"NON_CONFORMANT"`)

* `ERROR` (value: `"ERROR"`)




