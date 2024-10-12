# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryCode** | **String** | Output only. Two-letter upper-case country code of the product bidding category. | [optional] [readonly] 
**id** | **String** | Output only. ID of the product bidding category. This ID is equivalent to the google_product_category ID as described in this article: https://support.google.com/merchants/answer/6324436. | [optional] [readonly] 
**languageCode** | **String** | Output only. Language code of the product bidding category. | [optional] [readonly] 
**level** | **String** | Output only. Level of the product bidding category. | [optional] [readonly] 
**localizedName** | **String** | Output only. Display value of the product bidding category localized according to language_code. | [optional] [readonly] 
**productBiddingCategoryConstantParent** | **String** | Output only. Resource name of the parent product bidding category. | [optional] [readonly] 
**resourceName** | **String** | Output only. The resource name of the product bidding category. Product bidding category resource names have the form: &#x60;productBiddingCategoryConstants/{country_code}~{level}~{id}&#x60; | [optional] [readonly] 
**status** | **String** | Output only. Status of the product bidding category. | [optional] [readonly] 



## Enum: LevelEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `LEVEL1` (value: `"LEVEL1"`)

* `LEVEL2` (value: `"LEVEL2"`)

* `LEVEL3` (value: `"LEVEL3"`)

* `LEVEL4` (value: `"LEVEL4"`)

* `LEVEL5` (value: `"LEVEL5"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `OBSOLETE` (value: `"OBSOLETE"`)




