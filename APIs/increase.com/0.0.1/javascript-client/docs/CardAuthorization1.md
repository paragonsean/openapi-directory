# IncreaseApi.CardAuthorization1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier of the Account the authorization will debit. | 
**cardId** | **String** | The identifier of the Card that is being authorized. | 
**decision** | **String** | Whether or not the authorization was approved. | 
**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. | 
**merchantCategoryCode** | **String** | The Merchant Category Code (commonly abbreviated as MCC) of the merchant the card is transacting with. | 
**merchantCity** | **String** | The city the merchant resides in. | 
**merchantCountry** | **String** | The country the merchant resides in. | 
**merchantDescriptor** | **String** | The merchant descriptor of the merchant the card is transacting with. | 
**network** | **String** | The payment network used to process this card authorization | 
**networkDetails** | [**NetworkDetails**](NetworkDetails.md) |  | 
**presentmentAmount** | **Number** | The amount of the attempted authorization in the currency the card user sees at the time of purchase, in the minor unit of that currency. For dollars, for example, this is cents. | 
**presentmentCurrency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the user sees at the time of purchase. | 
**settlementAmount** | **Number** | The amount of the attempted authorization in the currency it will be settled in. This currency is the same as that of the Account the card belongs to. | 
**settlementCurrency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the transaction will be settled in. | 



## Enum: DecisionEnum


* `approve` (value: `"approve"`)

* `decline` (value: `"decline"`)





## Enum: NetworkEnum


* `visa` (value: `"visa"`)




