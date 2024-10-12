# AzureAlertsManagementServiceResourceProvider.SmartDetectorAlertRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smartDetectorAlertRulesCreateOrUpdate**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alertRuleName} | 
[**smartDetectorAlertRulesDelete**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alertRuleName} | 
[**smartDetectorAlertRulesGet**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alertRuleName} | 
[**smartDetectorAlertRulesList**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.alertsManagement/smartDetectorAlertRules | 
[**smartDetectorAlertRulesListByResourceGroup**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules | 



## smartDetectorAlertRulesCreateOrUpdate

> AlertRule smartDetectorAlertRulesCreateOrUpdate(subscriptionId, resourceGroupName, alertRuleName, apiVersion, parameters)



Create or update a Smart Detector alert rule.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';
let defaultClient = AzureAlertsManagementServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.SmartDetectorAlertRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let alertRuleName = "alertRuleName_example"; // String | The name of the alert rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AzureAlertsManagementServiceResourceProvider.AlertRule(); // AlertRule | Parameters supplied to the operation.
apiInstance.smartDetectorAlertRulesCreateOrUpdate(subscriptionId, resourceGroupName, alertRuleName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **alertRuleName** | **String**| The name of the alert rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**AlertRule**](AlertRule.md)| Parameters supplied to the operation. | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## smartDetectorAlertRulesDelete

> smartDetectorAlertRulesDelete(subscriptionId, resourceGroupName, alertRuleName, apiVersion)



Delete an existing Smart Detector alert rule.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';
let defaultClient = AzureAlertsManagementServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.SmartDetectorAlertRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let alertRuleName = "alertRuleName_example"; // String | The name of the alert rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.smartDetectorAlertRulesDelete(subscriptionId, resourceGroupName, alertRuleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **alertRuleName** | **String**| The name of the alert rule. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartDetectorAlertRulesGet

> AlertRule smartDetectorAlertRulesGet(subscriptionId, resourceGroupName, alertRuleName, apiVersion, opts)



Get a specific Smart Detector alert rule.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';
let defaultClient = AzureAlertsManagementServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.SmartDetectorAlertRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let alertRuleName = "alertRuleName_example"; // String | The name of the alert rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'expandDetector': true // Boolean | Indicates if Smart Detector should be expanded.
};
apiInstance.smartDetectorAlertRulesGet(subscriptionId, resourceGroupName, alertRuleName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **alertRuleName** | **String**| The name of the alert rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **expandDetector** | **Boolean**| Indicates if Smart Detector should be expanded. | [optional] 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartDetectorAlertRulesList

> AlertRulesList smartDetectorAlertRulesList(subscriptionId, apiVersion)



List all the existing Smart Detector alert rules within the subscription.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';
let defaultClient = AzureAlertsManagementServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.SmartDetectorAlertRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.smartDetectorAlertRulesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**AlertRulesList**](AlertRulesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartDetectorAlertRulesListByResourceGroup

> AlertRulesList smartDetectorAlertRulesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List all the existing Smart Detector alert rules within the subscription and resource group.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';
let defaultClient = AzureAlertsManagementServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.SmartDetectorAlertRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.smartDetectorAlertRulesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**AlertRulesList**](AlertRulesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

