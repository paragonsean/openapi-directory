# IncreaseApi.WireTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Account to which the transfer belongs. | 
**accountNumber** | **String** | The destination account number. | 
**amount** | **Number** | The transfer amount in USD cents. | 
**approval** | [**TransferApproval**](TransferApproval.md) |  | 
**beneficiaryAddressLine1** | **String** | The beneficiary&#39;s address line 1. | 
**beneficiaryAddressLine2** | **String** | The beneficiary&#39;s address line 2. | 
**beneficiaryAddressLine3** | **String** | The beneficiary&#39;s address line 3. | 
**beneficiaryName** | **String** | The beneficiary&#39;s name. | 
**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer&#39;s currency. For wire transfers this is always equal to &#x60;usd&#x60;. | 
**externalAccountId** | **String** | The identifier of the External Account the transfer was made to, if any. | 
**id** | **String** | The wire transfer&#39;s identifier. | 
**messageToRecipient** | **String** | The message that will show on the recipient&#39;s bank statement. | 
**network** | **String** | The transfer&#39;s network. | 
**reversal** | [**InboundWireReversal1**](InboundWireReversal1.md) |  | 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | 
**status** | **String** | The lifecycle status of the transfer. | 
**submission** | [**WireTransferSubmission**](WireTransferSubmission.md) |  | 
**transactionId** | **String** | The ID for the transaction funding the transfer. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;wire_transfer&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: NetworkEnum


* `wire` (value: `"wire"`)





## Enum: StatusEnum


* `canceled` (value: `"canceled"`)

* `requires_attention` (value: `"requires_attention"`)

* `pending_approval` (value: `"pending_approval"`)

* `rejected` (value: `"rejected"`)

* `reversed` (value: `"reversed"`)

* `complete` (value: `"complete"`)

* `pending_creating` (value: `"pending_creating"`)





## Enum: TypeEnum


* `wire_transfer` (value: `"wire_transfer"`)




