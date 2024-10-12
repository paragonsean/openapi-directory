

# PaymentService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payNowText** | **String** | The text displayed on the Pay Now button in Xero Online Invoicing. If this is not set it will default to Pay by credit card |  [optional] |
|**paymentServiceID** | **UUID** | Xero identifier |  [optional] |
|**paymentServiceName** | **String** | Name of payment service |  [optional] |
|**paymentServiceType** | **String** | This will always be CUSTOM for payment services created via the API. |  [optional] |
|**paymentServiceUrl** | **String** | The custom payment URL |  [optional] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



