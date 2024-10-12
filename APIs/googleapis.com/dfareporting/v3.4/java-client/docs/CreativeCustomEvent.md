

# CreativeCustomEvent

Creative Custom Event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserCustomEventId** | **String** | Unique ID of this event used by Reporting and Data Transfer. This is a read-only field. |  [optional] |
|**advertiserCustomEventName** | **String** | User-entered name for the event. |  [optional] |
|**advertiserCustomEventType** | [**AdvertiserCustomEventTypeEnum**](#AdvertiserCustomEventTypeEnum) | Type of the event. This is a read-only field. |  [optional] |
|**artworkLabel** | **String** | Artwork label column, used to link events in Campaign Manager back to events in Studio. This is a required field and should not be modified after insertion. |  [optional] |
|**artworkType** | [**ArtworkTypeEnum**](#ArtworkTypeEnum) | Artwork type used by the creative.This is a read-only field. |  [optional] |
|**exitClickThroughUrl** | [**CreativeClickThroughUrl**](CreativeClickThroughUrl.md) |  |  [optional] |
|**id** | **String** | ID of this event. This is a required field and should not be modified after insertion. |  [optional] |
|**popupWindowProperties** | [**PopupWindowProperties**](PopupWindowProperties.md) |  |  [optional] |
|**targetType** | [**TargetTypeEnum**](#TargetTypeEnum) | Target type used by the event. |  [optional] |
|**videoReportingId** | **String** | Video reporting ID, used to differentiate multiple videos in a single creative. This is a read-only field. |  [optional] |



## Enum: AdvertiserCustomEventTypeEnum

| Name | Value |
|---- | -----|
| TIMER | &quot;ADVERTISER_EVENT_TIMER&quot; |
| EXIT | &quot;ADVERTISER_EVENT_EXIT&quot; |
| COUNTER | &quot;ADVERTISER_EVENT_COUNTER&quot; |



## Enum: ArtworkTypeEnum

| Name | Value |
|---- | -----|
| FLASH | &quot;ARTWORK_TYPE_FLASH&quot; |
| HTML5 | &quot;ARTWORK_TYPE_HTML5&quot; |
| MIXED | &quot;ARTWORK_TYPE_MIXED&quot; |
| IMAGE | &quot;ARTWORK_TYPE_IMAGE&quot; |



## Enum: TargetTypeEnum

| Name | Value |
|---- | -----|
| BLANK | &quot;TARGET_BLANK&quot; |
| TOP | &quot;TARGET_TOP&quot; |
| SELF | &quot;TARGET_SELF&quot; |
| PARENT | &quot;TARGET_PARENT&quot; |
| POPUP | &quot;TARGET_POPUP&quot; |



