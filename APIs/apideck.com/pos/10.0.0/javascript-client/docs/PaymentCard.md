# PosApi.PaymentCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**Address**](Address.md) |  | [optional] 
**bin** | **String** | The first six digits of the card number, known as the Bank Identification Number (BIN). | [optional] 
**cardBrand** | **String** | The first six digits of the card number, known as the Bank Identification Number (BIN). | [optional] 
**cardType** | **String** |  | [optional] 
**cardholderName** | **String** |  | [optional] 
**customerId** | **String** |  | [optional] 
**enabled** | **Boolean** | Indicates whether or not a card can be used for payments. | [optional] 
**expMonth** | **Number** | The expiration month of the associated card as an integer between 1 and 12. | [optional] 
**expYear** | **Number** | The four-digit year of the card&#39;s expiration date. | [optional] 
**fingerprint** | **String** |  | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**last4** | **String** |  | [optional] 
**merchantId** | **String** |  | [optional] 
**prepaidType** | **String** |  | [optional] 
**referenceId** | **String** | An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system. | [optional] 
**version** | **String** |  | [optional] 



## Enum: CardBrandEnum


* `visa` (value: `"visa"`)

* `mastercard` (value: `"mastercard"`)

* `amex` (value: `"amex"`)

* `discover` (value: `"discover"`)

* `discover-diners` (value: `"discover-diners"`)

* `jcb` (value: `"jcb"`)

* `china-unionpay` (value: `"china-unionpay"`)

* `square-gift-card` (value: `"square-gift-card"`)

* `square-capital-card` (value: `"square-capital-card"`)

* `interac` (value: `"interac"`)

* `eftpos` (value: `"eftpos"`)

* `felica` (value: `"felica"`)

* `ebt` (value: `"ebt"`)

* `other` (value: `"other"`)





## Enum: CardTypeEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)

* `prepaid` (value: `"prepaid"`)

* `other` (value: `"other"`)





## Enum: PrepaidTypeEnum


* `non-prepaid` (value: `"non-prepaid"`)

* `prepaid` (value: `"prepaid"`)

* `unknown` (value: `"unknown"`)




