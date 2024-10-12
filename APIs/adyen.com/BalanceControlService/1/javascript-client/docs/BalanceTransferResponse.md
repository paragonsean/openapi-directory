# AdyenBalanceControlApi.BalanceTransferResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount of the transfer in [minor units](https://docs.adyen.com/development-resources/currency-codes). | 
**createdAt** | **Date** | The date when the balance transfer was requested. | 
**description** | **String** | A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description may be truncated. | [optional] 
**fromMerchant** | **String** | The unique identifier of the source merchant account from which funds are deducted. | 
**pspReference** | **String** | Adyen&#39;s 16-character string reference associated with the balance transfer. | 
**reference** | **String** | A reference for the balance transfer. If you don&#39;t provide this in the request, Adyen generates a unique reference. Maximum length: 80 characters. | [optional] 
**status** | **String** | The status of the balance transfer. Possible values: **transferred**, **failed**, **error**, and **notEnoughBalance**. | 
**toMerchant** | **String** | The unique identifier of the destination merchant account from which funds are transferred. | 
**type** | **String** | The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and **adjustment**. | 



## Enum: StatusEnum


* `error` (value: `"error"`)

* `failed` (value: `"failed"`)

* `notEnoughBalance` (value: `"notEnoughBalance"`)

* `transferred` (value: `"transferred"`)





## Enum: TypeEnum


* `tax` (value: `"tax"`)

* `fee` (value: `"fee"`)

* `terminalSale` (value: `"terminalSale"`)

* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)

* `adjustment` (value: `"adjustment"`)




