

# CheckTransfer

Check Transfers move funds from your Increase account by mailing a physical check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier of the Account from which funds will be transferred. |  |
|**addressCity** | **String** | The city of the check&#39;s destination. |  |
|**addressLine1** | **String** | The street address of the check&#39;s destination. |  |
|**addressLine2** | **String** | The second line of the address of the check&#39;s destination. |  |
|**addressState** | **String** | The state of the check&#39;s destination. |  |
|**addressZip** | **String** | The postal code of the check&#39;s destination. |  |
|**amount** | **Integer** | The transfer amount in USD cents. |  |
|**approval** | [**TransferApproval**](TransferApproval.md) |  |  |
|**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check&#39;s currency. |  |
|**deposit** | [**CheckTransferDeposit**](CheckTransferDeposit.md) |  |  |
|**id** | **String** | The Check transfer&#39;s identifier. |  |
|**mailedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check was mailed. |  |
|**message** | **String** | The descriptor that will be printed on the memo field on the check. |  |
|**note** | **String** | The descriptor that will be printed on the letter included with the check. |  |
|**recipientName** | **String** | The name that will be printed on the check. |  |
|**returnAddress** | [**ReturnAddress**](ReturnAddress.md) |  |  |
|**returnDetails** | [**CheckTransferReturn**](CheckTransferReturn.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the transfer. |  |
|**stopPaymentRequest** | [**CheckTransferStopPaymentRequest**](CheckTransferStopPaymentRequest.md) |  |  |
|**submission** | [**CheckTransferSubmission**](CheckTransferSubmission.md) |  |  |
|**submittedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check was submitted. |  |
|**transactionId** | **String** | The ID for the transaction caused by the transfer. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;check_transfer&#x60;. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_APPROVAL | &quot;pending_approval&quot; |
| PENDING_SUBMISSION | &quot;pending_submission&quot; |
| SUBMITTED | &quot;submitted&quot; |
| PENDING_MAILING | &quot;pending_mailing&quot; |
| MAILED | &quot;mailed&quot; |
| CANCELED | &quot;canceled&quot; |
| DEPOSITED | &quot;deposited&quot; |
| STOPPED | &quot;stopped&quot; |
| RETURNED | &quot;returned&quot; |
| REJECTED | &quot;rejected&quot; |
| REQUIRES_ATTENTION | &quot;requires_attention&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHECK_TRANSFER | &quot;check_transfer&quot; |



