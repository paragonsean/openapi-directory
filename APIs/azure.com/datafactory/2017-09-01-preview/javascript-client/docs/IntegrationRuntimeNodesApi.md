# DataFactoryManagementClient.IntegrationRuntimeNodesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationRuntimeNodesDelete**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName} | 
[**integrationRuntimeNodesGetIpAddress**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesGetIpAddress) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}/ipAddress | 
[**integrationRuntimeNodesUpdate**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName} | 



## integrationRuntimeNodesDelete

> integrationRuntimeNodesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion)



Deletes a self-hosted integration runtime node.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimeNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let nodeName = "nodeName_example"; // String | The integration runtime node name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimeNodesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **nodeName** | **String**| The integration runtime node name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimeNodesGetIpAddress

> IntegrationRuntimeNodesGetIpAddress200Response integrationRuntimeNodesGetIpAddress(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion)



Get the IP address of self-hosted integration runtime node.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimeNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let nodeName = "nodeName_example"; // String | The integration runtime node name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimeNodesGetIpAddress(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion, (error, data, response) => {
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
 **nodeName** | **String**| The integration runtime node name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationRuntimeNodesGetIpAddress200Response**](IntegrationRuntimeNodesGetIpAddress200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimeNodesUpdate

> IntegrationRuntimeNodesUpdate200Response integrationRuntimeNodesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion, updateIntegrationRuntimeNodeRequest)



Updates a self-hosted integration runtime node.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimeNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let nodeName = "nodeName_example"; // String | The integration runtime node name.
let apiVersion = "apiVersion_example"; // String | The API version.
let updateIntegrationRuntimeNodeRequest = new DataFactoryManagementClient.UpdateIntegrationRuntimeNodeRequest(); // UpdateIntegrationRuntimeNodeRequest | The parameters for updating an integration runtime node.
apiInstance.integrationRuntimeNodesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion, updateIntegrationRuntimeNodeRequest, (error, data, response) => {
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
 **nodeName** | **String**| The integration runtime node name. | 
 **apiVersion** | **String**| The API version. | 
 **updateIntegrationRuntimeNodeRequest** | [**UpdateIntegrationRuntimeNodeRequest**](UpdateIntegrationRuntimeNodeRequest.md)| The parameters for updating an integration runtime node. | 

### Return type

[**IntegrationRuntimeNodesUpdate200Response**](IntegrationRuntimeNodesUpdate200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

