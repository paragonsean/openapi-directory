

# TimeZone

The timezone ID and offset from Coordinated Universal Time (UTC). Only supported for the event types [`CARD_CLICKED`](https://developers.google.com/chat/api/reference/rest/v1/EventType#ENUM_VALUES.CARD_CLICKED) and [`SUBMIT_DIALOG`](https://developers.google.com/chat/api/reference/rest/v1/DialogEventType#ENUM_VALUES.SUBMIT_DIALOG).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The [IANA TZ](https://www.iana.org/time-zones) time zone database code, such as \&quot;America/Toronto\&quot;. |  [optional] |
|**offset** | **Integer** | The user timezone offset, in milliseconds, from Coordinated Universal Time (UTC). |  [optional] |



