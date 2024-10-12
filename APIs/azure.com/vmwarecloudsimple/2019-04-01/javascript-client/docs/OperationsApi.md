# VMwareCloudSimple.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsGet**](OperationsApi.md#operationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/operationResults/{operationId} | Implements get of async operation
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.VMwareCloudSimple/operations | Implements list of available operations



## operationsGet

> OperationResource operationsGet(subscriptionId, apiVersion, regionId, referer, operationId)

Implements get of async operation

Return an async operation

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.OperationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let referer = "referer_example"; // String | referer url
let operationId = "operationId_example"; // String | operation id
apiInstance.operationsGet(subscriptionId, apiVersion, regionId, referer, operationId, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **apiVersion** | **String**| Client API version. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **referer** | **String**| referer url | 
 **operationId** | **String**| operation id | 

### Return type

[**OperationResource**](OperationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsList

> AvailableOperationsListResponse operationsList(apiVersion)

Implements list of available operations

Return list of operations

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.OperationsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 

### Return type

[**AvailableOperationsListResponse**](AvailableOperationsListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

