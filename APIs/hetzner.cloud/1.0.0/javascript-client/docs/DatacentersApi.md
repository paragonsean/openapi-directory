# HetznerCloudApi.DatacentersApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacentersGet**](DatacentersApi.md#datacentersGet) | **GET** /datacenters | Get all Datacenters
[**datacentersIdGet**](DatacentersApi.md#datacentersIdGet) | **GET** /datacenters/{id} | Get a Datacenter



## datacentersGet

> DatacentersGet200Response datacentersGet(opts)

Get all Datacenters

Returns all Datacenter objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.DatacentersApi();
let opts = {
  'name': "name_example" // String | Can be used to filter Datacenters by their name. The response will only contain the Datacenter matching the specified name. When the name does not match the Datacenter name format, an `invalid_input` error is returned.
};
apiInstance.datacentersGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter Datacenters by their name. The response will only contain the Datacenter matching the specified name. When the name does not match the Datacenter name format, an &#x60;invalid_input&#x60; error is returned. | [optional] 

### Return type

[**DatacentersGet200Response**](DatacentersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datacentersIdGet

> DatacentersIdGet200Response datacentersIdGet(id)

Get a Datacenter

Returns a specific Datacenter object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.DatacentersApi();
let id = 56; // Number | ID of Datacenter
apiInstance.datacentersIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of Datacenter | 

### Return type

[**DatacentersIdGet200Response**](DatacentersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

