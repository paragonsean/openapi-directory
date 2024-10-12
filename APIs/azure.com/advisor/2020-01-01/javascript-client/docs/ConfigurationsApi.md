# AdvisorManagementClient.ConfigurationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationsCreateInResourceGroup**](ConfigurationsApi.md#configurationsCreateInResourceGroup) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Advisor/configurations/{configurationName} | Create/Overwrite Azure Advisor configuration.
[**configurationsCreateInSubscription**](ConfigurationsApi.md#configurationsCreateInSubscription) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/configurations/{configurationName} | Create/Overwrite Azure Advisor configuration.
[**configurationsListByResourceGroup**](ConfigurationsApi.md#configurationsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Advisor/configurations | Retrieve Azure Advisor configurations.
[**configurationsListBySubscription**](ConfigurationsApi.md#configurationsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/configurations | Retrieve Azure Advisor configurations.



## configurationsCreateInResourceGroup

> ConfigData configurationsCreateInResourceGroup(apiVersion, subscriptionId, configurationName, resourceGroup, configContract)

Create/Overwrite Azure Advisor configuration.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.ConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let configurationName = "configurationName_example"; // String | Advisor configuration name. Value must be 'default'
let resourceGroup = "resourceGroup_example"; // String | The name of the Azure resource group.
let configContract = new AdvisorManagementClient.ConfigData(); // ConfigData | The Azure Advisor configuration data structure.
apiInstance.configurationsCreateInResourceGroup(apiVersion, subscriptionId, configurationName, resourceGroup, configContract, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **configurationName** | **String**| Advisor configuration name. Value must be &#39;default&#39; | 
 **resourceGroup** | **String**| The name of the Azure resource group. | 
 **configContract** | [**ConfigData**](ConfigData.md)| The Azure Advisor configuration data structure. | 

### Return type

[**ConfigData**](ConfigData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configurationsCreateInSubscription

> ConfigData configurationsCreateInSubscription(apiVersion, subscriptionId, configurationName, configContract)

Create/Overwrite Azure Advisor configuration.

Create/Overwrite Azure Advisor configuration and also delete all configurations of contained resource groups.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.ConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let configurationName = "configurationName_example"; // String | Advisor configuration name. Value must be 'default'
let configContract = new AdvisorManagementClient.ConfigData(); // ConfigData | The Azure Advisor configuration data structure.
apiInstance.configurationsCreateInSubscription(apiVersion, subscriptionId, configurationName, configContract, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **configurationName** | **String**| Advisor configuration name. Value must be &#39;default&#39; | 
 **configContract** | [**ConfigData**](ConfigData.md)| The Azure Advisor configuration data structure. | 

### Return type

[**ConfigData**](ConfigData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configurationsListByResourceGroup

> ConfigurationListResult configurationsListByResourceGroup(apiVersion, subscriptionId, resourceGroup)

Retrieve Azure Advisor configurations.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.ConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The name of the Azure resource group.
apiInstance.configurationsListByResourceGroup(apiVersion, subscriptionId, resourceGroup, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroup** | **String**| The name of the Azure resource group. | 

### Return type

[**ConfigurationListResult**](ConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationsListBySubscription

> ConfigurationListResult configurationsListBySubscription(apiVersion, subscriptionId)

Retrieve Azure Advisor configurations.

Retrieve Azure Advisor configurations and also retrieve configurations of contained resource groups.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.ConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
apiInstance.configurationsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 

### Return type

[**ConfigurationListResult**](ConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

