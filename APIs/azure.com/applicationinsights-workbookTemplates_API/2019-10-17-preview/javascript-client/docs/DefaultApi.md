# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workbookTemplatesCreateOrUpdate**](DefaultApi.md#workbookTemplatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} | 
[**workbookTemplatesDelete**](DefaultApi.md#workbookTemplatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} | 
[**workbookTemplatesGet**](DefaultApi.md#workbookTemplatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} | 
[**workbookTemplatesListByResourceGroup**](DefaultApi.md#workbookTemplatesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates | 
[**workbookTemplatesUpdate**](DefaultApi.md#workbookTemplatesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} | 



## workbookTemplatesCreateOrUpdate

> WorkbookTemplate workbookTemplatesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookTemplateProperties)



Create a new workbook template.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let workbookTemplateProperties = new ApplicationInsightsManagementClient.WorkbookTemplate(); // WorkbookTemplate | Properties that need to be specified to create a new workbook.
apiInstance.workbookTemplatesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookTemplateProperties, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **workbookTemplateProperties** | [**WorkbookTemplate**](WorkbookTemplate.md)| Properties that need to be specified to create a new workbook. | 

### Return type

[**WorkbookTemplate**](WorkbookTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workbookTemplatesDelete

> workbookTemplatesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion)



Delete a workbook template.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.workbookTemplatesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workbookTemplatesGet

> WorkbookTemplate workbookTemplatesGet(subscriptionId, resourceGroupName, resourceName, apiVersion)



Get a single workbook template by its resourceName.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.workbookTemplatesGet(subscriptionId, resourceGroupName, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**WorkbookTemplate**](WorkbookTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workbookTemplatesListByResourceGroup

> WorkbookTemplatesListResult workbookTemplatesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get all Workbook templates defined within a specified resource group.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.workbookTemplatesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**WorkbookTemplatesListResult**](WorkbookTemplatesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workbookTemplatesUpdate

> WorkbookTemplate workbookTemplatesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, opts)



Updates a workbook template that has already been added.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'workbookTemplateUpdateParameters': new ApplicationInsightsManagementClient.WorkbookTemplateUpdateParameters() // WorkbookTemplateUpdateParameters | Properties that need to be specified to patch a workbook template.
};
apiInstance.workbookTemplatesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **workbookTemplateUpdateParameters** | [**WorkbookTemplateUpdateParameters**](WorkbookTemplateUpdateParameters.md)| Properties that need to be specified to patch a workbook template. | [optional] 

### Return type

[**WorkbookTemplate**](WorkbookTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

