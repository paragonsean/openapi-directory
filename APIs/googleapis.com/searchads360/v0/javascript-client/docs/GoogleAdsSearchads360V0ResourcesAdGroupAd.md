# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAdGroupAd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad** | [**GoogleAdsSearchads360V0ResourcesAd**](GoogleAdsSearchads360V0ResourcesAd.md) |  | [optional] 
**creationTime** | **String** | Output only. The timestamp when this ad_group_ad was created. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**engineId** | **String** | Output only. ID of the ad in the external engine account. This field is for SearchAds 360 account only, for example, Yahoo Japan, Microsoft, Baidu etc. For non-SearchAds 360 entity, use \&quot;ad_group_ad.ad.id\&quot; instead. | [optional] [readonly] 
**engineStatus** | **String** | Output only. Additional status of the ad in the external engine account. Possible statuses (depending on the type of external account) include active, eligible, pending review, etc. | [optional] [readonly] 
**labels** | **[String]** | Output only. The resource names of labels attached to this ad group ad. | [optional] [readonly] 
**lastModifiedTime** | **String** | Output only. The datetime when this ad group ad was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**resourceName** | **String** | Immutable. The resource name of the ad. Ad group ad resource names have the form: &#x60;customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}&#x60; | [optional] 
**status** | **String** | The status of the ad. | [optional] 



## Enum: EngineStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `AD_GROUP_AD_ELIGIBLE` (value: `"AD_GROUP_AD_ELIGIBLE"`)

* `AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN` (value: `"AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN"`)

* `AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW` (value: `"AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW"`)

* `AD_GROUP_AD_PARTIALLY_INVALID` (value: `"AD_GROUP_AD_PARTIALLY_INVALID"`)

* `AD_GROUP_AD_TO_BE_ACTIVATED` (value: `"AD_GROUP_AD_TO_BE_ACTIVATED"`)

* `AD_GROUP_AD_NOT_REVIEWED` (value: `"AD_GROUP_AD_NOT_REVIEWED"`)

* `AD_GROUP_AD_ON_HOLD` (value: `"AD_GROUP_AD_ON_HOLD"`)

* `AD_GROUP_AD_PAUSED` (value: `"AD_GROUP_AD_PAUSED"`)

* `AD_GROUP_AD_REMOVED` (value: `"AD_GROUP_AD_REMOVED"`)

* `AD_GROUP_AD_PENDING_REVIEW` (value: `"AD_GROUP_AD_PENDING_REVIEW"`)

* `AD_GROUP_AD_UNDER_REVIEW` (value: `"AD_GROUP_AD_UNDER_REVIEW"`)

* `AD_GROUP_AD_APPROVED` (value: `"AD_GROUP_AD_APPROVED"`)

* `AD_GROUP_AD_DISAPPROVED` (value: `"AD_GROUP_AD_DISAPPROVED"`)

* `AD_GROUP_AD_SERVING` (value: `"AD_GROUP_AD_SERVING"`)

* `AD_GROUP_AD_ACCOUNT_PAUSED` (value: `"AD_GROUP_AD_ACCOUNT_PAUSED"`)

* `AD_GROUP_AD_CAMPAIGN_PAUSED` (value: `"AD_GROUP_AD_CAMPAIGN_PAUSED"`)

* `AD_GROUP_AD_AD_GROUP_PAUSED` (value: `"AD_GROUP_AD_AD_GROUP_PAUSED"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)

* `REMOVED` (value: `"REMOVED"`)




