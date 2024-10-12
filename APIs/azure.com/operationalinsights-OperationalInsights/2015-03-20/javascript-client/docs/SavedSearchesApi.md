# AzureLogAnalytics.SavedSearchesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**savedSearchesCreateOrUpdate**](SavedSearchesApi.md#savedSearchesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches/{savedSearchId} | 
[**savedSearchesDelete**](SavedSearchesApi.md#savedSearchesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches/{savedSearchId} | 
[**savedSearchesGet**](SavedSearchesApi.md#savedSearchesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches/{savedSearchId} | 
[**savedSearchesListByWorkspace**](SavedSearchesApi.md#savedSearchesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches | 



## savedSearchesCreateOrUpdate

> SavedSearch savedSearchesCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion, parameters)



Creates or updates a saved search for a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.SavedSearchesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let savedSearchId = "savedSearchId_example"; // String | The id of the saved search.
let apiVersion = "apiVersion_example"; // String | The client API version.
let parameters = new AzureLogAnalytics.SavedSearch(); // SavedSearch | The parameters required to save a search.
apiInstance.savedSearchesCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription ID. | 
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **savedSearchId** | **String**| The id of the saved search. | 
 **apiVersion** | **String**| The client API version. | 
 **parameters** | [**SavedSearch**](SavedSearch.md)| The parameters required to save a search. | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## savedSearchesDelete

> savedSearchesDelete(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion)



Deletes the specified saved search in a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.SavedSearchesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let savedSearchId = "savedSearchId_example"; // String | The id of the saved search.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.savedSearchesDelete(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription ID. | 
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **savedSearchId** | **String**| The id of the saved search. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## savedSearchesGet

> SavedSearch savedSearchesGet(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion)



Gets the specified saved search for a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.SavedSearchesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let savedSearchId = "savedSearchId_example"; // String | The id of the saved search.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.savedSearchesGet(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription ID. | 
 **resourceGroupName** | **String**| The Resource Group name. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **savedSearchId** | **String**| The id of the saved search. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedSearchesListByWorkspace

> SavedSearchesListResult savedSearchesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the saved searches for a given Log Analytics Workspace

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.SavedSearchesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
apiInstance.savedSearchesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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

[**SavedSearchesListResult**](SavedSearchesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

