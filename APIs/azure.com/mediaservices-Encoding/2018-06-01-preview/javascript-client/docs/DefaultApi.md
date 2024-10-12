# AzureMediaServices.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsCancelJob**](DefaultApi.md#jobsCancelJob) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}/cancelJob | Cancel Job
[**jobsCreate**](DefaultApi.md#jobsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName} | Create Job
[**jobsDelete**](DefaultApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName} | Delete Job
[**jobsGet**](DefaultApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName} | Get Job
[**jobsList**](DefaultApi.md#jobsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs | List Jobs
[**transformsCreateOrUpdate**](DefaultApi.md#transformsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Create or Update Transform
[**transformsDelete**](DefaultApi.md#transformsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Delete Transform
[**transformsGet**](DefaultApi.md#transformsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Get Transform
[**transformsList**](DefaultApi.md#transformsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms | List Transforms
[**transformsUpdate**](DefaultApi.md#transformsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Update Transform



## jobsCancelJob

> jobsCancelJob(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion)

Cancel Job

Cancel a Job.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let jobName = "jobName_example"; // String | The Job name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.jobsCancelJob(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **jobName** | **String**| The Job name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsCreate

> Job jobsCreate(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, parameters)

Create Job

Creates a Job.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let jobName = "jobName_example"; // String | The Job name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.Job(); // Job | The request parameters
apiInstance.jobsCreate(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **jobName** | **String**| The Job name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**Job**](Job.md)| The request parameters | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsDelete

> jobsDelete(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion)

Delete Job

Deletes a Job.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let jobName = "jobName_example"; // String | The Job name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.jobsDelete(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **jobName** | **String**| The Job name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsGet

> Job jobsGet(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion)

Get Job

Gets a Job.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let jobName = "jobName_example"; // String | The Job name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.jobsGet(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **jobName** | **String**| The Job name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsList

> JobCollection jobsList(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, opts)

List Jobs

Lists all of the Jobs for the Transform.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | Restricts the set of items returned.
  'top': 56, // Number | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
  'skip': 56 // Number | Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1.
};
apiInstance.jobsList(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **filter** | **String**| Restricts the set of items returned. | [optional] 
 **top** | **Number**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] 
 **skip** | **Number**| Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1. | [optional] 

### Return type

[**JobCollection**](JobCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformsCreateOrUpdate

> Transform transformsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters)

Create or Update Transform

Creates or updates a new Transform.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.Transform(); // Transform | The request parameters
apiInstance.transformsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**Transform**](Transform.md)| The request parameters | 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transformsDelete

> transformsDelete(subscriptionId, resourceGroupName, accountName, transformName, apiVersion)

Delete Transform

Deletes a Transform.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.transformsDelete(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformsGet

> Transform transformsGet(subscriptionId, resourceGroupName, accountName, transformName, apiVersion)

Get Transform

Gets a Transform.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.transformsGet(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformsList

> TransformCollection transformsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List Transforms

Lists the Transforms in the account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | Restricts the set of items returned.
  'top': 56, // Number | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
  'skip': 56 // Number | Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1.
};
apiInstance.transformsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **filter** | **String**| Restricts the set of items returned. | [optional] 
 **top** | **Number**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] 
 **skip** | **Number**| Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1. | [optional] 

### Return type

[**TransformCollection**](TransformCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformsUpdate

> Transform transformsUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters)

Update Transform

Updates a Transform.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let transformName = "transformName_example"; // String | The Transform name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.Transform(); // Transform | The request parameters
apiInstance.transformsUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **transformName** | **String**| The Transform name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**Transform**](Transform.md)| The request parameters | 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

