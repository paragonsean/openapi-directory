# ComputeDiskAdminManagementClient.DiskMigrationJobsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diskMigrationJobsCancel**](DiskMigrationJobsApi.md#diskMigrationJobsCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migrationId}/Cancel | 
[**diskMigrationJobsCreate**](DiskMigrationJobsApi.md#diskMigrationJobsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migrationId} | 
[**diskMigrationJobsGet**](DiskMigrationJobsApi.md#diskMigrationJobsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migrationId} | 
[**diskMigrationJobsList**](DiskMigrationJobsApi.md#diskMigrationJobsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs | 



## diskMigrationJobsCancel

> DiskMigrationJobsGet200Response diskMigrationJobsCancel(subscriptionId, location, migrationId, apiVersion)



Cancel a disk migration job.

### Example

```javascript
import ComputeDiskAdminManagementClient from 'compute_disk_admin_management_client';
let defaultClient = ComputeDiskAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeDiskAdminManagementClient.DiskMigrationJobsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let migrationId = "migrationId_example"; // String | The migration job guid name.
let apiVersion = "'2018-07-30-preview'"; // String | Client API Version.
apiInstance.diskMigrationJobsCancel(subscriptionId, location, migrationId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **migrationId** | **String**| The migration job guid name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2018-07-30-preview&#39;]

### Return type

[**DiskMigrationJobsGet200Response**](DiskMigrationJobsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diskMigrationJobsCreate

> DiskMigrationJobsGet200Response diskMigrationJobsCreate(subscriptionId, location, migrationId, targetShare, apiVersion, disks)



Create a disk migration job.

### Example

```javascript
import ComputeDiskAdminManagementClient from 'compute_disk_admin_management_client';
let defaultClient = ComputeDiskAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeDiskAdminManagementClient.DiskMigrationJobsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let migrationId = "migrationId_example"; // String | The migration job guid name.
let targetShare = "targetShare_example"; // String | The target share name.
let apiVersion = "'2018-07-30-preview'"; // String | Client API Version.
let disks = [new ComputeDiskAdminManagementClient.DiskMigrationJobsCreateRequestInner()]; // [DiskMigrationJobsCreateRequestInner] | The parameters of disk list.
apiInstance.diskMigrationJobsCreate(subscriptionId, location, migrationId, targetShare, apiVersion, disks, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **migrationId** | **String**| The migration job guid name. | 
 **targetShare** | **String**| The target share name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2018-07-30-preview&#39;]
 **disks** | [**[DiskMigrationJobsCreateRequestInner]**](DiskMigrationJobsCreateRequestInner.md)| The parameters of disk list. | 

### Return type

[**DiskMigrationJobsGet200Response**](DiskMigrationJobsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## diskMigrationJobsGet

> DiskMigrationJobsGet200Response diskMigrationJobsGet(subscriptionId, location, migrationId, apiVersion)



Returns the requested disk migration job.

### Example

```javascript
import ComputeDiskAdminManagementClient from 'compute_disk_admin_management_client';
let defaultClient = ComputeDiskAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeDiskAdminManagementClient.DiskMigrationJobsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let migrationId = "migrationId_example"; // String | The migration job guid name.
let apiVersion = "'2018-07-30-preview'"; // String | Client API Version.
apiInstance.diskMigrationJobsGet(subscriptionId, location, migrationId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **migrationId** | **String**| The migration job guid name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2018-07-30-preview&#39;]

### Return type

[**DiskMigrationJobsGet200Response**](DiskMigrationJobsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diskMigrationJobsList

> DiskMigrationJobsList200Response diskMigrationJobsList(subscriptionId, location, apiVersion, opts)



Returns a list of disk migration jobs.

### Example

```javascript
import ComputeDiskAdminManagementClient from 'compute_disk_admin_management_client';
let defaultClient = ComputeDiskAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeDiskAdminManagementClient.DiskMigrationJobsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let apiVersion = "'2018-07-30-preview'"; // String | Client API Version.
let opts = {
  'status': "status_example" // String | The parameters of disk migration job status.
};
apiInstance.diskMigrationJobsList(subscriptionId, location, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2018-07-30-preview&#39;]
 **status** | **String**| The parameters of disk migration job status. | [optional] 

### Return type

[**DiskMigrationJobsList200Response**](DiskMigrationJobsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

