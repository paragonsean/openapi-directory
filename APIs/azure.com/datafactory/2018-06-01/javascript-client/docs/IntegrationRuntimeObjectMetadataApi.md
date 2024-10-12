# DataFactoryManagementClient.IntegrationRuntimeObjectMetadataApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationRuntimeObjectMetadataGet**](IntegrationRuntimeObjectMetadataApi.md#integrationRuntimeObjectMetadataGet) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getObjectMetadata | 
[**integrationRuntimeObjectMetadataRefresh**](IntegrationRuntimeObjectMetadataApi.md#integrationRuntimeObjectMetadataRefresh) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/refreshObjectMetadata | 



## integrationRuntimeObjectMetadataGet

> IntegrationRuntimeObjectMetadataGet200Response integrationRuntimeObjectMetadataGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, opts)



Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimeObjectMetadataApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'getMetadataRequest': new DataFactoryManagementClient.GetSsisObjectMetadataRequest() // GetSsisObjectMetadataRequest | The parameters for getting a SSIS object metadata.
};
apiInstance.integrationRuntimeObjectMetadataGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **getMetadataRequest** | [**GetSsisObjectMetadataRequest**](GetSsisObjectMetadataRequest.md)| The parameters for getting a SSIS object metadata. | [optional] 

### Return type

[**IntegrationRuntimeObjectMetadataGet200Response**](IntegrationRuntimeObjectMetadataGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationRuntimeObjectMetadataRefresh

> SsisObjectMetadataStatusResponse integrationRuntimeObjectMetadataRefresh(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Refresh a SSIS integration runtime object metadata.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimeObjectMetadataApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimeObjectMetadataRefresh(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**SsisObjectMetadataStatusResponse**](SsisObjectMetadataStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

