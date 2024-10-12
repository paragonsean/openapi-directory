# NetBoxApi.VirtualizationApi

All URIs are relative to *https://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'description': "description_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'description': "description_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'typeId': "typeId_example", // String | 
  'type': "type_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'groupIdN': "groupIdN_example", // String | 
  'groupN': "groupN_example", // String | 
  'typeIdN': "typeIdN_example", // String | 
  'typeN': "typeN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **typeId** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **groupIdN** | **String**|  | [optional] 
 **groupN** | **String**|  | [optional] 
 **typeIdN** | **String**|  | [optional] 
 **typeN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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

> VirtualMachineInterface virtualizationInterfacesCreate(writableVirtualMachineInterface)





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
let writableVirtualMachineInterface = new NetBoxApi.WritableVirtualMachineInterface(); // WritableVirtualMachineInterface | 
apiInstance.virtualizationInterfacesCreate(writableVirtualMachineInterface, (error, data, response) => {
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
 **writableVirtualMachineInterface** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

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

> VirtualizationInterfacesList200Response virtualizationInterfacesList(opts)



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'enabled': "enabled_example", // String | 
  'mtu': "mtu_example", // String | 
  'q': "q_example", // String | 
  'virtualMachineId': "virtualMachineId_example", // String | 
  'virtualMachine': "virtualMachine_example", // String | 
  'macAddress': "macAddress_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'mtuN': "mtuN_example", // String | 
  'mtuLte': "mtuLte_example", // String | 
  'mtuLt': "mtuLt_example", // String | 
  'mtuGte': "mtuGte_example", // String | 
  'mtuGt': "mtuGt_example", // String | 
  'virtualMachineIdN': "virtualMachineIdN_example", // String | 
  'virtualMachineN': "virtualMachineN_example", // String | 
  'macAddressN': "macAddressN_example", // String | 
  'macAddressIc': "macAddressIc_example", // String | 
  'macAddressNic': "macAddressNic_example", // String | 
  'macAddressIew': "macAddressIew_example", // String | 
  'macAddressNiew': "macAddressNiew_example", // String | 
  'macAddressIsw': "macAddressIsw_example", // String | 
  'macAddressNisw': "macAddressNisw_example", // String | 
  'macAddressIe': "macAddressIe_example", // String | 
  'macAddressNie': "macAddressNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **enabled** | **String**|  | [optional] 
 **mtu** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **virtualMachineId** | **String**|  | [optional] 
 **virtualMachine** | **String**|  | [optional] 
 **macAddress** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **mtuN** | **String**|  | [optional] 
 **mtuLte** | **String**|  | [optional] 
 **mtuLt** | **String**|  | [optional] 
 **mtuGte** | **String**|  | [optional] 
 **mtuGt** | **String**|  | [optional] 
 **virtualMachineIdN** | **String**|  | [optional] 
 **virtualMachineN** | **String**|  | [optional] 
 **macAddressN** | **String**|  | [optional] 
 **macAddressIc** | **String**|  | [optional] 
 **macAddressNic** | **String**|  | [optional] 
 **macAddressIew** | **String**|  | [optional] 
 **macAddressNiew** | **String**|  | [optional] 
 **macAddressIsw** | **String**|  | [optional] 
 **macAddressNisw** | **String**|  | [optional] 
 **macAddressIe** | **String**|  | [optional] 
 **macAddressNie** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**VirtualizationInterfacesList200Response**](VirtualizationInterfacesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationInterfacesPartialUpdate

> VirtualMachineInterface virtualizationInterfacesPartialUpdate(id, writableVirtualMachineInterface)





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
let writableVirtualMachineInterface = new NetBoxApi.WritableVirtualMachineInterface(); // WritableVirtualMachineInterface | 
apiInstance.virtualizationInterfacesPartialUpdate(id, writableVirtualMachineInterface, (error, data, response) => {
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
 **writableVirtualMachineInterface** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationInterfacesRead

> VirtualMachineInterface virtualizationInterfacesRead(id)



Call to super to allow for caching

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

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualizationInterfacesUpdate

> VirtualMachineInterface virtualizationInterfacesUpdate(id, writableVirtualMachineInterface)





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
let writableVirtualMachineInterface = new NetBoxApi.WritableVirtualMachineInterface(); // WritableVirtualMachineInterface | 
apiInstance.virtualizationInterfacesUpdate(id, writableVirtualMachineInterface, (error, data, response) => {
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
 **writableVirtualMachineInterface** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationVirtualMachinesCreate

> VirtualMachineWithConfigContext virtualizationVirtualMachinesCreate(writableVirtualMachineWithConfigContext)





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
let writableVirtualMachineWithConfigContext = new NetBoxApi.WritableVirtualMachineWithConfigContext(); // WritableVirtualMachineWithConfigContext | 
apiInstance.virtualizationVirtualMachinesCreate(writableVirtualMachineWithConfigContext, (error, data, response) => {
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
 **writableVirtualMachineWithConfigContext** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'cluster': "cluster_example", // String | 
  'vcpus': "vcpus_example", // String | 
  'memory': "memory_example", // String | 
  'disk': "disk_example", // String | 
  'localContextData': "localContextData_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'status': "status_example", // String | 
  'clusterGroupId': "clusterGroupId_example", // String | 
  'clusterGroup': "clusterGroup_example", // String | 
  'clusterTypeId': "clusterTypeId_example", // String | 
  'clusterType': "clusterType_example", // String | 
  'clusterId': "clusterId_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'platformId': "platformId_example", // String | 
  'platform': "platform_example", // String | 
  'macAddress': "macAddress_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'clusterN': "clusterN_example", // String | 
  'vcpusN': "vcpusN_example", // String | 
  'vcpusLte': "vcpusLte_example", // String | 
  'vcpusLt': "vcpusLt_example", // String | 
  'vcpusGte': "vcpusGte_example", // String | 
  'vcpusGt': "vcpusGt_example", // String | 
  'memoryN': "memoryN_example", // String | 
  'memoryLte': "memoryLte_example", // String | 
  'memoryLt': "memoryLt_example", // String | 
  'memoryGte': "memoryGte_example", // String | 
  'memoryGt': "memoryGt_example", // String | 
  'diskN': "diskN_example", // String | 
  'diskLte': "diskLte_example", // String | 
  'diskLt': "diskLt_example", // String | 
  'diskGte': "diskGte_example", // String | 
  'diskGt': "diskGt_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'statusN': "statusN_example", // String | 
  'clusterGroupIdN': "clusterGroupIdN_example", // String | 
  'clusterGroupN': "clusterGroupN_example", // String | 
  'clusterTypeIdN': "clusterTypeIdN_example", // String | 
  'clusterTypeN': "clusterTypeN_example", // String | 
  'clusterIdN': "clusterIdN_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'roleIdN': "roleIdN_example", // String | 
  'roleN': "roleN_example", // String | 
  'platformIdN': "platformIdN_example", // String | 
  'platformN': "platformN_example", // String | 
  'macAddressN': "macAddressN_example", // String | 
  'macAddressIc': "macAddressIc_example", // String | 
  'macAddressNic': "macAddressNic_example", // String | 
  'macAddressIew': "macAddressIew_example", // String | 
  'macAddressNiew': "macAddressNiew_example", // String | 
  'macAddressIsw': "macAddressIsw_example", // String | 
  'macAddressNisw': "macAddressNisw_example", // String | 
  'macAddressIe': "macAddressIe_example", // String | 
  'macAddressNie': "macAddressNie_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **cluster** | **String**|  | [optional] 
 **vcpus** | **String**|  | [optional] 
 **memory** | **String**|  | [optional] 
 **disk** | **String**|  | [optional] 
 **localContextData** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **clusterGroupId** | **String**|  | [optional] 
 **clusterGroup** | **String**|  | [optional] 
 **clusterTypeId** | **String**|  | [optional] 
 **clusterType** | **String**|  | [optional] 
 **clusterId** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **platformId** | **String**|  | [optional] 
 **platform** | **String**|  | [optional] 
 **macAddress** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **clusterN** | **String**|  | [optional] 
 **vcpusN** | **String**|  | [optional] 
 **vcpusLte** | **String**|  | [optional] 
 **vcpusLt** | **String**|  | [optional] 
 **vcpusGte** | **String**|  | [optional] 
 **vcpusGt** | **String**|  | [optional] 
 **memoryN** | **String**|  | [optional] 
 **memoryLte** | **String**|  | [optional] 
 **memoryLt** | **String**|  | [optional] 
 **memoryGte** | **String**|  | [optional] 
 **memoryGt** | **String**|  | [optional] 
 **diskN** | **String**|  | [optional] 
 **diskLte** | **String**|  | [optional] 
 **diskLt** | **String**|  | [optional] 
 **diskGte** | **String**|  | [optional] 
 **diskGt** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **clusterGroupIdN** | **String**|  | [optional] 
 **clusterGroupN** | **String**|  | [optional] 
 **clusterTypeIdN** | **String**|  | [optional] 
 **clusterTypeN** | **String**|  | [optional] 
 **clusterIdN** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **roleIdN** | **String**|  | [optional] 
 **roleN** | **String**|  | [optional] 
 **platformIdN** | **String**|  | [optional] 
 **platformN** | **String**|  | [optional] 
 **macAddressN** | **String**|  | [optional] 
 **macAddressIc** | **String**|  | [optional] 
 **macAddressNic** | **String**|  | [optional] 
 **macAddressIew** | **String**|  | [optional] 
 **macAddressNiew** | **String**|  | [optional] 
 **macAddressIsw** | **String**|  | [optional] 
 **macAddressNisw** | **String**|  | [optional] 
 **macAddressIe** | **String**|  | [optional] 
 **macAddressNie** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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

> VirtualMachineWithConfigContext virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachineWithConfigContext)





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
let writableVirtualMachineWithConfigContext = new NetBoxApi.WritableVirtualMachineWithConfigContext(); // WritableVirtualMachineWithConfigContext | 
apiInstance.virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachineWithConfigContext, (error, data, response) => {
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
 **writableVirtualMachineWithConfigContext** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualizationVirtualMachinesRead

> VirtualMachineWithConfigContext virtualizationVirtualMachinesRead(id)



Call to super to allow for caching

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

> VirtualMachineWithConfigContext virtualizationVirtualMachinesUpdate(id, writableVirtualMachineWithConfigContext)





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
let writableVirtualMachineWithConfigContext = new NetBoxApi.WritableVirtualMachineWithConfigContext(); // WritableVirtualMachineWithConfigContext | 
apiInstance.virtualizationVirtualMachinesUpdate(id, writableVirtualMachineWithConfigContext, (error, data, response) => {
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
 **writableVirtualMachineWithConfigContext** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

