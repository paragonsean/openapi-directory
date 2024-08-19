# IncreaseApi.CardProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card Dispute was created. | 
**description** | **String** | A description you can use to identify the Card Profile. | 
**digitalWallets** | [**DigitalWallets**](DigitalWallets.md) |  | 
**id** | **String** | The Card Profile identifier. | 
**status** | **String** | The status of the Card Profile. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_profile&#x60;. | 



## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `rejected` (value: `"rejected"`)

* `active` (value: `"active"`)

* `archived` (value: `"archived"`)





## Enum: TypeEnum


* `card_profile` (value: `"card_profile"`)




