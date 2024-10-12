# AdyenPaymentApi.PaymentResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | [**PaymentResultAdditionalData**](PaymentResultAdditionalData.md) |  | [optional] 
**authCode** | **String** | Authorisation code: * When the payment is authorised successfully, this field holds the authorisation code for the payment. * When the payment is not authorised, this field is empty. | [optional] 
**dccAmount** | [**Amount**](Amount.md) | Includes the currency of the conversion and the value of the transaction. &gt; This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). | [optional] 
**dccSignature** | **String** | Cryptographic signature used to verify &#x60;dccQuote&#x60;. &gt; This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). | [optional] 
**fraudResult** | [**FraudResult**](FraudResult.md) | The fraud result properties of the payment. | [optional] 
**issuerUrl** | **String** | The URL to direct the shopper to. &gt; In case of SecurePlus, do not redirect a shopper to this URL. | [optional] 
**md** | **String** | The payment session. | [optional] 
**paRequest** | **String** | The 3D request data for the issuer.  If the value is **CUPSecurePlus-CollectSMSVerificationCode**, collect an SMS code from the shopper and pass it in the &#x60;/authorise3D&#x60; request. For more information, see [3D Secure](https://docs.adyen.com/classic-integration/3d-secure). | [optional] 
**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. | [optional] 
**refusalReason** | **String** | If the payment&#39;s authorisation is refused or an error occurs during authorisation, this field holds Adyen&#39;s mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes &#x60;resultCode&#x60; and &#x60;refusalReason&#x60; values.  For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). | [optional] 
**resultCode** | **String** | The result of the payment. For more information, see [Result codes](https://docs.adyen.com/online-payments/payment-result-codes).  Possible values:  * **AuthenticationFinished** – The payment has been successfully authenticated with 3D Secure 2. Returned for 3D Secure 2 authentication-only transactions. * **AuthenticationNotRequired** – The transaction does not require 3D Secure authentication. Returned for [standalone authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). * **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state. * **Cancelled** – Indicates the payment has been cancelled (either by the shopper or the merchant) before processing was completed. This is a final state. * **ChallengeShopper** – The issuer requires further shopper interaction before the payment can be authenticated. Returned for 3D Secure 2 transactions. * **Error** – There was an error when the payment was being processed. The reason is given in the &#x60;refusalReason&#x60; field. This is a final state. * **IdentifyShopper** – The issuer requires the shopper&#39;s device fingerprint before the payment can be authenticated. Returned for 3D Secure 2 transactions. * **PartiallyAuthorised** – The payment has been authorised for a partial amount. This happens for card payments when the merchant supports Partial Authorisations and the cardholder has insufficient funds. * **Pending** – Indicates that it is not possible to obtain the final status of the payment. This can happen if the systems providing final status information for the payment are unavailable, or if the shopper needs to take further action to complete the payment. * **PresentToShopper** – Indicates that the response contains additional information that you need to present to a shopper, so that they can use it to complete a payment. * **Received** – Indicates the payment has successfully been received by Adyen, and will be processed. This is the initial state for all payments. * **RedirectShopper** – Indicates the shopper should be redirected to an external web page or app to complete the authorisation. * **Refused** – Indicates the payment was refused. The reason is given in the &#x60;refusalReason&#x60; field. This is a final state. | [optional] 



## Enum: ResultCodeEnum


* `AuthenticationFinished` (value: `"AuthenticationFinished"`)

* `AuthenticationNotRequired` (value: `"AuthenticationNotRequired"`)

* `Authorised` (value: `"Authorised"`)

* `Cancelled` (value: `"Cancelled"`)

* `ChallengeShopper` (value: `"ChallengeShopper"`)

* `Error` (value: `"Error"`)

* `IdentifyShopper` (value: `"IdentifyShopper"`)

* `PartiallyAuthorised` (value: `"PartiallyAuthorised"`)

* `Pending` (value: `"Pending"`)

* `PresentToShopper` (value: `"PresentToShopper"`)

* `Received` (value: `"Received"`)

* `RedirectShopper` (value: `"RedirectShopper"`)

* `Refused` (value: `"Refused"`)

* `Success` (value: `"Success"`)




