

# FirstAndThirdPartyAudience

Describes a first or third party audience list used for targeting. First party audiences are created via usage of client data. Third party audiences are provided by Third Party data providers and can only be licensed to customers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeDisplayAudienceSize** | **String** | Output only. The estimated audience size for the Display network in the past month. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only returned in GET request. |  [optional] [readonly] |
|**appId** | **String** | The app_id matches with the type of the mobile_device_ids being uploaded. Only applicable to audience_type &#x60;CUSTOMER_MATCH_DEVICE_ID&#x60; |  [optional] |
|**audienceSource** | [**AudienceSourceEnum**](#AudienceSourceEnum) | Output only. The source of the audience. |  [optional] [readonly] |
|**audienceType** | [**AudienceTypeEnum**](#AudienceTypeEnum) | The type of the audience. |  [optional] |
|**contactInfoList** | [**ContactInfoList**](ContactInfoList.md) |  |  [optional] |
|**description** | **String** | The user-provided description of the audience. Only applicable to first party audiences. |  [optional] |
|**displayAudienceSize** | **String** | Output only. The estimated audience size for the Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only returned in GET request. |  [optional] [readonly] |
|**displayDesktopAudienceSize** | **String** | Output only. The estimated desktop audience size in Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |  [optional] [readonly] |
|**displayMobileAppAudienceSize** | **String** | Output only. The estimated mobile app audience size in Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |  [optional] [readonly] |
|**displayMobileWebAudienceSize** | **String** | Output only. The estimated mobile web audience size in Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |  [optional] [readonly] |
|**displayName** | **String** | The display name of the first and third party audience. |  [optional] |
|**firstAndThirdPartyAudienceId** | **String** | Output only. The unique ID of the first and third party audience. Assigned by the system. |  [optional] [readonly] |
|**firstAndThirdPartyAudienceType** | [**FirstAndThirdPartyAudienceTypeEnum**](#FirstAndThirdPartyAudienceTypeEnum) | Whether the audience is a first or third party audience. |  [optional] |
|**gmailAudienceSize** | **String** | Output only. The estimated audience size for Gmail network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |  [optional] [readonly] |
|**membershipDurationDays** | **String** | The duration in days that an entry remains in the audience after the qualifying event. If the audience has no expiration, set the value of this field to 10000. Otherwise, the set value must be greater than 0 and less than or equal to 540. Only applicable to first party audiences. This field is required if one of the following audience_type is used: * &#x60;CUSTOMER_MATCH_CONTACT_INFO&#x60; * &#x60;CUSTOMER_MATCH_DEVICE_ID&#x60; |  [optional] |
|**mobileDeviceIdList** | [**MobileDeviceIdList**](MobileDeviceIdList.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the first and third party audience. |  [optional] [readonly] |
|**youtubeAudienceSize** | **String** | Output only. The estimated audience size for YouTube network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |  [optional] [readonly] |



## Enum: AudienceSourceEnum

| Name | Value |
|---- | -----|
| AUDIENCE_SOURCE_UNSPECIFIED | &quot;AUDIENCE_SOURCE_UNSPECIFIED&quot; |
| DISPLAY_VIDEO_360 | &quot;DISPLAY_VIDEO_360&quot; |
| CAMPAIGN_MANAGER | &quot;CAMPAIGN_MANAGER&quot; |
| AD_MANAGER | &quot;AD_MANAGER&quot; |
| SEARCH_ADS_360 | &quot;SEARCH_ADS_360&quot; |
| YOUTUBE | &quot;YOUTUBE&quot; |
| ADS_DATA_HUB | &quot;ADS_DATA_HUB&quot; |



## Enum: AudienceTypeEnum

| Name | Value |
|---- | -----|
| AUDIENCE_TYPE_UNSPECIFIED | &quot;AUDIENCE_TYPE_UNSPECIFIED&quot; |
| CUSTOMER_MATCH_CONTACT_INFO | &quot;CUSTOMER_MATCH_CONTACT_INFO&quot; |
| CUSTOMER_MATCH_DEVICE_ID | &quot;CUSTOMER_MATCH_DEVICE_ID&quot; |
| CUSTOMER_MATCH_USER_ID | &quot;CUSTOMER_MATCH_USER_ID&quot; |
| ACTIVITY_BASED | &quot;ACTIVITY_BASED&quot; |
| FREQUENCY_CAP | &quot;FREQUENCY_CAP&quot; |
| TAG_BASED | &quot;TAG_BASED&quot; |
| YOUTUBE_USERS | &quot;YOUTUBE_USERS&quot; |
| LICENSED | &quot;LICENSED&quot; |



## Enum: FirstAndThirdPartyAudienceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_UNSPECIFIED&quot; |
| FIRST_PARTY | &quot;FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_FIRST_PARTY&quot; |
| THIRD_PARTY | &quot;FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_THIRD_PARTY&quot; |



