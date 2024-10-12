# AzureLogAnalytics.WorkspacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} | 
[**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} | 
[**workspacesDisableIntelligencePack**](WorkspacesApi.md#workspacesDisableIntelligencePack) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/intelligencePacks/{intelligencePackName}/Disable | 
[**workspacesEnableIntelligencePack**](WorkspacesApi.md#workspacesEnableIntelligencePack) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/intelligencePacks/{intelligencePackName}/Enable | 
[**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} | 
[**workspacesGetSharedKeys**](WorkspacesApi.md#workspacesGetSharedKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/sharedKeys | 
[**workspacesList**](WorkspacesApi.md#workspacesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/workspaces | 
[**workspacesListByResourceGroup**](WorkspacesApi.md#workspacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces | 
[**workspacesListIntelligencePacks**](WorkspacesApi.md#workspacesListIntelligencePacks) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/intelligencePacks | 
[**workspacesListManagementGroups**](WorkspacesApi.md#workspacesListManagementGroups) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/managementGroups | 
[**workspacesListUsages**](WorkspacesApi.md#workspacesListUsages) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/usages | 
[**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} | 



## workspacesCreateOrUpdate

> Workspace workspacesCreateOrUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters)



Create or update a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureLogAnalytics.Workspace(); // Workspace | The parameters required to create or update a workspace.
apiInstance.workspacesCreateOrUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the workspace. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Workspace**](Workspace.md)| The parameters required to create or update a workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspacesDelete

> workspacesDelete(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Deletes a workspace instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesDelete(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the workspace. | 
 **workspaceName** | **String**| Name of the Log Analytics Workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspacesDisableIntelligencePack

> workspacesDisableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId)



Disables an intelligence pack for a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
let intelligencePackName = "intelligencePackName_example"; // String | The name of the intelligence pack to be disabled.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesDisableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace. | 
 **intelligencePackName** | **String**| The name of the intelligence pack to be disabled. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspacesEnableIntelligencePack

> workspacesEnableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId)



Enables an intelligence pack for a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
let intelligencePackName = "intelligencePackName_example"; // String | The name of the intelligence pack to be enabled.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesEnableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace. | 
 **intelligencePackName** | **String**| The name of the intelligence pack to be enabled. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspacesGet

> Workspace workspacesGet(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets a workspace instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesGet(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the workspace. | 
 **workspaceName** | **String**| Name of the Log Analytics Workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesGetSharedKeys

> SharedKeys workspacesGetSharedKeys(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the shared keys for a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesGetSharedKeys(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedKeys**](SharedKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesList

> WorkspaceListResult workspacesList(apiVersion, subscriptionId)



Gets the workspaces in a subscription.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListByResourceGroup

> WorkspaceListResult workspacesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets workspaces in a resource group.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListIntelligencePacks

> [IntelligencePack] workspacesListIntelligencePacks(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesListIntelligencePacks(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| Name of the Log Analytics Workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**[IntelligencePack]**](IntelligencePack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListManagementGroups

> WorkspaceListManagementGroupsResult workspacesListManagementGroups(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets a list of management groups connected to a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesListManagementGroups(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| The name of the workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**WorkspaceListManagementGroupsResult**](WorkspaceListManagementGroupsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListUsages

> WorkspaceListUsagesResult workspacesListUsages(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets a list of usage metrics for a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.workspacesListUsages(resourceGroupName, workspaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **workspaceName** | **String**| The name of the workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**WorkspaceListUsagesResult**](WorkspaceListUsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesUpdate

> Workspace workspacesUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters)



Updates a workspace.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.WorkspacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureLogAnalytics.Workspace(); // Workspace | The parameters required to patch a workspace.
apiInstance.workspacesUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the workspace. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Workspace**](Workspace.md)| The parameters required to patch a workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

