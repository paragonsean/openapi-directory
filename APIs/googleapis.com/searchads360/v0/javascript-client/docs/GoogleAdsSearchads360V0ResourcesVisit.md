# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesVisit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adId** | **String** | Output only. Ad ID. A value of 0 indicates that the ad is unattributed. | [optional] [readonly] 
**assetFieldType** | **String** | Output only. Asset field type of the visit event. | [optional] [readonly] 
**assetId** | **String** | Output only. ID of the asset which was interacted with during the visit event. | [optional] [readonly] 
**clickId** | **String** | Output only. A unique string for each visit that is passed to the landing page as the click id URL parameter. | [optional] [readonly] 
**criterionId** | **String** | Output only. Search Ads 360 keyword ID. A value of 0 indicates that the keyword is unattributed. | [optional] [readonly] 
**id** | **String** | Output only. The ID of the visit. | [optional] [readonly] 
**merchantId** | **String** | Output only. The Search Ads 360 inventory account ID containing the product that was clicked on. Search Ads 360 generates this ID when you link an inventory account in Search Ads 360. | [optional] [readonly] 
**productChannel** | **String** | Output only. The sales channel of the product that was clicked on: Online or Local. | [optional] [readonly] 
**productCountryCode** | **String** | Output only. The country (ISO-3166 format) registered for the inventory feed that contains the product clicked on. | [optional] [readonly] 
**productId** | **String** | Output only. The ID of the product clicked on. | [optional] [readonly] 
**productLanguageCode** | **String** | Output only. The language (ISO-639-1) that has been set for the Merchant Center feed containing data about the product. | [optional] [readonly] 
**productStoreId** | **String** | Output only. The store in the Local Inventory Ad that was clicked on. This should match the store IDs used in your local products feed. | [optional] [readonly] 
**resourceName** | **String** | Output only. The resource name of the visit. Visit resource names have the form: &#x60;customers/{customer_id}/visits/{ad_group_id}~{criterion_id}~{ds_visit_id}&#x60; | [optional] [readonly] 
**visitDateTime** | **String** | Output only. The timestamp of the visit event. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. | [optional] [readonly] 



## Enum: AssetFieldTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `HEADLINE` (value: `"HEADLINE"`)

* `DESCRIPTION` (value: `"DESCRIPTION"`)

* `MANDATORY_AD_TEXT` (value: `"MANDATORY_AD_TEXT"`)

* `MARKETING_IMAGE` (value: `"MARKETING_IMAGE"`)

* `MEDIA_BUNDLE` (value: `"MEDIA_BUNDLE"`)

* `YOUTUBE_VIDEO` (value: `"YOUTUBE_VIDEO"`)

* `BOOK_ON_GOOGLE` (value: `"BOOK_ON_GOOGLE"`)

* `LEAD_FORM` (value: `"LEAD_FORM"`)

* `PROMOTION` (value: `"PROMOTION"`)

* `CALLOUT` (value: `"CALLOUT"`)

* `STRUCTURED_SNIPPET` (value: `"STRUCTURED_SNIPPET"`)

* `SITELINK` (value: `"SITELINK"`)

* `MOBILE_APP` (value: `"MOBILE_APP"`)

* `HOTEL_CALLOUT` (value: `"HOTEL_CALLOUT"`)

* `CALL` (value: `"CALL"`)

* `PRICE` (value: `"PRICE"`)

* `LONG_HEADLINE` (value: `"LONG_HEADLINE"`)

* `BUSINESS_NAME` (value: `"BUSINESS_NAME"`)

* `SQUARE_MARKETING_IMAGE` (value: `"SQUARE_MARKETING_IMAGE"`)

* `PORTRAIT_MARKETING_IMAGE` (value: `"PORTRAIT_MARKETING_IMAGE"`)

* `LOGO` (value: `"LOGO"`)

* `LANDSCAPE_LOGO` (value: `"LANDSCAPE_LOGO"`)

* `VIDEO` (value: `"VIDEO"`)

* `CALL_TO_ACTION_SELECTION` (value: `"CALL_TO_ACTION_SELECTION"`)

* `AD_IMAGE` (value: `"AD_IMAGE"`)

* `BUSINESS_LOGO` (value: `"BUSINESS_LOGO"`)

* `HOTEL_PROPERTY` (value: `"HOTEL_PROPERTY"`)





## Enum: ProductChannelEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ONLINE` (value: `"ONLINE"`)

* `LOCAL` (value: `"LOCAL"`)




