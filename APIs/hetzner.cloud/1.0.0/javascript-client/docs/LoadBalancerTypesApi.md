# HetznerCloudApi.LoadBalancerTypesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadBalancerTypesGet**](LoadBalancerTypesApi.md#loadBalancerTypesGet) | **GET** /load_balancer_types | Get all Load Balancer Types
[**loadBalancerTypesIdGet**](LoadBalancerTypesApi.md#loadBalancerTypesIdGet) | **GET** /load_balancer_types/{id} | Get a Load Balancer Type



## loadBalancerTypesGet

> LoadBalancerTypesGet200Response loadBalancerTypesGet(opts)

Get all Load Balancer Types

Gets all Load Balancer type objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerTypesApi();
let opts = {
  'name': "name_example" // String | Can be used to filter Load Balancer types by their name. The response will only contain the Load Balancer type matching the specified name.
};
apiInstance.loadBalancerTypesGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter Load Balancer types by their name. The response will only contain the Load Balancer type matching the specified name. | [optional] 

### Return type

[**LoadBalancerTypesGet200Response**](LoadBalancerTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancerTypesIdGet

> LoadBalancerTypesIdGet200Response loadBalancerTypesIdGet(id)

Get a Load Balancer Type

Gets a specific Load Balancer type object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerTypesApi();
let id = 56; // Number | ID of Load Balancer type
apiInstance.loadBalancerTypesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of Load Balancer type | 

### Return type

[**LoadBalancerTypesIdGet200Response**](LoadBalancerTypesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

