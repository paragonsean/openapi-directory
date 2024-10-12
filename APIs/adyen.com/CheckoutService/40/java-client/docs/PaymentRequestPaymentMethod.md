

# PaymentRequestPaymentMethod

The type and required details of a payment method to use.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccountNumber** | **String** | The bank account number (without separators). |  |
|**bankAccountType** | [**BankAccountTypeEnum**](#BankAccountTypeEnum) | The bank account type (checking, savings...). |  [optional] |
|**bankLocationId** | **String** | The bank routing number of the account. The field value is &#x60;nil&#x60; in most cases. |  [optional] |
|**encryptedBankAccountNumber** | **String** | Encrypted bank account number. The bank account number (without separators). |  [optional] |
|**encryptedBankLocationId** | **String** | Encrypted location id. The bank routing number of the account. The field value is &#x60;nil&#x60; in most cases. |  [optional] |
|**ownerName** | **String** | The name of the bank account holder. |  |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **ach** |  |
|**billingAddress** | **String** | The address where to send the invoice. |  [optional] |
|**deliveryAddress** | **String** | The address where the goods should be delivered. |  [optional] |
|**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. |  [optional] |
|**amazonPayToken** | **String** | This is the &#x60;amazonPayToken&#x60; that you obtained from the [Get Checkout Session](https://amazon-pay-acquirer-guide.s3-eu-west-1.amazonaws.com/v1/amazon-pay-api-v2/checkout-session.html#get-checkout-session) response. This token is used for API only integration specifically. |  [optional] |
|**checkoutSessionId** | **String** | The &#x60;checkoutSessionId&#x60; is used to identify the checkout session at the Amazon Pay side. This field is required only for drop-in and components integration, where it replaces the amazonPayToken. |  [optional] |
|**applePayToken** | **String** | The stringified and base64 encoded &#x60;paymentData&#x60; you retrieved from the Apple framework. |  |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**issuer** | **String** | The shopper&#39;s bank. Specify this with the issuer value that corresponds to this bank. |  |
|**blikCode** | **String** | BLIK code consisting of 6 digits. |  [optional] |
|**brand** | **String** | Secondary brand of the card. For example: **plastix**, **hmclub**. |  [optional] |
|**cupsecureplusSmscode** | **String** |  |  [optional] |
|**cvc** | **String** | The card verification code. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**encryptedCardNumber** | **String** | The encrypted card number. |  [optional] |
|**encryptedExpiryMonth** | **String** | The encrypted card expiry month. |  [optional] |
|**encryptedExpiryYear** | **String** | The encrypted card expiry year. |  [optional] |
|**encryptedSecurityCode** | **String** | The encrypted card verification code. |  [optional] |
|**expiryMonth** | **String** | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**expiryYear** | **String** | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**holderName** | **String** | The name of the card holder. |  [optional] |
|**networkPaymentReference** | **String** | The network token reference. This is the [&#x60;networkTxReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-networkTxReference) from the response to the first payment. |  [optional] |
|**number** | **String** | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used for recurring payment only. |  [optional] |
|**threeDS2SdkVersion** | **String** | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK. |  [optional] |
|**firstName** | **String** | The shopper&#39;s first name. |  |
|**lastName** | **String** | The shopper&#39;s last name. |  |
|**shopperEmail** | **String** |  |  |
|**telephoneNumber** | **String** |  |  |
|**googlePayCardNetwork** | **String** | The selected payment card network.  |  [optional] |
|**googlePayToken** | **String** | The &#x60;token&#x60; that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) &#x60;PaymentData&#x60; response. |  |
|**subtype** | [**SubtypeEnum**](#SubtypeEnum) | The type of flow to initiate. |  [optional] |
|**masterpassTransactionId** | **String** | The Masterpass transaction ID. |  |
|**orderID** | **String** | The unique ID associated with the order. |  [optional] |
|**payeePreferred** | **String** | IMMEDIATE_PAYMENT_REQUIRED or UNRESTRICTED |  [optional] |
|**payerID** | **String** | The unique ID associated with the payer. |  [optional] |
|**payerSelected** | **String** | PAYPAL or PAYPAL_CREDIT |  [optional] |
|**virtualPaymentAddress** | **String** | The virtual payment address for UPI. |  [optional] |
|**samsungPayToken** | **String** | The payload you received from the Samsung Pay SDK response. |  |
|**iban** | **String** | The International Bank Account Number (IBAN). |  |
|**billingSequenceNumber** | **String** | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. |  |
|**visaCheckoutCallId** | **String** | The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID. |  |
|**appId** | **String** |  |  [optional] |
|**openid** | **String** |  |  [optional] |
|**clickAndCollect** | **String** | Set this to **true** if the shopper would like to pick up and collect their order, instead of having the goods delivered to them. |  [optional] |



## Enum: BankAccountTypeEnum

| Name | Value |
|---- | -----|
| BALANCE | &quot;balance&quot; |
| CHECKING | &quot;checking&quot; |
| DEPOSIT | &quot;deposit&quot; |
| GENERAL | &quot;general&quot; |
| OTHER | &quot;other&quot; |
| PAYMENT | &quot;payment&quot; |
| SAVINGS | &quot;savings&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACH | &quot;ach&quot; |
| ACH_PLAID | &quot;ach_plaid&quot; |
| AFTERPAY_DEFAULT | &quot;afterpay_default&quot; |
| AFTERPAYTOUCH | &quot;afterpaytouch&quot; |
| AFTERPAY_B2B | &quot;afterpay_b2b&quot; |
| CLEARPAY | &quot;clearpay&quot; |
| AMAZONPAY | &quot;amazonpay&quot; |
| ANDROIDPAY | &quot;androidpay&quot; |
| APPLEPAY | &quot;applepay&quot; |
| DIRECTDEBIT_GB | &quot;directdebit_GB&quot; |
| BILLDESK_ONLINE | &quot;billdesk_online&quot; |
| BILLDESK_WALLET | &quot;billdesk_wallet&quot; |
| BLIK | &quot;blik&quot; |
| BCMC | &quot;bcmc&quot; |
| SCHEME | &quot;scheme&quot; |
| NETWORK_TOKEN | &quot;networkToken&quot; |
| GIFTCARD | &quot;giftcard&quot; |
| CARD | &quot;card&quot; |
| CELLULANT | &quot;cellulant&quot; |
| DOKU_MANDIRI_VA | &quot;doku_mandiri_va&quot; |
| DOKU_CIMB_VA | &quot;doku_cimb_va&quot; |
| DOKU_DANAMON_VA | &quot;doku_danamon_va&quot; |
| DOKU_BNI_VA | &quot;doku_bni_va&quot; |
| DOKU_PERMATA_LITE_ATM | &quot;doku_permata_lite_atm&quot; |
| DOKU_BRI_VA | &quot;doku_bri_va&quot; |
| DOKU_BCA_VA | &quot;doku_bca_va&quot; |
| DOKU_ALFAMART | &quot;doku_alfamart&quot; |
| DOKU_INDOMARET | &quot;doku_indomaret&quot; |
| DOKU_WALLET | &quot;doku_wallet&quot; |
| DOKU_OVO | &quot;doku_ovo&quot; |
| DOTPAY | &quot;dotpay&quot; |
| DRAGONPAY_EBANKING | &quot;dragonpay_ebanking&quot; |
| DRAGONPAY_OTC_BANKING | &quot;dragonpay_otc_banking&quot; |
| DRAGONPAY_OTC_NON_BANKING | &quot;dragonpay_otc_non_banking&quot; |
| DRAGONPAY_OTC_PHILIPPINES | &quot;dragonpay_otc_philippines&quot; |
| ECONTEXT_SEVENELEVEN | &quot;econtext_seveneleven&quot; |
| ECONTEXT_STORES | &quot;econtext_stores&quot; |
| ONLINE_BANKING_PL | &quot;onlineBanking_PL&quot; |
| EPS | &quot;eps&quot; |
| ONLINE_BANKING_SK | &quot;onlineBanking_SK&quot; |
| ONLINE_BANKING_CZ | &quot;onlineBanking_CZ&quot; |
| GIROPAY | &quot;giropay&quot; |
| GOOGLEPAY | &quot;googlepay&quot; |
| IDEAL | &quot;ideal&quot; |
| KLARNA | &quot;klarna&quot; |
| KLARNAPAYMENTS | &quot;klarnapayments&quot; |
| KLARNAPAYMENTS_ACCOUNT | &quot;klarnapayments_account&quot; |
| KLARNAPAYMENTS_B2B | &quot;klarnapayments_b2b&quot; |
| KLARNA_PAYNOW | &quot;klarna_paynow&quot; |
| KLARNA_ACCOUNT | &quot;klarna_account&quot; |
| KLARNA_B2B | &quot;klarna_b2b&quot; |
| MASTERPASS | &quot;masterpass&quot; |
| MBWAY | &quot;mbway&quot; |
| MOBILEPAY | &quot;mobilepay&quot; |
| MOLPAY_EBANKING_FPX_MY | &quot;molpay_ebanking_fpx_MY&quot; |
| MOLPAY_EBANKING_TH | &quot;molpay_ebanking_TH&quot; |
| OPENINVOICE | &quot;openinvoice&quot; |
| AFTERPAY_DIRECTDEBIT | &quot;afterpay_directdebit&quot; |
| ATOME_POS | &quot;atome_pos&quot; |
| PAYPAL | &quot;paypal&quot; |
| PAYU_IN_UPI | &quot;payu_IN_upi&quot; |
| PAYWITHGOOGLE | &quot;paywithgoogle&quot; |
| ALIPAY | &quot;alipay&quot; |
| MULTIBANCO | &quot;multibanco&quot; |
| BANK_TRANSFER_IBAN | &quot;bankTransfer_IBAN&quot; |
| PAYBRIGHT | &quot;paybright&quot; |
| PAYNOW | &quot;paynow&quot; |
| AFFIRM | &quot;affirm&quot; |
| AFFIRM_POS | &quot;affirm_pos&quot; |
| TRUSTLY | &quot;trustly&quot; |
| TRUSTLYVECTOR | &quot;trustlyvector&quot; |
| ONEY | &quot;oney&quot; |
| FACILYPAY | &quot;facilypay&quot; |
| FACILYPAY_3X | &quot;facilypay_3x&quot; |
| FACILYPAY_4X | &quot;facilypay_4x&quot; |
| FACILYPAY_6X | &quot;facilypay_6x&quot; |
| FACILYPAY_10X | &quot;facilypay_10x&quot; |
| FACILYPAY_12X | &quot;facilypay_12x&quot; |
| UNIONPAY | &quot;unionpay&quot; |
| KCP_BANKTRANSFER | &quot;kcp_banktransfer&quot; |
| KCP_PAYCO | &quot;kcp_payco&quot; |
| KCP_CREDITCARD | &quot;kcp_creditcard&quot; |
| WECHATPAY_SDK | &quot;wechatpaySDK&quot; |
| WECHATPAY_QR | &quot;wechatpayQR&quot; |
| WECHATPAY_WEB | &quot;wechatpayWeb&quot; |
| MOLPAY_BOOST | &quot;molpay_boost&quot; |
| WALLET_IN | &quot;wallet_IN&quot; |
| PAYU_IN_CASHCARD | &quot;payu_IN_cashcard&quot; |
| PAYU_IN_NB | &quot;payu_IN_nb&quot; |
| UPI_QR | &quot;upi_qr&quot; |
| PAYTM | &quot;paytm&quot; |
| MOLPAY_EBANKING_VN | &quot;molpay_ebanking_VN&quot; |
| PAYBYBANK | &quot;paybybank&quot; |
| EBANKING_FI | &quot;ebanking_FI&quot; |
| MOLPAY_EBANKING_MY | &quot;molpay_ebanking_MY&quot; |
| MOLPAY_EBANKING_DIRECT_MY | &quot;molpay_ebanking_direct_MY&quot; |
| SWISH | &quot;swish&quot; |
| PIX | &quot;pix&quot; |
| WALLEY | &quot;walley&quot; |
| WALLEY_B2B | &quot;walley_b2b&quot; |
| ALMA | &quot;alma&quot; |
| PAYPO | &quot;paypo&quot; |
| MOLPAY_FPX | &quot;molpay_fpx&quot; |
| KONBINI | &quot;konbini&quot; |
| DIRECT_EBANKING | &quot;directEbanking&quot; |
| BOLETOBANCARIO | &quot;boletobancario&quot; |
| NETELLER | &quot;neteller&quot; |
| PAYSAFECARD | &quot;paysafecard&quot; |
| CASHTICKET | &quot;cashticket&quot; |
| IKANO | &quot;ikano&quot; |
| KARENMILLEN | &quot;karenmillen&quot; |
| OASIS | &quot;oasis&quot; |
| WAREHOUSE | &quot;warehouse&quot; |
| PRIMEIROPAY_BOLETO | &quot;primeiropay_boleto&quot; |
| MADA | &quot;mada&quot; |
| BENEFIT | &quot;benefit&quot; |
| KNET | &quot;knet&quot; |
| OMANNET | &quot;omannet&quot; |
| GOPAY_WALLET | &quot;gopay_wallet&quot; |
| KCP_NAVERPAY | &quot;kcp_naverpay&quot; |
| ONLINEBANKING_IN | &quot;onlinebanking_IN&quot; |
| FAWRY | &quot;fawry&quot; |
| ATOME | &quot;atome&quot; |
| MONEYBOOKERS | &quot;moneybookers&quot; |
| NAPS | &quot;naps&quot; |
| NORDEA | &quot;nordea&quot; |
| BOLETOBANCARIO_BRADESCO | &quot;boletobancario_bradesco&quot; |
| BOLETOBANCARIO_ITAU | &quot;boletobancario_itau&quot; |
| BOLETOBANCARIO_SANTANDER | &quot;boletobancario_santander&quot; |
| BOLETOBANCARIO_BANCODOBRASIL | &quot;boletobancario_bancodobrasil&quot; |
| BOLETOBANCARIO_HSBC | &quot;boletobancario_hsbc&quot; |
| MOLPAY_MAYBANK2U | &quot;molpay_maybank2u&quot; |
| MOLPAY_CIMB | &quot;molpay_cimb&quot; |
| MOLPAY_RHB | &quot;molpay_rhb&quot; |
| MOLPAY_AMB | &quot;molpay_amb&quot; |
| MOLPAY_HLB | &quot;molpay_hlb&quot; |
| MOLPAY_AFFIN_EPG | &quot;molpay_affin_epg&quot; |
| MOLPAY_BANKISLAM | &quot;molpay_bankislam&quot; |
| MOLPAY_PUBLICBANK | &quot;molpay_publicbank&quot; |
| FPX_AGROBANK | &quot;fpx_agrobank&quot; |
| TOUCHNGO | &quot;touchngo&quot; |
| MAYBANK2U_MAE | &quot;maybank2u_mae&quot; |
| DUITNOW | &quot;duitnow&quot; |
| PROMPTPAY | &quot;promptpay&quot; |
| TWINT_POS | &quot;twint_pos&quot; |
| ALIPAY_HK | &quot;alipay_hk&quot; |
| ALIPAY_HK_WEB | &quot;alipay_hk_web&quot; |
| ALIPAY_HK_WAP | &quot;alipay_hk_wap&quot; |
| ALIPAY_WAP | &quot;alipay_wap&quot; |
| BALANCEPLATFORM | &quot;balanceplatform&quot; |
| RATEPAY | &quot;ratepay&quot; |
| RATEPAY_DIRECTDEBIT | &quot;ratepay_directdebit&quot; |
| SAMSUNGPAY | &quot;samsungpay&quot; |
| SEPADIRECTDEBIT | &quot;sepadirectdebit&quot; |
| SEPADIRECTDEBIT_AMAZONPAY | &quot;sepadirectdebit_amazonpay&quot; |
| BCMC_MOBILE | &quot;bcmc_mobile&quot; |
| BCMC_MOBILE_QR | &quot;bcmc_mobile_QR&quot; |
| BCMC_MOBILE_APP | &quot;bcmc_mobile_app&quot; |
| MOMO_WALLET | &quot;momo_wallet&quot; |
| MOMO_WALLET_APP | &quot;momo_wallet_app&quot; |
| TWINT | &quot;twint&quot; |
| PAYMAYA_WALLET | &quot;paymaya_wallet&quot; |
| GRABPAY_SG | &quot;grabpay_SG&quot; |
| GRABPAY_MY | &quot;grabpay_MY&quot; |
| GRABPAY_TH | &quot;grabpay_TH&quot; |
| GRABPAY_ID | &quot;grabpay_ID&quot; |
| GRABPAY_VN | &quot;grabpay_VN&quot; |
| GRABPAY_PH | &quot;grabpay_PH&quot; |
| OXXO | &quot;oxxo&quot; |
| GCASH | &quot;gcash&quot; |
| DANA | &quot;dana&quot; |
| KAKAOPAY | &quot;kakaopay&quot; |
| TRUEMONEY | &quot;truemoney&quot; |
| UPI_COLLECT | &quot;upi_collect&quot; |
| UPI_INTENT | &quot;upi_intent&quot; |
| VIPPS | &quot;vipps&quot; |
| VISACHECKOUT | &quot;visacheckout&quot; |
| WECHATPAY | &quot;wechatpay&quot; |
| WECHATPAY_POS | &quot;wechatpay_pos&quot; |
| WECHATPAY_MINI_PROGRAM | &quot;wechatpayMiniProgram&quot; |
| ZIP | &quot;zip&quot; |
| ZIP_POS | &quot;zip_pos&quot; |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: SubtypeEnum

| Name | Value |
|---- | -----|
| REDIRECT | &quot;redirect&quot; |
| SDK | &quot;sdk&quot; |



