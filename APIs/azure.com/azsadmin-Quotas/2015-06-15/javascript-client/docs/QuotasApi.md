# NetworkAdminManagementClient.QuotasApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotasGet**](QuotasApi.md#quotasGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resourceName} | 
[**quotasList**](QuotasApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/locations/{location}/quotas | 



## quotasGet

> Quota quotasGet(subscriptionId, location, resourceName, apiVersion)



Get a quota by name.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.QuotasApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let resourceName = "resourceName_example"; // String | Name of the resource.
let apiVersion = "'2015-06-15'"; // String | Client API Version.
apiInstance.quotasGet(subscriptionId, location, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **resourceName** | **String**| Name of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]

### Return type

[**Quota**](Quota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotasList

> QuotaList quotasList(subscriptionId, location, apiVersion, opts)



List all quotas.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.QuotasApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let apiVersion = "'2015-06-15'"; // String | Client API Version.
let opts = {
  'filter': "filter_example" // String | OData filter parameter.
};
apiInstance.quotasList(subscriptionId, location, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]
 **filter** | **String**| OData filter parameter. | [optional] 

### Return type

[**QuotaList**](QuotaList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

