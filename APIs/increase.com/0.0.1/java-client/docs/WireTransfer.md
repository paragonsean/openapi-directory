

# WireTransfer

Wire transfers move funds between your Increase account and any other account accessible by Fedwire.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Account to which the transfer belongs. |  |
|**accountNumber** | **String** | The destination account number. |  |
|**amount** | **Integer** | The transfer amount in USD cents. |  |
|**approval** | [**TransferApproval**](TransferApproval.md) |  |  |
|**beneficiaryAddressLine1** | **String** | The beneficiary&#39;s address line 1. |  |
|**beneficiaryAddressLine2** | **String** | The beneficiary&#39;s address line 2. |  |
|**beneficiaryAddressLine3** | **String** | The beneficiary&#39;s address line 3. |  |
|**beneficiaryName** | **String** | The beneficiary&#39;s name. |  |
|**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer&#39;s currency. For wire transfers this is always equal to &#x60;usd&#x60;. |  |
|**externalAccountId** | **String** | The identifier of the External Account the transfer was made to, if any. |  |
|**id** | **String** | The wire transfer&#39;s identifier. |  |
|**messageToRecipient** | **String** | The message that will show on the recipient&#39;s bank statement. |  |
|**network** | [**NetworkEnum**](#NetworkEnum) | The transfer&#39;s network. |  |
|**reversal** | [**InboundWireReversal1**](InboundWireReversal1.md) |  |  |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the transfer. |  |
|**submission** | [**WireTransferSubmission**](WireTransferSubmission.md) |  |  |
|**transactionId** | **String** | The ID for the transaction funding the transfer. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;wire_transfer&#x60;. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: NetworkEnum

| Name | Value |
|---- | -----|
| WIRE | &quot;wire&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CANCELED | &quot;canceled&quot; |
| REQUIRES_ATTENTION | &quot;requires_attention&quot; |
| PENDING_APPROVAL | &quot;pending_approval&quot; |
| REJECTED | &quot;rejected&quot; |
| REVERSED | &quot;reversed&quot; |
| COMPLETE | &quot;complete&quot; |
| PENDING_CREATING | &quot;pending_creating&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WIRE_TRANSFER | &quot;wire_transfer&quot; |



