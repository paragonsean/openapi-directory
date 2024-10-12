# AdyenPaymentApi.AdditionalDataRiskStandalone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payPalCountryCode** | **String** | Shopper&#39;s country of residence in the form of ISO standard 3166 2-character country codes. | [optional] 
**payPalEmailId** | **String** | Shopper&#39;s email. | [optional] 
**payPalFirstName** | **String** | Shopper&#39;s first name. | [optional] 
**payPalLastName** | **String** | Shopper&#39;s last name. | [optional] 
**payPalPayerId** | **String** | Unique PayPal Customer Account identification number. Character length and limitations: 13 single-byte alphanumeric characters. | [optional] 
**payPalPhone** | **String** | Shopper&#39;s phone number. | [optional] 
**payPalProtectionEligibility** | **String** | Allowed values: * **Eligible** — Merchant is protected by PayPal&#39;s Seller Protection Policy for Unauthorized Payments and Item Not Received.  * **PartiallyEligible** — Merchant is protected by PayPal&#39;s Seller Protection Policy for Item Not Received.  * **Ineligible** — Merchant is not protected under the Seller Protection Policy. | [optional] 
**payPalTransactionId** | **String** | Unique transaction ID of the payment. | [optional] 
**avsResultRaw** | **String** | Raw AVS result received from the acquirer, where available. Example: D | [optional] 
**bin** | **String** | The Bank Identification Number of a credit card, which is the first six digits of a card number. Required for [tokenized card request](https://docs.adyen.com/risk-management/standalone-risk#tokenised-pan-request). | [optional] 
**cvcResultRaw** | **String** | Raw CVC result received from the acquirer, where available. Example: 1 | [optional] 
**riskToken** | **String** | Unique identifier or token for the shopper&#39;s card details. | [optional] 
**threeDAuthenticated** | **String** | A Boolean value indicating whether 3DS authentication was completed on this payment. Example: true | [optional] 
**threeDOffered** | **String** | A Boolean value indicating whether 3DS was offered for this payment. Example: true | [optional] 
**tokenDataType** | **String** | Required for PayPal payments only. The only supported value is: **paypal**. | [optional] 


