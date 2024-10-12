# IncreaseApi.AccountNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier for the account this Account Number belongs to. | 
**accountNumber** | **String** | The account number. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account Number was created. | 
**id** | **String** | The Account Number identifier. | 
**name** | **String** | The name you choose for the Account Number. | 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | 
**status** | **String** | This indicates if payments can be made to the Account Number. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;account_number&#x60;. | 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `disabled` (value: `"disabled"`)

* `canceled` (value: `"canceled"`)





## Enum: TypeEnum


* `account_number` (value: `"account_number"`)




