# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAdGroupCriterion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroup** | **String** | Immutable. The ad group to which the criterion belongs. | [optional] 
**ageRange** | [**GoogleAdsSearchads360V0CommonAgeRangeInfo**](GoogleAdsSearchads360V0CommonAgeRangeInfo.md) |  | [optional] 
**bidModifier** | **Number** | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. | [optional] 
**cpcBidMicros** | **String** | The CPC (cost-per-click) bid. | [optional] 
**creationTime** | **String** | Output only. The timestamp when this ad group criterion was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. | [optional] [readonly] 
**criterionId** | **String** | Output only. The ID of the criterion. | [optional] [readonly] 
**effectiveCpcBidMicros** | **String** | Output only. The effective CPC (cost-per-click) bid. | [optional] [readonly] 
**engineId** | **String** | Output only. ID of the ad group criterion in the external engine account. This field is for non-Google Ads account only, for example, Yahoo Japan, Microsoft, Baidu etc. For Google Ads entity, use \&quot;ad_group_criterion.criterion_id\&quot; instead. | [optional] [readonly] 
**engineStatus** | **String** | Output only. The Engine Status for ad group criterion. | [optional] [readonly] 
**finalUrlSuffix** | **String** | URL template for appending params to final URL. | [optional] 
**finalUrls** | **[String]** | The list of possible final URLs after all cross-domain redirects for the ad. | [optional] 
**gender** | [**GoogleAdsSearchads360V0CommonGenderInfo**](GoogleAdsSearchads360V0CommonGenderInfo.md) |  | [optional] 
**keyword** | [**GoogleAdsSearchads360V0CommonKeywordInfo**](GoogleAdsSearchads360V0CommonKeywordInfo.md) |  | [optional] 
**labels** | **[String]** | Output only. The resource names of labels attached to this ad group criterion. | [optional] [readonly] 
**lastModifiedTime** | **String** | Output only. The datetime when this ad group criterion was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**listingGroup** | [**GoogleAdsSearchads360V0CommonListingGroupInfo**](GoogleAdsSearchads360V0CommonListingGroupInfo.md) |  | [optional] 
**location** | [**GoogleAdsSearchads360V0CommonLocationInfo**](GoogleAdsSearchads360V0CommonLocationInfo.md) |  | [optional] 
**negative** | **Boolean** | Immutable. Whether to target (&#x60;false&#x60;) or exclude (&#x60;true&#x60;) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. | [optional] 
**positionEstimates** | [**GoogleAdsSearchads360V0ResourcesAdGroupCriterionPositionEstimates**](GoogleAdsSearchads360V0ResourcesAdGroupCriterionPositionEstimates.md) |  | [optional] 
**qualityInfo** | [**GoogleAdsSearchads360V0ResourcesAdGroupCriterionQualityInfo**](GoogleAdsSearchads360V0ResourcesAdGroupCriterionQualityInfo.md) |  | [optional] 
**resourceName** | **String** | Immutable. The resource name of the ad group criterion. Ad group criterion resource names have the form: &#x60;customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}&#x60; | [optional] 
**status** | **String** | The status of the criterion. This is the status of the ad group criterion entity, set by the client. Note: UI reports may incorporate additional information that affects whether a criterion is eligible to run. In some cases a criterion that&#39;s REMOVED in the API can still show as enabled in the UI. For example, campaigns by default show to users of all age ranges unless excluded. The UI will show each age range as \&quot;enabled\&quot;, since they&#39;re eligible to see the ads; but AdGroupCriterion.status will show \&quot;removed\&quot;, since no positive criterion was added. | [optional] 
**trackingUrlTemplate** | **String** | The URL template for constructing a tracking URL. | [optional] 
**type** | **String** | Output only. The type of the criterion. | [optional] [readonly] 
**userList** | [**GoogleAdsSearchads360V0CommonUserListInfo**](GoogleAdsSearchads360V0CommonUserListInfo.md) |  | [optional] 
**webpage** | [**GoogleAdsSearchads360V0CommonWebpageInfo**](GoogleAdsSearchads360V0CommonWebpageInfo.md) |  | [optional] 



## Enum: EngineStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `AD_GROUP_CRITERION_ELIGIBLE` (value: `"AD_GROUP_CRITERION_ELIGIBLE"`)

* `AD_GROUP_CRITERION_INAPPROPRIATE_FOR_CAMPAIGN` (value: `"AD_GROUP_CRITERION_INAPPROPRIATE_FOR_CAMPAIGN"`)

* `AD_GROUP_CRITERION_INVALID_MOBILE_SEARCH` (value: `"AD_GROUP_CRITERION_INVALID_MOBILE_SEARCH"`)

* `AD_GROUP_CRITERION_INVALID_PC_SEARCH` (value: `"AD_GROUP_CRITERION_INVALID_PC_SEARCH"`)

* `AD_GROUP_CRITERION_INVALID_SEARCH` (value: `"AD_GROUP_CRITERION_INVALID_SEARCH"`)

* `AD_GROUP_CRITERION_LOW_SEARCH_VOLUME` (value: `"AD_GROUP_CRITERION_LOW_SEARCH_VOLUME"`)

* `AD_GROUP_CRITERION_MOBILE_URL_UNDER_REVIEW` (value: `"AD_GROUP_CRITERION_MOBILE_URL_UNDER_REVIEW"`)

* `AD_GROUP_CRITERION_PARTIALLY_INVALID` (value: `"AD_GROUP_CRITERION_PARTIALLY_INVALID"`)

* `AD_GROUP_CRITERION_TO_BE_ACTIVATED` (value: `"AD_GROUP_CRITERION_TO_BE_ACTIVATED"`)

* `AD_GROUP_CRITERION_UNDER_REVIEW` (value: `"AD_GROUP_CRITERION_UNDER_REVIEW"`)

* `AD_GROUP_CRITERION_NOT_REVIEWED` (value: `"AD_GROUP_CRITERION_NOT_REVIEWED"`)

* `AD_GROUP_CRITERION_ON_HOLD` (value: `"AD_GROUP_CRITERION_ON_HOLD"`)

* `AD_GROUP_CRITERION_PENDING_REVIEW` (value: `"AD_GROUP_CRITERION_PENDING_REVIEW"`)

* `AD_GROUP_CRITERION_PAUSED` (value: `"AD_GROUP_CRITERION_PAUSED"`)

* `AD_GROUP_CRITERION_REMOVED` (value: `"AD_GROUP_CRITERION_REMOVED"`)

* `AD_GROUP_CRITERION_APPROVED` (value: `"AD_GROUP_CRITERION_APPROVED"`)

* `AD_GROUP_CRITERION_DISAPPROVED` (value: `"AD_GROUP_CRITERION_DISAPPROVED"`)

* `AD_GROUP_CRITERION_SERVING` (value: `"AD_GROUP_CRITERION_SERVING"`)

* `AD_GROUP_CRITERION_ACCOUNT_PAUSED` (value: `"AD_GROUP_CRITERION_ACCOUNT_PAUSED"`)





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




