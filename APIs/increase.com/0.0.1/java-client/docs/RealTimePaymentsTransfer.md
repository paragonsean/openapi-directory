

# RealTimePaymentsTransfer

Real Time Payments transfers move funds, within seconds, between your Increase account and any other account on the Real Time Payments network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Account from which the transfer was sent. |  |
|**amount** | **Integer** | The transfer amount in USD cents. |  |
|**approval** | [**TransferApproval**](TransferApproval.md) |  |  |
|**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**creditorName** | **String** | The name of the transfer&#39;s recipient as provided by the sender. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer&#39;s currency. For real time payments transfers this is always equal to &#x60;USD&#x60;. |  |
|**destinationAccountNumber** | **String** | The destination account number. |  |
|**destinationRoutingNumber** | **String** | The destination American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**externalAccountId** | **String** | The identifier of the External Account the transfer was made to, if any. |  |
|**id** | **String** | The Real Time Payments Transfer&#39;s identifier. |  |
|**rejection** | [**RealTimePaymentsTransferRejection**](RealTimePaymentsTransferRejection.md) |  |  |
|**remittanceInformation** | **String** | Unstructured information that will show on the recipient&#39;s bank statement. |  |
|**sourceAccountNumberId** | **String** | The Account Number the recipient will see as having sent the transfer. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the transfer. |  |
|**submission** | [**RealTimePaymentsTransferSubmission**](RealTimePaymentsTransferSubmission.md) |  |  |
|**transactionId** | **String** | The Transaction funding the transfer once it is complete. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;real_time_payments_transfer&#x60;. |  |



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
| CANCELED | &quot;canceled&quot; |
| PENDING_SUBMISSION | &quot;pending_submission&quot; |
| SUBMITTED | &quot;submitted&quot; |
| COMPLETE | &quot;complete&quot; |
| REJECTED | &quot;rejected&quot; |
| REQUIRES_ATTENTION | &quot;requires_attention&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REAL_TIME_PAYMENTS_TRANSFER | &quot;real_time_payments_transfer&quot; |



