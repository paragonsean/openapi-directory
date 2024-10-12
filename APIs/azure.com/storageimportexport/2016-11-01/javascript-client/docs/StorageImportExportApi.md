# StorageImportExport.StorageImportExportApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bitLockerKeysList**](StorageImportExportApi.md#bitLockerKeysList) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName}/listBitLockerKeys | 
[**jobsCreate**](StorageImportExportApi.md#jobsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} | 
[**jobsDelete**](StorageImportExportApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} | 
[**jobsGet**](StorageImportExportApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} | 
[**jobsListByResourceGroup**](StorageImportExportApi.md#jobsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs | 
[**jobsListBySubscription**](StorageImportExportApi.md#jobsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ImportExport/jobs | 
[**jobsUpdate**](StorageImportExportApi.md#jobsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} | 
[**locationsGet**](StorageImportExportApi.md#locationsGet) | **GET** /providers/Microsoft.ImportExport/locations/{locationName} | 
[**locationsList**](StorageImportExportApi.md#locationsList) | **GET** /providers/Microsoft.ImportExport/locations | 
[**operationsList**](StorageImportExportApi.md#operationsList) | **GET** /providers/Microsoft.ImportExport/operations | 



## bitLockerKeysList

> GetBitLockerKeysResponse bitLockerKeysList(jobName, subscriptionId, resourceGroupName, apiVersion, opts)



Returns the BitLocker Keys for all drives in the specified job.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let jobName = "jobName_example"; // String | The name of the import/export job.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.bitLockerKeysList(jobName, subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **jobName** | **String**| The name of the import/export job. | 
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**GetBitLockerKeysResponse**](GetBitLockerKeysResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsCreate

> JobResponse jobsCreate(jobName, subscriptionId, resourceGroupName, apiVersion, body, opts)



Creates a new job or updates an existing job in the specified subscription.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let jobName = "jobName_example"; // String | The name of the import/export job.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let body = new StorageImportExport.PutJobParameters(); // PutJobParameters | The parameters used for creating the job
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specifies the preferred language for the response.
  'xMsClientTenantId': "xMsClientTenantId_example" // String | The tenant ID of the client making the request.
};
apiInstance.jobsCreate(jobName, subscriptionId, resourceGroupName, apiVersion, body, opts, (error, data, response) => {
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
 **jobName** | **String**| The name of the import/export job. | 
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **body** | [**PutJobParameters**](PutJobParameters.md)| The parameters used for creating the job | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 
 **xMsClientTenantId** | **String**| The tenant ID of the client making the request. | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsDelete

> jobsDelete(jobName, subscriptionId, resourceGroupName, apiVersion, opts)



Deletes an existing job. Only jobs in the Creating or Completed states can be deleted.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let jobName = "jobName_example"; // String | The name of the import/export job.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.jobsDelete(jobName, subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **jobName** | **String**| The name of the import/export job. | 
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsGet

> JobResponse jobsGet(jobName, subscriptionId, resourceGroupName, apiVersion, opts)



Gets information about an existing job.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let jobName = "jobName_example"; // String | The name of the import/export job.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.jobsGet(jobName, subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **jobName** | **String**| The name of the import/export job. | 
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListByResourceGroup

> ListJobsResponse jobsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Returns all active and completed jobs in a resource group.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'top': 56, // Number | An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100.
  'filter': "filter_example", // String | Can be used to restrict the results to certain conditions.
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
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
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **top** | **Number**| An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100. | [optional] 
 **filter** | **String**| Can be used to restrict the results to certain conditions. | [optional] 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**ListJobsResponse**](ListJobsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsListBySubscription

> ListJobsResponse jobsListBySubscription(subscriptionId, apiVersion, opts)



Returns all active and completed jobs in a subscription.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'top': 56, // Number | An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100.
  'filter': "filter_example", // String | Can be used to restrict the results to certain conditions.
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.jobsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **top** | **Number**| An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100. | [optional] 
 **filter** | **String**| Can be used to restrict the results to certain conditions. | [optional] 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**ListJobsResponse**](ListJobsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsUpdate

> JobResponse jobsUpdate(jobName, subscriptionId, resourceGroupName, apiVersion, body, opts)



Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let jobName = "jobName_example"; // String | The name of the import/export job.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let body = new StorageImportExport.UpdateJobParameters(); // UpdateJobParameters | The parameters to update in the job
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.jobsUpdate(jobName, subscriptionId, resourceGroupName, apiVersion, body, opts, (error, data, response) => {
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
 **jobName** | **String**| The name of the import/export job. | 
 **subscriptionId** | **String**| The subscription ID for the Azure user. | 
 **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **body** | [**UpdateJobParameters**](UpdateJobParameters.md)| The parameters to update in the job | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locationsGet

> Location locationsGet(locationName, apiVersion, opts)



Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let locationName = "locationName_example"; // String | The name of the location. For example, West US or westus.
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.locationsGet(locationName, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The name of the location. For example, West US or westus. | 
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsList

> LocationsResponse locationsList(apiVersion, opts)



Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.locationsList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**LocationsResponse**](LocationsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsList

> ListOperationsResponse operationsList(apiVersion, opts)



Returns the list of operations supported by the import/export resource provider.

### Example

```javascript
import StorageImportExport from 'storage_import_export';
let defaultClient = StorageImportExport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageImportExport.StorageImportExportApi();
let apiVersion = "apiVersion_example"; // String | Specifies the API version to use for this request.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Specifies the preferred language for the response.
};
apiInstance.operationsList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Specifies the API version to use for this request. | 
 **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] 

### Return type

[**ListOperationsResponse**](ListOperationsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

