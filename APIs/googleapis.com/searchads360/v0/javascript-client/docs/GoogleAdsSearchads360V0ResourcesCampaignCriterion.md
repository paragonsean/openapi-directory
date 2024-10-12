# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCampaignCriterion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ageRange** | [**GoogleAdsSearchads360V0CommonAgeRangeInfo**](GoogleAdsSearchads360V0CommonAgeRangeInfo.md) |  | [optional] 
**bidModifier** | **Number** | The modifier for the bids when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. Use 0 to opt out of a Device type. | [optional] 
**criterionId** | **String** | Output only. The ID of the criterion. This field is ignored during mutate. | [optional] [readonly] 
**device** | [**GoogleAdsSearchads360V0CommonDeviceInfo**](GoogleAdsSearchads360V0CommonDeviceInfo.md) |  | [optional] 
**displayName** | **String** | Output only. The display name of the criterion. This field is ignored for mutates. | [optional] [readonly] 
**gender** | [**GoogleAdsSearchads360V0CommonGenderInfo**](GoogleAdsSearchads360V0CommonGenderInfo.md) |  | [optional] 
**keyword** | [**GoogleAdsSearchads360V0CommonKeywordInfo**](GoogleAdsSearchads360V0CommonKeywordInfo.md) |  | [optional] 
**language** | [**GoogleAdsSearchads360V0CommonLanguageInfo**](GoogleAdsSearchads360V0CommonLanguageInfo.md) |  | [optional] 
**lastModifiedTime** | **String** | Output only. The datetime when this campaign criterion was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**location** | [**GoogleAdsSearchads360V0CommonLocationInfo**](GoogleAdsSearchads360V0CommonLocationInfo.md) |  | [optional] 
**locationGroup** | [**GoogleAdsSearchads360V0CommonLocationGroupInfo**](GoogleAdsSearchads360V0CommonLocationGroupInfo.md) |  | [optional] 
**negative** | **Boolean** | Immutable. Whether to target (&#x60;false&#x60;) or exclude (&#x60;true&#x60;) the criterion. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the campaign criterion. Campaign criterion resource names have the form: &#x60;customers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}&#x60; | [optional] 
**status** | **String** | The status of the criterion. | [optional] 
**type** | **String** | Output only. The type of the criterion. | [optional] [readonly] 
**userList** | [**GoogleAdsSearchads360V0CommonUserListInfo**](GoogleAdsSearchads360V0CommonUserListInfo.md) |  | [optional] 
**webpage** | [**GoogleAdsSearchads360V0CommonWebpageInfo**](GoogleAdsSearchads360V0CommonWebpageInfo.md) |  | [optional] 



## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)

* `REMOVED` (value: `"REMOVED"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `KEYWORD` (value: `"KEYWORD"`)

* `PLACEMENT` (value: `"PLACEMENT"`)

* `MOBILE_APP_CATEGORY` (value: `"MOBILE_APP_CATEGORY"`)

* `MOBILE_APPLICATION` (value: `"MOBILE_APPLICATION"`)

* `DEVICE` (value: `"DEVICE"`)

* `LOCATION` (value: `"LOCATION"`)

* `LISTING_GROUP` (value: `"LISTING_GROUP"`)

* `AD_SCHEDULE` (value: `"AD_SCHEDULE"`)

* `AGE_RANGE` (value: `"AGE_RANGE"`)

* `GENDER` (value: `"GENDER"`)

* `INCOME_RANGE` (value: `"INCOME_RANGE"`)

* `PARENTAL_STATUS` (value: `"PARENTAL_STATUS"`)

* `YOUTUBE_VIDEO` (value: `"YOUTUBE_VIDEO"`)

* `YOUTUBE_CHANNEL` (value: `"YOUTUBE_CHANNEL"`)

* `USER_LIST` (value: `"USER_LIST"`)

* `PROXIMITY` (value: `"PROXIMITY"`)

* `TOPIC` (value: `"TOPIC"`)

* `LISTING_SCOPE` (value: `"LISTING_SCOPE"`)

* `LANGUAGE` (value: `"LANGUAGE"`)

* `IP_BLOCK` (value: `"IP_BLOCK"`)

* `CONTENT_LABEL` (value: `"CONTENT_LABEL"`)

* `CARRIER` (value: `"CARRIER"`)

* `USER_INTEREST` (value: `"USER_INTEREST"`)

* `WEBPAGE` (value: `"WEBPAGE"`)

* `OPERATING_SYSTEM_VERSION` (value: `"OPERATING_SYSTEM_VERSION"`)

* `APP_PAYMENT_MODEL` (value: `"APP_PAYMENT_MODEL"`)

* `MOBILE_DEVICE` (value: `"MOBILE_DEVICE"`)

* `CUSTOM_AFFINITY` (value: `"CUSTOM_AFFINITY"`)

* `CUSTOM_INTENT` (value: `"CUSTOM_INTENT"`)

* `LOCATION_GROUP` (value: `"LOCATION_GROUP"`)

* `CUSTOM_AUDIENCE` (value: `"CUSTOM_AUDIENCE"`)

* `COMBINED_AUDIENCE` (value: `"COMBINED_AUDIENCE"`)

* `KEYWORD_THEME` (value: `"KEYWORD_THEME"`)

* `AUDIENCE` (value: `"AUDIENCE"`)

* `LOCAL_SERVICE_ID` (value: `"LOCAL_SERVICE_ID"`)

* `BRAND` (value: `"BRAND"`)

* `BRAND_LIST` (value: `"BRAND_LIST"`)




