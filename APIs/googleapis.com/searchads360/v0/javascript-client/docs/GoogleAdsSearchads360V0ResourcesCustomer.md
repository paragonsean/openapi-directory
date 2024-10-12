# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCustomer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountStatus** | **String** | Output only. Account status, for example, Enabled, Paused, Removed, etc. | [optional] [readonly] 
**accountType** | **String** | Output only. Engine account type, for example, Google Ads, Microsoft Advertising, Yahoo Japan, Baidu, Facebook, Engine Track, etc. | [optional] [readonly] 
**autoTaggingEnabled** | **Boolean** | Whether auto-tagging is enabled for the customer. | [optional] 
**conversionTrackingSetting** | [**GoogleAdsSearchads360V0ResourcesConversionTrackingSetting**](GoogleAdsSearchads360V0ResourcesConversionTrackingSetting.md) |  | [optional] 
**creationTime** | **String** | Output only. The timestamp when this customer was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. | [optional] [readonly] 
**currencyCode** | **String** | Immutable. The currency in which the account operates. A subset of the currency codes from the ISO 4217 standard is supported. | [optional] 
**descriptiveName** | **String** | Optional, non-unique descriptive name of the customer. | [optional] 
**doubleClickCampaignManagerSetting** | [**GoogleAdsSearchads360V0ResourcesDoubleClickCampaignManagerSetting**](GoogleAdsSearchads360V0ResourcesDoubleClickCampaignManagerSetting.md) |  | [optional] 
**engineId** | **String** | Output only. ID of the account in the external engine account. | [optional] [readonly] 
**finalUrlSuffix** | **String** | The URL template for appending params to the final URL. | [optional] 
**id** | **String** | Output only. The ID of the customer. | [optional] [readonly] 
**lastModifiedTime** | **String** | Output only. The datetime when this customer was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**manager** | **Boolean** | Output only. Whether the customer is a manager. | [optional] [readonly] 
**resourceName** | **String** | Immutable. The resource name of the customer. Customer resource names have the form: &#x60;customers/{customer_id}&#x60; | [optional] 
**status** | **String** | Output only. The status of the customer. | [optional] [readonly] 
**timeZone** | **String** | Immutable. The local timezone ID of the customer. | [optional] 
**trackingUrlTemplate** | **String** | The URL template for constructing a tracking URL out of parameters. | [optional] 



## Enum: AccountStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `REMOVED` (value: `"REMOVED"`)

* `DRAFT` (value: `"DRAFT"`)





## Enum: AccountTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `BAIDU` (value: `"BAIDU"`)

* `ENGINE_TRACK` (value: `"ENGINE_TRACK"`)

* `FACEBOOK` (value: `"FACEBOOK"`)

* `FACEBOOK_GATEWAY` (value: `"FACEBOOK_GATEWAY"`)

* `GOOGLE_ADS` (value: `"GOOGLE_ADS"`)

* `MICROSOFT` (value: `"MICROSOFT"`)

* `SEARCH_ADS_360` (value: `"SEARCH_ADS_360"`)

* `YAHOO_JAPAN` (value: `"YAHOO_JAPAN"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `CANCELED` (value: `"CANCELED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `CLOSED` (value: `"CLOSED"`)




