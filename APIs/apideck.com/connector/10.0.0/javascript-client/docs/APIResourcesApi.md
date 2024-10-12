# ConnectorApi.APIResourcesApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiResourceCoverageOne**](APIResourcesApi.md#apiResourceCoverageOne) | **GET** /connector/apis/{id}/resources/{resource_id}/coverage | Get API Resource Coverage
[**apiResourcesOne**](APIResourcesApi.md#apiResourcesOne) | **GET** /connector/apis/{id}/resources/{resource_id} | Get API Resource



## apiResourceCoverageOne

> GetApiResourceCoverageResponse apiResourceCoverageOne(xApideckAppId, id, resourceId)

Get API Resource Coverage

Get API Resource Coverage

### Example

```javascript
import ConnectorApi from 'connector_api';
let defaultClient = ConnectorApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ConnectorApi.APIResourcesApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let id = "id_example"; // String | ID of the record you are acting upon.
let resourceId = "resourceId_example"; // String | ID of the resource you are acting upon.
apiInstance.apiResourceCoverageOne(xApideckAppId, id, resourceId, (error, data, response) => {
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
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **id** | **String**| ID of the record you are acting upon. | 
 **resourceId** | **String**| ID of the resource you are acting upon. | 

### Return type

[**GetApiResourceCoverageResponse**](GetApiResourceCoverageResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiResourcesOne

> GetApiResourceResponse apiResourcesOne(xApideckAppId, id, resourceId)

Get API Resource

Get API Resource

### Example

```javascript
import ConnectorApi from 'connector_api';
let defaultClient = ConnectorApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ConnectorApi.APIResourcesApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let id = "id_example"; // String | ID of the record you are acting upon.
let resourceId = "resourceId_example"; // String | ID of the resource you are acting upon.
apiInstance.apiResourcesOne(xApideckAppId, id, resourceId, (error, data, response) => {
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
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **id** | **String**| ID of the record you are acting upon. | 
 **resourceId** | **String**| ID of the resource you are acting upon. | 

### Return type

[**GetApiResourceResponse**](GetApiResourceResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

