

# CheckTransferInstruction

A Check Transfer Instruction object. This field will be present in the JSON response if and only if `category` is equal to `check_transfer_instruction`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The pending amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check&#39;s currency. |  |
|**transferId** | **String** | The identifier of the Check Transfer that led to this Pending Transaction. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



