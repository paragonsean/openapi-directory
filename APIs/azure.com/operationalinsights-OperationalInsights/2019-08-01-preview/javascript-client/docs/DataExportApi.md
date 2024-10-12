# AzureLogAnalytics.DataExportApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataExportCreateOrUpdate**](DataExportApi.md#dataExportCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName} | 
[**dataExportDelete**](DataExportApi.md#dataExportDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName} | 
[**dataExportGet**](DataExportApi.md#dataExportGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName} | 
[**dataExportListByWorkspace**](DataExportApi.md#dataExportListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports | 



## dataExportCreateOrUpdate

> DataExport dataExportCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion, parameters)



Create or update a data export.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataExportApi();
let subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
let dataExportName = "dataExportName_example"; // String | The data export rule name.
let apiVersion = "apiVersion_example"; // String | The client API version.
let parameters = new AzureLogAnalytics.DataExport(); // DataExport | The parameters required to create or update a data export.
apiInstance.dataExportCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | 
 **resourceGroupName** | **String**| The workspace&#39;s resource group name. | 
 **workspaceName** | **String**| The Log Analytics workspace name. | 
 **dataExportName** | **String**| The data export rule name. | 
 **apiVersion** | **String**| The client API version. | 
 **parameters** | [**DataExport**](DataExport.md)| The parameters required to create or update a data export. | 

### Return type

[**DataExport**](DataExport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataExportDelete

> dataExportDelete(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion)



Deletes the specified data export in a given workspace..

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataExportApi();
let subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
let dataExportName = "dataExportName_example"; // String | The data export rule name.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.dataExportDelete(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | 
 **resourceGroupName** | **String**| The workspace&#39;s resource group name. | 
 **workspaceName** | **String**| The Log Analytics workspace name. | 
 **dataExportName** | **String**| The data export rule name. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataExportGet

> DataExport dataExportGet(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion)



Gets a data export instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataExportApi();
let subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
let dataExportName = "dataExportName_example"; // String | The data export rule name.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.dataExportGet(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | 
 **resourceGroupName** | **String**| The workspace&#39;s resource group name. | 
 **workspaceName** | **String**| The Log Analytics workspace name. | 
 **dataExportName** | **String**| The data export rule name. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**DataExport**](DataExport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataExportListByWorkspace

> DataExportListResult dataExportListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Lists the data export instances within a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataExportApi();
let subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.dataExportListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | 
 **resourceGroupName** | **String**| The workspace&#39;s resource group name. | 
 **workspaceName** | **String**| The Log Analytics workspace name. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**DataExportListResult**](DataExportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

