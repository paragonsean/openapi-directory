# DisplayVideo360Api.YoutubeAdGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupFormat** | **String** | The format of the ads in the ad group. | [optional] 
**adGroupId** | **String** | The unique ID of the ad group. Assigned by the system. | [optional] 
**advertiserId** | **String** | The unique ID of the advertiser the ad group belongs to. | [optional] 
**biddingStrategy** | [**YoutubeAndPartnersBiddingStrategy**](YoutubeAndPartnersBiddingStrategy.md) |  | [optional] 
**displayName** | **String** | The display name of the ad group. Must be UTF-8 encoded with a maximum size of 255 bytes. | [optional] 
**entityStatus** | **String** | Controls whether or not the ad group can spend its budget and bid on inventory. If the ad group&#39;s parent line item is not active, the ad group can&#39;t spend its budget even if its own status is &#x60;ENTITY_STATUS_ACTIVE&#x60;. | [optional] 
**lineItemId** | **String** | The unique ID of the line item that the ad group belongs to. | [optional] 
**name** | **String** | The resource name of the ad group. | [optional] 
**productFeedData** | [**ProductFeedData**](ProductFeedData.md) |  | [optional] 
**targetingExpansion** | [**TargetingExpansionConfig**](TargetingExpansionConfig.md) |  | [optional] 
**youtubeAdIds** | **[String]** | The IDs of the youtube_ad_group_ad resources associated with the ad group. | [optional] 



## Enum: AdGroupFormatEnum


* `UNSPECIFIED` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_UNSPECIFIED"`)

* `IN_STREAM` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_IN_STREAM"`)

* `VIDEO_DISCOVERY` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_VIDEO_DISCOVERY"`)

* `BUMPER` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_BUMPER"`)

* `NON_SKIPPABLE_IN_STREAM` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_NON_SKIPPABLE_IN_STREAM"`)

* `AUDIO` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_AUDIO"`)

* `ACTION` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_ACTION"`)

* `REACH` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_REACH"`)

* `MASTHEAD` (value: `"YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_MASTHEAD"`)





## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




