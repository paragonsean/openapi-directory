# VMwareCloudSimple.DedicatedCloudServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dedicatedCloudServicesCreateOrUpdate**](DedicatedCloudServicesApi.md#dedicatedCloudServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicated cloud service PUT method
[**dedicatedCloudServicesDelete**](DedicatedCloudServicesApi.md#dedicatedCloudServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicatedCloudService DELETE method
[**dedicatedCloudServicesGet**](DedicatedCloudServicesApi.md#dedicatedCloudServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicatedCloudService GET method
[**dedicatedCloudServicesListByResourceGroup**](DedicatedCloudServicesApi.md#dedicatedCloudServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices | Implements list of dedicatedCloudService objects within RG method
[**dedicatedCloudServicesListBySubscription**](DedicatedCloudServicesApi.md#dedicatedCloudServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices | Implements list of dedicatedCloudService objects within subscription method
[**dedicatedCloudServicesUpdate**](DedicatedCloudServicesApi.md#dedicatedCloudServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicatedCloudService PATCH method



## dedicatedCloudServicesCreateOrUpdate

> DedicatedCloudService dedicatedCloudServicesCreateOrUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest)

Implements dedicated cloud service PUT method

Create dedicate cloud service

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud Service name
let apiVersion = "apiVersion_example"; // String | Client API version.
let dedicatedCloudServiceRequest = new VMwareCloudSimple.DedicatedCloudService(); // DedicatedCloudService | Create Dedicated Cloud Service request
apiInstance.dedicatedCloudServicesCreateOrUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group | 
 **dedicatedCloudServiceName** | **String**| dedicated cloud Service name | 
 **apiVersion** | **String**| Client API version. | 
 **dedicatedCloudServiceRequest** | [**DedicatedCloudService**](DedicatedCloudService.md)| Create Dedicated Cloud Service request | 

### Return type

[**DedicatedCloudService**](DedicatedCloudService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dedicatedCloudServicesDelete

> dedicatedCloudServicesDelete(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion)

Implements dedicatedCloudService DELETE method

Delete dedicate cloud service

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud service name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.dedicatedCloudServicesDelete(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **dedicatedCloudServiceName** | **String**| dedicated cloud service name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudServicesGet

> DedicatedCloudService dedicatedCloudServicesGet(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion)

Implements dedicatedCloudService GET method

Returns Dedicate Cloud Service

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud Service name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.dedicatedCloudServicesGet(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group | 
 **dedicatedCloudServiceName** | **String**| dedicated cloud Service name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DedicatedCloudService**](DedicatedCloudService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudServicesListByResourceGroup

> DedicatedCloudServiceListResponse dedicatedCloudServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

Implements list of dedicatedCloudService objects within RG method

Returns list of dedicated cloud services within a resource group

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the list operation
  'top': 56, // Number | The maximum number of record sets to return
  'skipToken': "skipToken_example" // String | to be used by nextLink implementation
};
apiInstance.dedicatedCloudServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group | 
 **apiVersion** | **String**| Client API version. | 
 **filter** | **String**| The filter to apply on the list operation | [optional] 
 **top** | **Number**| The maximum number of record sets to return | [optional] 
 **skipToken** | **String**| to be used by nextLink implementation | [optional] 

### Return type

[**DedicatedCloudServiceListResponse**](DedicatedCloudServiceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudServicesListBySubscription

> DedicatedCloudServiceListResponse dedicatedCloudServicesListBySubscription(subscriptionId, apiVersion, opts)

Implements list of dedicatedCloudService objects within subscription method

Returns list of dedicated cloud services within a subscription

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the list operation
  'top': 56, // Number | The maximum number of record sets to return
  'skipToken': "skipToken_example" // String | to be used by nextLink implementation
};
apiInstance.dedicatedCloudServicesListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the list operation | [optional] 
 **top** | **Number**| The maximum number of record sets to return | [optional] 
 **skipToken** | **String**| to be used by nextLink implementation | [optional] 

### Return type

[**DedicatedCloudServiceListResponse**](DedicatedCloudServiceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudServicesUpdate

> DedicatedCloudService dedicatedCloudServicesUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest)

Implements dedicatedCloudService PATCH method

Patch dedicated cloud service&#39;s properties

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud service name
let apiVersion = "apiVersion_example"; // String | Client API version.
let dedicatedCloudServiceRequest = new VMwareCloudSimple.PatchPayload(); // PatchPayload | Patch Dedicated Cloud Service request
apiInstance.dedicatedCloudServicesUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group | 
 **dedicatedCloudServiceName** | **String**| dedicated cloud service name | 
 **apiVersion** | **String**| Client API version. | 
 **dedicatedCloudServiceRequest** | [**PatchPayload**](PatchPayload.md)| Patch Dedicated Cloud Service request | 

### Return type

[**DedicatedCloudService**](DedicatedCloudService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

