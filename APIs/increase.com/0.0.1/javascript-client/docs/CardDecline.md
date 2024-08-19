# IncreaseApi.CardDecline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. | 
**digitalWalletTokenId** | **String** | If the authorization was attempted using a Digital Wallet Token (such as an Apple Pay purchase), the identifier of the token that was used. | 
**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. | 
**merchantCategoryCode** | **String** | The Merchant Category Code (commonly abbreviated as MCC) of the merchant the card is transacting with. | 
**merchantCity** | **String** | The city the merchant resides in. | 
**merchantCountry** | **String** | The country the merchant resides in. | 
**merchantDescriptor** | **String** | The merchant descriptor of the merchant the card is transacting with. | 
**merchantState** | **String** | The state the merchant resides in. | 
**network** | **String** | The payment network used to process this card authorization | 
**networkDetails** | [**NetworkDetails**](NetworkDetails.md) |  | 
**realTimeDecisionId** | **String** | The identifier of the Real-Time Decision sent to approve or decline this transaction. | 
**reason** | **String** | Why the transaction was declined. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: NetworkEnum


* `visa` (value: `"visa"`)





## Enum: ReasonEnum


* `card_not_active` (value: `"card_not_active"`)

* `entity_not_active` (value: `"entity_not_active"`)

* `group_locked` (value: `"group_locked"`)

* `insufficient_funds` (value: `"insufficient_funds"`)

* `cvv2_mismatch` (value: `"cvv2_mismatch"`)

* `transaction_not_allowed` (value: `"transaction_not_allowed"`)

* `breaches_limit` (value: `"breaches_limit"`)

* `webhook_declined` (value: `"webhook_declined"`)

* `webhook_timed_out` (value: `"webhook_timed_out"`)

* `declined_by_stand_in_processing` (value: `"declined_by_stand_in_processing"`)

* `invalid_physical_card` (value: `"invalid_physical_card"`)

* `missing_original_authorization` (value: `"missing_original_authorization"`)




