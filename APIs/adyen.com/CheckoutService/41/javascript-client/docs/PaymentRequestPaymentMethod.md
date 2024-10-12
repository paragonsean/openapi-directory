# AdyenCheckoutApi.PaymentRequestPaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankAccountNumber** | **String** | The bank account number (without separators). | 
**bankAccountType** | **String** | The bank account type (checking, savings...). | [optional] 
**bankLocationId** | **String** | The bank routing number of the account. The field value is &#x60;nil&#x60; in most cases. | [optional] 
**encryptedBankAccountNumber** | **String** | Encrypted bank account number. The bank account number (without separators). | [optional] 
**encryptedBankLocationId** | **String** | Encrypted location id. The bank routing number of the account. The field value is &#x60;nil&#x60; in most cases. | [optional] 
**ownerName** | **String** | The name of the bank account holder. | 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **ach** | [default to &#39;ach&#39;]
**billingAddress** | **String** | The address where to send the invoice. | [optional] 
**deliveryAddress** | **String** | The address where the goods should be delivered. | [optional] 
**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. | [optional] 
**amazonPayToken** | **String** | This is the &#x60;amazonPayToken&#x60; that you obtained from the [Get Checkout Session](https://amazon-pay-acquirer-guide.s3-eu-west-1.amazonaws.com/v1/amazon-pay-api-v2/checkout-session.html#get-checkout-session) response. This token is used for API only integration specifically. | [optional] 
**checkoutSessionId** | **String** | The &#x60;checkoutSessionId&#x60; is used to identify the checkout session at the Amazon Pay side. This field is required only for drop-in and components integration, where it replaces the amazonPayToken. | [optional] 
**applePayToken** | **String** | The stringified and base64 encoded &#x60;paymentData&#x60; you retrieved from the Apple framework. | 
**fundingSource** | **String** | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. | [optional] 
**issuer** | **String** | The shopper&#39;s bank. Specify this with the issuer value that corresponds to this bank. | 
**blikCode** | **String** | BLIK code consisting of 6 digits. | [optional] 
**brand** | **String** | Secondary brand of the card. For example: **plastix**, **hmclub**. | [optional] 
**cupsecureplusSmscode** | **String** |  | [optional] 
**cvc** | **String** | The card verification code. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). | [optional] 
**encryptedCardNumber** | **String** | The encrypted card number. | [optional] 
**encryptedExpiryMonth** | **String** | The encrypted card expiry month. | [optional] 
**encryptedExpiryYear** | **String** | The encrypted card expiry year. | [optional] 
**encryptedSecurityCode** | **String** | The encrypted card verification code. | [optional] 
**expiryMonth** | **String** | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). | [optional] 
**expiryYear** | **String** | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). | [optional] 
**holderName** | **String** | The name of the card holder. | [optional] 
**networkPaymentReference** | **String** | The network token reference. This is the [&#x60;networkTxReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-networkTxReference) from the response to the first payment. | [optional] 
**number** | **String** | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). | [optional] 
**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used for recurring payment only. | [optional] 
**threeDS2SdkVersion** | **String** | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK. | [optional] 
**firstName** | **String** | The shopper&#39;s first name. | 
**lastName** | **String** | The shopper&#39;s last name. | 
**shopperEmail** | **String** |  | 
**telephoneNumber** | **String** |  | 
**googlePayCardNetwork** | **String** | The selected payment card network.  | [optional] 
**googlePayToken** | **String** | The &#x60;token&#x60; that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) &#x60;PaymentData&#x60; response. | 
**subtype** | **String** | The type of flow to initiate. | [optional] 
**masterpassTransactionId** | **String** | The Masterpass transaction ID. | 
**orderID** | **String** | The unique ID associated with the order. | [optional] 
**payeePreferred** | **String** | IMMEDIATE_PAYMENT_REQUIRED or UNRESTRICTED | [optional] 
**payerID** | **String** | The unique ID associated with the payer. | [optional] 
**payerSelected** | **String** | PAYPAL or PAYPAL_CREDIT | [optional] 
**virtualPaymentAddress** | **String** | The virtual payment address for UPI. | [optional] 
**samsungPayToken** | **String** | The payload you received from the Samsung Pay SDK response. | 
**iban** | **String** | The International Bank Account Number (IBAN). | 
**billingSequenceNumber** | **String** | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. | 
**visaCheckoutCallId** | **String** | The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID. | 
**appId** | **String** |  | [optional] 
**openid** | **String** |  | [optional] 
**clickAndCollect** | **String** | Set this to **true** if the shopper would like to pick up and collect their order, instead of having the goods delivered to them. | [optional] 



## Enum: BankAccountTypeEnum


* `balance` (value: `"balance"`)

* `checking` (value: `"checking"`)

* `deposit` (value: `"deposit"`)

* `general` (value: `"general"`)

* `other` (value: `"other"`)

* `payment` (value: `"payment"`)

* `savings` (value: `"savings"`)





## Enum: TypeEnum


* `ach` (value: `"ach"`)

* `ach_plaid` (value: `"ach_plaid"`)

* `afterpay_default` (value: `"afterpay_default"`)

* `afterpaytouch` (value: `"afterpaytouch"`)

* `afterpay_b2b` (value: `"afterpay_b2b"`)

* `clearpay` (value: `"clearpay"`)

* `amazonpay` (value: `"amazonpay"`)

* `androidpay` (value: `"androidpay"`)

* `applepay` (value: `"applepay"`)

* `directdebit_GB` (value: `"directdebit_GB"`)

* `billdesk_online` (value: `"billdesk_online"`)

* `billdesk_wallet` (value: `"billdesk_wallet"`)

* `blik` (value: `"blik"`)

* `bcmc` (value: `"bcmc"`)

* `scheme` (value: `"scheme"`)

* `networkToken` (value: `"networkToken"`)

* `giftcard` (value: `"giftcard"`)

* `card` (value: `"card"`)

* `cellulant` (value: `"cellulant"`)

* `doku_mandiri_va` (value: `"doku_mandiri_va"`)

* `doku_cimb_va` (value: `"doku_cimb_va"`)

* `doku_danamon_va` (value: `"doku_danamon_va"`)

* `doku_bni_va` (value: `"doku_bni_va"`)

* `doku_permata_lite_atm` (value: `"doku_permata_lite_atm"`)

* `doku_bri_va` (value: `"doku_bri_va"`)

* `doku_bca_va` (value: `"doku_bca_va"`)

* `doku_alfamart` (value: `"doku_alfamart"`)

* `doku_indomaret` (value: `"doku_indomaret"`)

* `doku_wallet` (value: `"doku_wallet"`)

* `doku_ovo` (value: `"doku_ovo"`)

* `dotpay` (value: `"dotpay"`)

* `dragonpay_ebanking` (value: `"dragonpay_ebanking"`)

* `dragonpay_otc_banking` (value: `"dragonpay_otc_banking"`)

* `dragonpay_otc_non_banking` (value: `"dragonpay_otc_non_banking"`)

* `dragonpay_otc_philippines` (value: `"dragonpay_otc_philippines"`)

* `econtext_seveneleven` (value: `"econtext_seveneleven"`)

* `econtext_stores` (value: `"econtext_stores"`)

* `onlineBanking_PL` (value: `"onlineBanking_PL"`)

* `eps` (value: `"eps"`)

* `onlineBanking_SK` (value: `"onlineBanking_SK"`)

* `onlineBanking_CZ` (value: `"onlineBanking_CZ"`)

* `giropay` (value: `"giropay"`)

* `googlepay` (value: `"googlepay"`)

* `ideal` (value: `"ideal"`)

* `klarna` (value: `"klarna"`)

* `klarnapayments` (value: `"klarnapayments"`)

* `klarnapayments_account` (value: `"klarnapayments_account"`)

* `klarnapayments_b2b` (value: `"klarnapayments_b2b"`)

* `klarna_paynow` (value: `"klarna_paynow"`)

* `klarna_account` (value: `"klarna_account"`)

* `klarna_b2b` (value: `"klarna_b2b"`)

* `masterpass` (value: `"masterpass"`)

* `mbway` (value: `"mbway"`)

* `mobilepay` (value: `"mobilepay"`)

* `molpay_ebanking_fpx_MY` (value: `"molpay_ebanking_fpx_MY"`)

* `molpay_ebanking_TH` (value: `"molpay_ebanking_TH"`)

* `openinvoice` (value: `"openinvoice"`)

* `afterpay_directdebit` (value: `"afterpay_directdebit"`)

* `atome_pos` (value: `"atome_pos"`)

* `paypal` (value: `"paypal"`)

* `payu_IN_upi` (value: `"payu_IN_upi"`)

* `paywithgoogle` (value: `"paywithgoogle"`)

* `alipay` (value: `"alipay"`)

* `multibanco` (value: `"multibanco"`)

* `bankTransfer_IBAN` (value: `"bankTransfer_IBAN"`)

* `paybright` (value: `"paybright"`)

* `paynow` (value: `"paynow"`)

* `affirm` (value: `"affirm"`)

* `affirm_pos` (value: `"affirm_pos"`)

* `trustly` (value: `"trustly"`)

* `trustlyvector` (value: `"trustlyvector"`)

* `oney` (value: `"oney"`)

* `facilypay` (value: `"facilypay"`)

* `facilypay_3x` (value: `"facilypay_3x"`)

* `facilypay_4x` (value: `"facilypay_4x"`)

* `facilypay_6x` (value: `"facilypay_6x"`)

* `facilypay_10x` (value: `"facilypay_10x"`)

* `facilypay_12x` (value: `"facilypay_12x"`)

* `unionpay` (value: `"unionpay"`)

* `kcp_banktransfer` (value: `"kcp_banktransfer"`)

* `kcp_payco` (value: `"kcp_payco"`)

* `kcp_creditcard` (value: `"kcp_creditcard"`)

* `wechatpaySDK` (value: `"wechatpaySDK"`)

* `wechatpayQR` (value: `"wechatpayQR"`)

* `wechatpayWeb` (value: `"wechatpayWeb"`)

* `molpay_boost` (value: `"molpay_boost"`)

* `wallet_IN` (value: `"wallet_IN"`)

* `payu_IN_cashcard` (value: `"payu_IN_cashcard"`)

* `payu_IN_nb` (value: `"payu_IN_nb"`)

* `upi_qr` (value: `"upi_qr"`)

* `paytm` (value: `"paytm"`)

* `molpay_ebanking_VN` (value: `"molpay_ebanking_VN"`)

* `paybybank` (value: `"paybybank"`)

* `ebanking_FI` (value: `"ebanking_FI"`)

* `molpay_ebanking_MY` (value: `"molpay_ebanking_MY"`)

* `molpay_ebanking_direct_MY` (value: `"molpay_ebanking_direct_MY"`)

* `swish` (value: `"swish"`)

* `pix` (value: `"pix"`)

* `walley` (value: `"walley"`)

* `walley_b2b` (value: `"walley_b2b"`)

* `alma` (value: `"alma"`)

* `paypo` (value: `"paypo"`)

* `molpay_fpx` (value: `"molpay_fpx"`)

* `konbini` (value: `"konbini"`)

* `directEbanking` (value: `"directEbanking"`)

* `boletobancario` (value: `"boletobancario"`)

* `neteller` (value: `"neteller"`)

* `paysafecard` (value: `"paysafecard"`)

* `cashticket` (value: `"cashticket"`)

* `ikano` (value: `"ikano"`)

* `karenmillen` (value: `"karenmillen"`)

* `oasis` (value: `"oasis"`)

* `warehouse` (value: `"warehouse"`)

* `primeiropay_boleto` (value: `"primeiropay_boleto"`)

* `mada` (value: `"mada"`)

* `benefit` (value: `"benefit"`)

* `knet` (value: `"knet"`)

* `omannet` (value: `"omannet"`)

* `gopay_wallet` (value: `"gopay_wallet"`)

* `kcp_naverpay` (value: `"kcp_naverpay"`)

* `onlinebanking_IN` (value: `"onlinebanking_IN"`)

* `fawry` (value: `"fawry"`)

* `atome` (value: `"atome"`)

* `moneybookers` (value: `"moneybookers"`)

* `naps` (value: `"naps"`)

* `nordea` (value: `"nordea"`)

* `boletobancario_bradesco` (value: `"boletobancario_bradesco"`)

* `boletobancario_itau` (value: `"boletobancario_itau"`)

* `boletobancario_santander` (value: `"boletobancario_santander"`)

* `boletobancario_bancodobrasil` (value: `"boletobancario_bancodobrasil"`)

* `boletobancario_hsbc` (value: `"boletobancario_hsbc"`)

* `molpay_maybank2u` (value: `"molpay_maybank2u"`)

* `molpay_cimb` (value: `"molpay_cimb"`)

* `molpay_rhb` (value: `"molpay_rhb"`)

* `molpay_amb` (value: `"molpay_amb"`)

* `molpay_hlb` (value: `"molpay_hlb"`)

* `molpay_affin_epg` (value: `"molpay_affin_epg"`)

* `molpay_bankislam` (value: `"molpay_bankislam"`)

* `molpay_publicbank` (value: `"molpay_publicbank"`)

* `fpx_agrobank` (value: `"fpx_agrobank"`)

* `touchngo` (value: `"touchngo"`)

* `maybank2u_mae` (value: `"maybank2u_mae"`)

* `duitnow` (value: `"duitnow"`)

* `promptpay` (value: `"promptpay"`)

* `twint_pos` (value: `"twint_pos"`)

* `alipay_hk` (value: `"alipay_hk"`)

* `alipay_hk_web` (value: `"alipay_hk_web"`)

* `alipay_hk_wap` (value: `"alipay_hk_wap"`)

* `alipay_wap` (value: `"alipay_wap"`)

* `balanceplatform` (value: `"balanceplatform"`)

* `ratepay` (value: `"ratepay"`)

* `ratepay_directdebit` (value: `"ratepay_directdebit"`)

* `samsungpay` (value: `"samsungpay"`)

* `sepadirectdebit` (value: `"sepadirectdebit"`)

* `sepadirectdebit_amazonpay` (value: `"sepadirectdebit_amazonpay"`)

* `bcmc_mobile` (value: `"bcmc_mobile"`)

* `bcmc_mobile_QR` (value: `"bcmc_mobile_QR"`)

* `bcmc_mobile_app` (value: `"bcmc_mobile_app"`)

* `momo_wallet` (value: `"momo_wallet"`)

* `momo_wallet_app` (value: `"momo_wallet_app"`)

* `twint` (value: `"twint"`)

* `paymaya_wallet` (value: `"paymaya_wallet"`)

* `grabpay_SG` (value: `"grabpay_SG"`)

* `grabpay_MY` (value: `"grabpay_MY"`)

* `grabpay_TH` (value: `"grabpay_TH"`)

* `grabpay_ID` (value: `"grabpay_ID"`)

* `grabpay_VN` (value: `"grabpay_VN"`)

* `grabpay_PH` (value: `"grabpay_PH"`)

* `oxxo` (value: `"oxxo"`)

* `gcash` (value: `"gcash"`)

* `dana` (value: `"dana"`)

* `kakaopay` (value: `"kakaopay"`)

* `truemoney` (value: `"truemoney"`)

* `upi_collect` (value: `"upi_collect"`)

* `upi_intent` (value: `"upi_intent"`)

* `vipps` (value: `"vipps"`)

* `visacheckout` (value: `"visacheckout"`)

* `wechatpay` (value: `"wechatpay"`)

* `wechatpay_pos` (value: `"wechatpay_pos"`)

* `wechatpayMiniProgram` (value: `"wechatpayMiniProgram"`)

* `zip` (value: `"zip"`)

* `zip_pos` (value: `"zip_pos"`)





## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: SubtypeEnum


* `redirect` (value: `"redirect"`)

* `sdk` (value: `"sdk"`)




