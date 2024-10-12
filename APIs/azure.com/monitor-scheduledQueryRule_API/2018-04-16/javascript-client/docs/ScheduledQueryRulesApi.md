# MicrosoftInsights.ScheduledQueryRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduledQueryRulesCreateOrUpdate**](ScheduledQueryRulesApi.md#scheduledQueryRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} | 
[**scheduledQueryRulesDelete**](ScheduledQueryRulesApi.md#scheduledQueryRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} | 
[**scheduledQueryRulesGet**](ScheduledQueryRulesApi.md#scheduledQueryRulesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} | 
[**scheduledQueryRulesListByResourceGroup**](ScheduledQueryRulesApi.md#scheduledQueryRulesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules | 
[**scheduledQueryRulesListBySubscription**](ScheduledQueryRulesApi.md#scheduledQueryRulesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/scheduledQueryRules | 
[**scheduledQueryRulesUpdate**](ScheduledQueryRulesApi.md#scheduledQueryRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} | 



## scheduledQueryRulesCreateOrUpdate

> LogSearchRuleResource scheduledQueryRulesCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Creates or updates an log search rule.

### Example

```javascript
import MicrosoftInsights from 'microsoft_insights';
let defaultClient = MicrosoftInsights.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftInsights.ScheduledQueryRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new MicrosoftInsights.LogSearchRuleResource(); // LogSearchRuleResource | The parameters of the rule to create or update.
apiInstance.scheduledQueryRulesCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**LogSearchRuleResource**](LogSearchRuleResource.md)| The parameters of the rule to create or update. | 

### Return type

[**LogSearchRuleResource**](LogSearchRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## scheduledQueryRulesDelete

> scheduledQueryRulesDelete(resourceGroupName, ruleName, apiVersion, subscriptionId)



Deletes a Log Search rule

### Example

```javascript
import MicrosoftInsights from 'microsoft_insights';
let defaultClient = MicrosoftInsights.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftInsights.ScheduledQueryRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.scheduledQueryRulesDelete(resourceGroupName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
- **Accept**: application/json


## scheduledQueryRulesGet

> LogSearchRuleResource scheduledQueryRulesGet(resourceGroupName, ruleName, apiVersion, subscriptionId)



Gets an Log Search rule

### Example

```javascript
import MicrosoftInsights from 'microsoft_insights';
let defaultClient = MicrosoftInsights.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftInsights.ScheduledQueryRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.scheduledQueryRulesGet(resourceGroupName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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

[**LogSearchRuleResource**](LogSearchRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scheduledQueryRulesListByResourceGroup

> LogSearchRuleResourceCollection scheduledQueryRulesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



List the Log Search rules within a resource group.

### Example

```javascript
import MicrosoftInsights from 'microsoft_insights';
let defaultClient = MicrosoftInsights.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftInsights.ScheduledQueryRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
};
apiInstance.scheduledQueryRulesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx | [optional] 

### Return type

[**LogSearchRuleResourceCollection**](LogSearchRuleResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scheduledQueryRulesListBySubscription

> LogSearchRuleResourceCollection scheduledQueryRulesListBySubscription(apiVersion, subscriptionId, opts)



List the Log Search rules within a subscription group.

### Example

```javascript
import MicrosoftInsights from 'microsoft_insights';
let defaultClient = MicrosoftInsights.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftInsights.ScheduledQueryRulesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
};
apiInstance.scheduledQueryRulesListBySubscription(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx | [optional] 

### Return type

[**LogSearchRuleResourceCollection**](LogSearchRuleResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scheduledQueryRulesUpdate

> LogSearchRuleResource scheduledQueryRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Update log search Rule.

### Example

```javascript
import MicrosoftInsights from 'microsoft_insights';
let defaultClient = MicrosoftInsights.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftInsights.ScheduledQueryRulesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new MicrosoftInsights.LogSearchRuleResourcePatch(); // LogSearchRuleResourcePatch | The parameters of the rule to update.
apiInstance.scheduledQueryRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**LogSearchRuleResourcePatch**](LogSearchRuleResourcePatch.md)| The parameters of the rule to update. | 

### Return type

[**LogSearchRuleResource**](LogSearchRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

