# AdyenTerminalApi.PaymentResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountsResp** | [**AmountsResp**](AmountsResp.md) |  | [optional] 
**authenticationMethod** | **[String]** |  | [optional] 
**capturedSignature** | [**CapturedSignature**](CapturedSignature.md) |  | [optional] 
**currencyConversion** | [**[CurrencyConversion]**](CurrencyConversion.md) |  | [optional] 
**customerLanguage** | **String** |  | [optional] 
**instalment** | [**Instalment**](Instalment.md) |  | [optional] 
**merchantOverrideFlag** | **Boolean** |  | [optional] [default to false]
**onlineFlag** | **Boolean** |  | [optional] [default to true]
**paymentAcquirerData** | [**PaymentAcquirerData**](PaymentAcquirerData.md) |  | [optional] 
**paymentInstrumentData** | [**PaymentInstrumentData**](PaymentInstrumentData.md) |  | [optional] 
**paymentType** | [**PaymentType**](PaymentType.md) |  | [optional] 
**protectedSignature** | **String** |  | [optional] 
**validityDate** | **Date** |  | [optional] 



## Enum: [AuthenticationMethodEnum]


* `Bypass` (value: `"Bypass"`)

* `ManualVerification` (value: `"ManualVerification"`)

* `MerchantAuthentication` (value: `"MerchantAuthentication"`)

* `OfflinePIN` (value: `"OfflinePIN"`)

* `OnlinePIN` (value: `"OnlinePIN"`)

* `PaperSignature` (value: `"PaperSignature"`)

* `SecureCertificate` (value: `"SecureCertificate"`)

* `SecureNoCertificate` (value: `"SecureNoCertificate"`)

* `SecuredChannel` (value: `"SecuredChannel"`)

* `SignatureCapture` (value: `"SignatureCapture"`)

* `UnknownMethod` (value: `"UnknownMethod"`)




