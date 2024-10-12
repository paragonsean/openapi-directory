# AppStoreConnectApi.AppPreOrdersApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appPreOrdersCreateInstance**](AppPreOrdersApi.md#appPreOrdersCreateInstance) | **POST** /v1/appPreOrders | 
[**appPreOrdersDeleteInstance**](AppPreOrdersApi.md#appPreOrdersDeleteInstance) | **DELETE** /v1/appPreOrders/{id} | 
[**appPreOrdersGetInstance**](AppPreOrdersApi.md#appPreOrdersGetInstance) | **GET** /v1/appPreOrders/{id} | 
[**appPreOrdersUpdateInstance**](AppPreOrdersApi.md#appPreOrdersUpdateInstance) | **PATCH** /v1/appPreOrders/{id} | 



## appPreOrdersCreateInstance

> AppPreOrderResponse appPreOrdersCreateInstance(appPreOrderCreateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPreOrdersApi();
let appPreOrderCreateRequest = new AppStoreConnectApi.AppPreOrderCreateRequest(); // AppPreOrderCreateRequest | AppPreOrder representation
apiInstance.appPreOrdersCreateInstance(appPreOrderCreateRequest, (error, data, response) => {
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
 **appPreOrderCreateRequest** | [**AppPreOrderCreateRequest**](AppPreOrderCreateRequest.md)| AppPreOrder representation | 

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appPreOrdersDeleteInstance

> appPreOrdersDeleteInstance(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPreOrdersApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.appPreOrdersDeleteInstance(id, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPreOrdersGetInstance

> AppPreOrderResponse appPreOrdersGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPreOrdersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPreOrders': ["null"], // [String] | the fields to include for returned resources of type appPreOrders
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appPreOrdersGetInstance(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppPreOrders** | [**[String]**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPreOrdersUpdateInstance

> AppPreOrderResponse appPreOrdersUpdateInstance(id, appPreOrderUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPreOrdersApi();
let id = "id_example"; // String | the id of the requested resource
let appPreOrderUpdateRequest = new AppStoreConnectApi.AppPreOrderUpdateRequest(); // AppPreOrderUpdateRequest | AppPreOrder representation
apiInstance.appPreOrdersUpdateInstance(id, appPreOrderUpdateRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **appPreOrderUpdateRequest** | [**AppPreOrderUpdateRequest**](AppPreOrderUpdateRequest.md)| AppPreOrder representation | 

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

