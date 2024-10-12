

# CardDonations


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Secondary brand of the card. For example: **plastix**, **hmclub**. |  [optional] |
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**cupsecureplusSmscode** | **String** |  |  [optional] |
|**cvc** | **String** | The card verification code. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**encryptedCardNumber** | **String** | The encrypted card number. |  [optional] |
|**encryptedExpiryMonth** | **String** | The encrypted card expiry month. |  [optional] |
|**encryptedExpiryYear** | **String** | The encrypted card expiry year. |  [optional] |
|**encryptedSecurityCode** | **String** | The encrypted card verification code. |  [optional] |
|**expiryMonth** | **String** | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**expiryYear** | **String** | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |  [optional] |
|**holderName** | **String** | The name of the card holder. |  [optional] |
|**networkPaymentReference** | **String** | The network token reference. This is the [&#x60;networkTxReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-networkTxReference) from the response to the first payment. |  [optional] |
|**number** | **String** | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used only for recurring payments in India. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**threeDS2SdkVersion** | **String** | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Default payment method details. Common for scheme payment methods, and for simple payment method details. |  [optional] |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BCMC | &quot;bcmc&quot; |
| SCHEME | &quot;scheme&quot; |
| NETWORK_TOKEN | &quot;networkToken&quot; |
| GIFTCARD | &quot;giftcard&quot; |
| CARD | &quot;card&quot; |



