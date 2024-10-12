

# GoogleAdsSearchads360V0ResourcesAdGroupCriterion

An ad group criterion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroup** | **String** | Immutable. The ad group to which the criterion belongs. |  [optional] |
|**ageRange** | [**GoogleAdsSearchads360V0CommonAgeRangeInfo**](GoogleAdsSearchads360V0CommonAgeRangeInfo.md) |  |  [optional] |
|**bidModifier** | **Double** | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. |  [optional] |
|**cpcBidMicros** | **String** | The CPC (cost-per-click) bid. |  [optional] |
|**creationTime** | **String** | Output only. The timestamp when this ad group criterion was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. |  [optional] [readonly] |
|**criterionId** | **String** | Output only. The ID of the criterion. |  [optional] [readonly] |
|**effectiveCpcBidMicros** | **String** | Output only. The effective CPC (cost-per-click) bid. |  [optional] [readonly] |
|**engineId** | **String** | Output only. ID of the ad group criterion in the external engine account. This field is for non-Google Ads account only, for example, Yahoo Japan, Microsoft, Baidu etc. For Google Ads entity, use \&quot;ad_group_criterion.criterion_id\&quot; instead. |  [optional] [readonly] |
|**engineStatus** | [**EngineStatusEnum**](#EngineStatusEnum) | Output only. The Engine Status for ad group criterion. |  [optional] [readonly] |
|**finalUrlSuffix** | **String** | URL template for appending params to final URL. |  [optional] |
|**finalUrls** | **List&lt;String&gt;** | The list of possible final URLs after all cross-domain redirects for the ad. |  [optional] |
|**gender** | [**GoogleAdsSearchads360V0CommonGenderInfo**](GoogleAdsSearchads360V0CommonGenderInfo.md) |  |  [optional] |
|**keyword** | [**GoogleAdsSearchads360V0CommonKeywordInfo**](GoogleAdsSearchads360V0CommonKeywordInfo.md) |  |  [optional] |
|**labels** | **List&lt;String&gt;** | Output only. The resource names of labels attached to this ad group criterion. |  [optional] [readonly] |
|**lastModifiedTime** | **String** | Output only. The datetime when this ad group criterion was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**listingGroup** | [**GoogleAdsSearchads360V0CommonListingGroupInfo**](GoogleAdsSearchads360V0CommonListingGroupInfo.md) |  |  [optional] |
|**location** | [**GoogleAdsSearchads360V0CommonLocationInfo**](GoogleAdsSearchads360V0CommonLocationInfo.md) |  |  [optional] |
|**negative** | **Boolean** | Immutable. Whether to target (&#x60;false&#x60;) or exclude (&#x60;true&#x60;) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. |  [optional] |
|**positionEstimates** | [**GoogleAdsSearchads360V0ResourcesAdGroupCriterionPositionEstimates**](GoogleAdsSearchads360V0ResourcesAdGroupCriterionPositionEstimates.md) |  |  [optional] |
|**qualityInfo** | [**GoogleAdsSearchads360V0ResourcesAdGroupCriterionQualityInfo**](GoogleAdsSearchads360V0ResourcesAdGroupCriterionQualityInfo.md) |  |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the ad group criterion. Ad group criterion resource names have the form: &#x60;customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the criterion. This is the status of the ad group criterion entity, set by the client. Note: UI reports may incorporate additional information that affects whether a criterion is eligible to run. In some cases a criterion that&#39;s REMOVED in the API can still show as enabled in the UI. For example, campaigns by default show to users of all age ranges unless excluded. The UI will show each age range as \&quot;enabled\&quot;, since they&#39;re eligible to see the ads; but AdGroupCriterion.status will show \&quot;removed\&quot;, since no positive criterion was added. |  [optional] |
|**trackingUrlTemplate** | **String** | The URL template for constructing a tracking URL. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the criterion. |  [optional] [readonly] |
|**userList** | [**GoogleAdsSearchads360V0CommonUserListInfo**](GoogleAdsSearchads360V0CommonUserListInfo.md) |  |  [optional] |
|**webpage** | [**GoogleAdsSearchads360V0CommonWebpageInfo**](GoogleAdsSearchads360V0CommonWebpageInfo.md) |  |  [optional] |



## Enum: EngineStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| AD_GROUP_CRITERION_ELIGIBLE | &quot;AD_GROUP_CRITERION_ELIGIBLE&quot; |
| AD_GROUP_CRITERION_INAPPROPRIATE_FOR_CAMPAIGN | &quot;AD_GROUP_CRITERION_INAPPROPRIATE_FOR_CAMPAIGN&quot; |
| AD_GROUP_CRITERION_INVALID_MOBILE_SEARCH | &quot;AD_GROUP_CRITERION_INVALID_MOBILE_SEARCH&quot; |
| AD_GROUP_CRITERION_INVALID_PC_SEARCH | &quot;AD_GROUP_CRITERION_INVALID_PC_SEARCH&quot; |
| AD_GROUP_CRITERION_INVALID_SEARCH | &quot;AD_GROUP_CRITERION_INVALID_SEARCH&quot; |
| AD_GROUP_CRITERION_LOW_SEARCH_VOLUME | &quot;AD_GROUP_CRITERION_LOW_SEARCH_VOLUME&quot; |
| AD_GROUP_CRITERION_MOBILE_URL_UNDER_REVIEW | &quot;AD_GROUP_CRITERION_MOBILE_URL_UNDER_REVIEW&quot; |
| AD_GROUP_CRITERION_PARTIALLY_INVALID | &quot;AD_GROUP_CRITERION_PARTIALLY_INVALID&quot; |
| AD_GROUP_CRITERION_TO_BE_ACTIVATED | &quot;AD_GROUP_CRITERION_TO_BE_ACTIVATED&quot; |
| AD_GROUP_CRITERION_UNDER_REVIEW | &quot;AD_GROUP_CRITERION_UNDER_REVIEW&quot; |
| AD_GROUP_CRITERION_NOT_REVIEWED | &quot;AD_GROUP_CRITERION_NOT_REVIEWED&quot; |
| AD_GROUP_CRITERION_ON_HOLD | &quot;AD_GROUP_CRITERION_ON_HOLD&quot; |
| AD_GROUP_CRITERION_PENDING_REVIEW | &quot;AD_GROUP_CRITERION_PENDING_REVIEW&quot; |
| AD_GROUP_CRITERION_PAUSED | &quot;AD_GROUP_CRITERION_PAUSED&quot; |
| AD_GROUP_CRITERION_REMOVED | &quot;AD_GROUP_CRITERION_REMOVED&quot; |
| AD_GROUP_CRITERION_APPROVED | &quot;AD_GROUP_CRITERION_APPROVED&quot; |
| AD_GROUP_CRITERION_DISAPPROVED | &quot;AD_GROUP_CRITERION_DISAPPROVED&quot; |
| AD_GROUP_CRITERION_SERVING | &quot;AD_GROUP_CRITERION_SERVING&quot; |
| AD_GROUP_CRITERION_ACCOUNT_PAUSED | &quot;AD_GROUP_CRITERION_ACCOUNT_PAUSED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| REMOVED | &quot;REMOVED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| KEYWORD | &quot;KEYWORD&quot; |
| PLACEMENT | &quot;PLACEMENT&quot; |
| MOBILE_APP_CATEGORY | &quot;MOBILE_APP_CATEGORY&quot; |
| MOBILE_APPLICATION | &quot;MOBILE_APPLICATION&quot; |
| DEVICE | &quot;DEVICE&quot; |
| LOCATION | &quot;LOCATION&quot; |
| LISTING_GROUP | &quot;LISTING_GROUP&quot; |
| AD_SCHEDULE | &quot;AD_SCHEDULE&quot; |
| AGE_RANGE | &quot;AGE_RANGE&quot; |
| GENDER | &quot;GENDER&quot; |
| INCOME_RANGE | &quot;INCOME_RANGE&quot; |
| PARENTAL_STATUS | &quot;PARENTAL_STATUS&quot; |
| YOUTUBE_VIDEO | &quot;YOUTUBE_VIDEO&quot; |
| YOUTUBE_CHANNEL | &quot;YOUTUBE_CHANNEL&quot; |
| USER_LIST | &quot;USER_LIST&quot; |
| PROXIMITY | &quot;PROXIMITY&quot; |
| TOPIC | &quot;TOPIC&quot; |
| LISTING_SCOPE | &quot;LISTING_SCOPE&quot; |
| LANGUAGE | &quot;LANGUAGE&quot; |
| IP_BLOCK | &quot;IP_BLOCK&quot; |
| CONTENT_LABEL | &quot;CONTENT_LABEL&quot; |
| CARRIER | &quot;CARRIER&quot; |
| USER_INTEREST | &quot;USER_INTEREST&quot; |
| WEBPAGE | &quot;WEBPAGE&quot; |
| OPERATING_SYSTEM_VERSION | &quot;OPERATING_SYSTEM_VERSION&quot; |
| APP_PAYMENT_MODEL | &quot;APP_PAYMENT_MODEL&quot; |
| MOBILE_DEVICE | &quot;MOBILE_DEVICE&quot; |
| CUSTOM_AFFINITY | &quot;CUSTOM_AFFINITY&quot; |
| CUSTOM_INTENT | &quot;CUSTOM_INTENT&quot; |
| LOCATION_GROUP | &quot;LOCATION_GROUP&quot; |
| CUSTOM_AUDIENCE | &quot;CUSTOM_AUDIENCE&quot; |
| COMBINED_AUDIENCE | &quot;COMBINED_AUDIENCE&quot; |
| KEYWORD_THEME | &quot;KEYWORD_THEME&quot; |
| AUDIENCE | &quot;AUDIENCE&quot; |
| LOCAL_SERVICE_ID | &quot;LOCAL_SERVICE_ID&quot; |
| BRAND | &quot;BRAND&quot; |
| BRAND_LIST | &quot;BRAND_LIST&quot; |



