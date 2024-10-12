# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesConversion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adId** | **String** | Output only. Ad ID. A value of 0 indicates that the ad is unattributed. | [optional] [readonly] 
**advertiserConversionId** | **String** | Output only. For offline conversions, this is an ID provided by advertisers. If an advertiser doesn&#39;t specify such an ID, Search Ads 360 generates one. For online conversions, this is equal to the id column or the floodlight_order_id column depending on the advertiser&#39;s Floodlight instructions. | [optional] [readonly] 
**assetFieldType** | **String** | Output only. Asset field type of the conversion event. | [optional] [readonly] 
**assetId** | **String** | Output only. ID of the asset which was interacted with during the conversion event. | [optional] [readonly] 
**attributionType** | **String** | Output only. What the conversion is attributed to: Visit or Keyword+Ad. | [optional] [readonly] 
**clickId** | **String** | Output only. A unique string, for the visit that the conversion is attributed to, that is passed to the landing page as the click id URL parameter. | [optional] [readonly] 
**conversionDateTime** | **String** | Output only. The timestamp of the conversion event. | [optional] [readonly] 
**conversionLastModifiedDateTime** | **String** | Output only. The timestamp of the last time the conversion was modified. | [optional] [readonly] 
**conversionQuantity** | **String** | Output only. The quantity of items recorded by the conversion, as determined by the qty url parameter. The advertiser is responsible for dynamically populating the parameter (such as number of items sold in the conversion), otherwise it defaults to 1. | [optional] [readonly] 
**conversionRevenueMicros** | **String** | Output only. The adjusted revenue in micros for the conversion event. This will always be in the currency of the serving account. | [optional] [readonly] 
**conversionVisitDateTime** | **String** | Output only. The timestamp of the visit that the conversion is attributed to. | [optional] [readonly] 
**criterionId** | **String** | Output only. Search Ads 360 criterion ID. A value of 0 indicates that the criterion is unattributed. | [optional] [readonly] 
**floodlightOrderId** | **String** | Output only. The Floodlight order ID provided by the advertiser for the conversion. | [optional] [readonly] 
**floodlightOriginalRevenue** | **String** | Output only. The original, unchanged revenue associated with the Floodlight event (in the currency of the current report), before Floodlight currency instruction modifications. | [optional] [readonly] 
**id** | **String** | Output only. The ID of the conversion | [optional] [readonly] 
**merchantId** | **String** | Output only. The SearchAds360 inventory account ID containing the product that was clicked on. SearchAds360 generates this ID when you link an inventory account in SearchAds360. | [optional] [readonly] 
**productChannel** | **String** | Output only. The sales channel of the product that was clicked on: Online or Local. | [optional] [readonly] 
**productCountryCode** | **String** | Output only. The country (ISO-3166-format) registered for the inventory feed that contains the product clicked on. | [optional] [readonly] 
**productId** | **String** | Output only. The ID of the product clicked on. | [optional] [readonly] 
**productLanguageCode** | **String** | Output only. The language (ISO-639-1) that has been set for the Merchant Center feed containing data about the product. | [optional] [readonly] 
**productStoreId** | **String** | Output only. The store in the Local Inventory Ad that was clicked on. This should match the store IDs used in your local products feed. | [optional] [readonly] 
**resourceName** | **String** | Output only. The resource name of the conversion. Conversion resource names have the form: &#x60;customers/{customer_id}/conversions/{ad_group_id}~{criterion_id}~{ds_conversion_id}&#x60; | [optional] [readonly] 
**status** | **String** | Output only. The status of the conversion, either ENABLED or REMOVED.. | [optional] [readonly] 
**visitId** | **String** | Output only. The SearchAds360 visit ID that the conversion is attributed to. | [optional] [readonly] 



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





## Enum: AttributionTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `VISIT` (value: `"VISIT"`)

* `CRITERION_AD` (value: `"CRITERION_AD"`)





## Enum: ProductChannelEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ONLINE` (value: `"ONLINE"`)

* `LOCAL` (value: `"LOCAL"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `REMOVED` (value: `"REMOVED"`)




