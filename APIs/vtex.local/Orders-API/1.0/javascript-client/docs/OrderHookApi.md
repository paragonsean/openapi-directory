# OrdersApi.OrderHookApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteHookConfiguration**](OrderHookApi.md#deleteHookConfiguration) | **DELETE** /api/orders/hook/config | Delete hook configuration
[**getHookConfiguration**](OrderHookApi.md#getHookConfiguration) | **GET** /api/orders/hook/config | Get hook configuration
[**hookConfiguration**](OrderHookApi.md#hookConfiguration) | **POST** /api/orders/hook/config | Create or update hook configuration



## deleteHookConfiguration

> deleteHookConfiguration(accept, contentType)

Delete hook configuration

Deletes a given hook configuration.    Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrderHookApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
apiInstance.deleteHookConfiguration(accept, contentType, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getHookConfiguration

> getHookConfiguration(contentType, accept, opts)

Get hook configuration

Retrieves a given hook&#39;s configuration details. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).     &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrderHookApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'clientEmail': "customer@mail.com", // String | Customer email.
  'page': "10", // String | Page number for result pagination.
  'perPage': "15" // String | Page quantity for result pagination.
};
apiInstance.getHookConfiguration(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **clientEmail** | **String**| Customer email. | [optional] 
 **page** | **String**| Page number for result pagination. | [optional] 
 **perPage** | **String**| Page quantity for result pagination. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## hookConfiguration

> HookConfiguration hookConfiguration(contentType, accept, hookConfigurationRequest)

Create or update hook configuration

Configures filtering rules applied to orders hook. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).    There are two types of filtering that can be used:      - &#x60;FromWorkflow&#x60;: filters orders by status.     - &#x60;FromOrders&#x60;: uses JSONata expressions to filter orders according to any property in the orders JSON document.     This enables stores to filter delivered orders and orders in which products have been added or removed, for example.    To learn more, access the [JSONata documentation](https://docs.jsonata.org/overview.html) and test filtering JSONata expressions with our [expressions API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/expressions/jsonata).

### Example

```javascript
import OrdersApi from 'orders_api';
let defaultClient = OrdersApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new OrdersApi.OrderHookApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let hookConfigurationRequest = {"filter":{"disableSingleFire":false,"expression":"value > 100","type":"FromOrders"},"hook":{"headers":{"key":"value"},"url":"https://endpoint.example/path"}}; // HookConfigurationRequest | 
apiInstance.hookConfiguration(contentType, accept, hookConfigurationRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **hookConfigurationRequest** | [**HookConfigurationRequest**](HookConfigurationRequest.md)|  | 

### Return type

[**HookConfiguration**](HookConfiguration.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

