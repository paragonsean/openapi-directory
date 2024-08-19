# NetworkAdminManagementClient.NetworkApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotasCreateOrUpdate**](NetworkApi.md#quotasCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resourceName} | 
[**quotasDelete**](NetworkApi.md#quotasDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resourceName} | 



## quotasCreateOrUpdate

> Quota quotasCreateOrUpdate(subscriptionId, location, resourceName, apiVersion, quota)



Create or update a quota.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let resourceName = "resourceName_example"; // String | Name of the resource.
let apiVersion = "'2015-06-15'"; // String | Client API Version.
let quota = new NetworkAdminManagementClient.Quota(); // Quota | New network quota to create.
apiInstance.quotasCreateOrUpdate(subscriptionId, location, resourceName, apiVersion, quota, (error, data, response) => {
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
 **quota** | [**Quota**](Quota.md)| New network quota to create. | 

### Return type

[**Quota**](Quota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quotasDelete

> quotasDelete(subscriptionId, location, resourceName, apiVersion)



Delete a quota by name.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let resourceName = "resourceName_example"; // String | Name of the resource.
let apiVersion = "'2015-06-15'"; // String | Client API Version.
apiInstance.quotasDelete(subscriptionId, location, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **resourceName** | **String**| Name of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

