# StreamAnalyticsManagementClient.TransformationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transformationsCreateOrReplace**](TransformationsApi.md#transformationsCreateOrReplace) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName} | 
[**transformationsGet**](TransformationsApi.md#transformationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName} | 
[**transformationsUpdate**](TransformationsApi.md#transformationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName} | 



## transformationsCreateOrReplace

> Transformation transformationsCreateOrReplace(apiVersion, subscriptionId, resourceGroupName, jobName, transformationName, transformation, opts)



Creates a transformation or replaces an already existing transformation under an existing streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.TransformationsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let transformationName = "transformationName_example"; // String | The name of the transformation.
let transformation = new StreamAnalyticsManagementClient.Transformation(); // Transformation | The definition of the transformation that will be used to create a new transformation or replace the existing one under the streaming job.
let opts = {
  'ifMatch': "ifMatch_example", // String | The ETag of the transformation. Omit this value to always overwrite the current transformation. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new transformation to be created, but to prevent updating an existing transformation. Other values will result in a 412 Pre-condition Failed response.
};
apiInstance.transformationsCreateOrReplace(apiVersion, subscriptionId, resourceGroupName, jobName, transformationName, transformation, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **jobName** | **String**| The name of the streaming job. | 
 **transformationName** | **String**| The name of the transformation. | 
 **transformation** | [**Transformation**](Transformation.md)| The definition of the transformation that will be used to create a new transformation or replace the existing one under the streaming job. | 
 **ifMatch** | **String**| The ETag of the transformation. Omit this value to always overwrite the current transformation. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new transformation to be created, but to prevent updating an existing transformation. Other values will result in a 412 Pre-condition Failed response. | [optional] 

### Return type

[**Transformation**](Transformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transformationsGet

> Transformation transformationsGet(apiVersion, subscriptionId, resourceGroupName, jobName, transformationName)



Gets details about the specified transformation.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.TransformationsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let transformationName = "transformationName_example"; // String | The name of the transformation.
apiInstance.transformationsGet(apiVersion, subscriptionId, resourceGroupName, jobName, transformationName, (error, data, response) => {
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
 **subscriptionId** | **String**| GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **jobName** | **String**| The name of the streaming job. | 
 **transformationName** | **String**| The name of the transformation. | 

### Return type

[**Transformation**](Transformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformationsUpdate

> Transformation transformationsUpdate(apiVersion, subscriptionId, resourceGroupName, jobName, transformationName, transformation, opts)



Updates an existing transformation under an existing streaming job. This can be used to partially update (ie. update one or two properties) a transformation without affecting the rest the job or transformation definition.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.TransformationsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let transformationName = "transformationName_example"; // String | The name of the transformation.
let transformation = new StreamAnalyticsManagementClient.Transformation(); // Transformation | A Transformation object. The properties specified here will overwrite the corresponding properties in the existing transformation (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing transformation will remain the same and not change as a result of this PATCH operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the transformation. Omit this value to always overwrite the current transformation. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
};
apiInstance.transformationsUpdate(apiVersion, subscriptionId, resourceGroupName, jobName, transformationName, transformation, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **jobName** | **String**| The name of the streaming job. | 
 **transformationName** | **String**| The name of the transformation. | 
 **transformation** | [**Transformation**](Transformation.md)| A Transformation object. The properties specified here will overwrite the corresponding properties in the existing transformation (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing transformation will remain the same and not change as a result of this PATCH operation. | 
 **ifMatch** | **String**| The ETag of the transformation. Omit this value to always overwrite the current transformation. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 

### Return type

[**Transformation**](Transformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

