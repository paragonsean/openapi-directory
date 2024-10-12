# AutomationManagement.HybridRunbookWorkerGroupApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hybridRunbookWorkerGroupDelete**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName} | 
[**hybridRunbookWorkerGroupGet**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName} | 
[**hybridRunbookWorkerGroupListByAutomationAccount**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups | 
[**hybridRunbookWorkerGroupUpdate**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName} | 



## hybridRunbookWorkerGroupDelete

> hybridRunbookWorkerGroupDelete(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion)



Delete a hybrid runbook worker group.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.HybridRunbookWorkerGroupApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let hybridRunbookWorkerGroupName = "hybridRunbookWorkerGroupName_example"; // String | The hybrid runbook worker group name
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.hybridRunbookWorkerGroupDelete(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **hybridRunbookWorkerGroupName** | **String**| The hybrid runbook worker group name | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hybridRunbookWorkerGroupGet

> HybridRunbookWorkerGroup hybridRunbookWorkerGroupGet(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion)



Retrieve a hybrid runbook worker group.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.HybridRunbookWorkerGroupApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let hybridRunbookWorkerGroupName = "hybridRunbookWorkerGroupName_example"; // String | The hybrid runbook worker group name
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.hybridRunbookWorkerGroupGet(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **hybridRunbookWorkerGroupName** | **String**| The hybrid runbook worker group name | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**HybridRunbookWorkerGroup**](HybridRunbookWorkerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hybridRunbookWorkerGroupListByAutomationAccount

> HybridRunbookWorkerGroupsListResult hybridRunbookWorkerGroupListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts)



Retrieve a list of hybrid runbook worker groups.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.HybridRunbookWorkerGroupApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.hybridRunbookWorkerGroupListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**HybridRunbookWorkerGroupsListResult**](HybridRunbookWorkerGroupsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hybridRunbookWorkerGroupUpdate

> HybridRunbookWorkerGroup hybridRunbookWorkerGroupUpdate(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion, parameters)



Update a hybrid runbook worker group.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.HybridRunbookWorkerGroupApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let hybridRunbookWorkerGroupName = "hybridRunbookWorkerGroupName_example"; // String | The hybrid runbook worker group name
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AutomationManagement.HybridRunbookWorkerGroupUpdateParameters(); // HybridRunbookWorkerGroupUpdateParameters | The hybrid runbook worker group
apiInstance.hybridRunbookWorkerGroupUpdate(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **hybridRunbookWorkerGroupName** | **String**| The hybrid runbook worker group name | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**HybridRunbookWorkerGroupUpdateParameters**](HybridRunbookWorkerGroupUpdateParameters.md)| The hybrid runbook worker group | 

### Return type

[**HybridRunbookWorkerGroup**](HybridRunbookWorkerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

