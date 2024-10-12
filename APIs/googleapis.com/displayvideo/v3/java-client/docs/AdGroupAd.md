

# AdGroupAd

A single ad associated with an ad group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroupAdId** | **String** | The unique ID of the ad. Assigned by the system. |  [optional] |
|**adGroupId** | **String** | The unique ID of the ad group that the ad belongs to. |  [optional] |
|**adUrls** | [**List&lt;AdUrl&gt;**](AdUrl.md) | List of URLs used by the ad. |  [optional] |
|**advertiserId** | **String** | The unique ID of the advertiser the ad belongs to. |  [optional] |
|**audioAd** | [**AudioAd**](AudioAd.md) |  |  [optional] |
|**bumperAd** | [**BumperAd**](BumperAd.md) |  |  [optional] |
|**displayName** | **String** | The display name of the ad. Must be UTF-8 encoded with a maximum size of 255 bytes. |  [optional] |
|**displayVideoSourceAd** | [**DisplayVideoSourceAd**](DisplayVideoSourceAd.md) |  |  [optional] |
|**entityStatus** | [**EntityStatusEnum**](#EntityStatusEnum) | The entity status of the ad. |  [optional] |
|**inStreamAd** | [**InStreamAd**](InStreamAd.md) |  |  [optional] |
|**mastheadAd** | [**MastheadAd**](MastheadAd.md) |  |  [optional] |
|**name** | **String** | The resource name of the ad. |  [optional] |
|**nonSkippableAd** | [**NonSkippableAd**](NonSkippableAd.md) |  |  [optional] |
|**videoDiscoverAd** | [**VideoDiscoveryAd**](VideoDiscoveryAd.md) |  |  [optional] |
|**videoPerformanceAd** | [**VideoPerformanceAd**](VideoPerformanceAd.md) |  |  [optional] |



## Enum: EntityStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



