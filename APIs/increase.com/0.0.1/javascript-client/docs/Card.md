# IncreaseApi.Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier for the account this card belongs to. | 
**billingAddress** | [**BillingAddress**](BillingAddress.md) |  | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card was created. | 
**description** | **String** | The card&#39;s description for display purposes. | 
**digitalWallet** | [**DigitalWallet**](DigitalWallet.md) |  | 
**expirationMonth** | **Number** | The month the card expires in M format (e.g., August is 8). | 
**expirationYear** | **Number** | The year the card expires in YYYY format (e.g., 2025). | 
**id** | **String** | The card identifier. | 
**last4** | **String** | The last 4 digits of the Card&#39;s Primary Account Number. | 
**status** | **String** | This indicates if payments can be made with the card. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;card&#x60;. | 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `disabled` (value: `"disabled"`)

* `canceled` (value: `"canceled"`)





## Enum: TypeEnum


* `card` (value: `"card"`)




