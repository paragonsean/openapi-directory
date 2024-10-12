# MonitorManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertRulesUpdate**](DefaultApi.md#alertRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName} | 



## alertRulesUpdate

> AlertRuleResource alertRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, alertRulesResource)



Updates an existing AlertRuleResource. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let alertRulesResource = new MonitorManagementClient.AlertRuleResourcePatch(); // AlertRuleResourcePatch | Parameters supplied to the operation.
apiInstance.alertRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, alertRulesResource, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **alertRulesResource** | [**AlertRuleResourcePatch**](AlertRuleResourcePatch.md)| Parameters supplied to the operation. | 

### Return type

[**AlertRuleResource**](AlertRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

