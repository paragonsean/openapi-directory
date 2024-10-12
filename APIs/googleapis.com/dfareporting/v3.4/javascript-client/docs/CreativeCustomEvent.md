# CampaignManager360Api.CreativeCustomEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserCustomEventId** | **String** | Unique ID of this event used by Reporting and Data Transfer. This is a read-only field. | [optional] 
**advertiserCustomEventName** | **String** | User-entered name for the event. | [optional] 
**advertiserCustomEventType** | **String** | Type of the event. This is a read-only field. | [optional] 
**artworkLabel** | **String** | Artwork label column, used to link events in Campaign Manager back to events in Studio. This is a required field and should not be modified after insertion. | [optional] 
**artworkType** | **String** | Artwork type used by the creative.This is a read-only field. | [optional] 
**exitClickThroughUrl** | [**CreativeClickThroughUrl**](CreativeClickThroughUrl.md) |  | [optional] 
**id** | **String** | ID of this event. This is a required field and should not be modified after insertion. | [optional] 
**popupWindowProperties** | [**PopupWindowProperties**](PopupWindowProperties.md) |  | [optional] 
**targetType** | **String** | Target type used by the event. | [optional] 
**videoReportingId** | **String** | Video reporting ID, used to differentiate multiple videos in a single creative. This is a read-only field. | [optional] 



## Enum: AdvertiserCustomEventTypeEnum


* `TIMER` (value: `"ADVERTISER_EVENT_TIMER"`)

* `EXIT` (value: `"ADVERTISER_EVENT_EXIT"`)

* `COUNTER` (value: `"ADVERTISER_EVENT_COUNTER"`)





## Enum: ArtworkTypeEnum


* `FLASH` (value: `"ARTWORK_TYPE_FLASH"`)

* `HTML5` (value: `"ARTWORK_TYPE_HTML5"`)

* `MIXED` (value: `"ARTWORK_TYPE_MIXED"`)

* `IMAGE` (value: `"ARTWORK_TYPE_IMAGE"`)





## Enum: TargetTypeEnum


* `BLANK` (value: `"TARGET_BLANK"`)

* `TOP` (value: `"TARGET_TOP"`)

* `SELF` (value: `"TARGET_SELF"`)

* `PARENT` (value: `"TARGET_PARENT"`)

* `POPUP` (value: `"TARGET_POPUP"`)




