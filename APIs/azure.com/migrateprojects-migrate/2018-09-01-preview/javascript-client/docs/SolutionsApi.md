# AzureMigrateHub.SolutionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**solutionsCleanupSolutionData**](SolutionsApi.md#solutionsCleanupSolutionData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}/cleanupData | Cleanup the solution data in the migrate project.
[**solutionsDeleteSolution**](SolutionsApi.md#solutionsDeleteSolution) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Delete the solution
[**solutionsEnumerateSolutions**](SolutionsApi.md#solutionsEnumerateSolutions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions | Gets the list of solutions in the migrate project.
[**solutionsGetConfig**](SolutionsApi.md#solutionsGetConfig) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}/getConfig | Gets the config for the solution in the migrate project.
[**solutionsGetSolution**](SolutionsApi.md#solutionsGetSolution) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Gets a solution in the migrate project.
[**solutionsPatchSolution**](SolutionsApi.md#solutionsPatchSolution) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Update solution.
[**solutionsPutSolution**](SolutionsApi.md#solutionsPutSolution) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Creates a solution in the migrate project.



## solutionsCleanupSolutionData

> solutionsCleanupSolutionData(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion)

Cleanup the solution data in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
apiInstance.solutionsCleanupSolutionData(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, (error, data, response) => {
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
 **solutionName** | **String**| Unique name of a migration solution within a migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## solutionsDeleteSolution

> solutionsDeleteSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, opts)

Delete the solution

Delete the solution. Deleting non-existent project is a no-operation.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.solutionsDeleteSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, opts, (error, data, response) => {
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
 **solutionName** | **String**| Unique name of a migration solution within a migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## solutionsEnumerateSolutions

> SolutionsCollection solutionsEnumerateSolutions(subscriptionId, resourceGroupName, migrateProjectName, apiVersion)

Gets the list of solutions in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
apiInstance.solutionsEnumerateSolutions(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, (error, data, response) => {
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

[**SolutionsCollection**](SolutionsCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## solutionsGetConfig

> SolutionConfig solutionsGetConfig(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion)

Gets the config for the solution in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
apiInstance.solutionsGetConfig(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, (error, data, response) => {
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
 **solutionName** | **String**| Unique name of a migration solution within a migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 

### Return type

[**SolutionConfig**](SolutionConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## solutionsGetSolution

> Solution solutionsGetSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion)

Gets a solution in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
apiInstance.solutionsGetSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, (error, data, response) => {
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
 **solutionName** | **String**| Unique name of a migration solution within a migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 

### Return type

[**Solution**](Solution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## solutionsPatchSolution

> Solution solutionsPatchSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput)

Update solution.

Update a solution with specified name. Supports partial updates, for example only tags can be provided.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let solutionInput = new AzureMigrateHub.Solution(); // Solution | The input for the solution.
apiInstance.solutionsPatchSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput, (error, data, response) => {
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
 **solutionName** | **String**| Unique name of a migration solution within a migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **solutionInput** | [**Solution**](Solution.md)| The input for the solution. | 

### Return type

[**Solution**](Solution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## solutionsPutSolution

> Solution solutionsPutSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput)

Creates a solution in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.SolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let solutionInput = new AzureMigrateHub.Solution(); // Solution | The input for the solution.
apiInstance.solutionsPutSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput, (error, data, response) => {
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
 **solutionName** | **String**| Unique name of a migration solution within a migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **solutionInput** | [**Solution**](Solution.md)| The input for the solution. | 

### Return type

[**Solution**](Solution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

