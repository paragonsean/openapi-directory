# AzureLogAnalytics.WorkspacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesDeleteGateways**](WorkspacesApi.md#workspacesDeleteGateways) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/gateways/{gatewayId} | 
[**workspacesGetPurgeStatus**](WorkspacesApi.md#workspacesGetPurgeStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/operations/{purgeId} | 
[**workspacesGetSchema**](WorkspacesApi.md#workspacesGetSchema) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/schema | 
[**workspacesListKeys**](WorkspacesApi.md#workspacesListKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/listKeys | 
[**workspacesListLinkTargets**](WorkspacesApi.md#workspacesListLinkTargets) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/linkTargets | 
[**workspacesPurge**](WorkspacesApi.md#workspacesPurge) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/purge | 
[**workspacesRegenerateSharedKeys**](WorkspacesApi.md#workspacesRegenerateSharedKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/regenerateSharedKey | 



## workspacesDeleteGateways

> workspacesDeleteGateways(subscriptionId, resourceGroupName, workspaceName, gatewayId, apiVersion)



Delete a Log Analytics gateway.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let gatewayId = "gatewayId_example"; // String | The Log Analytics gateway Id.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.workspacesDeleteGateways(subscriptionId, resourceGroupName, workspaceName, gatewayId, apiVersion, (error, data, response) => {
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
 **gatewayId** | **String**| The Log Analytics gateway Id. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspacesGetPurgeStatus

> WorkspacePurgeStatusResponse workspacesGetPurgeStatus(resourceGroupName, apiVersion, subscriptionId, workspaceName, purgeId)



Gets status of an ongoing purge operation.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let purgeId = "purgeId_example"; // String | In a purge status request, this is the Id of the operation the status of which is returned.
apiInstance.workspacesGetPurgeStatus(resourceGroupName, apiVersion, subscriptionId, workspaceName, purgeId, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **purgeId** | **String**| In a purge status request, this is the Id of the operation the status of which is returned. | 

### Return type

[**WorkspacePurgeStatusResponse**](WorkspacePurgeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesGetSchema

> SearchGetSchemaResponse workspacesGetSchema(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the schema for a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
apiInstance.workspacesGetSchema(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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

[**SearchGetSchemaResponse**](SearchGetSchemaResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListKeys

> SharedKeys workspacesListKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Gets the shared keys for a Log Analytics Workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.workspacesListKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 

### Return type

[**SharedKeys**](SharedKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListLinkTargets

> [LinkTarget] workspacesListLinkTargets(apiVersion, subscriptionId)



Get a list of workspaces which the current user has administrator privileges and are not associated with an Azure Subscription. The subscriptionId parameter in the Url is ignored.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
apiInstance.workspacesListLinkTargets(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 

### Return type

[**[LinkTarget]**](LinkTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesPurge

> WorkspacePurgeResponse workspacesPurge(resourceGroupName, apiVersion, subscriptionId, workspaceName, body)



Purges data in an Log Analytics workspace by a set of user-defined filters.  In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let body = new AzureLogAnalytics.WorkspacePurgeBody(); // WorkspacePurgeBody | Describes the body of a request to purge data in a single table of an Log Analytics Workspace
apiInstance.workspacesPurge(resourceGroupName, apiVersion, subscriptionId, workspaceName, body, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Subscription ID. | 
 **workspaceName** | **String**| The Log Analytics Workspace name. | 
 **body** | [**WorkspacePurgeBody**](WorkspacePurgeBody.md)| Describes the body of a request to purge data in a single table of an Log Analytics Workspace | 

### Return type

[**WorkspacePurgeResponse**](WorkspacePurgeResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspacesRegenerateSharedKeys

> SharedKeys workspacesRegenerateSharedKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Regenerates the shared keys for a Log Analytics Workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
let workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.workspacesRegenerateSharedKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 

### Return type

[**SharedKeys**](SharedKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

