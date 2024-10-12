# AdyenCheckoutApi.PaymentCompletionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MD** | **String** | A payment session identifier returned by the card issuer. | [optional] 
**paReq** | **String** | (3D) Payment Authentication Request data for the card issuer. | [optional] 
**paRes** | **String** | (3D) Payment Authentication Response data by the card issuer. | [optional] 
**authorizationToken** | **String** |  | [optional] 
**billingToken** | **String** | PayPal-generated token for recurring payments. | [optional] 
**cupsecureplusSmscode** | **String** | The SMS verification code collected from the shopper. | [optional] 
**facilitatorAccessToken** | **String** | PayPal-generated third party access token. | [optional] 
**oneTimePasscode** | **String** | A random number sent to the mobile phone number of the shopper to verify the payment. | [optional] 
**orderID** | **String** | PayPal-assigned ID for the order. | [optional] 
**payerID** | **String** | PayPal-assigned ID for the payer (shopper). | [optional] 
**payload** | **String** | Payload appended to the &#x60;returnURL&#x60; as a result of the redirect. | [optional] 
**paymentID** | **String** | PayPal-generated ID for the payment. | [optional] 
**paymentStatus** | **String** | Value passed from the WeChat MiniProgram &#x60;wx.requestPayment&#x60; **complete** callback. Possible values: any value starting with &#x60;requestPayment:&#x60;. | [optional] 
**redirectResult** | **String** | The result of the redirect as appended to the &#x60;returnURL&#x60;. | [optional] 
**resultCode** | **String** | Value you received from the WeChat Pay SDK. | [optional] 
**threeDSResult** | **String** | Base64-encoded string returned by the Component after the challenge flow. It contains the following parameters: &#x60;transStatus&#x60;, &#x60;authorisationToken&#x60;. | [optional] 
**threeds2ChallengeResult** | **String** | Base64-encoded string returned by the Component after the challenge flow. It contains the following parameter: &#x60;transStatus&#x60;. | [optional] 
**threeds2Fingerprint** | **String** | Base64-encoded string returned by the Component after the challenge flow. It contains the following parameter: &#x60;threeDSCompInd&#x60;. | [optional] 


