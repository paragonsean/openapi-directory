

# DonationPaymentRequestPaymentMethod

The type and required details of a payment method to use.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applePayToken** | **String** | The stringified and base64 encoded &#x60;paymentData&#x60; you retrieved from the Apple framework. |  |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **applepay** |  [optional] |
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
|**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used only for recurring payments in India. |  [optional] |
|**threeDS2SdkVersion** | **String** | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK. |  [optional] |
|**googlePayCardNetwork** | **String** | The selected payment card network.  |  [optional] |
|**googlePayToken** | **String** | The &#x60;token&#x60; that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) &#x60;PaymentData&#x60; response. |  |
|**issuer** | **String** | The iDEAL issuer value of the shopper&#39;s selected bank. Set this to an **id** of an iDEAL issuer to preselect it. |  |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APPLEPAY | &quot;applepay&quot; |
| BCMC | &quot;bcmc&quot; |
| SCHEME | &quot;scheme&quot; |
| NETWORK_TOKEN | &quot;networkToken&quot; |
| GIFTCARD | &quot;giftcard&quot; |
| CARD | &quot;card&quot; |
| GOOGLEPAY | &quot;googlepay&quot; |
| IDEAL | &quot;ideal&quot; |
| PAYWITHGOOGLE | &quot;paywithgoogle&quot; |



