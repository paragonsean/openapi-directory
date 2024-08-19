

# InboundRealTimePaymentsTransferConfirmation

A Inbound Real Time Payments Transfer Confirmation object. This field will be present in the JSON response if and only if `category` is equal to `inbound_real_time_payments_transfer_confirmation`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount in the minor unit of the transfer&#39;s currency. For dollars, for example, this is cents. |  |
|**creditorName** | **String** | The name the sender of the transfer specified as the recipient of the transfer. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the transfer&#39;s currency. This will always be \&quot;USD\&quot; for a Real Time Payments transfer. |  |
|**debtorAccountNumber** | **String** | The account number of the account that sent the transfer. |  |
|**debtorName** | **String** | The name provided by the sender of the transfer. |  |
|**debtorRoutingNumber** | **String** | The routing number of the account that sent the transfer. |  |
|**remittanceInformation** | **String** | Additional information included with the transfer. |  |
|**transactionIdentification** | **String** | The Real Time Payments network identification of the transfer |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



