# HetznerCloudApi.ISOsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isosGet**](ISOsApi.md#isosGet) | **GET** /isos | Get all ISOs
[**isosIdGet**](ISOsApi.md#isosIdGet) | **GET** /isos/{id} | Get an ISO



## isosGet

> IsosGet200Response isosGet(opts)

Get all ISOs

Returns all available ISO objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ISOsApi();
let opts = {
  'name': "name_example", // String | Can be used to filter ISOs by their name. The response will only contain the ISO matching the specified name.
  'architecture': "architecture_example", // String | Return only ISOs with the given architecture.
  'includeArchitectureWildcard': true // Boolean | Include Images with wildcard architecture (architecture is null). Works only if architecture filter is specified.
};
apiInstance.isosGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter ISOs by their name. The response will only contain the ISO matching the specified name. | [optional] 
 **architecture** | **String**| Return only ISOs with the given architecture. | [optional] 
 **includeArchitectureWildcard** | **Boolean**| Include Images with wildcard architecture (architecture is null). Works only if architecture filter is specified. | [optional] 

### Return type

[**IsosGet200Response**](IsosGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## isosIdGet

> IsosIdGet200Response isosIdGet(id)

Get an ISO

Returns a specific ISO object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ISOsApi();
let id = 56; // Number | ID of the ISO
apiInstance.isosIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the ISO | 

### Return type

[**IsosIdGet200Response**](IsosIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

