# MotaWordApi.ProjectPayment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **String** | Last 4 digits of the credit card you are using one-time. This parameter is only required when stripe_token is provided. | [optional] 
**budgetCode** | **String** | Optional with corporate accounts. Not available for others. | [optional] 
**cardId** | **Number** | Optional. &#x60;client&#x60;, &#x60;app&#x60;, &#x60;corporate_card&#x60; methods require a credit card ID. &#x60;credit&#x60; method requires Stripe token and bin. | [optional] 
**paymentCode** | **String** | Optional. &#x60;corporate&#x60; payment method requires this.s | [optional] 
**paymentMethod** | **String** | Optional. Determines which method to use for payment. &#x60;client&#x60;, &#x60;app&#x60;, &#x60;corporate_card&#x60; methods require a credit card ID. &#x60;credit&#x60; method requires Stripe token and bin. &#x60;corporate&#x60; method follows corporate account policy automatically, either follows invoicing flow or automatically charges corporate&#39;s primary card. | [optional] 
**stripeToken** | **String** | This is required if you are using a one-time credit card. This is the token generted from frontend via Stripe SDK. If you are using a one-time card with &#x60;stripe_token&#x60;, you must also provide &#x60;bin&#x60;, last 4 digits of the card. | [optional] 



## Enum: PaymentMethodEnum


* `corporate` (value: `"corporate"`)

* `client` (value: `"client"`)

* `app` (value: `"app"`)

* `credit` (value: `"credit"`)

* `corporate_card` (value: `"corporate_card"`)




