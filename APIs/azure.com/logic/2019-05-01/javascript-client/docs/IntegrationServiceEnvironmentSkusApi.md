# LogicManagementClient.IntegrationServiceEnvironmentSkusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationServiceEnvironmentSkusList**](IntegrationServiceEnvironmentSkusApi.md#integrationServiceEnvironmentSkusList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/skus | 



## integrationServiceEnvironmentSkusList

> IntegrationServiceEnvironmentSkuList integrationServiceEnvironmentSkusList(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion)



Gets a list of integration service environment Skus.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentSkusApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationServiceEnvironmentSkusList(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroup** | **String**| The resource group. | 
 **integrationServiceEnvironmentName** | **String**| The integration service environment name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationServiceEnvironmentSkuList**](IntegrationServiceEnvironmentSkuList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

