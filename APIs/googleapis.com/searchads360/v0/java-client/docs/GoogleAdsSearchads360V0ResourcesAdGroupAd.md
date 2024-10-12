

# GoogleAdsSearchads360V0ResourcesAdGroupAd

An ad group ad.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ad** | [**GoogleAdsSearchads360V0ResourcesAd**](GoogleAdsSearchads360V0ResourcesAd.md) |  |  [optional] |
|**creationTime** | **String** | Output only. The timestamp when this ad_group_ad was created. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**engineId** | **String** | Output only. ID of the ad in the external engine account. This field is for SearchAds 360 account only, for example, Yahoo Japan, Microsoft, Baidu etc. For non-SearchAds 360 entity, use \&quot;ad_group_ad.ad.id\&quot; instead. |  [optional] [readonly] |
|**engineStatus** | [**EngineStatusEnum**](#EngineStatusEnum) | Output only. Additional status of the ad in the external engine account. Possible statuses (depending on the type of external account) include active, eligible, pending review, etc. |  [optional] [readonly] |
|**labels** | **List&lt;String&gt;** | Output only. The resource names of labels attached to this ad group ad. |  [optional] [readonly] |
|**lastModifiedTime** | **String** | Output only. The datetime when this ad group ad was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**resourceName** | **String** | Immutable. The resource name of the ad. Ad group ad resource names have the form: &#x60;customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the ad. |  [optional] |



## Enum: EngineStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| AD_GROUP_AD_ELIGIBLE | &quot;AD_GROUP_AD_ELIGIBLE&quot; |
| AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN | &quot;AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN&quot; |
| AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW | &quot;AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW&quot; |
| AD_GROUP_AD_PARTIALLY_INVALID | &quot;AD_GROUP_AD_PARTIALLY_INVALID&quot; |
| AD_GROUP_AD_TO_BE_ACTIVATED | &quot;AD_GROUP_AD_TO_BE_ACTIVATED&quot; |
| AD_GROUP_AD_NOT_REVIEWED | &quot;AD_GROUP_AD_NOT_REVIEWED&quot; |
| AD_GROUP_AD_ON_HOLD | &quot;AD_GROUP_AD_ON_HOLD&quot; |
| AD_GROUP_AD_PAUSED | &quot;AD_GROUP_AD_PAUSED&quot; |
| AD_GROUP_AD_REMOVED | &quot;AD_GROUP_AD_REMOVED&quot; |
| AD_GROUP_AD_PENDING_REVIEW | &quot;AD_GROUP_AD_PENDING_REVIEW&quot; |
| AD_GROUP_AD_UNDER_REVIEW | &quot;AD_GROUP_AD_UNDER_REVIEW&quot; |
| AD_GROUP_AD_APPROVED | &quot;AD_GROUP_AD_APPROVED&quot; |
| AD_GROUP_AD_DISAPPROVED | &quot;AD_GROUP_AD_DISAPPROVED&quot; |
| AD_GROUP_AD_SERVING | &quot;AD_GROUP_AD_SERVING&quot; |
| AD_GROUP_AD_ACCOUNT_PAUSED | &quot;AD_GROUP_AD_ACCOUNT_PAUSED&quot; |
| AD_GROUP_AD_CAMPAIGN_PAUSED | &quot;AD_GROUP_AD_CAMPAIGN_PAUSED&quot; |
| AD_GROUP_AD_AD_GROUP_PAUSED | &quot;AD_GROUP_AD_AD_GROUP_PAUSED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| REMOVED | &quot;REMOVED&quot; |



