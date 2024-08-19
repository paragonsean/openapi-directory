# IncreaseApi.CardAuthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The pending amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s currency. | 
**digitalWalletTokenId** | **String** | If the authorization was made via a Digital Wallet Token (such as an Apple Pay purchase), the identifier of the token that was used. | 
**id** | **String** | The Card Authorization identifier. | 
**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. | 
**merchantCategoryCode** | **String** | The Merchant Category Code (commonly abbreviated as MCC) of the merchant the card is transacting with. | 
**merchantCity** | **String** | The city the merchant resides in. | 
**merchantCountry** | **String** | The country the merchant resides in. | 
**merchantDescriptor** | **String** | The merchant descriptor of the merchant the card is transacting with. | 
**network** | **String** | The payment network used to process this card authorization | 
**networkDetails** | [**NetworkDetails**](NetworkDetails.md) |  | 
**realTimeDecisionId** | **String** | The identifier of the Real-Time Decision sent to approve or decline this transaction. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_authorization&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: NetworkEnum


* `visa` (value: `"visa"`)





## Enum: TypeEnum


* `card_authorization` (value: `"card_authorization"`)




