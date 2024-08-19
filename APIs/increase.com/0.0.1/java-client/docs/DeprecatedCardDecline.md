

# DeprecatedCardDecline

A Deprecated Card Decline object. This field will be present in the JSON response if and only if `category` is equal to `card_route_decline`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination account currency. |  |
|**merchantAcceptorId** | **String** |  |  |
|**merchantCategoryCode** | **String** |  |  |
|**merchantCity** | **String** |  |  |
|**merchantCountry** | **String** |  |  |
|**merchantDescriptor** | **String** |  |  |
|**merchantState** | **String** |  |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



