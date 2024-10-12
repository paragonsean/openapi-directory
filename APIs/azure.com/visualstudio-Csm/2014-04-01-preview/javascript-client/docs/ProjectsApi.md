# VisualStudioResourceProviderClient.ProjectsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsCreate**](ProjectsApi.md#projectsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName} | Projects_Create
[**projectsGet**](ProjectsApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName} | Projects_Get
[**projectsGetJobStatus**](ProjectsApi.md#projectsGetJobStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName}/subContainers/{subContainerName}/status | Projects_GetJobStatus
[**projectsListByResourceGroup**](ProjectsApi.md#projectsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project | Projects_ListByResourceGroup
[**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName} | Projects_Update



## projectsCreate

> ProjectResource projectsCreate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body, opts)

Projects_Create

Creates a Team Services project in the collection with the specified name. &#39;VersionControlOption&#39; and &#39;ProcessTemplateId&#39; must be specified in the resource properties. Valid values for VersionControlOption: Git, Tfvc. Valid values for ProcessTemplateId: 6B724908-EF14-45CF-84F8-768B5384DA45, ADCC42AB-9882-485E-A3ED-7678F01F66BC, 27450541-8E31-4150-9947-DC59F998FC01 (these IDs correspond to Scrum, Agile, and CMMI process templates).

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ProjectsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
let resourceName = "resourceName_example"; // String | Name of the Team Services project.
let body = new VisualStudioResourceProviderClient.ProjectResource(); // ProjectResource | The request data.
let opts = {
  'validating': "validating_example" // String | This parameter is ignored and should be set to an empty string.
};
apiInstance.projectsCreate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **rootResourceName** | **String**| Name of the Team Services account. | 
 **resourceName** | **String**| Name of the Team Services project. | 
 **body** | [**ProjectResource**](ProjectResource.md)| The request data. | 
 **validating** | **String**| This parameter is ignored and should be set to an empty string. | [optional] 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsGet

> ProjectResource projectsGet(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName)

Projects_Get

Gets the details of a Team Services project resource.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ProjectsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
let resourceName = "resourceName_example"; // String | Name of the Team Services project.
apiInstance.projectsGet(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **rootResourceName** | **String**| Name of the Team Services account. | 
 **resourceName** | **String**| Name of the Team Services project. | 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetJobStatus

> ProjectResource projectsGetJobStatus(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, subContainerName, operation, opts)

Projects_GetJobStatus

Gets the status of the project resource creation job.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ProjectsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
let resourceName = "resourceName_example"; // String | Name of the Team Services project.
let subContainerName = "subContainerName_example"; // String | This parameter should be set to the resourceName.
let operation = "operation_example"; // String | The operation type. The only supported value is 'put'.
let opts = {
  'jobId': "jobId_example" // String | The job identifier.
};
apiInstance.projectsGetJobStatus(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, subContainerName, operation, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **rootResourceName** | **String**| Name of the Team Services account. | 
 **resourceName** | **String**| Name of the Team Services project. | 
 **subContainerName** | **String**| This parameter should be set to the resourceName. | 
 **operation** | **String**| The operation type. The only supported value is &#39;put&#39;. | 
 **jobId** | **String**| The job identifier. | [optional] 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListByResourceGroup

> ProjectResourceListResult projectsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, rootResourceName)

Projects_ListByResourceGroup

Gets all Visual Studio Team Services project resources created in the specified Team Services account.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ProjectsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
apiInstance.projectsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, rootResourceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **rootResourceName** | **String**| Name of the Team Services account. | 

### Return type

[**ProjectResourceListResult**](ProjectResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsUpdate

> ProjectResource projectsUpdate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body)

Projects_Update

Updates the tags of the specified Team Services project.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ProjectsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
let resourceName = "resourceName_example"; // String | Name of the Team Services project.
let body = new VisualStudioResourceProviderClient.ProjectResource(); // ProjectResource | The request data.
apiInstance.projectsUpdate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **rootResourceName** | **String**| Name of the Team Services account. | 
 **resourceName** | **String**| Name of the Team Services project. | 
 **body** | [**ProjectResource**](ProjectResource.md)| The request data. | 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

