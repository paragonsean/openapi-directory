# ComputeAdminClient.QuotasApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotasCreateOrUpdate**](QuotasApi.md#quotasCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quotaName} | Creates or Updates a Compute Quota.
[**quotasDelete**](QuotasApi.md#quotasDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quotaName} | Deletes specified Compute quota
[**quotasGet**](QuotasApi.md#quotasGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quotaName} | Returns the requested Compute quota.
[**quotasList**](QuotasApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas | Lists all Compute quotas.



## quotasCreateOrUpdate

> QuotasGet200Response quotasCreateOrUpdate(subscriptionId, location, quotaName, apiVersion, newQuota)

Creates or Updates a Compute Quota.

Creates or Updates a Compute Quota with the provided quota parameters.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.QuotasApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let quotaName = "quotaName_example"; // String | Name of the quota.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let newQuota = new ComputeAdminClient.QuotasGet200Response(); // QuotasGet200Response | New quota to create.
apiInstance.quotasCreateOrUpdate(subscriptionId, location, quotaName, apiVersion, newQuota, (error, data, response) => {
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
 **quotaName** | **String**| Name of the quota. | 
 **apiVersion** | **String**| Client API Version. | 
 **newQuota** | [**QuotasGet200Response**](QuotasGet200Response.md)| New quota to create. | 

### Return type

[**QuotasGet200Response**](QuotasGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quotasDelete

> quotasDelete(subscriptionId, location, quotaName, apiVersion)

Deletes specified Compute quota

Delete an existing Compute quota.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.QuotasApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let quotaName = "quotaName_example"; // String | Name of the quota.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.quotasDelete(subscriptionId, location, quotaName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **quotaName** | **String**| Name of the quota. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## quotasGet

> QuotasGet200Response quotasGet(subscriptionId, location, quotaName, apiVersion)

Returns the requested Compute quota.

Get an existing Compute Quota.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.QuotasApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let quotaName = "quotaName_example"; // String | Name of the quota.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.quotasGet(subscriptionId, location, quotaName, apiVersion, (error, data, response) => {
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
 **quotaName** | **String**| Name of the quota. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**QuotasGet200Response**](QuotasGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotasList

> QuotasList200Response quotasList(subscriptionId, location, apiVersion)

Lists all Compute quotas.

Get a list of existing Compute quotas.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.QuotasApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.quotasList(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**QuotasList200Response**](QuotasList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

