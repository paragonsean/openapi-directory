# StreamAnalyticsManagementClient.InputsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inputsCreateOrReplace**](InputsApi.md#inputsCreateOrReplace) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/inputs/{inputName} | 
[**inputsDelete**](InputsApi.md#inputsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/inputs/{inputName} | 
[**inputsGet**](InputsApi.md#inputsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/inputs/{inputName} | 
[**inputsListByStreamingJob**](InputsApi.md#inputsListByStreamingJob) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/inputs | 
[**inputsTest**](InputsApi.md#inputsTest) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/inputs/{inputName}/test | 
[**inputsUpdate**](InputsApi.md#inputsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/inputs/{inputName} | 



## inputsCreateOrReplace

> Input inputsCreateOrReplace(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, input, opts)



Creates an input or replaces an already existing input under an existing streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.InputsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let inputName = "inputName_example"; // String | The name of the input.
let input = new StreamAnalyticsManagementClient.Input(); // Input | The definition of the input that will be used to create a new input or replace the existing one under the streaming job.
let opts = {
  'ifMatch': "ifMatch_example", // String | The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new input to be created, but to prevent updating an existing input. Other values will result in a 412 Pre-condition Failed response.
};
apiInstance.inputsCreateOrReplace(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, input, opts, (error, data, response) => {
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
 **inputName** | **String**| The name of the input. | 
 **input** | [**Input**](Input.md)| The definition of the input that will be used to create a new input or replace the existing one under the streaming job. | 
 **ifMatch** | **String**| The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new input to be created, but to prevent updating an existing input. Other values will result in a 412 Pre-condition Failed response. | [optional] 

### Return type

[**Input**](Input.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inputsDelete

> inputsDelete(apiVersion, subscriptionId, resourceGroupName, jobName, inputName)



Deletes an input from the streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.InputsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let inputName = "inputName_example"; // String | The name of the input.
apiInstance.inputsDelete(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **jobName** | **String**| The name of the streaming job. | 
 **inputName** | **String**| The name of the input. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inputsGet

> Input inputsGet(apiVersion, subscriptionId, resourceGroupName, jobName, inputName)



Gets details about the specified input.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.InputsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let inputName = "inputName_example"; // String | The name of the input.
apiInstance.inputsGet(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, (error, data, response) => {
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
 **inputName** | **String**| The name of the input. | 

### Return type

[**Input**](Input.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inputsListByStreamingJob

> InputListResult inputsListByStreamingJob(apiVersion, subscriptionId, resourceGroupName, jobName, opts)



Lists all of the inputs under the specified streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.InputsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let opts = {
  'select': "select_example" // String | The $select OData query parameter. This is a comma-separated list of structural properties to include in the response, or \"*\" to include all properties. By default, all properties are returned except diagnostics. Currently only accepts '*' as a valid value.
};
apiInstance.inputsListByStreamingJob(apiVersion, subscriptionId, resourceGroupName, jobName, opts, (error, data, response) => {
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
 **select** | **String**| The $select OData query parameter. This is a comma-separated list of structural properties to include in the response, or \&quot;*\&quot; to include all properties. By default, all properties are returned except diagnostics. Currently only accepts &#39;*&#39; as a valid value. | [optional] 

### Return type

[**InputListResult**](InputListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inputsTest

> ResourceTestStatus inputsTest(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, opts)



Tests whether an input’s datasource is reachable and usable by the Azure Stream Analytics service.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.InputsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let inputName = "inputName_example"; // String | The name of the input.
let opts = {
  'input': new StreamAnalyticsManagementClient.Input() // Input | If the input specified does not already exist, this parameter must contain the full input definition intended to be tested. If the input specified already exists, this parameter can be left null to test the existing input as is or if specified, the properties specified will overwrite the corresponding properties in the existing input (exactly like a PATCH operation) and the resulting input will be tested.
};
apiInstance.inputsTest(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, opts, (error, data, response) => {
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
 **inputName** | **String**| The name of the input. | 
 **input** | [**Input**](Input.md)| If the input specified does not already exist, this parameter must contain the full input definition intended to be tested. If the input specified already exists, this parameter can be left null to test the existing input as is or if specified, the properties specified will overwrite the corresponding properties in the existing input (exactly like a PATCH operation) and the resulting input will be tested. | [optional] 

### Return type

[**ResourceTestStatus**](ResourceTestStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inputsUpdate

> Input inputsUpdate(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, input, opts)



Updates an existing input under an existing streaming job. This can be used to partially update (ie. update one or two properties) an input without affecting the rest the job or input definition.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.InputsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let inputName = "inputName_example"; // String | The name of the input.
let input = new StreamAnalyticsManagementClient.Input(); // Input | An Input object. The properties specified here will overwrite the corresponding properties in the existing input (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing input will remain the same and not change as a result of this PATCH operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
};
apiInstance.inputsUpdate(apiVersion, subscriptionId, resourceGroupName, jobName, inputName, input, opts, (error, data, response) => {
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
 **inputName** | **String**| The name of the input. | 
 **input** | [**Input**](Input.md)| An Input object. The properties specified here will overwrite the corresponding properties in the existing input (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing input will remain the same and not change as a result of this PATCH operation. | 
 **ifMatch** | **String**| The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 

### Return type

[**Input**](Input.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

