# AdyenCheckoutApi.PaymentResponseAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paymentData** | **String** | Encoded payment data. | [optional] 
**paymentMethodType** | **String** | Specifies the payment method. | [optional] 
**type** | **String** | **await** | 
**url** | **String** | Specifies the URL to redirect to. | [optional] 
**data** | **{String: String}** | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. | [optional] 
**method** | **String** | Specifies the HTTP method, for example GET or POST. | [optional] 
**nativeRedirectData** | **String** | Native SDK&#39;s redirect data containing the direct issuer link and state data that must be submitted to the /v1/nativeRedirect/redirectResult. | [optional] 
**expiresAt** | **String** | The date time of the voucher expiry. | [optional] 
**qrCodeData** | **String** | The contents of the QR code as a UTF8 string. | [optional] 
**sdkData** | **{String: String}** | The data to pass to the SDK. | [optional] 
**authorisationToken** | **String** | A token needed to authorise a payment. | [optional] 
**subtype** | **String** | A subtype of the token. | [optional] 
**token** | **String** | A token to pass to the 3DS2 Component to get the fingerprint. | [optional] 
**alternativeReference** | **String** | The voucher alternative reference code. | [optional] 
**collectionInstitutionNumber** | **String** | A collection institution number (store number) for Econtext Pay-Easy ATM. | [optional] 
**downloadUrl** | **String** | The URL to download the voucher. | [optional] 
**entity** | **String** | An entity number of Multibanco. | [optional] 
**initialAmount** | [**Amount**](Amount.md) | The initial amount. | [optional] 
**instructionsUrl** | **String** | The URL to the detailed instructions to make payment using the voucher. | [optional] 
**issuer** | **String** | The issuer of the voucher. | [optional] 
**maskedTelephoneNumber** | **String** | The shopper telephone number (partially masked). | [optional] 
**merchantName** | **String** | The merchant name. | [optional] 
**merchantReference** | **String** | The merchant reference. | [optional] 
**reference** | **String** | The voucher reference code. | [optional] 
**shopperEmail** | **String** | The shopper email. | [optional] 
**shopperName** | **String** | The shopper name. | [optional] 
**surcharge** | [**Amount**](Amount.md) | The surcharge amount. | [optional] 
**totalAmount** | [**Amount**](Amount.md) | The total amount (initial plus surcharge amount). | [optional] 



## Enum: TypeEnum


* `await` (value: `"await"`)

* `nativeRedirect` (value: `"nativeRedirect"`)

* `qrCode` (value: `"qrCode"`)

* `redirect` (value: `"redirect"`)

* `sdk` (value: `"sdk"`)

* `wechatpaySDK` (value: `"wechatpaySDK"`)

* `threeDS2` (value: `"threeDS2"`)

* `voucher` (value: `"voucher"`)




