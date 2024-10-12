# VMwareCloudSimple.DedicatedCloudNodesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dedicatedCloudNodesCreateOrUpdate**](DedicatedCloudNodesApi.md#dedicatedCloudNodesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node PUT method
[**dedicatedCloudNodesDelete**](DedicatedCloudNodesApi.md#dedicatedCloudNodesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node DELETE method
[**dedicatedCloudNodesGet**](DedicatedCloudNodesApi.md#dedicatedCloudNodesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node GET method
[**dedicatedCloudNodesListByResourceGroup**](DedicatedCloudNodesApi.md#dedicatedCloudNodesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes | Implements list of dedicated cloud nodes within RG method
[**dedicatedCloudNodesListBySubscription**](DedicatedCloudNodesApi.md#dedicatedCloudNodesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes | Implements list of dedicated cloud nodes within subscription method
[**dedicatedCloudNodesUpdate**](DedicatedCloudNodesApi.md#dedicatedCloudNodesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node PATCH method



## dedicatedCloudNodesCreateOrUpdate

> DedicatedCloudNode dedicatedCloudNodesCreateOrUpdate(subscriptionId, resourceGroupName, referer, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest)

Implements dedicated cloud node PUT method

Returns dedicated cloud node by its name

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let referer = "referer_example"; // String | referer url
let dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
let apiVersion = "apiVersion_example"; // String | Client API version.
let dedicatedCloudNodeRequest = new VMwareCloudSimple.DedicatedCloudNode(); // DedicatedCloudNode | Create Dedicated Cloud Node request
apiInstance.dedicatedCloudNodesCreateOrUpdate(subscriptionId, resourceGroupName, referer, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest, (error, data, response) => {
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
 **referer** | **String**| referer url | 
 **dedicatedCloudNodeName** | **String**| dedicated cloud node name | 
 **apiVersion** | **String**| Client API version. | 
 **dedicatedCloudNodeRequest** | [**DedicatedCloudNode**](DedicatedCloudNode.md)| Create Dedicated Cloud Node request | 

### Return type

[**DedicatedCloudNode**](DedicatedCloudNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dedicatedCloudNodesDelete

> dedicatedCloudNodesDelete(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion)

Implements dedicated cloud node DELETE method

Delete dedicated cloud node

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.dedicatedCloudNodesDelete(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion, (error, data, response) => {
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
 **dedicatedCloudNodeName** | **String**| dedicated cloud node name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudNodesGet

> DedicatedCloudNode dedicatedCloudNodesGet(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion)

Implements dedicated cloud node GET method

Returns dedicated cloud node

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.dedicatedCloudNodesGet(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion, (error, data, response) => {
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
 **dedicatedCloudNodeName** | **String**| dedicated cloud node name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DedicatedCloudNode**](DedicatedCloudNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudNodesListByResourceGroup

> DedicatedCloudNodeListResponse dedicatedCloudNodesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

Implements list of dedicated cloud nodes within RG method

Returns list of dedicate cloud nodes within resource group

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the list operation
  'top': 56, // Number | The maximum number of record sets to return
  'skipToken': "skipToken_example" // String | to be used by nextLink implementation
};
apiInstance.dedicatedCloudNodesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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

[**DedicatedCloudNodeListResponse**](DedicatedCloudNodeListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudNodesListBySubscription

> DedicatedCloudNodeListResponse dedicatedCloudNodesListBySubscription(subscriptionId, apiVersion, opts)

Implements list of dedicated cloud nodes within subscription method

Returns list of dedicate cloud nodes within subscription

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the list operation
  'top': 56, // Number | The maximum number of record sets to return
  'skipToken': "skipToken_example" // String | to be used by nextLink implementation
};
apiInstance.dedicatedCloudNodesListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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

[**DedicatedCloudNodeListResponse**](DedicatedCloudNodeListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedCloudNodesUpdate

> DedicatedCloudNode dedicatedCloudNodesUpdate(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest)

Implements dedicated cloud node PATCH method

Patches dedicated node properties

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.DedicatedCloudNodesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
let apiVersion = "apiVersion_example"; // String | Client API version.
let dedicatedCloudNodeRequest = new VMwareCloudSimple.PatchPayload(); // PatchPayload | Patch Dedicated Cloud Node request
apiInstance.dedicatedCloudNodesUpdate(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest, (error, data, response) => {
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
 **dedicatedCloudNodeName** | **String**| dedicated cloud node name | 
 **apiVersion** | **String**| Client API version. | 
 **dedicatedCloudNodeRequest** | [**PatchPayload**](PatchPayload.md)| Patch Dedicated Cloud Node request | 

### Return type

[**DedicatedCloudNode**](DedicatedCloudNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

