

# AccountTransferIntention

A Account Transfer Intention object. This field will be present in the JSON response if and only if `category` is equal to `account_transfer_intention`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The pending amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. |  |
|**description** | **String** | The description you chose to give the transfer. |  |
|**destinationAccountId** | **String** | The identifier of the Account to where the Account Transfer was sent. |  |
|**sourceAccountId** | **String** | The identifier of the Account from where the Account Transfer was sent. |  |
|**transferId** | **String** | The identifier of the Account Transfer that led to this Pending Transaction. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



