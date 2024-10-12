# StreamAnalyticsManagementClient.FunctionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**functionsCreateOrReplace**](FunctionsApi.md#functionsCreateOrReplace) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName} | 
[**functionsDelete**](FunctionsApi.md#functionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName} | 
[**functionsGet**](FunctionsApi.md#functionsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName} | 
[**functionsListByStreamingJob**](FunctionsApi.md#functionsListByStreamingJob) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions | 
[**functionsRetrieveDefaultDefinition**](FunctionsApi.md#functionsRetrieveDefaultDefinition) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}/RetrieveDefaultDefinition | 
[**functionsTest**](FunctionsApi.md#functionsTest) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}/test | 
[**functionsUpdate**](FunctionsApi.md#functionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName} | 



## functionsCreateOrReplace

> Function functionsCreateOrReplace(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, _function, opts)



Creates a function or replaces an already existing function under an existing streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let functionName = "functionName_example"; // String | The name of the function.
let _function = new StreamAnalyticsManagementClient.Function(); // Function | The definition of the function that will be used to create a new function or replace the existing one under the streaming job.
let opts = {
  'ifMatch': "ifMatch_example", // String | The ETag of the function. Omit this value to always overwrite the current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new function to be created, but to prevent updating an existing function. Other values will result in a 412 Pre-condition Failed response.
};
apiInstance.functionsCreateOrReplace(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, _function, opts, (error, data, response) => {
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
 **functionName** | **String**| The name of the function. | 
 **_function** | [**Function**](Function.md)| The definition of the function that will be used to create a new function or replace the existing one under the streaming job. | 
 **ifMatch** | **String**| The ETag of the function. Omit this value to always overwrite the current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new function to be created, but to prevent updating an existing function. Other values will result in a 412 Pre-condition Failed response. | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionsDelete

> functionsDelete(apiVersion, subscriptionId, resourceGroupName, jobName, functionName)



Deletes a function from the streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let functionName = "functionName_example"; // String | The name of the function.
apiInstance.functionsDelete(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, (error, data, response) => {
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
 **functionName** | **String**| The name of the function. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## functionsGet

> Function functionsGet(apiVersion, subscriptionId, resourceGroupName, jobName, functionName)



Gets details about the specified function.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let functionName = "functionName_example"; // String | The name of the function.
apiInstance.functionsGet(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, (error, data, response) => {
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
 **functionName** | **String**| The name of the function. | 

### Return type

[**Function**](Function.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsListByStreamingJob

> FunctionListResult functionsListByStreamingJob(apiVersion, subscriptionId, resourceGroupName, jobName, opts)



Lists all of the functions under the specified streaming job.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let opts = {
  'select': "select_example" // String | The $select OData query parameter. This is a comma-separated list of structural properties to include in the response, or \"*\" to include all properties. By default, all properties are returned except diagnostics. Currently only accepts '*' as a valid value.
};
apiInstance.functionsListByStreamingJob(apiVersion, subscriptionId, resourceGroupName, jobName, opts, (error, data, response) => {
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

[**FunctionListResult**](FunctionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsRetrieveDefaultDefinition

> Function functionsRetrieveDefaultDefinition(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, opts)



Retrieves the default definition of a function based on the parameters specified.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let functionName = "functionName_example"; // String | The name of the function.
let opts = {
  'functionRetrieveDefaultDefinitionParameters': new StreamAnalyticsManagementClient.FunctionRetrieveDefaultDefinitionParameters() // FunctionRetrieveDefaultDefinitionParameters | Parameters used to specify the type of function to retrieve the default definition for.
};
apiInstance.functionsRetrieveDefaultDefinition(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, opts, (error, data, response) => {
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
 **functionName** | **String**| The name of the function. | 
 **functionRetrieveDefaultDefinitionParameters** | [**FunctionRetrieveDefaultDefinitionParameters**](FunctionRetrieveDefaultDefinitionParameters.md)| Parameters used to specify the type of function to retrieve the default definition for. | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionsTest

> FunctionsTest200Response functionsTest(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, opts)



Tests if the information provided for a function is valid. This can range from testing the connection to the underlying web service behind the function or making sure the function code provided is syntactically correct.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let functionName = "functionName_example"; // String | The name of the function.
let opts = {
  '_function': new StreamAnalyticsManagementClient.Function() // Function | If the function specified does not already exist, this parameter must contain the full function definition intended to be tested. If the function specified already exists, this parameter can be left null to test the existing function as is or if specified, the properties specified will overwrite the corresponding properties in the existing function (exactly like a PATCH operation) and the resulting function will be tested.
};
apiInstance.functionsTest(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, opts, (error, data, response) => {
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
 **functionName** | **String**| The name of the function. | 
 **_function** | [**Function**](Function.md)| If the function specified does not already exist, this parameter must contain the full function definition intended to be tested. If the function specified already exists, this parameter can be left null to test the existing function as is or if specified, the properties specified will overwrite the corresponding properties in the existing function (exactly like a PATCH operation) and the resulting function will be tested. | [optional] 

### Return type

[**FunctionsTest200Response**](FunctionsTest200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionsUpdate

> Function functionsUpdate(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, _function, opts)



Updates an existing function under an existing streaming job. This can be used to partially update (ie. update one or two properties) a function without affecting the rest the job or function definition.

### Example

```javascript
import StreamAnalyticsManagementClient from 'stream_analytics_management_client';
let defaultClient = StreamAnalyticsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StreamAnalyticsManagementClient.FunctionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let jobName = "jobName_example"; // String | The name of the streaming job.
let functionName = "functionName_example"; // String | The name of the function.
let _function = new StreamAnalyticsManagementClient.Function(); // Function | A function object. The properties specified here will overwrite the corresponding properties in the existing function (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing function will remain the same and not change as a result of this PATCH operation.
let opts = {
  'ifMatch': "ifMatch_example" // String | The ETag of the function. Omit this value to always overwrite the current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
};
apiInstance.functionsUpdate(apiVersion, subscriptionId, resourceGroupName, jobName, functionName, _function, opts, (error, data, response) => {
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
 **functionName** | **String**| The name of the function. | 
 **_function** | [**Function**](Function.md)| A function object. The properties specified here will overwrite the corresponding properties in the existing function (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing function will remain the same and not change as a result of this PATCH operation. | 
 **ifMatch** | **String**| The ETag of the function. Omit this value to always overwrite the current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

