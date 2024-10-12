

# CardRefund

A Card Refund object. This field will be present in the JSON response if and only if `category` is equal to `card_refund`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The pending amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**cardSettlementTransactionId** | **String** | The identifier for the Transaction this refunds, if any. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s currency. |  |
|**id** | **String** | The Card Refund identifier. |  |
|**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. |  |
|**merchantCategoryCode** | **String** | The 4-digit MCC describing the merchant&#39;s business. |  |
|**merchantCity** | **String** | The city the merchant resides in. |  |
|**merchantCountry** | **String** | The country the merchant resides in. |  |
|**merchantName** | **String** | The name of the merchant. |  |
|**merchantState** | **String** | The state the merchant resides in. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_refund&#x60;. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CARD_REFUND | &quot;card_refund&quot; |



