

# PaymentMethodSetupInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterpayTouch** | [**AfterpayTouchInfo**](AfterpayTouchInfo.md) | Afterpay Touch details. |  [optional] |
|**applePay** | [**ApplePayInfo**](ApplePayInfo.md) | Apple Pay details. |  [optional] |
|**bcmc** | [**BcmcInfo**](BcmcInfo.md) | Bancontact details. |  [optional] |
|**businessLineId** | **String** | The unique identifier of the business line. Required if you have a [platform setup](https://docs.adyen.com/marketplaces-and-platforms/platform-structure-resources/platform-setup/). |  [optional] |
|**cartesBancaires** | [**CartesBancairesInfo**](CartesBancairesInfo.md) | Cartes Bancaires details. |  [optional] |
|**clearpay** | [**ClearpayInfo**](ClearpayInfo.md) | Clearpay details. |  [optional] |
|**countries** | **List&lt;String&gt;** | The list of countries where a payment method is available. By default, all countries supported by the payment method. |  [optional] |
|**cup** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | China Union Pay details. |  [optional] |
|**currencies** | **List&lt;String&gt;** | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |  [optional] |
|**customRoutingFlags** | **List&lt;String&gt;** | The list of custom routing flags to route payment to the intended acquirer. |  [optional] |
|**diners** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Diners details. |  [optional] |
|**discover** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Discover details. |  [optional] |
|**eftposAustralia** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Eftpos Australia details. |  [optional] |
|**giroPay** | [**GiroPayInfo**](GiroPayInfo.md) | giropay details. |  [optional] |
|**girocard** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Girocard details. |  [optional] |
|**googlePay** | [**GooglePayInfo**](GooglePayInfo.md) | Google Pay details. |  [optional] |
|**ideal** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | iDeal details. |  [optional] |
|**interacCard** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Interac Card details. |  [optional] |
|**jcb** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | JCB details. |  [optional] |
|**klarna** | [**KlarnaInfo**](KlarnaInfo.md) | Klarna details. |  [optional] |
|**maestro** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Maestro details. |  [optional] |
|**mc** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | MasterCard details. |  [optional] |
|**mealVoucherFR** | [**MealVoucherFRInfo**](MealVoucherFRInfo.md) | Meal Voucher FR details. |  [optional] |
|**paypal** | [**PayPalInfo**](PayPalInfo.md) | PayPal details. |  [optional] |
|**reference** | **String** | Your reference for the payment method. Supported characters a-z, A-Z, 0-9. |  [optional] |
|**shopperInteraction** | [**ShopperInteractionEnum**](#ShopperInteractionEnum) | The sales channel. Required if the merchant account does not have a sales channel. When you provide this field, it overrides the default sales channel set on the merchant account.  Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**.  |  [optional] |
|**sofort** | [**SofortInfo**](SofortInfo.md) | Sofort details. |  [optional] |
|**storeIds** | **List&lt;String&gt;** | The unique identifier of the store for which to configure the payment method, if any. |  [optional] |
|**swish** | [**SwishInfo**](SwishInfo.md) | Swish details. |  [optional] |
|**twint** | [**TwintInfo**](TwintInfo.md) | Twint details. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). |  |
|**vipps** | [**VippsInfo**](VippsInfo.md) | Vipps details. |  [optional] |
|**visa** | [**GenericPmWithTdiInfo**](GenericPmWithTdiInfo.md) | Visa details. |  [optional] |



## Enum: ShopperInteractionEnum

| Name | Value |
|---- | -----|
| E_COMMERCE | &quot;eCommerce&quot; |
| POS | &quot;pos&quot; |
| MOTO | &quot;moto&quot; |
| CONT_AUTH | &quot;contAuth&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AFTERPAYTOUCH | &quot;afterpaytouch&quot; |
| ALIPAY | &quot;alipay&quot; |
| ALIPAY_HK | &quot;alipay_hk&quot; |
| AMEX | &quot;amex&quot; |
| APPLEPAY | &quot;applepay&quot; |
| BCMC | &quot;bcmc&quot; |
| BLIK | &quot;blik&quot; |
| CARTEBANCAIRE | &quot;cartebancaire&quot; |
| CLEARPAY | &quot;clearpay&quot; |
| CUP | &quot;cup&quot; |
| DINERS | &quot;diners&quot; |
| DIRECTDEBIT_GB | &quot;directdebit_GB&quot; |
| DISCOVER | &quot;discover&quot; |
| EBANKING_FI | &quot;ebanking_FI&quot; |
| EFTPOS_AUSTRALIA | &quot;eftpos_australia&quot; |
| ELO | &quot;elo&quot; |
| ELOCREDIT | &quot;elocredit&quot; |
| ELODEBIT | &quot;elodebit&quot; |
| GIROCARD | &quot;girocard&quot; |
| GOOGLEPAY | &quot;googlepay&quot; |
| HIPER | &quot;hiper&quot; |
| HIPERCARD | &quot;hipercard&quot; |
| IDEAL | &quot;ideal&quot; |
| INTERAC_CARD | &quot;interac_card&quot; |
| JCB | &quot;jcb&quot; |
| KLARNA | &quot;klarna&quot; |
| KLARNA_ACCOUNT | &quot;klarna_account&quot; |
| KLARNA_PAYNOW | &quot;klarna_paynow&quot; |
| MAESTRO | &quot;maestro&quot; |
| MBWAY | &quot;mbway&quot; |
| MC | &quot;mc&quot; |
| MCDEBIT | &quot;mcdebit&quot; |
| MEAL_VOUCHER_FR | &quot;mealVoucher_FR&quot; |
| MOBILEPAY | &quot;mobilepay&quot; |
| MULTIBANCO | &quot;multibanco&quot; |
| ONLINE_BANKING_PL | &quot;onlineBanking_PL&quot; |
| PAYBYBANK | &quot;paybybank&quot; |
| PAYPAL | &quot;paypal&quot; |
| PAYSHOP | &quot;payshop&quot; |
| SWISH | &quot;swish&quot; |
| TRUSTLY | &quot;trustly&quot; |
| TWINT | &quot;twint&quot; |
| TWINT_POS | &quot;twint_pos&quot; |
| VIPPS | &quot;vipps&quot; |
| VISA | &quot;visa&quot; |
| VISADEBIT | &quot;visadebit&quot; |
| VPAY | &quot;vpay&quot; |
| WECHATPAY | &quot;wechatpay&quot; |
| WECHATPAY_POS | &quot;wechatpay_pos&quot; |



