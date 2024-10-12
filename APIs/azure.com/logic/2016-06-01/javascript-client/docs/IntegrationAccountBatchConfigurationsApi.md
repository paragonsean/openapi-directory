# LogicManagementClient.IntegrationAccountBatchConfigurationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountBatchConfigurationsCreateOrUpdate**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName} | 
[**integrationAccountBatchConfigurationsDelete**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName} | 
[**integrationAccountBatchConfigurationsGet**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName} | 
[**integrationAccountBatchConfigurationsList**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations | 



## integrationAccountBatchConfigurationsCreateOrUpdate

> BatchConfiguration integrationAccountBatchConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion, batchConfiguration)



Create or update a batch configuration for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountBatchConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let batchConfigurationName = "batchConfigurationName_example"; // String | The batch configuration name.
let apiVersion = "apiVersion_example"; // String | The API version.
let batchConfiguration = new LogicManagementClient.BatchConfiguration(); // BatchConfiguration | The batch configuration.
apiInstance.integrationAccountBatchConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion, batchConfiguration, (error, data, response) => {
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
 **batchConfigurationName** | **String**| The batch configuration name. | 
 **apiVersion** | **String**| The API version. | 
 **batchConfiguration** | [**BatchConfiguration**](BatchConfiguration.md)| The batch configuration. | 

### Return type

[**BatchConfiguration**](BatchConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationAccountBatchConfigurationsDelete

> integrationAccountBatchConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion)



Delete a batch configuration for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountBatchConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let batchConfigurationName = "batchConfigurationName_example"; // String | The batch configuration name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountBatchConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion, (error, data, response) => {
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
 **batchConfigurationName** | **String**| The batch configuration name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## integrationAccountBatchConfigurationsGet

> BatchConfiguration integrationAccountBatchConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion)



Get a batch configuration for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountBatchConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let batchConfigurationName = "batchConfigurationName_example"; // String | The batch configuration name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountBatchConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion, (error, data, response) => {
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
 **batchConfigurationName** | **String**| The batch configuration name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**BatchConfiguration**](BatchConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountBatchConfigurationsList

> BatchConfigurationCollection integrationAccountBatchConfigurationsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



List the batch configurations for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountBatchConfigurationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountBatchConfigurationsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, (error, data, response) => {
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

### Return type

[**BatchConfigurationCollection**](BatchConfigurationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

