# AzureMigrateHub.MigrateProjectsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrateProjectsDeleteMigrateProject**](MigrateProjectsApi.md#migrateProjectsDeleteMigrateProject) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Delete the migrate project
[**migrateProjectsGetMigrateProject**](MigrateProjectsApi.md#migrateProjectsGetMigrateProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Method to get a migrate project.
[**migrateProjectsPatchMigrateProject**](MigrateProjectsApi.md#migrateProjectsPatchMigrateProject) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Update migrate project.
[**migrateProjectsPutMigrateProject**](MigrateProjectsApi.md#migrateProjectsPutMigrateProject) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Method to create or update a migrate project.
[**migrateProjectsRefreshMigrateProjectSummary**](MigrateProjectsApi.md#migrateProjectsRefreshMigrateProjectSummary) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/refreshSummary | Refresh the summary of the migrate project.
[**migrateProjectsRegisterTool**](MigrateProjectsApi.md#migrateProjectsRegisterTool) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/registerTool | Registers a tool with the migrate project.



## migrateProjectsDeleteMigrateProject

> migrateProjectsDeleteMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts)

Delete the migrate project

Delete the migrate project. Deleting non-existent project is a no-operation.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MigrateProjectsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.migrateProjectsDeleteMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## migrateProjectsGetMigrateProject

> MigrateProject migrateProjectsGetMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion)

Method to get a migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MigrateProjectsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
apiInstance.migrateProjectsGetMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 

### Return type

[**MigrateProject**](MigrateProject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrateProjectsPatchMigrateProject

> MigrateProject migrateProjectsPatchMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, opts)

Update migrate project.

Update a migrate project with specified name. Supports partial updates, for example only tags can be provided.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MigrateProjectsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let body = new AzureMigrateHub.MigrateProject(); // MigrateProject | Body with migrate project details.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.migrateProjectsPatchMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **body** | [**MigrateProject**](MigrateProject.md)| Body with migrate project details. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**MigrateProject**](MigrateProject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## migrateProjectsPutMigrateProject

> MigrateProject migrateProjectsPutMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, opts)

Method to create or update a migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MigrateProjectsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let body = new AzureMigrateHub.MigrateProject(); // MigrateProject | Body with migrate project details.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.migrateProjectsPutMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **body** | [**MigrateProject**](MigrateProject.md)| Body with migrate project details. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**MigrateProject**](MigrateProject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## migrateProjectsRefreshMigrateProjectSummary

> RefreshSummaryResult migrateProjectsRefreshMigrateProjectSummary(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input)

Refresh the summary of the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MigrateProjectsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let input = new AzureMigrateHub.RefreshSummaryInput(); // RefreshSummaryInput | The goal input which needs to be refreshed.
apiInstance.migrateProjectsRefreshMigrateProjectSummary(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **input** | [**RefreshSummaryInput**](RefreshSummaryInput.md)| The goal input which needs to be refreshed. | 

### Return type

[**RefreshSummaryResult**](RefreshSummaryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## migrateProjectsRegisterTool

> RegistrationResult migrateProjectsRegisterTool(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input, opts)

Registers a tool with the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MigrateProjectsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let input = new AzureMigrateHub.RegisterToolInput(); // RegisterToolInput | Input containing the name of the tool to be registered.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.migrateProjectsRegisterTool(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **input** | [**RegisterToolInput**](RegisterToolInput.md)| Input containing the name of the tool to be registered. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**RegistrationResult**](RegistrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

