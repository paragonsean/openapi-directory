# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotationsCreate**](DefaultApi.md#annotationsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations | 
[**annotationsDelete**](DefaultApi.md#annotationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations/{annotationId} | 
[**annotationsGet**](DefaultApi.md#annotationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations/{annotationId} | 
[**annotationsList**](DefaultApi.md#annotationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations | 



## annotationsCreate

> [Annotation] annotationsCreate(resourceGroupName, apiVersion, subscriptionId, resourceName, annotationProperties)



Create an Annotation of an Application Insights component.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let annotationProperties = new ApplicationInsightsManagementClient.Annotation(); // Annotation | Properties that need to be specified to create an annotation of a Application Insights component.
apiInstance.annotationsCreate(resourceGroupName, apiVersion, subscriptionId, resourceName, annotationProperties, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **annotationProperties** | [**Annotation**](Annotation.md)| Properties that need to be specified to create an annotation of a Application Insights component. | 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## annotationsDelete

> annotationsDelete(resourceGroupName, apiVersion, subscriptionId, resourceName, annotationId)



Delete an Annotation of an Application Insights component.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let annotationId = "annotationId_example"; // String | The unique annotation ID. This is unique within a Application Insights component.
apiInstance.annotationsDelete(resourceGroupName, apiVersion, subscriptionId, resourceName, annotationId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **annotationId** | **String**| The unique annotation ID. This is unique within a Application Insights component. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## annotationsGet

> [Annotation] annotationsGet(resourceGroupName, apiVersion, subscriptionId, resourceName, annotationId)



Get the annotation for given id.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let annotationId = "annotationId_example"; // String | The unique annotation ID. This is unique within a Application Insights component.
apiInstance.annotationsGet(resourceGroupName, apiVersion, subscriptionId, resourceName, annotationId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **annotationId** | **String**| The unique annotation ID. This is unique within a Application Insights component. | 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationsList

> AnnotationsListResult annotationsList(resourceGroupName, apiVersion, subscriptionId, resourceName, start, end)



Gets the list of annotations for a component for given time range

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let start = "start_example"; // String | The start time to query from for annotations, cannot be older than 90 days from current date.
let end = "end_example"; // String | The end time to query for annotations.
apiInstance.annotationsList(resourceGroupName, apiVersion, subscriptionId, resourceName, start, end, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **start** | **String**| The start time to query from for annotations, cannot be older than 90 days from current date. | 
 **end** | **String**| The end time to query for annotations. | 

### Return type

[**AnnotationsListResult**](AnnotationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

