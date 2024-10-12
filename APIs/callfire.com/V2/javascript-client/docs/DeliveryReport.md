# CallFireApiDocumentation.DeliveryReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaignId** | **Number** | ~ | [optional] 
**carrier** | **String** | ~ | [optional] 
**deliveryCategory** | **String** | ~ | [optional] 
**deliveryState** | **String** | ~ | [optional] 
**fromNumber** | **String** | ~ | [optional] 
**messageText** | **String** | ~ | [optional] 
**toNumber** | **String** | ~ | [optional] 
**updated** | **Date** | ~ | [optional] 



## Enum: DeliveryCategoryEnum


* `NO_DATA` (value: `"NO_DATA"`)

* `OPTED_OUT` (value: `"OPTED_OUT"`)

* `BOUNCED` (value: `"BOUNCED"`)

* `NO_CREDITS` (value: `"NO_CREDITS"`)

* `DELIVERED` (value: `"DELIVERED"`)





## Enum: DeliveryStateEnum


* `DELIVERED` (value: `"DELIVERED"`)

* `UNSENT_OPTED_OUT_GLOBAL` (value: `"UNSENT_OPTED_OUT_GLOBAL"`)

* `UNSENT_OPTED_OUT_LOCAL` (value: `"UNSENT_OPTED_OUT_LOCAL"`)

* `UNSENT_NO_CREDITS` (value: `"UNSENT_NO_CREDITS"`)

* `GATEWAY_REJECTED` (value: `"GATEWAY_REJECTED"`)

* `CARRIER_REJECTED` (value: `"CARRIER_REJECTED"`)

* `NOT_DELIVERED` (value: `"NOT_DELIVERED"`)

* `UNSENT_INVALID_NUMBER` (value: `"UNSENT_INVALID_NUMBER"`)

* `UNSENT_BAD_DATA` (value: `"UNSENT_BAD_DATA"`)

* `UNSENT_FORCE_STOPPED` (value: `"UNSENT_FORCE_STOPPED"`)

* `UNSENT_PERIOD_LIMIT` (value: `"UNSENT_PERIOD_LIMIT"`)

* `UNSENT_INTERNATIONAL` (value: `"UNSENT_INTERNATIONAL"`)

* `UNSENT_INVALID_TIMEZONE_OR_DNC` (value: `"UNSENT_INVALID_TIMEZONE_OR_DNC"`)

* `UNSENT_ALREADY_SCRUBBED` (value: `"UNSENT_ALREADY_SCRUBBED"`)

* `UNSENT_SYSTEM_ERROR` (value: `"UNSENT_SYSTEM_ERROR"`)

* `UNSENT_NO_WIRELESS_CARRIER` (value: `"UNSENT_NO_WIRELESS_CARRIER"`)

* `UNSENT_MESSAGE_TOO_LONG` (value: `"UNSENT_MESSAGE_TOO_LONG"`)

* `UNSENT_MESSAGE_BLOCKED` (value: `"UNSENT_MESSAGE_BLOCKED"`)

* `UNSENT_QUEUE_LIMIT_REACHED` (value: `"UNSENT_QUEUE_LIMIT_REACHED"`)

* `UNSENT_TOKEN_LIMIT_REACHED` (value: `"UNSENT_TOKEN_LIMIT_REACHED"`)

* `UNSENT_TIME_LIMIT_REACHED` (value: `"UNSENT_TIME_LIMIT_REACHED"`)

* `UNSENT_SCHEDULER_CAPACITY_EXCEEDED` (value: `"UNSENT_SCHEDULER_CAPACITY_EXCEEDED"`)

* `SPAM_DETECTED` (value: `"SPAM_DETECTED"`)

* `UNSENT_NO_GATEWAY` (value: `"UNSENT_NO_GATEWAY"`)

* `UNSENT_DAILY_LIMIT_REACHED` (value: `"UNSENT_DAILY_LIMIT_REACHED"`)

* `ORIGINATED` (value: `"ORIGINATED"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `FORWARDED` (value: `"FORWARDED"`)

* `NOT_GIVEN` (value: `"NOT_GIVEN"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `RETRY_MMS_AS_SMS` (value: `"RETRY_MMS_AS_SMS"`)

* `QUEUED` (value: `"QUEUED"`)

* `QUEUED_TRANSCODE` (value: `"QUEUED_TRANSCODE"`)

* `ORIGINAL` (value: `"ORIGINAL"`)

* `DUPE` (value: `"DUPE"`)

* `TRUNCATED` (value: `"TRUNCATED"`)

* `REQUEUED_RATE_LIMITED` (value: `"REQUEUED_RATE_LIMITED"`)

* `BUFFERED` (value: `"BUFFERED"`)

* `RATE_LIMIT_EXCEEDED` (value: `"RATE_LIMIT_EXCEEDED"`)

* `SERVICE_UNAVAILABLE` (value: `"SERVICE_UNAVAILABLE"`)

* `SEND_MMS_AS_SMS` (value: `"SEND_MMS_AS_SMS"`)

* `REQUEUED_RECOVERABLE_ERROR` (value: `"REQUEUED_RECOVERABLE_ERROR"`)

* `SEND_WITH_ADDITIONAL_SPID` (value: `"SEND_WITH_ADDITIONAL_SPID"`)

* `UNSENT_FREE_TRIAL` (value: `"UNSENT_FREE_TRIAL"`)




