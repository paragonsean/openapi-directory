# AzureLogAnalytics.DataSourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataSourcesCreateOrUpdate**](DataSourcesApi.md#dataSourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources/{dataSourceName} | 
[**dataSourcesDelete**](DataSourcesApi.md#dataSourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources/{dataSourceName} | 
[**dataSourcesGet**](DataSourcesApi.md#dataSourcesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources/{dataSourceName} | 
[**dataSourcesListByWorkspace**](DataSourcesApi.md#dataSourcesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources | 



## dataSourcesCreateOrUpdate

> DataSource dataSourcesCreateOrUpdate(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId, parameters)



Create or update a data source.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataSourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that will contain the datasource
let dataSourceName = "dataSourceName_example"; // String | The name of the datasource resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureLogAnalytics.DataSource(); // DataSource | The parameters required to create or update a datasource.
apiInstance.dataSourcesCreateOrUpdate(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **workspaceName** | **String**| Name of the Log Analytics Workspace that will contain the datasource | 
 **dataSourceName** | **String**| The name of the datasource resource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DataSource**](DataSource.md)| The parameters required to create or update a datasource. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataSourcesDelete

> dataSourcesDelete(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId)



Deletes a data source instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataSourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the datasource.
let dataSourceName = "dataSourceName_example"; // String | Name of the datasource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dataSourcesDelete(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the datasource. | 
 **dataSourceName** | **String**| Name of the datasource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dataSourcesGet

> DataSource dataSourcesGet(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId)



Gets a datasource instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataSourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the datasource.
let dataSourceName = "dataSourceName_example"; // String | Name of the datasource
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dataSourcesGet(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the datasource. | 
 **dataSourceName** | **String**| Name of the datasource | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSourcesListByWorkspace

> DataSourceListResult dataSourcesListByWorkspace(resourceGroupName, workspaceName, filter, apiVersion, subscriptionId, opts)



Gets the first page of data source instances in a workspace with the link to the next page.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DataSourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | The workspace that contains the data sources.
let filter = "filter_example"; // String | The filter to apply on the operation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'skiptoken': "skiptoken_example" // String | Starting point of the collection of data source instances.
};
apiInstance.dataSourcesListByWorkspace(resourceGroupName, workspaceName, filter, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **workspaceName** | **String**| The workspace that contains the data sources. | 
 **filter** | **String**| The filter to apply on the operation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **skiptoken** | **String**| Starting point of the collection of data source instances. | [optional] 

### Return type

[**DataSourceListResult**](DataSourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

