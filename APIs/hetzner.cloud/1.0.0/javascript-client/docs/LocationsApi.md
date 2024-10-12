# HetznerCloudApi.LocationsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsGet**](LocationsApi.md#locationsGet) | **GET** /locations | Get all Locations
[**locationsIdGet**](LocationsApi.md#locationsIdGet) | **GET** /locations/{id} | Get a Location



## locationsGet

> LocationsGet200Response locationsGet(opts)

Get all Locations

Returns all Location objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LocationsApi();
let opts = {
  'name': "name_example" // String | Can be used to filter Locations by their name. The response will only contain the Location matching the specified name.
};
apiInstance.locationsGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter Locations by their name. The response will only contain the Location matching the specified name. | [optional] 

### Return type

[**LocationsGet200Response**](LocationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsIdGet

> LocationsIdGet200Response locationsIdGet(id)

Get a Location

Returns a specific Location object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LocationsApi();
let id = 56; // Number | ID of Location
apiInstance.locationsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of Location | 

### Return type

[**LocationsIdGet200Response**](LocationsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

