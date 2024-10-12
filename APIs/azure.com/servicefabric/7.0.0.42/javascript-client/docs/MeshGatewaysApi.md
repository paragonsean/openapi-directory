# ServiceFabricClientApis.MeshGatewaysApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshGatewayCreateOrUpdate**](MeshGatewaysApi.md#meshGatewayCreateOrUpdate) | **PUT** /Resources/Gateways/{gatewayResourceName} | Creates or updates a Gateway resource.
[**meshGatewayDelete**](MeshGatewaysApi.md#meshGatewayDelete) | **DELETE** /Resources/Gateways/{gatewayResourceName} | Deletes the Gateway resource.
[**meshGatewayGet**](MeshGatewaysApi.md#meshGatewayGet) | **GET** /Resources/Gateways/{gatewayResourceName} | Gets the Gateway resource with the given name.
[**meshGatewayList**](MeshGatewaysApi.md#meshGatewayList) | **GET** /Resources/Gateways | Lists all the gateway resources.



## meshGatewayCreateOrUpdate

> GatewayResourceDescription meshGatewayCreateOrUpdate(apiVersion, gatewayResourceName, gatewayResourceDescription)

Creates or updates a Gateway resource.

Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshGatewaysApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
let gatewayResourceDescription = new ServiceFabricClientApis.GatewayResourceDescription(); // GatewayResourceDescription | Description for creating a Gateway resource.
apiInstance.meshGatewayCreateOrUpdate(apiVersion, gatewayResourceName, gatewayResourceDescription, (error, data, response) => {
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
 **gatewayResourceName** | **String**| The identity of the gateway. | 
 **gatewayResourceDescription** | [**GatewayResourceDescription**](GatewayResourceDescription.md)| Description for creating a Gateway resource. | 

### Return type

[**GatewayResourceDescription**](GatewayResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshGatewayDelete

> meshGatewayDelete(apiVersion, gatewayResourceName)

Deletes the Gateway resource.

Deletes the Gateway resource identified by the name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshGatewaysApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
apiInstance.meshGatewayDelete(apiVersion, gatewayResourceName, (error, data, response) => {
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
 **gatewayResourceName** | **String**| The identity of the gateway. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshGatewayGet

> GatewayResourceDescription meshGatewayGet(apiVersion, gatewayResourceName)

Gets the Gateway resource with the given name.

Gets the information about the Gateway resource with the given name. The information include the description and other properties of the Gateway.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshGatewaysApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
apiInstance.meshGatewayGet(apiVersion, gatewayResourceName, (error, data, response) => {
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
 **gatewayResourceName** | **String**| The identity of the gateway. | 

### Return type

[**GatewayResourceDescription**](GatewayResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshGatewayList

> PagedGatewayResourceDescriptionList meshGatewayList(apiVersion)

Lists all the gateway resources.

Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshGatewaysApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
apiInstance.meshGatewayList(apiVersion, (error, data, response) => {
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

[**PagedGatewayResourceDescriptionList**](PagedGatewayResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

