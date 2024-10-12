

# GoogleAdsSearchads360V0ResourcesCampaignCriterion

A campaign criterion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageRange** | [**GoogleAdsSearchads360V0CommonAgeRangeInfo**](GoogleAdsSearchads360V0CommonAgeRangeInfo.md) |  |  [optional] |
|**bidModifier** | **Float** | The modifier for the bids when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. Use 0 to opt out of a Device type. |  [optional] |
|**criterionId** | **String** | Output only. The ID of the criterion. This field is ignored during mutate. |  [optional] [readonly] |
|**device** | [**GoogleAdsSearchads360V0CommonDeviceInfo**](GoogleAdsSearchads360V0CommonDeviceInfo.md) |  |  [optional] |
|**displayName** | **String** | Output only. The display name of the criterion. This field is ignored for mutates. |  [optional] [readonly] |
|**gender** | [**GoogleAdsSearchads360V0CommonGenderInfo**](GoogleAdsSearchads360V0CommonGenderInfo.md) |  |  [optional] |
|**keyword** | [**GoogleAdsSearchads360V0CommonKeywordInfo**](GoogleAdsSearchads360V0CommonKeywordInfo.md) |  |  [optional] |
|**language** | [**GoogleAdsSearchads360V0CommonLanguageInfo**](GoogleAdsSearchads360V0CommonLanguageInfo.md) |  |  [optional] |
|**lastModifiedTime** | **String** | Output only. The datetime when this campaign criterion was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**location** | [**GoogleAdsSearchads360V0CommonLocationInfo**](GoogleAdsSearchads360V0CommonLocationInfo.md) |  |  [optional] |
|**locationGroup** | [**GoogleAdsSearchads360V0CommonLocationGroupInfo**](GoogleAdsSearchads360V0CommonLocationGroupInfo.md) |  |  [optional] |
|**negative** | **Boolean** | Immutable. Whether to target (&#x60;false&#x60;) or exclude (&#x60;true&#x60;) the criterion. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the campaign criterion. Campaign criterion resource names have the form: &#x60;customers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the criterion. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the criterion. |  [optional] [readonly] |
|**userList** | [**GoogleAdsSearchads360V0CommonUserListInfo**](GoogleAdsSearchads360V0CommonUserListInfo.md) |  |  [optional] |
|**webpage** | [**GoogleAdsSearchads360V0CommonWebpageInfo**](GoogleAdsSearchads360V0CommonWebpageInfo.md) |  |  [optional] |



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



