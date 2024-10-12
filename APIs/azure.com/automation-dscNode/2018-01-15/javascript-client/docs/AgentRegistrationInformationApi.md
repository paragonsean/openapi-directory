# AutomationManagement.AgentRegistrationInformationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agentRegistrationInformationGet**](AgentRegistrationInformationApi.md#agentRegistrationInformationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/agentRegistrationInformation | 
[**agentRegistrationInformationRegenerateKey**](AgentRegistrationInformationApi.md#agentRegistrationInformationRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/agentRegistrationInformation/regenerateKey | 



## agentRegistrationInformationGet

> AgentRegistration agentRegistrationInformationGet(subscriptionId, resourceGroupName, automationAccountName, apiVersion)



Retrieve the automation agent registration information.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.AgentRegistrationInformationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.agentRegistrationInformationGet(subscriptionId, resourceGroupName, automationAccountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**AgentRegistration**](AgentRegistration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## agentRegistrationInformationRegenerateKey

> AgentRegistration agentRegistrationInformationRegenerateKey(subscriptionId, resourceGroupName, automationAccountName, apiVersion, parameters)



Regenerate a primary or secondary agent registration key

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.AgentRegistrationInformationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AutomationManagement.AgentRegistrationRegenerateKeyParameter(); // AgentRegistrationRegenerateKeyParameter | The name of the agent registration key to be regenerated
apiInstance.agentRegistrationInformationRegenerateKey(subscriptionId, resourceGroupName, automationAccountName, apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**AgentRegistrationRegenerateKeyParameter**](AgentRegistrationRegenerateKeyParameter.md)| The name of the agent registration key to be regenerated | 

### Return type

[**AgentRegistration**](AgentRegistration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain

