# AutomationManagement.DscNodeConfigurationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dscNodeConfigurationCreateOrUpdate**](DscNodeConfigurationApi.md#dscNodeConfigurationCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName} | 
[**dscNodeConfigurationDelete**](DscNodeConfigurationApi.md#dscNodeConfigurationDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName} | 
[**dscNodeConfigurationGet**](DscNodeConfigurationApi.md#dscNodeConfigurationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName} | 
[**dscNodeConfigurationListByAutomationAccount**](DscNodeConfigurationApi.md#dscNodeConfigurationListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations | 



## dscNodeConfigurationCreateOrUpdate

> dscNodeConfigurationCreateOrUpdate(resourceGroupName, automationAccountName, nodeConfigurationName, subscriptionId, apiVersion, parameters)



Create the node configuration identified by node configuration name.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeConfigurationApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeConfigurationName = "nodeConfigurationName_example"; // String | The Dsc node configuration name.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AutomationManagement.DscNodeConfigurationCreateOrUpdateParameters(); // DscNodeConfigurationCreateOrUpdateParameters | The create or update parameters for configuration.
apiInstance.dscNodeConfigurationCreateOrUpdate(resourceGroupName, automationAccountName, nodeConfigurationName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **nodeConfigurationName** | **String**| The Dsc node configuration name. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DscNodeConfigurationCreateOrUpdateParameters**](DscNodeConfigurationCreateOrUpdateParameters.md)| The create or update parameters for configuration. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dscNodeConfigurationDelete

> dscNodeConfigurationDelete(subscriptionId, resourceGroupName, automationAccountName, nodeConfigurationName, apiVersion)



Delete the Dsc node configurations by node configuration.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeConfigurationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeConfigurationName = "nodeConfigurationName_example"; // String | The Dsc node configuration name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscNodeConfigurationDelete(subscriptionId, resourceGroupName, automationAccountName, nodeConfigurationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **nodeConfigurationName** | **String**| The Dsc node configuration name. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscNodeConfigurationGet

> DscNodeConfiguration dscNodeConfigurationGet(subscriptionId, resourceGroupName, automationAccountName, nodeConfigurationName, apiVersion)



Retrieve the Dsc node configurations by node configuration.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeConfigurationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeConfigurationName = "nodeConfigurationName_example"; // String | The Dsc node configuration name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscNodeConfigurationGet(subscriptionId, resourceGroupName, automationAccountName, nodeConfigurationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **nodeConfigurationName** | **String**| The Dsc node configuration name. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DscNodeConfiguration**](DscNodeConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscNodeConfigurationListByAutomationAccount

> DscNodeConfigurationListResult dscNodeConfigurationListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts)



Retrieve a list of dsc node configurations.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscNodeConfigurationApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'skip': 56, // Number | The number of rows to skip.
  'top': 56, // Number | The number of rows to take.
  'inlinecount': "inlinecount_example" // String | Return total rows.
};
apiInstance.dscNodeConfigurationListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **skip** | **Number**| The number of rows to skip. | [optional] 
 **top** | **Number**| The number of rows to take. | [optional] 
 **inlinecount** | **String**| Return total rows. | [optional] 

### Return type

[**DscNodeConfigurationListResult**](DscNodeConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

