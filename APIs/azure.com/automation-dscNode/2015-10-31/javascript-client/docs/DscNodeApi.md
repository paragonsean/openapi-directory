# AutomationManagement.DscNodeApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dscNodeDelete**](DscNodeApi.md#dscNodeDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId} | 
[**dscNodeGet**](DscNodeApi.md#dscNodeGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId} | 
[**dscNodeListByAutomationAccount**](DscNodeApi.md#dscNodeListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes | 
[**dscNodeUpdate**](DscNodeApi.md#dscNodeUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId} | 



## dscNodeDelete

> DscNode dscNodeDelete(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion)



Delete the dsc node identified by node id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeId = "nodeId_example"; // String | The node id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscNodeDelete(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion, (error, data, response) => {
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
 **nodeId** | **String**| The node id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DscNode**](DscNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscNodeGet

> DscNode dscNodeGet(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion)



Retrieve the dsc node identified by node id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeId = "nodeId_example"; // String | The node id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscNodeGet(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion, (error, data, response) => {
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
 **nodeId** | **String**| The node id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DscNode**](DscNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscNodeListByAutomationAccount

> DscNodeListResult dscNodeListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts)



Retrieve a list of dsc nodes.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.dscNodeListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts, (error, data, response) => {
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

[**DscNodeListResult**](DscNodeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscNodeUpdate

> DscNode dscNodeUpdate(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion, parameters)



Update the dsc node.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeId = "nodeId_example"; // String | Parameters supplied to the update dsc node.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AutomationManagement.DscNodeUpdateParameters(); // DscNodeUpdateParameters | Parameters supplied to the update dsc node.
apiInstance.dscNodeUpdate(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **nodeId** | **String**| Parameters supplied to the update dsc node. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DscNodeUpdateParameters**](DscNodeUpdateParameters.md)| Parameters supplied to the update dsc node. | 

### Return type

[**DscNode**](DscNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

