# LogisticsApi.ShippingPoliciesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiLogisticsPvtShippingPoliciesGet**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesGet) | **GET** /api/logistics/pvt/shipping-policies | List shipping policies
[**apiLogisticsPvtShippingPoliciesIdDelete**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesIdDelete) | **DELETE** /api/logistics/pvt/shipping-policies/{id} | Delete shipping policies by ID
[**apiLogisticsPvtShippingPoliciesIdGet**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesIdGet) | **GET** /api/logistics/pvt/shipping-policies/{id} | Retrieve shipping policy by ID
[**apiLogisticsPvtShippingPoliciesIdPut**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesIdPut) | **PUT** /api/logistics/pvt/shipping-policies/{id} | Update shipping policy
[**apiLogisticsPvtShippingPoliciesPost**](ShippingPoliciesApi.md#apiLogisticsPvtShippingPoliciesPost) | **POST** /api/logistics/pvt/shipping-policies | Create shipping policy



## apiLogisticsPvtShippingPoliciesGet

> apiLogisticsPvtShippingPoliciesGet(accept, contentType, page, perPage)

List shipping policies

This endpoint lists existing shipping policies from carriers in your store.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.ShippingPoliciesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Type of the content being sent
let page = "page"; // String | Desired number of pages to retrieve information from your Shipping Policies.
let perPage = "perPage"; // String | Desired number of items per page, to retrieve information from your Shipping Policies.
apiInstance.apiLogisticsPvtShippingPoliciesGet(accept, contentType, page, perPage, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **page** | **String**| Desired number of pages to retrieve information from your Shipping Policies. | 
 **perPage** | **String**| Desired number of items per page, to retrieve information from your Shipping Policies. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiLogisticsPvtShippingPoliciesIdDelete

> apiLogisticsPvtShippingPoliciesIdDelete(accept, contentType, id)

Delete shipping policies by ID

This endpoint deletes existing shipping policies from carriers in your store, searching by their IDs.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.ShippingPoliciesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Type of the content being sent
let id = "id"; // String | ID of the shipping policy.
apiInstance.apiLogisticsPvtShippingPoliciesIdDelete(accept, contentType, id, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **id** | **String**| ID of the shipping policy. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiLogisticsPvtShippingPoliciesIdGet

> apiLogisticsPvtShippingPoliciesIdGet(accept, contentType, id)

Retrieve shipping policy by ID

This endpoint lists existing [shipping policies](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) from carriers in your store, searching by their IDs.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.ShippingPoliciesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Type of the content being sent
let id = "id"; // String | ID of the shipping policy.
apiInstance.apiLogisticsPvtShippingPoliciesIdGet(accept, contentType, id, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **id** | **String**| ID of the shipping policy. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiLogisticsPvtShippingPoliciesIdPut

> apiLogisticsPvtShippingPoliciesIdPut(accept, contentType, id, opts)

Update shipping policy

This endpoint updates information on existing Shipping Policies from carriers.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.ShippingPoliciesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Type of the content being sent
let id = "shippingpolicyid1"; // String | Shipping policy's ID
let opts = {
  'requestBody1': new LogisticsApi.RequestBody1() // RequestBody1 | 
};
apiInstance.apiLogisticsPvtShippingPoliciesIdPut(accept, contentType, id, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **id** | **String**| Shipping policy&#39;s ID | 
 **requestBody1** | [**RequestBody1**](RequestBody1.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiLogisticsPvtShippingPoliciesPost

> apiLogisticsPvtShippingPoliciesPost(accept, contentType, opts)

Create shipping policy

This endpoint creates new shipping policies from carriers in your store.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.ShippingPoliciesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Type of the content being sent
let opts = {
  'requestBody': new LogisticsApi.RequestBody() // RequestBody | 
};
apiInstance.apiLogisticsPvtShippingPoliciesPost(accept, contentType, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

