

# DeliveryReport

~

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignId** | **Long** | ~ |  [optional] |
|**carrier** | **String** | ~ |  [optional] |
|**deliveryCategory** | [**DeliveryCategoryEnum**](#DeliveryCategoryEnum) | ~ |  [optional] |
|**deliveryState** | [**DeliveryStateEnum**](#DeliveryStateEnum) | ~ |  [optional] |
|**fromNumber** | **String** | ~ |  [optional] |
|**messageText** | **String** | ~ |  [optional] |
|**toNumber** | **String** | ~ |  [optional] |
|**updated** | **OffsetDateTime** | ~ |  [optional] |



## Enum: DeliveryCategoryEnum

| Name | Value |
|---- | -----|
| NO_DATA | &quot;NO_DATA&quot; |
| OPTED_OUT | &quot;OPTED_OUT&quot; |
| BOUNCED | &quot;BOUNCED&quot; |
| NO_CREDITS | &quot;NO_CREDITS&quot; |
| DELIVERED | &quot;DELIVERED&quot; |



## Enum: DeliveryStateEnum

| Name | Value |
|---- | -----|
| DELIVERED | &quot;DELIVERED&quot; |
| UNSENT_OPTED_OUT_GLOBAL | &quot;UNSENT_OPTED_OUT_GLOBAL&quot; |
| UNSENT_OPTED_OUT_LOCAL | &quot;UNSENT_OPTED_OUT_LOCAL&quot; |
| UNSENT_NO_CREDITS | &quot;UNSENT_NO_CREDITS&quot; |
| GATEWAY_REJECTED | &quot;GATEWAY_REJECTED&quot; |
| CARRIER_REJECTED | &quot;CARRIER_REJECTED&quot; |
| NOT_DELIVERED | &quot;NOT_DELIVERED&quot; |
| UNSENT_INVALID_NUMBER | &quot;UNSENT_INVALID_NUMBER&quot; |
| UNSENT_BAD_DATA | &quot;UNSENT_BAD_DATA&quot; |
| UNSENT_FORCE_STOPPED | &quot;UNSENT_FORCE_STOPPED&quot; |
| UNSENT_PERIOD_LIMIT | &quot;UNSENT_PERIOD_LIMIT&quot; |
| UNSENT_INTERNATIONAL | &quot;UNSENT_INTERNATIONAL&quot; |
| UNSENT_INVALID_TIMEZONE_OR_DNC | &quot;UNSENT_INVALID_TIMEZONE_OR_DNC&quot; |
| UNSENT_ALREADY_SCRUBBED | &quot;UNSENT_ALREADY_SCRUBBED&quot; |
| UNSENT_SYSTEM_ERROR | &quot;UNSENT_SYSTEM_ERROR&quot; |
| UNSENT_NO_WIRELESS_CARRIER | &quot;UNSENT_NO_WIRELESS_CARRIER&quot; |
| UNSENT_MESSAGE_TOO_LONG | &quot;UNSENT_MESSAGE_TOO_LONG&quot; |
| UNSENT_MESSAGE_BLOCKED | &quot;UNSENT_MESSAGE_BLOCKED&quot; |
| UNSENT_QUEUE_LIMIT_REACHED | &quot;UNSENT_QUEUE_LIMIT_REACHED&quot; |
| UNSENT_TOKEN_LIMIT_REACHED | &quot;UNSENT_TOKEN_LIMIT_REACHED&quot; |
| UNSENT_TIME_LIMIT_REACHED | &quot;UNSENT_TIME_LIMIT_REACHED&quot; |
| UNSENT_SCHEDULER_CAPACITY_EXCEEDED | &quot;UNSENT_SCHEDULER_CAPACITY_EXCEEDED&quot; |
| SPAM_DETECTED | &quot;SPAM_DETECTED&quot; |
| UNSENT_NO_GATEWAY | &quot;UNSENT_NO_GATEWAY&quot; |
| UNSENT_DAILY_LIMIT_REACHED | &quot;UNSENT_DAILY_LIMIT_REACHED&quot; |
| ORIGINATED | &quot;ORIGINATED&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| FORWARDED | &quot;FORWARDED&quot; |
| NOT_GIVEN | &quot;NOT_GIVEN&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| RETRY_MMS_AS_SMS | &quot;RETRY_MMS_AS_SMS&quot; |
| QUEUED | &quot;QUEUED&quot; |
| QUEUED_TRANSCODE | &quot;QUEUED_TRANSCODE&quot; |
| ORIGINAL | &quot;ORIGINAL&quot; |
| DUPE | &quot;DUPE&quot; |
| TRUNCATED | &quot;TRUNCATED&quot; |
| REQUEUED_RATE_LIMITED | &quot;REQUEUED_RATE_LIMITED&quot; |
| BUFFERED | &quot;BUFFERED&quot; |
| RATE_LIMIT_EXCEEDED | &quot;RATE_LIMIT_EXCEEDED&quot; |
| SERVICE_UNAVAILABLE | &quot;SERVICE_UNAVAILABLE&quot; |
| SEND_MMS_AS_SMS | &quot;SEND_MMS_AS_SMS&quot; |
| REQUEUED_RECOVERABLE_ERROR | &quot;REQUEUED_RECOVERABLE_ERROR&quot; |
| SEND_WITH_ADDITIONAL_SPID | &quot;SEND_WITH_ADDITIONAL_SPID&quot; |
| UNSENT_FREE_TRIAL | &quot;UNSENT_FREE_TRIAL&quot; |



