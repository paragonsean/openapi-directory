# HetznerCloudApi.ServerTypesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverTypesGet**](ServerTypesApi.md#serverTypesGet) | **GET** /server_types | Get all Server Types
[**serverTypesIdGet**](ServerTypesApi.md#serverTypesIdGet) | **GET** /server_types/{id} | Get a Server Type



## serverTypesGet

> ServerTypesGet200Response serverTypesGet(opts)

Get all Server Types

Gets all Server type objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerTypesApi();
let opts = {
  'name': "name_example" // String | Can be used to filter Server types by their name. The response will only contain the Server type matching the specified name.
};
apiInstance.serverTypesGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter Server types by their name. The response will only contain the Server type matching the specified name. | [optional] 

### Return type

[**ServerTypesGet200Response**](ServerTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverTypesIdGet

> ServerTypesIdGet200Response serverTypesIdGet(id)

Get a Server Type

Gets a specific Server type object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerTypesApi();
let id = 56; // Number | ID of Server Type
apiInstance.serverTypesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of Server Type | 

### Return type

[**ServerTypesIdGet200Response**](ServerTypesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

