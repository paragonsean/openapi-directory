

# GoogleAdsSearchads360V0ResourcesListingGroupFilterDimensionProductBiddingCategory

One element of a bidding category at a certain level. Top-level categories are at level 1, their children at level 2, and so on. We currently support up to 5 levels. The user must specify a dimension type that indicates the level of the category. All cases of the same subdivision must have the same dimension type (category level).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the product bidding category. This ID is equivalent to the google_product_category ID as described in this article: https://support.google.com/merchants/answer/6324436 |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Indicates the level of the category in the taxonomy. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| LEVEL1 | &quot;LEVEL1&quot; |
| LEVEL2 | &quot;LEVEL2&quot; |
| LEVEL3 | &quot;LEVEL3&quot; |
| LEVEL4 | &quot;LEVEL4&quot; |
| LEVEL5 | &quot;LEVEL5&quot; |



