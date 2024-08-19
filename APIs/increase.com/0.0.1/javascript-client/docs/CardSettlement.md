# IncreaseApi.CardSettlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount in the minor unit of the transaction&#39;s settlement currency. For dollars, for example, this is cents. | 
**cardAuthorization** | **String** | The Card Authorization that was created prior to this Card Settlement, if on exists. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s settlement currency. | 
**id** | **String** | The Card Settlement identifier. | 
**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. | 
**merchantCategoryCode** | **String** | The 4-digit MCC describing the merchant&#39;s business. | 
**merchantCity** | **String** | The city the merchant resides in. | 
**merchantCountry** | **String** | The country the merchant resides in. | 
**merchantName** | **String** | The name of the merchant. | 
**merchantState** | **String** | The state the merchant resides in. | 
**pendingTransactionId** | **String** | The identifier of the Pending Transaction associated with this Transaction. | 
**presentmentAmount** | **Number** | The amount in the minor unit of the transaction&#39;s presentment currency. | 
**presentmentCurrency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s presentment currency. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_settlement&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: TypeEnum


* `card_settlement` (value: `"card_settlement"`)




