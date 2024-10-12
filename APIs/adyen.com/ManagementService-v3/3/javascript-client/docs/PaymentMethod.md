# ManagementApi.PaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterpayTouch** | [**AfterpayTouchInfo**](AfterpayTouchInfo.md) | Afterpay Touch details. | [optional] 
**allowed** | **Boolean** | Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your merchant account. | [optional] 
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
**enabled** | **Boolean** | Indicates whether the payment method is enabled (**true**) or disabled (**false**). | [optional] 
**giroPay** | [**GiroPayInfo**](GiroPayInfo.md) | giropay details. | [optional] 
**girocard** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Girocard details. | [optional] 
**googlePay** | [**GooglePayInfo**](GooglePayInfo.md) | Google Pay details. | [optional] 
**id** | **String** | The identifier of the resource. | 
**ideal** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | iDeal details. | [optional] 
**interacCard** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Interac Card details. | [optional] 
**jcb** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | JCB details. | [optional] 
**klarna** | [**KlarnaInfo**](KlarnaInfo.md) | Klarna details. | [optional] 
**maestro** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Maestro details. | [optional] 
**mc** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | MasterCard details. | [optional] 
**mealVoucherFR** | [**MealVoucherFRInfo**](MealVoucherFRInfo.md) | Meal Voucher FR details. | [optional] 
**paypal** | [**PayPalInfo**](PayPalInfo.md) | PayPal details. | [optional] 
**reference** | **String** | Your reference for the payment method. Supported characters a-z, A-Z, 0-9. | [optional] 
**shopperInteraction** | **String** | The sales channel. | [optional] 
**sofort** | [**SofortInfo**](SofortInfo.md) | Sofort details. | [optional] 
**storeIds** | **[String]** | The unique identifier of the store for which to configure the payment method, if any. | [optional] 
**swish** | [**SwishInfo**](SwishInfo.md) | Swish details. | [optional] 
**twint** | [**TwintInfo**](TwintInfo.md) | Twint details. | [optional] 
**type** | **String** | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). | [optional] 
**verificationStatus** | **String** | Payment method status. Possible values: * **valid** * **pending** * **invalid** * **rejected** | [optional] 
**vipps** | [**VippsInfo**](VippsInfo.md) | Vipps details. | [optional] 
**visa** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Visa details. | [optional] 



## Enum: VerificationStatusEnum


* `valid` (value: `"valid"`)

* `pending` (value: `"pending"`)

* `invalid` (value: `"invalid"`)

* `rejected` (value: `"rejected"`)




