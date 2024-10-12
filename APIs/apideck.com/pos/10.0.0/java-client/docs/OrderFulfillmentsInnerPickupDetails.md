

# OrderFulfillmentsInnerPickupDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**autoCompleteDuration** | **String** | The duration of time after which an open and accepted pickup fulfillment is automatically moved to the COMPLETED state. The duration must be in RFC 3339 format (for example, &#39;P1W3D&#39;). |  [optional] |
|**cancelReason** | **String** | A description of why the pickup was canceled. |  [optional] |
|**canceledAt** | **OffsetDateTime** | Indicating when the fulfillment was canceled. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). |  [optional] |
|**curbsidePickupDetails** | [**OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails**](OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails.md) |  |  [optional] |
|**expiredAt** | **OffsetDateTime** | Indicating when the fulfillment expired. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). |  [optional] |
|**expiresAt** | **OffsetDateTime** | Indicating when this fulfillment expires if it is not accepted. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). The expiration time can only be set up to 7 days in the future. If &#x60;expires_at&#x60; is not set, this pickup fulfillment is automatically accepted when  placed. |  [optional] |
|**isCurbsidePickup** | **Boolean** | If set to &#x60;true&#x60;, indicates that this pickup order is for curbside pickup, not in-store pickup. |  [optional] |
|**note** | **String** | A note meant to provide additional instructions about the pickup fulfillment displayed in the Square Point of Sale application and set by the API. |  [optional] |
|**pickedUpAt** | **OffsetDateTime** | Indicating when the fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). |  [optional] |
|**pickupAt** | **OffsetDateTime** | The timestamp that represents the start of the pickup window. Must be in RFC 3339 timestamp format, e.g.,  \&quot;2016-09-04T23:59:33.123Z\&quot;.  For fulfillments with the schedule type &#x60;ASAP&#x60;, this is automatically set to the current time plus the expected duration to prepare the fulfillment. |  [optional] |
|**pickupWindowDuration** | **String** | The window of time in which the order should be picked up after the &#x60;pickup_at&#x60; timestamp. Must be in RFC 3339 duration format, e.g., \&quot;P1W3D\&quot;. Can be used as an informational guideline for merchants. |  [optional] |
|**placedAt** | **OffsetDateTime** | Indicating when the fulfillment was placed. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). |  [optional] |
|**prepTimeDuration** | **String** | The duration of time it takes to prepare this fulfillment. The duration must be in RFC 3339 format (for example, \&quot;P1W3D\&quot;). |  [optional] |
|**readyAt** | **OffsetDateTime** | Indicating when the fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). |  [optional] |
|**recipient** | [**OrderFulfillmentsInnerPickupDetailsRecipient**](OrderFulfillmentsInnerPickupDetailsRecipient.md) |  |  [optional] |
|**rejectedAt** | **OffsetDateTime** | Indicating when the fulfillment was rejected. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). |  [optional] |
|**scheduleType** | [**ScheduleTypeEnum**](#ScheduleTypeEnum) | The schedule type of the pickup fulfillment. |  [optional] |



## Enum: ScheduleTypeEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;scheduled&quot; |



