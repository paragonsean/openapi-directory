# SchedulerManagementClient.JobCollectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobCollectionsCreateOrUpdate**](JobCollectionsApi.md#jobCollectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} | 
[**jobCollectionsDelete**](JobCollectionsApi.md#jobCollectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} | 
[**jobCollectionsDisable**](JobCollectionsApi.md#jobCollectionsDisable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/disable | 
[**jobCollectionsEnable**](JobCollectionsApi.md#jobCollectionsEnable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/enable | 
[**jobCollectionsGet**](JobCollectionsApi.md#jobCollectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} | 
[**jobCollectionsListByResourceGroup**](JobCollectionsApi.md#jobCollectionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections | 
[**jobCollectionsListBySubscription**](JobCollectionsApi.md#jobCollectionsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Scheduler/jobCollections | 
[**jobCollectionsPatch**](JobCollectionsApi.md#jobCollectionsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} | 



## jobCollectionsCreateOrUpdate

> JobCollectionDefinition jobCollectionsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection)



Provisions a new job collection or updates an existing job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
let jobCollection = new SchedulerManagementClient.JobCollectionDefinition(); // JobCollectionDefinition | The job collection definition.
apiInstance.jobCollectionsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 
 **jobCollection** | [**JobCollectionDefinition**](JobCollectionDefinition.md)| The job collection definition. | 

### Return type

[**JobCollectionDefinition**](JobCollectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## jobCollectionsDelete

> jobCollectionsDelete(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Deletes a job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobCollectionsDelete(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobCollectionsDisable

> jobCollectionsDisable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Disables all of the jobs in the job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobCollectionsDisable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobCollectionsEnable

> jobCollectionsEnable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Enables all of the jobs in the job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobCollectionsEnable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobCollectionsGet

> JobCollectionDefinition jobCollectionsGet(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Gets a job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobCollectionsGet(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**JobCollectionDefinition**](JobCollectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobCollectionsListByResourceGroup

> JobCollectionListResult jobCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Gets all job collections under specified resource group.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**JobCollectionListResult**](JobCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobCollectionsListBySubscription

> JobCollectionListResult jobCollectionsListBySubscription(subscriptionId, apiVersion)



Gets all job collections under specified subscription.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobCollectionsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**JobCollectionListResult**](JobCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobCollectionsPatch

> JobCollectionDefinition jobCollectionsPatch(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection)



Patches an existing job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';
let defaultClient = SchedulerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SchedulerManagementClient.JobCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
let jobCollection = new SchedulerManagementClient.JobCollectionDefinition(); // JobCollectionDefinition | The job collection definition.
apiInstance.jobCollectionsPatch(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 
 **jobCollection** | [**JobCollectionDefinition**](JobCollectionDefinition.md)| The job collection definition. | 

### Return type

[**JobCollectionDefinition**](JobCollectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

