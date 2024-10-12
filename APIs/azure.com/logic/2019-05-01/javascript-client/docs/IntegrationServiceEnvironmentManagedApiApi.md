# LogicManagementClient.IntegrationServiceEnvironmentManagedApiApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationServiceEnvironmentManagedApisDelete**](IntegrationServiceEnvironmentManagedApiApi.md#integrationServiceEnvironmentManagedApisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/managedApis/{apiName} | 
[**integrationServiceEnvironmentManagedApisGet**](IntegrationServiceEnvironmentManagedApiApi.md#integrationServiceEnvironmentManagedApisGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/managedApis/{apiName} | 
[**integrationServiceEnvironmentManagedApisPut**](IntegrationServiceEnvironmentManagedApiApi.md#integrationServiceEnvironmentManagedApisPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/managedApis/{apiName} | 



## integrationServiceEnvironmentManagedApisDelete

> integrationServiceEnvironmentManagedApisDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion)



Deletes the integration service environment managed Api.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentManagedApiApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiName = "apiName_example"; // String | The api name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationServiceEnvironmentManagedApisDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroup** | **String**| The resource group. | 
 **integrationServiceEnvironmentName** | **String**| The integration service environment name. | 
 **apiName** | **String**| The api name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationServiceEnvironmentManagedApisGet

> ManagedApi integrationServiceEnvironmentManagedApisGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion)



Gets the integration service environment managed Api.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentManagedApiApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group name.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiName = "apiName_example"; // String | The api name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationServiceEnvironmentManagedApisGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion, (error, data, response) => {
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
 **resourceGroup** | **String**| The resource group name. | 
 **integrationServiceEnvironmentName** | **String**| The integration service environment name. | 
 **apiName** | **String**| The api name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**ManagedApi**](ManagedApi.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationServiceEnvironmentManagedApisPut

> ManagedApi integrationServiceEnvironmentManagedApisPut(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion)



Puts the integration service environment managed Api.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentManagedApiApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group name.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiName = "apiName_example"; // String | The api name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationServiceEnvironmentManagedApisPut(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion, (error, data, response) => {
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
 **resourceGroup** | **String**| The resource group name. | 
 **integrationServiceEnvironmentName** | **String**| The integration service environment name. | 
 **apiName** | **String**| The api name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**ManagedApi**](ManagedApi.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

