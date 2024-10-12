# ManagementApi.PaymentMethodsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMerchantsMerchantIdPaymentMethodSettings**](PaymentMethodsMerchantLevelApi.md#getMerchantsMerchantIdPaymentMethodSettings) | **GET** /merchants/{merchantId}/paymentMethodSettings | Get all payment methods
[**getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId**](PaymentMethodsMerchantLevelApi.md#getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Get payment method details
[**getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains**](PaymentMethodsMerchantLevelApi.md#getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | Get Apple Pay domains
[**patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId**](PaymentMethodsMerchantLevelApi.md#patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId) | **PATCH** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Update a payment method
[**postMerchantsMerchantIdPaymentMethodSettings**](PaymentMethodsMerchantLevelApi.md#postMerchantsMerchantIdPaymentMethodSettings) | **POST** /merchants/{merchantId}/paymentMethodSettings | Request a payment method
[**postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains**](PaymentMethodsMerchantLevelApi.md#postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains) | **POST** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | Add an Apple Pay domain



## getMerchantsMerchantIdPaymentMethodSettings

> PaymentMethodResponse getMerchantsMerchantIdPaymentMethodSettings(merchantId, opts)

Get all payment methods

Returns details for all payment methods of the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PaymentMethodsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'storeId': "storeId_example", // String | The unique identifier of the store for which to return the payment methods.
  'businessLineId': "businessLineId_example", // String | The unique identifier of the Business Line for which to return the payment methods.
  'pageSize': 56, // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
  'pageNumber': 56 // Number | The number of the page to fetch.
};
apiInstance.getMerchantsMerchantIdPaymentMethodSettings(merchantId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **storeId** | **String**| The unique identifier of the store for which to return the payment methods. | [optional] 
 **businessLineId** | **String**| The unique identifier of the Business Line for which to return the payment methods. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId

> PaymentMethod getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId)

Get payment method details

Returns details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PaymentMethodsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
apiInstance.getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **paymentMethodId** | **String**| The unique identifier of the payment method. | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains

> ApplePayInfo getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains(merchantId, paymentMethodId)

Get Apple Pay domains

Returns all Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PaymentMethodsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
apiInstance.getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains(merchantId, paymentMethodId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **paymentMethodId** | **String**| The unique identifier of the payment method. | 

### Return type

[**ApplePayInfo**](ApplePayInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId

> PaymentMethod patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId, opts)

Update a payment method

Updates payment method details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PaymentMethodsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
let opts = {
  'updatePaymentMethodInfo': new ManagementApi.UpdatePaymentMethodInfo() // UpdatePaymentMethodInfo | 
};
apiInstance.patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **paymentMethodId** | **String**| The unique identifier of the payment method. | 
 **updatePaymentMethodInfo** | [**UpdatePaymentMethodInfo**](UpdatePaymentMethodInfo.md)|  | [optional] 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdPaymentMethodSettings

> PaymentMethod postMerchantsMerchantIdPaymentMethodSettings(merchantId, opts)

Request a payment method

Sends a request to add a new payment method to the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PaymentMethodsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'paymentMethodSetupInfo': new ManagementApi.PaymentMethodSetupInfo() // PaymentMethodSetupInfo | 
};
apiInstance.postMerchantsMerchantIdPaymentMethodSettings(merchantId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **paymentMethodSetupInfo** | [**PaymentMethodSetupInfo**](PaymentMethodSetupInfo.md)|  | [optional] 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains

> postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains(merchantId, paymentMethodId, opts)

Add an Apple Pay domain

Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PaymentMethodsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
let opts = {
  'applePayInfo': new ManagementApi.ApplePayInfo() // ApplePayInfo | 
};
apiInstance.postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains(merchantId, paymentMethodId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **paymentMethodId** | **String**| The unique identifier of the payment method. | 
 **applePayInfo** | [**ApplePayInfo**](ApplePayInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

