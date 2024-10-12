

# ReviewsCreateReviewsRequestInner

Schema items of the body.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackEndpoint** | **String** | Optional CallbackEndpoint. |  [optional] |
|**content** | **String** | Content to review. |  |
|**contentId** | **String** | Content Identifier. |  |
|**metadata** | [**List&lt;ReviewsCreateReviewsRequestInnerMetadataInner&gt;**](ReviewsCreateReviewsRequestInnerMetadataInner.md) | Optional metadata details. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the content. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;Image&quot; |
| TEXT | &quot;Text&quot; |



