# IxApi.NetworkFeaturesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkFeaturesList**](NetworkFeaturesApi.md#networkFeaturesList) | **GET** /network-features | 
[**networkFeaturesRead**](NetworkFeaturesApi.md#networkFeaturesRead) | **GET** /network-features/{id} | 



## networkFeaturesList

> [NetworkFeature] networkFeaturesList(opts)



List available network features.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeaturesApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'type': "type_example", // String | Filter by type
  'required': "required_example", // String | Filter by required
  'networkService': "networkService_example", // String | Filter by network_service
  'name': "name_example" // String | Filter by name
};
apiInstance.networkFeaturesList(opts, (error, data, response) => {
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
 **type** | **String**| Filter by type | [optional] 
 **required** | **String**| Filter by required | [optional] 
 **networkService** | **String**| Filter by network_service | [optional] 
 **name** | **String**| Filter by name | [optional] 

### Return type

[**[NetworkFeature]**](NetworkFeature.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkFeaturesRead

> NetworkFeature networkFeaturesRead(id)



Get a single network feature by it&#39;s id.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeaturesApi();
let id = "id_example"; // String | Get by id
apiInstance.networkFeaturesRead(id, (error, data, response) => {
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

[**NetworkFeature**](NetworkFeature.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

