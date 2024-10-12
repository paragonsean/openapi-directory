

# UpdateorderFormconfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowManualPrice** | **Boolean** | Allows the editing of SKU prices right in the cart. |  |
|**allowMultipleDeliveries** | **Boolean** | On the same purchase, allows the selection of items from multiple delivery channels. |  |
|**apps** | [**List&lt;UpdateorderFormconfigurationRequestAppsInner&gt;**](UpdateorderFormconfigurationRequestAppsInner.md) | Array of objects containing Apps configuration information. |  |
|**decimalDigitsPrecision** | **Integer** | Number of price digits. |  |
|**maskFirstPurchaseData** | **Boolean** | Allows, on a first purchase, masking client&#39;s data. It could be useful when a shared cart is used and the client doesn&#39;t want to share its data. |  [optional] |
|**maxNumberOfWhiteLabelSellers** | **Integer** | Allows the input of a limit of white label sellers involved on the cart. |  [optional] |
|**minimumQuantityAccumulatedForItems** | **Integer** | Minimum SKU quantity by cart. |  |
|**minimumValueAccumulated** | **Integer** | Minimum cart value. |  |
|**paymentConfiguration** | [**PaymentConfiguration**](PaymentConfiguration.md) |  |  |
|**paymentSystemToCheckFirstInstallment** | **String** | If you want to apply a first installment discount to a particular payment system, set this field to that payment system&#39;s ID. Learn more: [Configuring a discount for orders prepaid in full](https://help.vtex.com/en/tutorial/configurar-desconto-de-preco-a-vista--7Lfcj9Wb5dpYfA2gKkACIt). |  [optional] |
|**recaptchaValidation** | **String** | Configures reCAPTCHA validation for the account, defining in which situations the shopper will be prompted to validate a purchase with reCAPTCHA. Learn more about [reCAPTCHA validation for VTEX stores](https://help.vtex.com/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP)    Possible values are:  - &#x60;\&quot;never\&quot;&#x60;: no purchases are validated with reCAPTCHA.  - &#x60;\&quot;always\&quot;&#x60;: every purchase is validated with reCAPTCHA.  - &#x60;\&quot;vtexCriteria\&quot;&#x60;: only some purchases are validated with reCAPTCHA in order to minimize friction and improve shopping experience. VTEX’s algorithm determines which sessions are trustworthy and which should be validated with reCAPTCHA. This is the recommended option. |  [optional] |
|**taxConfiguration** | [**UpdateorderFormconfigurationRequestTaxConfiguration**](UpdateorderFormconfigurationRequestTaxConfiguration.md) |  |  |



