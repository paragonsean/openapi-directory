# MlTeamAccountManagementClient.ProjectsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsCreateOrUpdate**](ProjectsApi.md#projectsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} | 
[**projectsDelete**](ProjectsApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} | 
[**projectsGet**](ProjectsApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} | 
[**projectsListByWorkspace**](ProjectsApi.md#projectsListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces{workspaceName}/projects | 
[**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} | 



## projectsCreateOrUpdate

> Project projectsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters)



Creates or updates a project with the specified parameters.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.ProjectsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
let parameters = new MlTeamAccountManagementClient.Project(); // Project | The parameters for creating or updating a project.
apiInstance.projectsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters, (error, data, response) => {
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
 **projectName** | **String**| The name of the machine learning project under a team account workspace. | 
 **parameters** | [**Project**](Project.md)| The parameters for creating or updating a project. | 

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsDelete

> projectsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName)



Deletes a project.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.ProjectsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
apiInstance.projectsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, (error, data, response) => {
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
 **projectName** | **String**| The name of the machine learning project under a team account workspace. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGet

> Project projectsGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName)



Gets the properties of the specified machine learning project.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.ProjectsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
apiInstance.projectsGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, (error, data, response) => {
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
 **projectName** | **String**| The name of the machine learning project under a team account workspace. | 

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListByWorkspace

> ProjectListResult projectsListByWorkspace(apiVersion, subscriptionId, accountName, workspaceName, resourceGroupName)



Lists all the available machine learning projects under the specified workspace.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.ProjectsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
apiInstance.projectsListByWorkspace(apiVersion, subscriptionId, accountName, workspaceName, resourceGroupName, (error, data, response) => {
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
 **workspaceName** | **String**| The name of the machine learning team account workspace. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 

### Return type

[**ProjectListResult**](ProjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsUpdate

> Project projectsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters)



Updates a project with the specified parameters.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.ProjectsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
let projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
let parameters = new MlTeamAccountManagementClient.ProjectUpdateParameters(); // ProjectUpdateParameters | The parameters for updating a machine learning team account.
apiInstance.projectsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters, (error, data, response) => {
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
 **projectName** | **String**| The name of the machine learning project under a team account workspace. | 
 **parameters** | [**ProjectUpdateParameters**](ProjectUpdateParameters.md)| The parameters for updating a machine learning team account. | 

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

