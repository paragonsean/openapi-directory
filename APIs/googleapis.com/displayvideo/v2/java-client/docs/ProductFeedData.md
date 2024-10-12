

# ProductFeedData

The details of product feed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isFeedDisabled** | **Boolean** | Whether the product feed has opted-out of showing products. |  [optional] |
|**productMatchDimensions** | [**List&lt;ProductMatchDimension&gt;**](ProductMatchDimension.md) | A list of dimensions used to match products. |  [optional] |
|**productMatchType** | [**ProductMatchTypeEnum**](#ProductMatchTypeEnum) | How products are selected by the product feed. |  [optional] |



## Enum: ProductMatchTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRODUCT_MATCH_TYPE_UNSPECIFIED&quot; |
| ALL_PRODUCTS | &quot;PRODUCT_MATCH_TYPE_ALL_PRODUCTS&quot; |
| SPECIFIC_PRODUCTS | &quot;PRODUCT_MATCH_TYPE_SPECIFIC_PRODUCTS&quot; |
| CUSTOM_LABEL | &quot;PRODUCT_MATCH_TYPE_CUSTOM_LABEL&quot; |



