

# CardDecline

A Card Decline object. This field will be present in the JSON response if and only if `category` is equal to `card_decline`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. |  |
|**digitalWalletTokenId** | **String** | If the authorization was attempted using a Digital Wallet Token (such as an Apple Pay purchase), the identifier of the token that was used. |  |
|**merchantAcceptorId** | **String** | The merchant identifier (commonly abbreviated as MID) of the merchant the card is transacting with. |  |
|**merchantCategoryCode** | **String** | The Merchant Category Code (commonly abbreviated as MCC) of the merchant the card is transacting with. |  |
|**merchantCity** | **String** | The city the merchant resides in. |  |
|**merchantCountry** | **String** | The country the merchant resides in. |  |
|**merchantDescriptor** | **String** | The merchant descriptor of the merchant the card is transacting with. |  |
|**merchantState** | **String** | The state the merchant resides in. |  |
|**network** | [**NetworkEnum**](#NetworkEnum) | The payment network used to process this card authorization |  |
|**networkDetails** | [**NetworkDetails**](NetworkDetails.md) |  |  |
|**realTimeDecisionId** | **String** | The identifier of the Real-Time Decision sent to approve or decline this transaction. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Why the transaction was declined. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: NetworkEnum

| Name | Value |
|---- | -----|
| VISA | &quot;visa&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| CARD_NOT_ACTIVE | &quot;card_not_active&quot; |
| ENTITY_NOT_ACTIVE | &quot;entity_not_active&quot; |
| GROUP_LOCKED | &quot;group_locked&quot; |
| INSUFFICIENT_FUNDS | &quot;insufficient_funds&quot; |
| CVV2_MISMATCH | &quot;cvv2_mismatch&quot; |
| TRANSACTION_NOT_ALLOWED | &quot;transaction_not_allowed&quot; |
| BREACHES_LIMIT | &quot;breaches_limit&quot; |
| WEBHOOK_DECLINED | &quot;webhook_declined&quot; |
| WEBHOOK_TIMED_OUT | &quot;webhook_timed_out&quot; |
| DECLINED_BY_STAND_IN_PROCESSING | &quot;declined_by_stand_in_processing&quot; |
| INVALID_PHYSICAL_CARD | &quot;invalid_physical_card&quot; |
| MISSING_ORIGINAL_AUTHORIZATION | &quot;missing_original_authorization&quot; |



