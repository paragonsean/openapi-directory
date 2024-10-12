

# GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant

A Product Bidding Category.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryCode** | **String** | Output only. Two-letter upper-case country code of the product bidding category. |  [optional] [readonly] |
|**id** | **String** | Output only. ID of the product bidding category. This ID is equivalent to the google_product_category ID as described in this article: https://support.google.com/merchants/answer/6324436. |  [optional] [readonly] |
|**languageCode** | **String** | Output only. Language code of the product bidding category. |  [optional] [readonly] |
|**level** | [**LevelEnum**](#LevelEnum) | Output only. Level of the product bidding category. |  [optional] [readonly] |
|**localizedName** | **String** | Output only. Display value of the product bidding category localized according to language_code. |  [optional] [readonly] |
|**productBiddingCategoryConstantParent** | **String** | Output only. Resource name of the parent product bidding category. |  [optional] [readonly] |
|**resourceName** | **String** | Output only. The resource name of the product bidding category. Product bidding category resource names have the form: &#x60;productBiddingCategoryConstants/{country_code}~{level}~{id}&#x60; |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. Status of the product bidding category. |  [optional] [readonly] |



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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| OBSOLETE | &quot;OBSOLETE&quot; |



