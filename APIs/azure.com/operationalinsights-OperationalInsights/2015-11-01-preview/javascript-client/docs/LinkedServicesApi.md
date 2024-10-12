# AzureLogAnalytics.LinkedServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**linkedServicesCreateOrUpdate**](LinkedServicesApi.md#linkedServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices/{linkedServiceName} | 
[**linkedServicesDelete**](LinkedServicesApi.md#linkedServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices/{linkedServiceName} | 
[**linkedServicesGet**](LinkedServicesApi.md#linkedServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices/{linkedServiceName} | 
[**linkedServicesListByWorkspace**](LinkedServicesApi.md#linkedServicesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices | 



## linkedServicesCreateOrUpdate

> LinkedService linkedServicesCreateOrUpdate(resourceGroupName, workspaceName, linkedServiceName, subscriptionId, apiVersion, parameters)



Create or update a linked service.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.LinkedServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that will contain the linkedServices resource
let linkedServiceName = "linkedServiceName_example"; // String | Name of the linkedServices resource
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AzureLogAnalytics.LinkedService(); // LinkedService | The parameters required to create or update a linked service.
apiInstance.linkedServicesCreateOrUpdate(resourceGroupName, workspaceName, linkedServiceName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace that will contain the linkedServices resource | 
 **linkedServiceName** | **String**| Name of the linkedServices resource | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**LinkedService**](LinkedService.md)| The parameters required to create or update a linked service. | 

### Return type

[**LinkedService**](LinkedService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkedServicesDelete

> linkedServicesDelete(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId)



Deletes a linked service instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.LinkedServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the linkedServices resource
let linkedServiceName = "linkedServiceName_example"; // String | Name of the linked service.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.linkedServicesDelete(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the linkedServices resource | 
 **linkedServiceName** | **String**| Name of the linked service. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## linkedServicesGet

> LinkedService linkedServicesGet(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId)



Gets a linked service instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.LinkedServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the linkedServices resource
let linkedServiceName = "linkedServiceName_example"; // String | Name of the linked service.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.linkedServicesGet(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the linkedServices resource | 
 **linkedServiceName** | **String**| Name of the linked service. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LinkedService**](LinkedService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## linkedServicesListByWorkspace

> LinkedServiceListResult linkedServicesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the linked services instances in a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.LinkedServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the linked services.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.linkedServicesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the linked services. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LinkedServiceListResult**](LinkedServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

