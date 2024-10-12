# TwilioApi.ApiV2010AccountUsageUsageTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the trigger monitors. | [optional] 
**apiVersion** | **String** | The API version used to create the resource. | [optional] 
**callbackMethod** | **String** | The HTTP method we use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**callbackUrl** | **String** | The URL we call using the &#x60;callback_method&#x60; when the trigger fires. | [optional] 
**currentValue** | **String** | The current value of the field the trigger is watching. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateFired** | **String** | The date and time in GMT that the trigger was last fired specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the trigger. | [optional] 
**recurring** | [**UsageTriggerEnumRecurring**](UsageTriggerEnumRecurring.md) |  | [optional] 
**sid** | **String** | The unique string that that we created to identify the UsageTrigger resource. | [optional] 
**triggerBy** | [**UsageTriggerEnumTriggerField**](UsageTriggerEnumTriggerField.md) |  | [optional] 
**triggerValue** | **String** | The value at which the trigger will fire.  Must be a positive, numeric value. | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 
**usageCategory** | [**UsageTriggerEnumUsageCategory**](UsageTriggerEnumUsageCategory.md) |  | [optional] 
**usageRecordUri** | **String** | The URI of the [UsageRecord](https://www.twilio.com/docs/usage/api/usage-record) resource this trigger watches, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 



## Enum: CallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




