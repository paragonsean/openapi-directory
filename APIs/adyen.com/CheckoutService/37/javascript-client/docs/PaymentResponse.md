# AdyenCheckoutApi.PaymentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | [**BalanceCheckResponseAdditionalData**](BalanceCheckResponseAdditionalData.md) |  | [optional] 
**details** | [**[InputDetail]**](InputDetail.md) | When non-empty, contains all the fields that you must submit to the &#x60;/payments/details&#x60; endpoint. | [optional] 
**fraudResult** | [**FraudResult**](FraudResult.md) | The fraud result properties of the payment. | [optional] 
**order** | [**CheckoutOrderResponse**](CheckoutOrderResponse.md) | Contains updated information regarding the order in case order information was provided in the request. | [optional] 
**outputDetails** | **{String: String}** | Contains the details that will be presented to the shopper. | [optional] 
**paymentData** | **String** | When non-empty, contains a value that you must submit to the &#x60;/payments/details&#x60; endpoint. | [optional] 
**pspReference** | **String** | Adyen&#39;s 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.  &gt; For payment methods that require a redirect or additional action, you will get this value in the &#x60;/payments/details&#x60; response. | [optional] 
**redirect** | [**Redirect**](Redirect.md) | When the payment flow requires a redirect, this object contains information about the redirect URL. | [optional] 
**refusalReason** | **String** | If the payment&#39;s authorisation is refused or an error occurs during authorisation, this field holds Adyen&#39;s mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes &#x60;resultCode&#x60; and &#x60;refusalReason&#x60; values.  For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). | [optional] 
**refusalReasonCode** | **String** | Code that specifies the refusal reason. For more information, see [Authorisation refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). | [optional] 
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




