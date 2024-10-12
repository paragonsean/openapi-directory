# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workbooksCreateOrUpdate**](DefaultApi.md#workbooksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} | 
[**workbooksDelete**](DefaultApi.md#workbooksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} | 
[**workbooksGet**](DefaultApi.md#workbooksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} | 
[**workbooksListByResourceGroup**](DefaultApi.md#workbooksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks | 
[**workbooksUpdate**](DefaultApi.md#workbooksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} | 



## workbooksCreateOrUpdate

> Workbook workbooksCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties)



Create a new workbook.

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
let workbookProperties = new ApplicationInsightsManagementClient.Workbook(); // Workbook | Properties that need to be specified to create a new workbook.
apiInstance.workbooksCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties, (error, data, response) => {
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
 **workbookProperties** | [**Workbook**](Workbook.md)| Properties that need to be specified to create a new workbook. | 

### Return type

[**Workbook**](Workbook.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workbooksDelete

> workbooksDelete(subscriptionId, resourceGroupName, resourceName, apiVersion)



Delete a workbook.

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
apiInstance.workbooksDelete(subscriptionId, resourceGroupName, resourceName, apiVersion, (error, data, response) => {
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


## workbooksGet

> Workbook workbooksGet(subscriptionId, resourceGroupName, resourceName, apiVersion)



Get a single workbook by its resourceName.

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
apiInstance.workbooksGet(subscriptionId, resourceGroupName, resourceName, apiVersion, (error, data, response) => {
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

[**Workbook**](Workbook.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workbooksListByResourceGroup

> WorkbooksListResult workbooksListByResourceGroup(subscriptionId, resourceGroupName, category, apiVersion, opts)



Get all Workbooks defined within a specified resource group and category.

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
let category = "category_example"; // String | Category of workbook to return.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'tags': ["null"], // [String] | Tags presents on each workbook returned.
  'canFetchContent': true // Boolean | Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks.
};
apiInstance.workbooksListByResourceGroup(subscriptionId, resourceGroupName, category, apiVersion, opts, (error, data, response) => {
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
 **category** | **String**| Category of workbook to return. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **tags** | [**[String]**](String.md)| Tags presents on each workbook returned. | [optional] 
 **canFetchContent** | **Boolean**| Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks. | [optional] 

### Return type

[**WorkbooksListResult**](WorkbooksListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workbooksUpdate

> Workbook workbooksUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties)



Updates a workbook that has already been added.

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
let workbookProperties = new ApplicationInsightsManagementClient.Workbook(); // Workbook | Properties that need to be specified to create a new workbook.
apiInstance.workbooksUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties, (error, data, response) => {
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
 **workbookProperties** | [**Workbook**](Workbook.md)| Properties that need to be specified to create a new workbook. | 

### Return type

[**Workbook**](Workbook.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

