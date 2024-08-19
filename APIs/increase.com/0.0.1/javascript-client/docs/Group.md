# IncreaseApi.Group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achDebitStatus** | **String** | If the Group is allowed to create ACH debits. | 
**activationStatus** | **String** | If the Group is activated or not. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Group was created. | 
**id** | **String** | The Group identifier. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;group&#x60;. | 



## Enum: AchDebitStatusEnum


* `disabled` (value: `"disabled"`)

* `enabled` (value: `"enabled"`)





## Enum: ActivationStatusEnum


* `unactivated` (value: `"unactivated"`)

* `activated` (value: `"activated"`)





## Enum: TypeEnum


* `group` (value: `"group"`)




