

# PaymentCard

A card's non-confidential details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**Address**](Address.md) |  |  [optional] |
|**bin** | **String** | The first six digits of the card number, known as the Bank Identification Number (BIN). |  [optional] |
|**cardBrand** | [**CardBrandEnum**](#CardBrandEnum) | The first six digits of the card number, known as the Bank Identification Number (BIN). |  [optional] |
|**cardType** | [**CardTypeEnum**](#CardTypeEnum) |  |  [optional] |
|**cardholderName** | **String** |  |  [optional] |
|**customerId** | **String** |  |  [optional] |
|**enabled** | **Boolean** | Indicates whether or not a card can be used for payments. |  [optional] |
|**expMonth** | **Integer** | The expiration month of the associated card as an integer between 1 and 12. |  [optional] |
|**expYear** | **Integer** | The four-digit year of the card&#39;s expiration date. |  [optional] |
|**fingerprint** | **String** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**last4** | **String** |  |  [optional] |
|**merchantId** | **String** |  |  [optional] |
|**prepaidType** | [**PrepaidTypeEnum**](#PrepaidTypeEnum) |  |  [optional] |
|**referenceId** | **String** | An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system. |  [optional] |
|**version** | **String** |  |  [optional] |



## Enum: CardBrandEnum

| Name | Value |
|---- | -----|
| VISA | &quot;visa&quot; |
| MASTERCARD | &quot;mastercard&quot; |
| AMEX | &quot;amex&quot; |
| DISCOVER | &quot;discover&quot; |
| DISCOVER_DINERS | &quot;discover-diners&quot; |
| JCB | &quot;jcb&quot; |
| CHINA_UNIONPAY | &quot;china-unionpay&quot; |
| SQUARE_GIFT_CARD | &quot;square-gift-card&quot; |
| SQUARE_CAPITAL_CARD | &quot;square-capital-card&quot; |
| INTERAC | &quot;interac&quot; |
| EFTPOS | &quot;eftpos&quot; |
| FELICA | &quot;felica&quot; |
| EBT | &quot;ebt&quot; |
| OTHER | &quot;other&quot; |



## Enum: CardTypeEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |
| PREPAID | &quot;prepaid&quot; |
| OTHER | &quot;other&quot; |



## Enum: PrepaidTypeEnum

| Name | Value |
|---- | -----|
| NON_PREPAID | &quot;non-prepaid&quot; |
| PREPAID | &quot;prepaid&quot; |
| UNKNOWN | &quot;unknown&quot; |



