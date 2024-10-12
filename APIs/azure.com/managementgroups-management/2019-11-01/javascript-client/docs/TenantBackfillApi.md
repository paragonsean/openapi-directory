# ManagementGroups.TenantBackfillApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**startTenantBackfill**](TenantBackfillApi.md#startTenantBackfill) | **POST** /providers/Microsoft.Management/startTenantBackfill | 
[**tenantBackfillStatus**](TenantBackfillApi.md#tenantBackfillStatus) | **POST** /providers/Microsoft.Management/tenantBackfillStatus | 



## startTenantBackfill

> TenantBackfillStatusResult startTenantBackfill(apiVersion)



Starts backfilling subscriptions for the Tenant.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.TenantBackfillApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
apiInstance.startTenantBackfill(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 

### Return type

[**TenantBackfillStatusResult**](TenantBackfillStatusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenantBackfillStatus

> TenantBackfillStatusResult tenantBackfillStatus(apiVersion)



Gets tenant backfill status

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.TenantBackfillApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
apiInstance.tenantBackfillStatus(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 

### Return type

[**TenantBackfillStatusResult**](TenantBackfillStatusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

