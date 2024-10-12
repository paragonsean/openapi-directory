

# GoogleAdsSearchads360V0ResourcesVisit

A visit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** | Output only. Ad ID. A value of 0 indicates that the ad is unattributed. |  [optional] [readonly] |
|**assetFieldType** | [**AssetFieldTypeEnum**](#AssetFieldTypeEnum) | Output only. Asset field type of the visit event. |  [optional] [readonly] |
|**assetId** | **String** | Output only. ID of the asset which was interacted with during the visit event. |  [optional] [readonly] |
|**clickId** | **String** | Output only. A unique string for each visit that is passed to the landing page as the click id URL parameter. |  [optional] [readonly] |
|**criterionId** | **String** | Output only. Search Ads 360 keyword ID. A value of 0 indicates that the keyword is unattributed. |  [optional] [readonly] |
|**id** | **String** | Output only. The ID of the visit. |  [optional] [readonly] |
|**merchantId** | **String** | Output only. The Search Ads 360 inventory account ID containing the product that was clicked on. Search Ads 360 generates this ID when you link an inventory account in Search Ads 360. |  [optional] [readonly] |
|**productChannel** | [**ProductChannelEnum**](#ProductChannelEnum) | Output only. The sales channel of the product that was clicked on: Online or Local. |  [optional] [readonly] |
|**productCountryCode** | **String** | Output only. The country (ISO-3166 format) registered for the inventory feed that contains the product clicked on. |  [optional] [readonly] |
|**productId** | **String** | Output only. The ID of the product clicked on. |  [optional] [readonly] |
|**productLanguageCode** | **String** | Output only. The language (ISO-639-1) that has been set for the Merchant Center feed containing data about the product. |  [optional] [readonly] |
|**productStoreId** | **String** | Output only. The store in the Local Inventory Ad that was clicked on. This should match the store IDs used in your local products feed. |  [optional] [readonly] |
|**resourceName** | **String** | Output only. The resource name of the visit. Visit resource names have the form: &#x60;customers/{customer_id}/visits/{ad_group_id}~{criterion_id}~{ds_visit_id}&#x60; |  [optional] [readonly] |
|**visitDateTime** | **String** | Output only. The timestamp of the visit event. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. |  [optional] [readonly] |



## Enum: AssetFieldTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| HEADLINE | &quot;HEADLINE&quot; |
| DESCRIPTION | &quot;DESCRIPTION&quot; |
| MANDATORY_AD_TEXT | &quot;MANDATORY_AD_TEXT&quot; |
| MARKETING_IMAGE | &quot;MARKETING_IMAGE&quot; |
| MEDIA_BUNDLE | &quot;MEDIA_BUNDLE&quot; |
| YOUTUBE_VIDEO | &quot;YOUTUBE_VIDEO&quot; |
| BOOK_ON_GOOGLE | &quot;BOOK_ON_GOOGLE&quot; |
| LEAD_FORM | &quot;LEAD_FORM&quot; |
| PROMOTION | &quot;PROMOTION&quot; |
| CALLOUT | &quot;CALLOUT&quot; |
| STRUCTURED_SNIPPET | &quot;STRUCTURED_SNIPPET&quot; |
| SITELINK | &quot;SITELINK&quot; |
| MOBILE_APP | &quot;MOBILE_APP&quot; |
| HOTEL_CALLOUT | &quot;HOTEL_CALLOUT&quot; |
| CALL | &quot;CALL&quot; |
| PRICE | &quot;PRICE&quot; |
| LONG_HEADLINE | &quot;LONG_HEADLINE&quot; |
| BUSINESS_NAME | &quot;BUSINESS_NAME&quot; |
| SQUARE_MARKETING_IMAGE | &quot;SQUARE_MARKETING_IMAGE&quot; |
| PORTRAIT_MARKETING_IMAGE | &quot;PORTRAIT_MARKETING_IMAGE&quot; |
| LOGO | &quot;LOGO&quot; |
| LANDSCAPE_LOGO | &quot;LANDSCAPE_LOGO&quot; |
| VIDEO | &quot;VIDEO&quot; |
| CALL_TO_ACTION_SELECTION | &quot;CALL_TO_ACTION_SELECTION&quot; |
| AD_IMAGE | &quot;AD_IMAGE&quot; |
| BUSINESS_LOGO | &quot;BUSINESS_LOGO&quot; |
| HOTEL_PROPERTY | &quot;HOTEL_PROPERTY&quot; |



## Enum: ProductChannelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ONLINE | &quot;ONLINE&quot; |
| LOCAL | &quot;LOCAL&quot; |



