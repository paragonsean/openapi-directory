

# AccountTransfer

Account transfers move funds between your own accounts at Increase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Account to which the transfer belongs. |  |
|**amount** | **Integer** | The transfer amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**approval** | [**TransferApproval**](TransferApproval.md) |  |  |
|**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. |  |
|**description** | **String** | The description that will show on the transactions. |  |
|**destinationAccountId** | **String** | The destination account&#39;s identifier. |  |
|**destinationTransactionId** | **String** | The ID for the transaction receiving the transfer. |  |
|**id** | **String** | The account transfer&#39;s identifier. |  |
|**network** | [**NetworkEnum**](#NetworkEnum) | The transfer&#39;s network. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the transfer. |  |
|**transactionId** | **String** | The ID for the transaction funding the transfer. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;account_transfer&#x60;. |  |



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
| ACCOUNT | &quot;account&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_APPROVAL | &quot;pending_approval&quot; |
| CANCELED | &quot;canceled&quot; |
| COMPLETE | &quot;complete&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_TRANSFER | &quot;account_transfer&quot; |



