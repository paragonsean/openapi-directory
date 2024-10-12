# ComputeAdminClient.QuotasApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotasCreateOrUpdate**](QuotasApi.md#quotasCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quotaName} | Creates or Updates a Quota.
[**quotasDelete**](QuotasApi.md#quotasDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quotaName} | Deletes specified quota
[**quotasGet**](QuotasApi.md#quotasGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quotaName} | Returns the requested quota.
[**quotasList**](QuotasApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/quotas | Lists all quotas.



## quotasCreateOrUpdate

> Quota quotasCreateOrUpdate(subscriptionId, location, quotaName, apiVersion, newQuota)

Creates or Updates a Quota.

Creates or Updates a Quota.

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
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
let newQuota = new ComputeAdminClient.Quota(); // Quota | New quota to create.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]
 **newQuota** | [**Quota**](Quota.md)| New quota to create. | 

### Return type

[**Quota**](Quota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quotasDelete

> quotasDelete(subscriptionId, location, quotaName, apiVersion)

Deletes specified quota

Delete an existing quota.

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
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## quotasGet

> Quota quotasGet(subscriptionId, location, quotaName, apiVersion)

Returns the requested quota.

Get an existing Quota.

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
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

[**Quota**](Quota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotasList

> QuotaList quotasList(subscriptionId, location, apiVersion)

Lists all quotas.

Get a list of existing quotas.

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
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

[**QuotaList**](QuotaList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

