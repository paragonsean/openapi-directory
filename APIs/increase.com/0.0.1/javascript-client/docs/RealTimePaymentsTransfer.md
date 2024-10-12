# IncreaseApi.RealTimePaymentsTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Account from which the transfer was sent. | 
**amount** | **Number** | The transfer amount in USD cents. | 
**approval** | [**TransferApproval**](TransferApproval.md) |  | 
**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**creditorName** | **String** | The name of the transfer&#39;s recipient as provided by the sender. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer&#39;s currency. For real time payments transfers this is always equal to &#x60;USD&#x60;. | 
**destinationAccountNumber** | **String** | The destination account number. | 
**destinationRoutingNumber** | **String** | The destination American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | 
**externalAccountId** | **String** | The identifier of the External Account the transfer was made to, if any. | 
**id** | **String** | The Real Time Payments Transfer&#39;s identifier. | 
**rejection** | [**RealTimePaymentsTransferRejection**](RealTimePaymentsTransferRejection.md) |  | 
**remittanceInformation** | **String** | Unstructured information that will show on the recipient&#39;s bank statement. | 
**sourceAccountNumberId** | **String** | The Account Number the recipient will see as having sent the transfer. | 
**status** | **String** | The lifecycle status of the transfer. | 
**submission** | [**RealTimePaymentsTransferSubmission**](RealTimePaymentsTransferSubmission.md) |  | 
**transactionId** | **String** | The Transaction funding the transfer once it is complete. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;real_time_payments_transfer&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: StatusEnum


* `pending_approval` (value: `"pending_approval"`)

* `canceled` (value: `"canceled"`)

* `pending_submission` (value: `"pending_submission"`)

* `submitted` (value: `"submitted"`)

* `complete` (value: `"complete"`)

* `rejected` (value: `"rejected"`)

* `requires_attention` (value: `"requires_attention"`)





## Enum: TypeEnum


* `real_time_payments_transfer` (value: `"real_time_payments_transfer"`)




