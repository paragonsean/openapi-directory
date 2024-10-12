# MicrosoftNetApp.VolumesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesCreateOrUpdate**](VolumesApi.md#volumesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} | Create or Update a volume
[**volumesDelete**](VolumesApi.md#volumesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} | Delete a volume
[**volumesGet**](VolumesApi.md#volumesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} | Describe a volume
[**volumesList**](VolumesApi.md#volumesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes | Describe all volumes
[**volumesUpdate**](VolumesApi.md#volumesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} | Update a volume



## volumesCreateOrUpdate

> Volume volumesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)

Create or Update a volume

Create or update the specified volume within the capacity pool

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-07-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.Volume(); // Volume | Volume object supplied in the body of the operation.
apiInstance.volumesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-07-01&#39;]
 **body** | [**Volume**](Volume.md)| Volume object supplied in the body of the operation. | 

### Return type

[**Volume**](Volume.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## volumesDelete

> volumesDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Delete a volume

Delete the specified volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-07-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-07-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## volumesGet

> Volume volumesGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Describe a volume

Get the details of the specified volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-07-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-07-01&#39;]

### Return type

[**Volume**](Volume.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesList

> VolumeList volumesList(subscriptionId, resourceGroupName, accountName, poolName, apiVersion)

Describe all volumes

List all volumes within the capacity pool

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let apiVersion = "'2019-07-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesList(subscriptionId, resourceGroupName, accountName, poolName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-07-01&#39;]

### Return type

[**VolumeList**](VolumeList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesUpdate

> Volume volumesUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)

Update a volume

Patch the specified volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-07-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.VolumePatch(); // VolumePatch | Volume object supplied in the body of the operation.
apiInstance.volumesUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-07-01&#39;]
 **body** | [**VolumePatch**](VolumePatch.md)| Volume object supplied in the body of the operation. | 

### Return type

[**Volume**](Volume.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

