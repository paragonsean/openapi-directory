# ApiManagementClient.TenantConfigurationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantConfigurationDeploy**](TenantConfigurationApi.md#tenantConfigurationDeploy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/deploy | 
[**tenantConfigurationSave**](TenantConfigurationApi.md#tenantConfigurationSave) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/save | 
[**tenantConfigurationValidate**](TenantConfigurationApi.md#tenantConfigurationValidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/validate | 



## tenantConfigurationDeploy

> TenantConfigurationDeploy200Response tenantConfigurationDeploy(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters)



This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.TenantConfigurationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
let parameters = new ApiManagementClient.TenantConfigurationDeployRequest(); // TenantConfigurationDeployRequest | Deploy Configuration parameters.
apiInstance.tenantConfigurationDeploy(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 
 **parameters** | [**TenantConfigurationDeployRequest**](TenantConfigurationDeployRequest.md)| Deploy Configuration parameters. | 

### Return type

[**TenantConfigurationDeploy200Response**](TenantConfigurationDeploy200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenantConfigurationSave

> TenantConfigurationDeploy200Response tenantConfigurationSave(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters)



This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.TenantConfigurationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
let parameters = new ApiManagementClient.TenantConfigurationSaveRequest(); // TenantConfigurationSaveRequest | Save Configuration parameters.
apiInstance.tenantConfigurationSave(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 
 **parameters** | [**TenantConfigurationSaveRequest**](TenantConfigurationSaveRequest.md)| Save Configuration parameters. | 

### Return type

[**TenantConfigurationDeploy200Response**](TenantConfigurationDeploy200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenantConfigurationValidate

> TenantConfigurationDeploy200Response tenantConfigurationValidate(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters)



This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.TenantConfigurationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
let parameters = new ApiManagementClient.TenantConfigurationDeployRequest(); // TenantConfigurationDeployRequest | Validate Configuration parameters.
apiInstance.tenantConfigurationValidate(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 
 **parameters** | [**TenantConfigurationDeployRequest**](TenantConfigurationDeployRequest.md)| Validate Configuration parameters. | 

### Return type

[**TenantConfigurationDeploy200Response**](TenantConfigurationDeploy200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

