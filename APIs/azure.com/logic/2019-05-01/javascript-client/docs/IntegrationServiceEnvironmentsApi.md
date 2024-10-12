# LogicManagementClient.IntegrationServiceEnvironmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationServiceEnvironmentsCreateOrUpdate**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} | 
[**integrationServiceEnvironmentsDelete**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} | 
[**integrationServiceEnvironmentsGet**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} | 
[**integrationServiceEnvironmentsListByResourceGroup**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments | 
[**integrationServiceEnvironmentsListBySubscription**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Logic/integrationServiceEnvironments | 
[**integrationServiceEnvironmentsUpdate**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} | 



## integrationServiceEnvironmentsCreateOrUpdate

> IntegrationServiceEnvironment integrationServiceEnvironmentsCreateOrUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment)



Creates or updates an integration service environment.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiVersion = "apiVersion_example"; // String | The API version.
let integrationServiceEnvironment = new LogicManagementClient.IntegrationServiceEnvironment(); // IntegrationServiceEnvironment | The integration service environment.
apiInstance.integrationServiceEnvironmentsCreateOrUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment, (error, data, response) => {
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
 **integrationServiceEnvironment** | [**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)| The integration service environment. | 

### Return type

[**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationServiceEnvironmentsDelete

> integrationServiceEnvironmentsDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion)



Deletes an integration service environment.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationServiceEnvironmentsDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationServiceEnvironmentsGet

> IntegrationServiceEnvironment integrationServiceEnvironmentsGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion)



Gets an integration service environment.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationServiceEnvironmentsGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, (error, data, response) => {
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

[**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationServiceEnvironmentsListByResourceGroup

> IntegrationServiceEnvironmentListResult integrationServiceEnvironmentsListByResourceGroup(subscriptionId, resourceGroup, apiVersion, opts)



Gets a list of integration service environments by resource group.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.integrationServiceEnvironmentsListByResourceGroup(subscriptionId, resourceGroup, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**IntegrationServiceEnvironmentListResult**](IntegrationServiceEnvironmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationServiceEnvironmentsListBySubscription

> IntegrationServiceEnvironmentListResult integrationServiceEnvironmentsListBySubscription(subscriptionId, apiVersion, opts)



Gets a list of integration service environments by subscription.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.integrationServiceEnvironmentsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**IntegrationServiceEnvironmentListResult**](IntegrationServiceEnvironmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationServiceEnvironmentsUpdate

> IntegrationServiceEnvironment integrationServiceEnvironmentsUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment)



Updates an integration service environment.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroup = "resourceGroup_example"; // String | The resource group.
let integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
let apiVersion = "apiVersion_example"; // String | The API version.
let integrationServiceEnvironment = new LogicManagementClient.IntegrationServiceEnvironment(); // IntegrationServiceEnvironment | The integration service environment.
apiInstance.integrationServiceEnvironmentsUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment, (error, data, response) => {
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
 **integrationServiceEnvironment** | [**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)| The integration service environment. | 

### Return type

[**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

