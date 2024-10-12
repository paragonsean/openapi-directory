

# InboundRealTimePaymentsTransferDecline

A Inbound Real Time Payments Transfer Decline object. This field will be present in the JSON response if and only if `category` is equal to `inbound_real_time_payments_transfer_decline`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**creditorName** | **String** | The name the sender of the transfer specified as the recipient of the transfer. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the declined transfer&#39;s currency. This will always be \&quot;USD\&quot; for a Real Time Payments transfer. |  |
|**debtorAccountNumber** | **String** | The account number of the account that sent the transfer. |  |
|**debtorName** | **String** | The name provided by the sender of the transfer. |  |
|**debtorRoutingNumber** | **String** | The routing number of the account that sent the transfer. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Why the transfer was declined. |  |
|**remittanceInformation** | **String** | Additional information included with the transfer. |  |
|**transactionIdentification** | **String** | The Real Time Payments network identification of the declined transfer. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ACCOUNT_NUMBER_CANCELED | &quot;account_number_canceled&quot; |
| ACCOUNT_NUMBER_DISABLED | &quot;account_number_disabled&quot; |
| GROUP_LOCKED | &quot;group_locked&quot; |
| ENTITY_NOT_ACTIVE | &quot;entity_not_active&quot; |
| REAL_TIME_PAYMENTS_NOT_ENABLED | &quot;real_time_payments_not_enabled&quot; |



