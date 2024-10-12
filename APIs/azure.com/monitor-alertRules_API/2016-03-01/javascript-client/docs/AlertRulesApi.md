# MonitorManagementClient.AlertRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertRulesCreateOrUpdate**](AlertRulesApi.md#alertRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName} | 
[**alertRulesDelete**](AlertRulesApi.md#alertRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName} | 
[**alertRulesGet**](AlertRulesApi.md#alertRulesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName} | 
[**alertRulesListByResourceGroup**](AlertRulesApi.md#alertRulesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules | 
[**alertRulesListBySubscription**](AlertRulesApi.md#alertRulesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/alertrules | 



## alertRulesCreateOrUpdate

> AlertRuleResource alertRulesCreateOrUpdate(resourceGroupName, ruleName, apiVersion, subscriptionId, parameters)



Creates or updates an alert rule.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let parameters = new MonitorManagementClient.AlertRuleResource(); // AlertRuleResource | The parameters of the rule to create or update.
apiInstance.alertRulesCreateOrUpdate(resourceGroupName, ruleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **parameters** | [**AlertRuleResource**](AlertRuleResource.md)| The parameters of the rule to create or update. | 

### Return type

[**AlertRuleResource**](AlertRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertRulesDelete

> alertRulesDelete(resourceGroupName, ruleName, apiVersion, subscriptionId)



Deletes an alert rule

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.alertRulesDelete(resourceGroupName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## alertRulesGet

> AlertRuleResource alertRulesGet(resourceGroupName, ruleName, apiVersion, subscriptionId)



Gets an alert rule

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.alertRulesGet(resourceGroupName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**AlertRuleResource**](AlertRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertRulesListByResourceGroup

> AlertRuleResourceCollection alertRulesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



List the alert rules within a resource group.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.alertRulesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**AlertRuleResourceCollection**](AlertRuleResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertRulesListBySubscription

> AlertRuleResourceCollection alertRulesListBySubscription(apiVersion, subscriptionId)



List the alert rules within a subscription.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRulesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.alertRulesListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**AlertRuleResourceCollection**](AlertRuleResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

