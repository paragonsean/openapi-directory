# LogicManagementClient.IntegrationAccountRosettaNetProcessConfigurationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rosettaNetProcessConfigurationsCreateOrUpdate**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations/{rosettaNetProcessConfigurationName} | 
[**rosettaNetProcessConfigurationsDelete**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations/{rosettaNetProcessConfigurationName} | 
[**rosettaNetProcessConfigurationsGet**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations/{rosettaNetProcessConfigurationName} | 
[**rosettaNetProcessConfigurationsListByIntegrationAccounts**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsListByIntegrationAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations | 



## rosettaNetProcessConfigurationsCreateOrUpdate

> IntegrationAccountRosettaNetProcessConfiguration rosettaNetProcessConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion, rosettaNetProcessConfiguration)



Creates or updates an integration account RosettaNetProcessConfiguration.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountRosettaNetProcessConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let rosettaNetProcessConfigurationName = "rosettaNetProcessConfigurationName_example"; // String | The integration account RosettaNet ProcessConfiguration name.
let apiVersion = "apiVersion_example"; // String | The API version.
let rosettaNetProcessConfiguration = new LogicManagementClient.IntegrationAccountRosettaNetProcessConfiguration(); // IntegrationAccountRosettaNetProcessConfiguration | The integration account RosettaNet ProcessConfiguration.
apiInstance.rosettaNetProcessConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion, rosettaNetProcessConfiguration, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **rosettaNetProcessConfigurationName** | **String**| The integration account RosettaNet ProcessConfiguration name. | 
 **apiVersion** | **String**| The API version. | 
 **rosettaNetProcessConfiguration** | [**IntegrationAccountRosettaNetProcessConfiguration**](IntegrationAccountRosettaNetProcessConfiguration.md)| The integration account RosettaNet ProcessConfiguration. | 

### Return type

[**IntegrationAccountRosettaNetProcessConfiguration**](IntegrationAccountRosettaNetProcessConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rosettaNetProcessConfigurationsDelete

> rosettaNetProcessConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion)



Deletes an integration account RosettaNet ProcessConfiguration.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountRosettaNetProcessConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let rosettaNetProcessConfigurationName = "rosettaNetProcessConfigurationName_example"; // String | The integration account RosettaNetProcessConfiguration name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rosettaNetProcessConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **rosettaNetProcessConfigurationName** | **String**| The integration account RosettaNetProcessConfiguration name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## rosettaNetProcessConfigurationsGet

> IntegrationAccountRosettaNetProcessConfiguration rosettaNetProcessConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion)



Gets an integration account RosettaNetProcessConfiguration.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountRosettaNetProcessConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let rosettaNetProcessConfigurationName = "rosettaNetProcessConfigurationName_example"; // String | The integration account RosettaNetProcessConfiguration name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rosettaNetProcessConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **rosettaNetProcessConfigurationName** | **String**| The integration account RosettaNetProcessConfiguration name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountRosettaNetProcessConfiguration**](IntegrationAccountRosettaNetProcessConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rosettaNetProcessConfigurationsListByIntegrationAccounts

> IntegrationAccountRosettaNetProcessConfigurationListResult rosettaNetProcessConfigurationsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account RosettaNet process configurations.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountRosettaNetProcessConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.rosettaNetProcessConfigurationsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**IntegrationAccountRosettaNetProcessConfigurationListResult**](IntegrationAccountRosettaNetProcessConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

