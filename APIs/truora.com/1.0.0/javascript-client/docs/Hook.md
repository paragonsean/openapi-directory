# ChecksApi.Hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **[String]** | Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three | [optional] 
**eventType** | **String** | Entity events you want to be notified. If all is selected, there is no need to enter actions | [optional] 
**signingKey** | **String** | Secret random hexadecimal key used to sign the event and confirm its legitimacy. Signing keys are used to decode the JWT you get as payload from events | [optional] 
**status** | **String** | indicates whether the hook is active or not. enabled by default | [optional] 
**subscriberType** | **String** | Platform with an endpoint ready to process the information. Only web is supported currently | [optional] 
**subscriberUrl** | **String** | Link where notification requests will be sent, required when subscriber_type is web | [optional] 



## Enum: EventTypeEnum


* `all` (value: `"all"`)

* `check` (value: `"check"`)





## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




