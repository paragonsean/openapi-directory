

# PaymentResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountsResp** | [**AmountsResp**](AmountsResp.md) |  |  [optional] |
|**authenticationMethod** | [**List&lt;AuthenticationMethodEnum&gt;**](#List&lt;AuthenticationMethodEnum&gt;) |  |  [optional] |
|**capturedSignature** | [**CapturedSignature**](CapturedSignature.md) |  |  [optional] |
|**currencyConversion** | [**List&lt;CurrencyConversion&gt;**](CurrencyConversion.md) |  |  [optional] |
|**customerLanguage** | **String** |  |  [optional] |
|**instalment** | [**Instalment**](Instalment.md) |  |  [optional] |
|**merchantOverrideFlag** | **Boolean** |  |  [optional] |
|**onlineFlag** | **Boolean** |  |  [optional] |
|**paymentAcquirerData** | [**PaymentAcquirerData**](PaymentAcquirerData.md) |  |  [optional] |
|**paymentInstrumentData** | [**PaymentInstrumentData**](PaymentInstrumentData.md) |  |  [optional] |
|**paymentType** | **PaymentType** |  |  [optional] |
|**protectedSignature** | **String** |  |  [optional] |
|**validityDate** | **LocalDate** |  |  [optional] |



## Enum: List&lt;AuthenticationMethodEnum&gt;

| Name | Value |
|---- | -----|
| BYPASS | &quot;Bypass&quot; |
| MANUAL_VERIFICATION | &quot;ManualVerification&quot; |
| MERCHANT_AUTHENTICATION | &quot;MerchantAuthentication&quot; |
| OFFLINE_PIN | &quot;OfflinePIN&quot; |
| ONLINE_PIN | &quot;OnlinePIN&quot; |
| PAPER_SIGNATURE | &quot;PaperSignature&quot; |
| SECURE_CERTIFICATE | &quot;SecureCertificate&quot; |
| SECURE_NO_CERTIFICATE | &quot;SecureNoCertificate&quot; |
| SECURED_CHANNEL | &quot;SecuredChannel&quot; |
| SIGNATURE_CAPTURE | &quot;SignatureCapture&quot; |
| UNKNOWN_METHOD | &quot;UnknownMethod&quot; |



