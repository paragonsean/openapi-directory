# NetBoxApi.VirtualizationApi

All URIs are relative to *http://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualizationChoicesList**](VirtualizationApi.md#virtualizationChoicesList) | **GET** /virtualization/_choices/ | 
[**virtualizationChoicesRead**](VirtualizationApi.md#virtualizationChoicesRead) | **GET** /virtualization/_choices/{id}/ | 
[**virtualizationClusterGroupsCreate**](VirtualizationApi.md#virtualizationClusterGroupsCreate) | **POST** /virtualization/cluster-groups/ | 
[**virtualizationClusterGroupsDelete**](VirtualizationApi.md#virtualizationClusterGroupsDelete) | **DELETE** /virtualization/cluster-groups/{id}/ | 
[**virtualizationClusterGroupsList**](VirtualizationApi.md#virtualizationClusterGroupsList) | **GET** /virtualization/cluster-groups/ | 
[**virtualizationClusterGroupsPartialUpdate**](VirtualizationApi.md#virtualizationClusterGroupsPartialUpdate) | **PATCH** /virtualization/cluster-groups/{id}/ | 
[**virtualizationClusterGroupsRead**](VirtualizationApi.md#virtualizationClusterGroupsRead) | **GET** /virtualization/cluster-groups/{id}/ | 
[**virtualizationClusterGroupsUpdate**](VirtualizationApi.md#virtualizationClusterGroupsUpdate) | **PUT** /virtualization/cluster-groups/{id}/ | 
[**virtualizationClusterTypesCreate**](VirtualizationApi.md#virtualizationClusterTypesCreate) | **POST** /virtualization/cluster-types/ | 
[**virtualizationClusterTypesDelete**](VirtualizationApi.md#virtualizationClusterTypesDelete) | **DELETE** /virtualization/cluster-types/{id}/ | 
[**virtualizationClusterTypesList**](VirtualizationApi.md#virtualizationClusterTypesList) | **GET** /virtualization/cluster-types/ | 
[**virtualizationClusterTypesPartialUpdate**](VirtualizationApi.md#virtualizationClusterTypesPartialUpdate) | **PATCH** /virtualization/cluster-types/{id}/ | 
[**virtualizationClusterTypesRead**](VirtualizationApi.md#virtualizationClusterTypesRead) | **GET** /virtualization/cluster-types/{id}/ | 
[**virtualizationClusterTypesUpdate**](VirtualizationApi.md#virtualizationClusterTypesUpdate) | **PUT** /virtualization/cluster-types/{id}/ | 
[**virtualizationClustersCreate**](VirtualizationApi.md#virtualizationClustersCreate) | **POST** /virtualization/clusters/ | 
[**virtualizationClustersDelete**](VirtualizationApi.md#virtualizationClustersDelete) | **DELETE** /virtualization/clusters/{id}/ | 
[**virtualizationClustersList**](VirtualizationApi.md#virtualizationClustersList) | **GET** /virtualization/clusters/ | 
[**virtualizationClustersPartialUpdate**](VirtualizationApi.md#virtualizationClustersPartialUpdate) | **PATCH** /virtualization/clusters/{id}/ | 
[**virtualizationClustersRead**](VirtualizationApi.md#virtualizationClustersRead) | **GET** /virtualization/clusters/{id}/ | 
[**virtualizationClustersUpdate**](VirtualizationApi.md#virtualizationClustersUpdate) | **PUT** /virtualization/clusters/{id}/ | 
[**virtualizationInterfacesCreate**](VirtualizationApi.md#virtualizationInterfacesCreate) | **POST** /virtualization/interfaces/ | 
[**virtualizationInterfacesDelete**](VirtualizationApi.md#virtualizationInterfacesDelete) | **DELETE** /virtualization/interfaces/{id}/ | 
[**virtualizationInterfacesList**](VirtualizationApi.md#virtualizationInterfacesList) | **GET** /virtualization/interfaces/ | 
[**virtualizationInterfacesPartialUpdate**](VirtualizationApi.md#virtualizationInterfacesPartialUpdate) | **PATCH** /virtualization/interfaces/{id}/ | 
[**virtualizationInterfacesRead**](VirtualizationApi.md#virtualizationInterfacesRead) | **GET** /virtualization/interfaces/{id}/ | 
[**virtualizationInterfacesUpdate**](VirtualizationApi.md#virtualizationInterfacesUpdate) | **PUT** /virtualization/interfaces/{id}/ | 
[**virtualizationVirtualMachinesCreate**](VirtualizationApi.md#virtualizationVirtualMachinesCreate) | **POST** /virtualization/virtual-machines/ | 
[**virtualizationVirtualMachinesDelete**](VirtualizationApi.md#virtualizationVirtualMachinesDelete) | **DELETE** /virtualization/virtual-machines/{id}/ | 
[**virtualizationVirtualMachinesList**](VirtualizationApi.md#virtualizationVirtualMachinesList) | **GET** /virtualization/virtual-machines/ | 
[**virtualizationVirtualMachinesPartialUpdate**](VirtualizationApi.md#virtualizationVirtualMachinesPartialUpdate) | **PATCH** /virtualization/virtual-machines/{id}/ | 
[**virtualizationVirtualMachinesRead**](VirtualizationApi.md#virtualizationVirtualMachinesRead) | **GET** /virtualization/virtual-machines/{id}/ | 
[**virtualizationVirtualMachinesUpdate**](VirtualizationApi.md#virtualizationVirtualMachinesUpdate) | **PUT** /virtualization/virtual-machines/{id}/ | 



## virtualizationChoicesList

> virtualizationChoicesList()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
apiInstance.virtualizationChoicesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationChoicesRead

> virtualizationChoicesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = "id_example"; // String | 
apiInstance.virtualizationChoicesRead(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationClusterGroupsCreate

> ClusterGroup virtualizationClusterGroupsCreate(clusterGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let clusterGroup = new NetBoxApi.ClusterGroup(); // ClusterGroup | 
apiInstance.virtualizationClusterGroupsCreate(clusterGroup, (error, data, response) => {
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
 **clusterGroup** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClusterGroupsDelete

> virtualizationClusterGroupsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster group.
apiInstance.virtualizationClusterGroupsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster group. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationClusterGroupsList

> VirtualizationClusterGroupsList200Response virtualizationClusterGroupsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.virtualizationClusterGroupsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**VirtualizationClusterGroupsList200Response**](VirtualizationClusterGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationClusterGroupsPartialUpdate

> ClusterGroup virtualizationClusterGroupsPartialUpdate(id, clusterGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster group.
let clusterGroup = new NetBoxApi.ClusterGroup(); // ClusterGroup | 
apiInstance.virtualizationClusterGroupsPartialUpdate(id, clusterGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster group. | 
 **clusterGroup** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClusterGroupsRead

> ClusterGroup virtualizationClusterGroupsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster group.
apiInstance.virtualizationClusterGroupsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster group. | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationClusterGroupsUpdate

> ClusterGroup virtualizationClusterGroupsUpdate(id, clusterGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster group.
let clusterGroup = new NetBoxApi.ClusterGroup(); // ClusterGroup | 
apiInstance.virtualizationClusterGroupsUpdate(id, clusterGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster group. | 
 **clusterGroup** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClusterTypesCreate

> ClusterType virtualizationClusterTypesCreate(clusterType)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let clusterType = new NetBoxApi.ClusterType(); // ClusterType | 
apiInstance.virtualizationClusterTypesCreate(clusterType, (error, data, response) => {
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
 **clusterType** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClusterTypesDelete

> virtualizationClusterTypesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster type.
apiInstance.virtualizationClusterTypesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster type. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationClusterTypesList

> VirtualizationClusterTypesList200Response virtualizationClusterTypesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.virtualizationClusterTypesList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**VirtualizationClusterTypesList200Response**](VirtualizationClusterTypesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationClusterTypesPartialUpdate

> ClusterType virtualizationClusterTypesPartialUpdate(id, clusterType)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster type.
let clusterType = new NetBoxApi.ClusterType(); // ClusterType | 
apiInstance.virtualizationClusterTypesPartialUpdate(id, clusterType, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster type. | 
 **clusterType** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClusterTypesRead

> ClusterType virtualizationClusterTypesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster type.
apiInstance.virtualizationClusterTypesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster type. | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationClusterTypesUpdate

> ClusterType virtualizationClusterTypesUpdate(id, clusterType)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster type.
let clusterType = new NetBoxApi.ClusterType(); // ClusterType | 
apiInstance.virtualizationClusterTypesUpdate(id, clusterType, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster type. | 
 **clusterType** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClustersCreate

> Cluster virtualizationClustersCreate(writableCluster)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let writableCluster = new NetBoxApi.WritableCluster(); // WritableCluster | 
apiInstance.virtualizationClustersCreate(writableCluster, (error, data, response) => {
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
 **writableCluster** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClustersDelete

> virtualizationClustersDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster.
apiInstance.virtualizationClustersDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationClustersList

> VirtualizationClustersList200Response virtualizationClustersList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let opts = {
  'name': "name_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'typeId': "typeId_example", // String | 
  'type': "type_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.virtualizationClustersList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **typeId** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**VirtualizationClustersList200Response**](VirtualizationClustersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationClustersPartialUpdate

> Cluster virtualizationClustersPartialUpdate(id, writableCluster)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster.
let writableCluster = new NetBoxApi.WritableCluster(); // WritableCluster | 
apiInstance.virtualizationClustersPartialUpdate(id, writableCluster, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster. | 
 **writableCluster** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationClustersRead

> Cluster virtualizationClustersRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster.
apiInstance.virtualizationClustersRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationClustersUpdate

> Cluster virtualizationClustersUpdate(id, writableCluster)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this cluster.
let writableCluster = new NetBoxApi.WritableCluster(); // WritableCluster | 
apiInstance.virtualizationClustersUpdate(id, writableCluster, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this cluster. | 
 **writableCluster** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationInterfacesCreate

> Interface virtualizationInterfacesCreate(writableInterface)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let writableInterface = new NetBoxApi.WritableInterface(); // WritableInterface | 
apiInstance.virtualizationInterfacesCreate(writableInterface, (error, data, response) => {
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
 **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationInterfacesDelete

> virtualizationInterfacesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this interface.
apiInstance.virtualizationInterfacesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this interface. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationInterfacesList

> DcimInterfacesList200Response virtualizationInterfacesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let opts = {
  'name': "name_example", // String | 
  'enabled': "enabled_example", // String | 
  'mtu': 3.4, // Number | 
  'virtualMachineId': "virtualMachineId_example", // String | 
  'virtualMachine': "virtualMachine_example", // String | 
  'macAddress': "macAddress_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.virtualizationInterfacesList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **enabled** | **String**|  | [optional] 
 **mtu** | **Number**|  | [optional] 
 **virtualMachineId** | **String**|  | [optional] 
 **virtualMachine** | **String**|  | [optional] 
 **macAddress** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**DcimInterfacesList200Response**](DcimInterfacesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationInterfacesPartialUpdate

> Interface virtualizationInterfacesPartialUpdate(id, writableInterface)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this interface.
let writableInterface = new NetBoxApi.WritableInterface(); // WritableInterface | 
apiInstance.virtualizationInterfacesPartialUpdate(id, writableInterface, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this interface. | 
 **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationInterfacesRead

> Interface virtualizationInterfacesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this interface.
apiInstance.virtualizationInterfacesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this interface. | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationInterfacesUpdate

> Interface virtualizationInterfacesUpdate(id, writableInterface)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this interface.
let writableInterface = new NetBoxApi.WritableInterface(); // WritableInterface | 
apiInstance.virtualizationInterfacesUpdate(id, writableInterface, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this interface. | 
 **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationVirtualMachinesCreate

> VirtualMachine virtualizationVirtualMachinesCreate(writableVirtualMachine)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let writableVirtualMachine = new NetBoxApi.WritableVirtualMachine(); // WritableVirtualMachine | 
apiInstance.virtualizationVirtualMachinesCreate(writableVirtualMachine, (error, data, response) => {
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
 **writableVirtualMachine** | [**WritableVirtualMachine**](WritableVirtualMachine.md)|  | 

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationVirtualMachinesDelete

> virtualizationVirtualMachinesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this virtual machine.
apiInstance.virtualizationVirtualMachinesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this virtual machine. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualizationVirtualMachinesList

> VirtualizationVirtualMachinesList200Response virtualizationVirtualMachinesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let opts = {
  'name': "name_example", // String | 
  'cluster': "cluster_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'status': "status_example", // String | 
  'clusterGroupId': "clusterGroupId_example", // String | 
  'clusterGroup': "clusterGroup_example", // String | 
  'clusterTypeId': "clusterTypeId_example", // String | 
  'clusterType': "clusterType_example", // String | 
  'clusterId': "clusterId_example", // String | 
  'regionId': 3.4, // Number | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'platformId': "platformId_example", // String | 
  'platform': "platform_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.virtualizationVirtualMachinesList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **cluster** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **clusterGroupId** | **String**|  | [optional] 
 **clusterGroup** | **String**|  | [optional] 
 **clusterTypeId** | **String**|  | [optional] 
 **clusterType** | **String**|  | [optional] 
 **clusterId** | **String**|  | [optional] 
 **regionId** | **Number**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **platformId** | **String**|  | [optional] 
 **platform** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**VirtualizationVirtualMachinesList200Response**](VirtualizationVirtualMachinesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationVirtualMachinesPartialUpdate

> VirtualMachine virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachine)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this virtual machine.
let writableVirtualMachine = new NetBoxApi.WritableVirtualMachine(); // WritableVirtualMachine | 
apiInstance.virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachine, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this virtual machine. | 
 **writableVirtualMachine** | [**WritableVirtualMachine**](WritableVirtualMachine.md)|  | 

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationVirtualMachinesRead

> VirtualMachineWithConfigContext virtualizationVirtualMachinesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this virtual machine.
apiInstance.virtualizationVirtualMachinesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this virtual machine. | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationVirtualMachinesUpdate

> VirtualMachine virtualizationVirtualMachinesUpdate(id, writableVirtualMachine)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.VirtualizationApi();
let id = 56; // Number | A unique integer value identifying this virtual machine.
let writableVirtualMachine = new NetBoxApi.WritableVirtualMachine(); // WritableVirtualMachine | 
apiInstance.virtualizationVirtualMachinesUpdate(id, writableVirtualMachine, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this virtual machine. | 
 **writableVirtualMachine** | [**WritableVirtualMachine**](WritableVirtualMachine.md)|  | 

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

