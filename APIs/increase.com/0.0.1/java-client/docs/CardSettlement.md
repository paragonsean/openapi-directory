

# CardSettlement

A Card Settlement object. This field will be present in the JSON response if and only if `category` is equal to `card_settlement`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount in the minor unit of the transaction&#39;s settlement currency. For dollars, for example, this is cents. |  |
|**cardAuthorization** | **String** | The Card Authorization that was created prior to this Card Settlement, if on exists. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s settlement currency. |  |
|**id** | **String** | The Card Settlement identifier. |  |
|**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. |  |
|**merchantCategoryCode** | **String** | The 4-digit MCC describing the merchant&#39;s business. |  |
|**merchantCity** | **String** | The city the merchant resides in. |  |
|**merchantCountry** | **String** | The country the merchant resides in. |  |
|**merchantName** | **String** | The name of the merchant. |  |
|**merchantState** | **String** | The state the merchant resides in. |  |
|**pendingTransactionId** | **String** | The identifier of the Pending Transaction associated with this Transaction. |  |
|**presentmentAmount** | **Integer** | The amount in the minor unit of the transaction&#39;s presentment currency. |  |
|**presentmentCurrency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s presentment currency. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_settlement&#x60;. |  |



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
| CARD_SETTLEMENT | &quot;card_settlement&quot; |



