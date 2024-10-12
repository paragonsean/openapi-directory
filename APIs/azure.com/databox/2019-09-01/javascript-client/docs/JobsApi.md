# DataBoxManagementClient.JobsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsBookShipmentPickUp**](JobsApi.md#jobsBookShipmentPickUp) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/bookShipmentPickUp | 
[**jobsCancel**](JobsApi.md#jobsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/cancel | 
[**jobsCreate**](JobsApi.md#jobsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName} | 
[**jobsDelete**](JobsApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName} | 
[**jobsGet**](JobsApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName} | 
[**jobsList**](JobsApi.md#jobsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/jobs | 
[**jobsListByResourceGroup**](JobsApi.md#jobsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs | 
[**jobsListCredentials**](JobsApi.md#jobsListCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/listCredentials | 
[**jobsUpdate**](JobsApi.md#jobsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName} | 



## jobsBookShipmentPickUp

> ShipmentPickUpResponse jobsBookShipmentPickUp(subscriptionId, resourceGroupName, jobName, apiVersion, shipmentPickUpRequest)



Book shipment pick up.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let shipmentPickUpRequest = new DataBoxManagementClient.ShipmentPickUpRequest(); // ShipmentPickUpRequest | Details of shipment pick up request.
apiInstance.jobsBookShipmentPickUp(subscriptionId, resourceGroupName, jobName, apiVersion, shipmentPickUpRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **shipmentPickUpRequest** | [**ShipmentPickUpRequest**](ShipmentPickUpRequest.md)| Details of shipment pick up request. | 

### Return type

[**ShipmentPickUpResponse**](ShipmentPickUpResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsCancel

> jobsCancel(subscriptionId, resourceGroupName, jobName, apiVersion, cancellationReason)



CancelJob.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let cancellationReason = new DataBoxManagementClient.CancellationReason(); // CancellationReason | Reason for cancellation.
apiInstance.jobsCancel(subscriptionId, resourceGroupName, jobName, apiVersion, cancellationReason, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **cancellationReason** | [**CancellationReason**](CancellationReason.md)| Reason for cancellation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsCreate

> JobResource jobsCreate(subscriptionId, resourceGroupName, jobName, apiVersion, jobResource)



Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let jobResource = new DataBoxManagementClient.JobResource(); // JobResource | Job details from request body.
apiInstance.jobsCreate(subscriptionId, resourceGroupName, jobName, apiVersion, jobResource, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **jobResource** | [**JobResource**](JobResource.md)| Job details from request body. | 

### Return type

[**JobResource**](JobResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsDelete

> jobsDelete(subscriptionId, resourceGroupName, jobName, apiVersion)



Deletes a job.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.jobsDelete(subscriptionId, resourceGroupName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsGet

> JobResource jobsGet(subscriptionId, resourceGroupName, jobName, apiVersion, opts)



Gets information about the specified job.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'expand': "expand_example" // String | $expand is supported on details parameter for job, which provides details on the job stages.
};
apiInstance.jobsGet(subscriptionId, resourceGroupName, jobName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **expand** | **String**| $expand is supported on details parameter for job, which provides details on the job stages. | [optional] 

### Return type

[**JobResource**](JobResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsList

> JobResourceList jobsList(subscriptionId, apiVersion, opts)



Lists all the jobs available under the subscription.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'skipToken': "skipToken_example" // String | $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.
};
apiInstance.jobsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **apiVersion** | **String**| The API Version | 
 **skipToken** | **String**| $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs. | [optional] 

### Return type

[**JobResourceList**](JobResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListByResourceGroup

> JobResourceList jobsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Lists all the jobs available under the given resource group.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let apiVersion = "apiVersion_example"; // String | The API Version
let opts = {
  'skipToken': "skipToken_example" // String | $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.
};
apiInstance.jobsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **apiVersion** | **String**| The API Version | 
 **skipToken** | **String**| $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs. | [optional] 

### Return type

[**JobResourceList**](JobResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListCredentials

> UnencryptedCredentialsList jobsListCredentials(subscriptionId, resourceGroupName, jobName, apiVersion)



This method gets the unencrypted secrets related to the job.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.jobsListCredentials(subscriptionId, resourceGroupName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

[**UnencryptedCredentialsList**](UnencryptedCredentialsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsUpdate

> JobResource jobsUpdate(subscriptionId, resourceGroupName, jobName, apiVersion, jobResourceUpdateParameter, opts)



Updates the properties of an existing job.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let jobName = "jobName_example"; // String | The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
let jobResourceUpdateParameter = new DataBoxManagementClient.JobResourceUpdateParameter(); // JobResourceUpdateParameter | Job update parameters from request body.
let opts = {
  'ifMatch': "ifMatch_example" // String | Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value.
};
apiInstance.jobsUpdate(subscriptionId, resourceGroupName, jobName, apiVersion, jobResourceUpdateParameter, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **jobName** | **String**| The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 
 **jobResourceUpdateParameter** | [**JobResourceUpdateParameter**](JobResourceUpdateParameter.md)| Job update parameters from request body. | 
 **ifMatch** | **String**| Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value. | [optional] 

### Return type

[**JobResource**](JobResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

