# DisplayVideo360Api.AdGroupAd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupAdId** | **String** | The unique ID of the ad. Assigned by the system. | [optional] 
**adGroupId** | **String** | The unique ID of the ad group that the ad belongs to. | [optional] 
**adUrls** | [**[AdUrl]**](AdUrl.md) | List of URLs used by the ad. | [optional] 
**advertiserId** | **String** | The unique ID of the advertiser the ad belongs to. | [optional] 
**audioAd** | [**AudioAd**](AudioAd.md) |  | [optional] 
**bumperAd** | [**BumperAd**](BumperAd.md) |  | [optional] 
**displayName** | **String** | The display name of the ad. Must be UTF-8 encoded with a maximum size of 255 bytes. | [optional] 
**displayVideoSourceAd** | [**DisplayVideoSourceAd**](DisplayVideoSourceAd.md) |  | [optional] 
**entityStatus** | **String** | The entity status of the ad. | [optional] 
**inStreamAd** | [**InStreamAd**](InStreamAd.md) |  | [optional] 
**mastheadAd** | [**MastheadAd**](MastheadAd.md) |  | [optional] 
**name** | **String** | The resource name of the ad. | [optional] 
**nonSkippableAd** | [**NonSkippableAd**](NonSkippableAd.md) |  | [optional] 
**videoDiscoverAd** | [**VideoDiscoveryAd**](VideoDiscoveryAd.md) |  | [optional] 
**videoPerformanceAd** | [**VideoPerformanceAd**](VideoPerformanceAd.md) |  | [optional] 



## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




