# IxApi.MetroAreaNetworksApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metroAreaNetworksList**](MetroAreaNetworksApi.md#metroAreaNetworksList) | **GET** /metro-area-networks | 
[**metroAreaNetworksRead**](MetroAreaNetworksApi.md#metroAreaNetworksRead) | **GET** /metro-area-networks/{id} | 



## metroAreaNetworksList

> [MetroAreaNetwork] metroAreaNetworksList(opts)



List all MetroAreaNetworks

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MetroAreaNetworksApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'name': "name_example", // String | Filter by name
  'metroArea': "metroArea_example", // String | Filter by metro_area
  'serviceProvider': "serviceProvider_example" // String | Filter by service_provider
};
apiInstance.metroAreaNetworksList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **name** | **String**| Filter by name | [optional] 
 **metroArea** | **String**| Filter by metro_area | [optional] 
 **serviceProvider** | **String**| Filter by service_provider | [optional] 

### Return type

[**[MetroAreaNetwork]**](MetroAreaNetwork.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metroAreaNetworksRead

> MetroAreaNetwork metroAreaNetworksRead(id)



Retrieve a MetroAreaNetwork

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MetroAreaNetworksApi();
let id = "id_example"; // String | Get by id
apiInstance.metroAreaNetworksRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**MetroAreaNetwork**](MetroAreaNetwork.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

