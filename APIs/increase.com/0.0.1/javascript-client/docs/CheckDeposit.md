# IncreaseApi.CheckDeposit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Account the check was deposited into. | 
**amount** | **Number** | The deposited amount in the minor unit of the destination account currency. For dollars, for example, this is cents. | 
**backImageFileId** | **String** | The ID for the File containing the image of the back of the check. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the deposit. | 
**depositAcceptance** | [**CheckDepositAcceptance**](CheckDepositAcceptance.md) |  | 
**depositRejection** | [**CheckDepositRejection**](CheckDepositRejection.md) |  | 
**depositReturn** | [**CheckDepositReturn**](CheckDepositReturn.md) |  | 
**frontImageFileId** | **String** | The ID for the File containing the image of the front of the check. | 
**id** | **String** | The deposit&#39;s identifier. | 
**status** | **String** | The status of the Check Deposit. | 
**transactionId** | **String** | The ID for the Transaction created by the deposit. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;check_deposit&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `submitted` (value: `"submitted"`)

* `rejected` (value: `"rejected"`)

* `returned` (value: `"returned"`)





## Enum: TypeEnum


* `check_deposit` (value: `"check_deposit"`)




