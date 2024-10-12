

# StandalonePaymentCancelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |  [optional] |
|**merchantAccount** | **String** | The merchant account that is used to process the payment. |  |
|**paymentReference** | **String** | The [&#x60;reference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment that you want to cancel. |  |
|**reference** | **String** | Your reference for the cancel request. Maximum length: 80 characters. |  [optional] |



