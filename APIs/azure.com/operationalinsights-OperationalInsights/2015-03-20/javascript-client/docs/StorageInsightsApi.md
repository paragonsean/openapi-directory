# AzureLogAnalytics.StorageInsightsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageInsightsCreateOrUpdate**](StorageInsightsApi.md#storageInsightsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName} | 
[**storageInsightsDelete**](StorageInsightsApi.md#storageInsightsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName} | 
[**storageInsightsGet**](StorageInsightsApi.md#storageInsightsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName} | 
[**storageInsightsListByWorkspace**](StorageInsightsApi.md#storageInsightsListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs | 



## storageInsightsCreateOrUpdate

> StorageInsight storageInsightsCreateOrUpdate(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId, parameters)



Create or update a storage insight.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.StorageInsightsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let storageInsightName = "storageInsightName_example"; // String | Name of the storageInsightsConfigs resource
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let parameters = new AzureLogAnalytics.StorageInsight(); // StorageInsight | The parameters required to create or update a storage insight.
apiInstance.storageInsightsCreateOrUpdate(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **storageInsightName** | **String**| Name of the storageInsightsConfigs resource | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 
 **parameters** | [**StorageInsight**](StorageInsight.md)| The parameters required to create or update a storage insight. | 

### Return type

[**StorageInsight**](StorageInsight.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageInsightsDelete

> storageInsightsDelete(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId)



Deletes a storageInsightsConfigs resource

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.StorageInsightsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let storageInsightName = "storageInsightName_example"; // String | Name of the storageInsightsConfigs resource
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
apiInstance.storageInsightsDelete(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **storageInsightName** | **String**| Name of the storageInsightsConfigs resource | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageInsightsGet

> StorageInsight storageInsightsGet(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId)



Gets a storage insight instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.StorageInsightsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let storageInsightName = "storageInsightName_example"; // String | Name of the storageInsightsConfigs resource
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
apiInstance.storageInsightsGet(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **storageInsightName** | **String**| Name of the storageInsightsConfigs resource | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 

### Return type

[**StorageInsight**](StorageInsight.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageInsightsListByWorkspace

> StorageInsightListResult storageInsightsListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Lists the storage insight instances within a workspace

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.StorageInsightsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
apiInstance.storageInsightsListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 

### Return type

[**StorageInsightListResult**](StorageInsightListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

