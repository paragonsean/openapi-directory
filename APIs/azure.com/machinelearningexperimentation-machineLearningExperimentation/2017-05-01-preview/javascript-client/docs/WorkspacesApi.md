# MlTeamAccountManagementClient.WorkspacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} | 
[**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} | 
[**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} | 
[**workspacesListByAccounts**](WorkspacesApi.md#workspacesListByAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces | 
[**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} | 



## workspacesCreateOrUpdate

> Workspace workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters)



Creates or updates a machine learning workspace with the specified parameters.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let parameters = new MlTeamAccountManagementClient.Workspace(); // Workspace | The parameters for creating or updating a machine learning workspace.
apiInstance.workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **workspaceName** | **String**| The name of the machine learning team account workspace. | 
 **parameters** | [**Workspace**](Workspace.md)| The parameters for creating or updating a machine learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspacesDelete

> workspacesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName)



Deletes a machine learning workspace.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
apiInstance.workspacesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **workspaceName** | **String**| The name of the machine learning team account workspace. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesGet

> Workspace workspacesGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName)



Gets the properties of the specified machine learning workspace.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
apiInstance.workspacesGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **workspaceName** | **String**| The name of the machine learning team account workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListByAccounts

> WorkspaceListResult workspacesListByAccounts(apiVersion, subscriptionId, accountName, resourceGroupName)



Lists all the available machine learning workspaces under the specified team account.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
apiInstance.workspacesListByAccounts(apiVersion, subscriptionId, accountName, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesUpdate

> Workspace workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters)



Updates a machine learning workspace with the specified parameters.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let parameters = new MlTeamAccountManagementClient.WorkspaceUpdateParameters(); // WorkspaceUpdateParameters | The parameters for updating a machine learning workspace.
apiInstance.workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **workspaceName** | **String**| The name of the machine learning team account workspace. | 
 **parameters** | [**WorkspaceUpdateParameters**](WorkspaceUpdateParameters.md)| The parameters for updating a machine learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

