# ServiceFabricClientApis.MeshNetworksApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshNetworkCreateOrUpdate**](MeshNetworksApi.md#meshNetworkCreateOrUpdate) | **PUT** /Resources/Networks/{networkResourceName} | Creates or updates a Network resource.
[**meshNetworkDelete**](MeshNetworksApi.md#meshNetworkDelete) | **DELETE** /Resources/Networks/{networkResourceName} | Deletes the Network resource.
[**meshNetworkGet**](MeshNetworksApi.md#meshNetworkGet) | **GET** /Resources/Networks/{networkResourceName} | Gets the Network resource with the given name.
[**meshNetworkList**](MeshNetworksApi.md#meshNetworkList) | **GET** /Resources/Networks | Lists all the network resources.



## meshNetworkCreateOrUpdate

> NetworkResourceDescription meshNetworkCreateOrUpdate(apiVersion, networkResourceName, networkResourceDescription)

Creates or updates a Network resource.

Creates a Network resource with the specified name, description and properties. If Network resource with the same name exists, then it is updated with the specified description and properties. Network resource provides connectivity between application services.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshNetworksApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let networkResourceName = "networkResourceName_example"; // String | The identity of the network.
let networkResourceDescription = new ServiceFabricClientApis.NetworkResourceDescription(); // NetworkResourceDescription | Description for creating a Network resource.
apiInstance.meshNetworkCreateOrUpdate(apiVersion, networkResourceName, networkResourceDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **networkResourceName** | **String**| The identity of the network. | 
 **networkResourceDescription** | [**NetworkResourceDescription**](NetworkResourceDescription.md)| Description for creating a Network resource. | 

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshNetworkDelete

> meshNetworkDelete(apiVersion, networkResourceName)

Deletes the Network resource.

Deletes the Network resource identified by the name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshNetworksApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let networkResourceName = "networkResourceName_example"; // String | The identity of the network.
apiInstance.meshNetworkDelete(apiVersion, networkResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **networkResourceName** | **String**| The identity of the network. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshNetworkGet

> NetworkResourceDescription meshNetworkGet(apiVersion, networkResourceName)

Gets the Network resource with the given name.

Gets the information about the Network resource with the given name. The information include the description and other properties of the Network.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshNetworksApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let networkResourceName = "networkResourceName_example"; // String | The identity of the network.
apiInstance.meshNetworkGet(apiVersion, networkResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **networkResourceName** | **String**| The identity of the network. | 

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshNetworkList

> PagedNetworkResourceDescriptionList meshNetworkList(apiVersion)

Lists all the network resources.

Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshNetworksApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
apiInstance.meshNetworkList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]

### Return type

[**PagedNetworkResourceDescriptionList**](PagedNetworkResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

