# ManagementApi.AccountStoreLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMerchantsMerchantIdStores**](AccountStoreLevelApi.md#getMerchantsMerchantIdStores) | **GET** /merchants/{merchantId}/stores | Get a list of stores
[**getMerchantsMerchantIdStoresStoreId**](AccountStoreLevelApi.md#getMerchantsMerchantIdStoresStoreId) | **GET** /merchants/{merchantId}/stores/{storeId} | Get a store
[**getStores**](AccountStoreLevelApi.md#getStores) | **GET** /stores | Get a list of stores
[**getStoresStoreId**](AccountStoreLevelApi.md#getStoresStoreId) | **GET** /stores/{storeId} | Get a store
[**patchMerchantsMerchantIdStoresStoreId**](AccountStoreLevelApi.md#patchMerchantsMerchantIdStoresStoreId) | **PATCH** /merchants/{merchantId}/stores/{storeId} | Update a store
[**patchStoresStoreId**](AccountStoreLevelApi.md#patchStoresStoreId) | **PATCH** /stores/{storeId} | Update a store
[**postMerchantsMerchantIdStores**](AccountStoreLevelApi.md#postMerchantsMerchantIdStores) | **POST** /merchants/{merchantId}/stores | Create a store
[**postStores**](AccountStoreLevelApi.md#postStores) | **POST** /stores | Create a store



## getMerchantsMerchantIdStores

> ListStoresResponse getMerchantsMerchantIdStores(merchantId, opts)

Get a list of stores

Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56, // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
  'reference': "reference_example" // String | The reference of the store.
};
apiInstance.getMerchantsMerchantIdStores(merchantId, opts, (error, data, response) => {
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
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 
 **reference** | **String**| The reference of the store. | [optional] 

### Return type

[**ListStoresResponse**](ListStoresResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdStoresStoreId

> Store getMerchantsMerchantIdStoresStoreId(merchantId, storeId)

Get a store

Returns the details of the store identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let storeId = "storeId_example"; // String | The unique identifier of the store.
apiInstance.getMerchantsMerchantIdStoresStoreId(merchantId, storeId, (error, data, response) => {
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
 **storeId** | **String**| The unique identifier of the store. | 

### Return type

[**Store**](Store.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStores

> ListStoresResponse getStores(opts)

Get a list of stores

Returns a list of stores. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56, // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
  'reference': "reference_example", // String | The reference of the store.
  'merchantId': "merchantId_example" // String | The unique identifier of the merchant account.
};
apiInstance.getStores(opts, (error, data, response) => {
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
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 
 **reference** | **String**| The reference of the store. | [optional] 
 **merchantId** | **String**| The unique identifier of the merchant account. | [optional] 

### Return type

[**ListStoresResponse**](ListStoresResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStoresStoreId

> Store getStoresStoreId(storeId)

Get a store

Returns the details of the store identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let storeId = "storeId_example"; // String | The unique identifier of the store.
apiInstance.getStoresStoreId(storeId, (error, data, response) => {
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
 **storeId** | **String**| The unique identifier of the store. | 

### Return type

[**Store**](Store.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdStoresStoreId

> Store patchMerchantsMerchantIdStoresStoreId(merchantId, storeId, opts)

Update a store

Updates the store identified in the path. You can only update some store parameters.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let storeId = "storeId_example"; // String | The unique identifier of the store.
let opts = {
  'updateStoreRequest': new ManagementApi.UpdateStoreRequest() // UpdateStoreRequest | 
};
apiInstance.patchMerchantsMerchantIdStoresStoreId(merchantId, storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| The unique identifier of the store. | 
 **updateStoreRequest** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchStoresStoreId

> Store patchStoresStoreId(storeId, opts)

Update a store

Updates the store identified in the path. You can only update some store parameters.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let storeId = "storeId_example"; // String | The unique identifier of the store.
let opts = {
  'updateStoreRequest': new ManagementApi.UpdateStoreRequest() // UpdateStoreRequest | 
};
apiInstance.patchStoresStoreId(storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| The unique identifier of the store. | 
 **updateStoreRequest** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdStores

> Store postMerchantsMerchantIdStores(merchantId, opts)

Create a store

Creates a store for the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'storeCreationRequest': new ManagementApi.StoreCreationRequest() // StoreCreationRequest | 
};
apiInstance.postMerchantsMerchantIdStores(merchantId, opts, (error, data, response) => {
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
 **storeCreationRequest** | [**StoreCreationRequest**](StoreCreationRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postStores

> Store postStores(opts)

Create a store

Creates a store for the merchant account specified in the request.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

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

let apiInstance = new ManagementApi.AccountStoreLevelApi();
let opts = {
  'storeCreationWithMerchantCodeRequest': new ManagementApi.StoreCreationWithMerchantCodeRequest() // StoreCreationWithMerchantCodeRequest | 
};
apiInstance.postStores(opts, (error, data, response) => {
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
 **storeCreationWithMerchantCodeRequest** | [**StoreCreationWithMerchantCodeRequest**](StoreCreationWithMerchantCodeRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

