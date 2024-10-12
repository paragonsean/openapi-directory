# SubscriptionsManagementClient.DirectoryTenantsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directoryTenantsCreateOrUpdate**](DirectoryTenantsApi.md#directoryTenantsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant} | 
[**directoryTenantsDelete**](DirectoryTenantsApi.md#directoryTenantsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant} | 
[**directoryTenantsGet**](DirectoryTenantsApi.md#directoryTenantsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant} | 
[**directoryTenantsList**](DirectoryTenantsApi.md#directoryTenantsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants | 



## directoryTenantsCreateOrUpdate

> DirectoryTenant directoryTenantsCreateOrUpdate(subscriptionId, resourceGroupName, tenant, apiVersion, newTenant)



Create or updates a directory tenant.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DirectoryTenantsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let tenant = "tenant_example"; // String | Directory tenant name.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
let newTenant = new SubscriptionsManagementClient.DirectoryTenant(); // DirectoryTenant | New directory tenant properties.
apiInstance.directoryTenantsCreateOrUpdate(subscriptionId, resourceGroupName, tenant, apiVersion, newTenant, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **tenant** | **String**| Directory tenant name. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]
 **newTenant** | [**DirectoryTenant**](DirectoryTenant.md)| New directory tenant properties. | 

### Return type

[**DirectoryTenant**](DirectoryTenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## directoryTenantsDelete

> directoryTenantsDelete(subscriptionId, resourceGroupName, tenant, apiVersion)



Delete a directory tenant under a resource group.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DirectoryTenantsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let tenant = "tenant_example"; // String | Directory tenant name.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.directoryTenantsDelete(subscriptionId, resourceGroupName, tenant, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **tenant** | **String**| Directory tenant name. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directoryTenantsGet

> DirectoryTenant directoryTenantsGet(subscriptionId, resourceGroupName, tenant, apiVersion)



Get a directory tenant by name.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DirectoryTenantsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let tenant = "tenant_example"; // String | Directory tenant name.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.directoryTenantsGet(subscriptionId, resourceGroupName, tenant, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **tenant** | **String**| Directory tenant name. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**DirectoryTenant**](DirectoryTenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## directoryTenantsList

> DirectoryTenantList directoryTenantsList(subscriptionId, resourceGroupName, apiVersion)



Lists all the directory tenants under the current subscription and given resource group name.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DirectoryTenantsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.directoryTenantsList(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**DirectoryTenantList**](DirectoryTenantList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

