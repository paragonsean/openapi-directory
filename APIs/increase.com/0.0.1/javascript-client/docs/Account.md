# IncreaseApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Account currency. | 
**entityId** | **String** | The identifier for the Entity the Account belongs to. | 
**id** | **String** | The Account identifier. | 
**informationalEntityId** | **String** | The identifier of an Entity that, while not owning the Account, is associated with its activity. | 
**interestAccrued** | **String** | The interest accrued but not yet paid, expressed as a string containing a floating-point value. | 
**interestAccruedAt** | **Date** | The latest [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which interest was accrued. | 
**name** | **String** | The name you choose for the Account. | 
**status** | **String** | The status of the Account. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;account&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: StatusEnum


* `open` (value: `"open"`)

* `closed` (value: `"closed"`)





## Enum: TypeEnum


* `account` (value: `"account"`)




