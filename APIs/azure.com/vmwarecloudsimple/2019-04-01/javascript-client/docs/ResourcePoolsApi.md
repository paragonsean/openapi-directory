# VMwareCloudSimple.ResourcePoolsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcePoolsGet**](ResourcePoolsApi.md#resourcePoolsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/resourcePools/{resourcePoolName} | Implements get of resource pool
[**resourcePoolsList**](ResourcePoolsApi.md#resourcePoolsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/resourcePools | Implements get of resource pools list



## resourcePoolsGet

> ResourcePool resourcePoolsGet(subscriptionId, apiVersion, regionId, pcName, resourcePoolName)

Implements get of resource pool

Returns resource pool templates by its name

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.ResourcePoolsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let resourcePoolName = "resourcePoolName_example"; // String | resource pool id (vsphereId)
apiInstance.resourcePoolsGet(subscriptionId, apiVersion, regionId, pcName, resourcePoolName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **apiVersion** | **String**| Client API version. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **resourcePoolName** | **String**| resource pool id (vsphereId) | 

### Return type

[**ResourcePool**](ResourcePool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcePoolsList

> ResourcePoolsListResponse resourcePoolsList(subscriptionId, regionId, pcName, apiVersion)

Implements get of resource pools list

Returns list of resource pools in region for private cloud

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.ResourcePoolsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.resourcePoolsList(subscriptionId, regionId, pcName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**ResourcePoolsListResponse**](ResourcePoolsListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

