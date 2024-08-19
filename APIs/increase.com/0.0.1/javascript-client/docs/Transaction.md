# IncreaseApi.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier for the Account the Transaction belongs to. | 
**amount** | **Number** | The Transaction amount in the minor unit of its currency. For dollars, for example, this is cents. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Transaction occured. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Transaction&#39;s currency. This will match the currency on the Transcation&#39;s Account. | 
**description** | **String** | For a Transaction related to a transfer, this is the description you provide. For a Transaction related to a payment, this is the description the vendor provides. | 
**id** | **String** | The Transaction identifier. | 
**routeId** | **String** | The identifier for the route this Transaction came through. Routes are things like cards and ACH details. | 
**routeType** | **String** | The type of the route this Transaction came through. | 
**source** | [**TransactionSource**](TransactionSource.md) |  | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;transaction&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: RouteTypeEnum


* `account_number` (value: `"account_number"`)

* `card` (value: `"card"`)





## Enum: TypeEnum


* `transaction` (value: `"transaction"`)




