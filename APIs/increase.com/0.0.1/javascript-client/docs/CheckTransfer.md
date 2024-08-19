# IncreaseApi.CheckTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier of the Account from which funds will be transferred. | 
**addressCity** | **String** | The city of the check&#39;s destination. | 
**addressLine1** | **String** | The street address of the check&#39;s destination. | 
**addressLine2** | **String** | The second line of the address of the check&#39;s destination. | 
**addressState** | **String** | The state of the check&#39;s destination. | 
**addressZip** | **String** | The postal code of the check&#39;s destination. | 
**amount** | **Number** | The transfer amount in USD cents. | 
**approval** | [**TransferApproval**](TransferApproval.md) |  | 
**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check&#39;s currency. | 
**deposit** | [**CheckTransferDeposit**](CheckTransferDeposit.md) |  | 
**id** | **String** | The Check transfer&#39;s identifier. | 
**mailedAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check was mailed. | 
**message** | **String** | The descriptor that will be printed on the memo field on the check. | 
**note** | **String** | The descriptor that will be printed on the letter included with the check. | 
**recipientName** | **String** | The name that will be printed on the check. | 
**returnAddress** | [**ReturnAddress**](ReturnAddress.md) |  | 
**returnDetails** | [**CheckTransferReturn**](CheckTransferReturn.md) |  | 
**status** | **String** | The lifecycle status of the transfer. | 
**stopPaymentRequest** | [**CheckTransferStopPaymentRequest**](CheckTransferStopPaymentRequest.md) |  | 
**submission** | [**CheckTransferSubmission**](CheckTransferSubmission.md) |  | 
**submittedAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check was submitted. | 
**transactionId** | **String** | The ID for the transaction caused by the transfer. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;check_transfer&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: StatusEnum


* `pending_approval` (value: `"pending_approval"`)

* `pending_submission` (value: `"pending_submission"`)

* `submitted` (value: `"submitted"`)

* `pending_mailing` (value: `"pending_mailing"`)

* `mailed` (value: `"mailed"`)

* `canceled` (value: `"canceled"`)

* `deposited` (value: `"deposited"`)

* `stopped` (value: `"stopped"`)

* `returned` (value: `"returned"`)

* `rejected` (value: `"rejected"`)

* `requires_attention` (value: `"requires_attention"`)





## Enum: TypeEnum


* `check_transfer` (value: `"check_transfer"`)




