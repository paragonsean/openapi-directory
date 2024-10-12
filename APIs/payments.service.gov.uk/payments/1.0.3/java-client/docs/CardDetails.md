

# CardDetails

A structure representing the payment card

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**Address**](Address.md) |  |  [optional] |
|**cardBrand** | **String** |  |  [optional] [readonly] |
|**cardType** | [**CardTypeEnum**](#CardTypeEnum) | The card type, &#x60;debit&#x60; or &#x60;credit&#x60; or &#x60;null&#x60; if not able to determine |  [optional] [readonly] |
|**cardholderName** | **String** |  |  [optional] [readonly] |
|**expiryDate** | **String** | The expiry date of the card in MM/yy format |  [optional] [readonly] |
|**firstDigitsCardNumber** | **String** |  |  [optional] [readonly] |
|**lastDigitsCardNumber** | **String** |  |  [optional] [readonly] |



## Enum: CardTypeEnum

| Name | Value |
|---- | -----|
| DEBIT | &quot;debit&quot; |
| CREDIT | &quot;credit&quot; |
| NULL | &quot;null&quot; |



