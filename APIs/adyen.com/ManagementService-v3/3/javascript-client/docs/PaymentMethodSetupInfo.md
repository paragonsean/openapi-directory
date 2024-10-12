# ManagementApi.PaymentMethodSetupInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterpayTouch** | [**AfterpayTouchInfo**](AfterpayTouchInfo.md) | Afterpay Touch details. | [optional] 
**applePay** | [**ApplePayInfo**](ApplePayInfo.md) | Apple Pay details. | [optional] 
**bcmc** | [**BcmcInfo**](BcmcInfo.md) | Bancontact details. | [optional] 
**businessLineId** | **String** | The unique identifier of the business line. Required if you have a [platform setup](https://docs.adyen.com/marketplaces-and-platforms/platform-structure-resources/platform-setup/). | [optional] 
**cartesBancaires** | [**CartesBancairesInfo**](CartesBancairesInfo.md) | Cartes Bancaires details. | [optional] 
**clearpay** | [**ClearpayInfo**](ClearpayInfo.md) | Clearpay details. | [optional] 
**countries** | **[String]** | The list of countries where a payment method is available. By default, all countries supported by the payment method. | [optional] 
**cup** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | China Union Pay details. | [optional] 
**currencies** | **[String]** | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. | [optional] 
**customRoutingFlags** | **[String]** | The list of custom routing flags to route payment to the intended acquirer. | [optional] 
**diners** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Diners details. | [optional] 
**discover** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Discover details. | [optional] 
**eftposAustralia** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Eftpos Australia details. | [optional] 
**giroPay** | [**GiroPayInfo**](GiroPayInfo.md) | giropay details. | [optional] 
**girocard** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Girocard details. | [optional] 
**googlePay** | [**GooglePayInfo**](GooglePayInfo.md) | Google Pay details. | [optional] 
**ideal** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | iDeal details. | [optional] 
**interacCard** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Interac Card details. | [optional] 
**jcb** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | JCB details. | [optional] 
**klarna** | [**KlarnaInfo**](KlarnaInfo.md) | Klarna details. | [optional] 
**maestro** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Maestro details. | [optional] 
**mc** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | MasterCard details. | [optional] 
**mealVoucherFR** | [**MealVoucherFRInfo**](MealVoucherFRInfo.md) | Meal Voucher FR details. | [optional] 
**paypal** | [**PayPalInfo**](PayPalInfo.md) | PayPal details. | [optional] 
**reference** | **String** | Your reference for the payment method. Supported characters a-z, A-Z, 0-9. | [optional] 
**shopperInteraction** | **String** | The sales channel. Required if the merchant account does not have a sales channel. When you provide this field, it overrides the default sales channel set on the merchant account.  Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**.  | [optional] 
**sofort** | [**SofortInfo**](SofortInfo.md) | Sofort details. | [optional] 
**storeIds** | **[String]** | The unique identifier of the store for which to configure the payment method, if any. | [optional] 
**swish** | [**SwishInfo**](SwishInfo.md) | Swish details. | [optional] 
**twint** | [**TwintInfo**](TwintInfo.md) | Twint details. | [optional] 
**type** | **String** | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). | 
**vipps** | [**VippsInfo**](VippsInfo.md) | Vipps details. | [optional] 
**visa** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Visa details. | [optional] 



## Enum: ShopperInteractionEnum


* `eCommerce` (value: `"eCommerce"`)

* `pos` (value: `"pos"`)

* `moto` (value: `"moto"`)

* `contAuth` (value: `"contAuth"`)





## Enum: TypeEnum


* `afterpaytouch` (value: `"afterpaytouch"`)

* `alipay` (value: `"alipay"`)

* `alipay_hk` (value: `"alipay_hk"`)

* `amex` (value: `"amex"`)

* `applepay` (value: `"applepay"`)

* `bcmc` (value: `"bcmc"`)

* `blik` (value: `"blik"`)

* `cartebancaire` (value: `"cartebancaire"`)

* `clearpay` (value: `"clearpay"`)

* `cup` (value: `"cup"`)

* `diners` (value: `"diners"`)

* `directdebit_GB` (value: `"directdebit_GB"`)

* `discover` (value: `"discover"`)

* `ebanking_FI` (value: `"ebanking_FI"`)

* `eftpos_australia` (value: `"eftpos_australia"`)

* `elo` (value: `"elo"`)

* `elocredit` (value: `"elocredit"`)

* `elodebit` (value: `"elodebit"`)

* `girocard` (value: `"girocard"`)

* `googlepay` (value: `"googlepay"`)

* `hiper` (value: `"hiper"`)

* `hipercard` (value: `"hipercard"`)

* `ideal` (value: `"ideal"`)

* `interac_card` (value: `"interac_card"`)

* `jcb` (value: `"jcb"`)

* `klarna` (value: `"klarna"`)

* `klarna_account` (value: `"klarna_account"`)

* `klarna_paynow` (value: `"klarna_paynow"`)

* `maestro` (value: `"maestro"`)

* `mbway` (value: `"mbway"`)

* `mc` (value: `"mc"`)

* `mcdebit` (value: `"mcdebit"`)

* `mealVoucher_FR` (value: `"mealVoucher_FR"`)

* `mobilepay` (value: `"mobilepay"`)

* `multibanco` (value: `"multibanco"`)

* `onlineBanking_PL` (value: `"onlineBanking_PL"`)

* `paybybank` (value: `"paybybank"`)

* `paypal` (value: `"paypal"`)

* `payshop` (value: `"payshop"`)

* `swish` (value: `"swish"`)

* `trustly` (value: `"trustly"`)

* `twint` (value: `"twint"`)

* `twint_pos` (value: `"twint_pos"`)

* `vipps` (value: `"vipps"`)

* `visa` (value: `"visa"`)

* `visadebit` (value: `"visadebit"`)

* `vpay` (value: `"vpay"`)

* `wechatpay` (value: `"wechatpay"`)

* `wechatpay_pos` (value: `"wechatpay_pos"`)




