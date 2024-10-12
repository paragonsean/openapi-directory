# FortniteRestApi.StatsApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statsIdPlateformIdGet**](StatsApi.md#statsIdPlateformIdGet) | **GET** /stats/id/{plateform}/{id} | Get user&#39;s stats by user id
[**statsPlateformUsernameGet**](StatsApi.md#statsPlateformUsernameGet) | **GET** /stats/{plateform}/{username} | Get user&#39;s stats by username



## statsIdPlateformIdGet

> StatsIdPlateformIdGet200Response statsIdPlateformIdGet(plateform, id)

Get user&#39;s stats by user id

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';
let defaultClient = FortniteRestApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FortniteRestApi.StatsApi();
let plateform = "plateform_example"; // String | Playing plateform, can be xb1, ps4 or pc
let id = "id_example"; // String | Player ID
apiInstance.statsIdPlateformIdGet(plateform, id, (error, data, response) => {
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
 **plateform** | **String**| Playing plateform, can be xb1, ps4 or pc | 
 **id** | **String**| Player ID | 

### Return type

[**StatsIdPlateformIdGet200Response**](StatsIdPlateformIdGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## statsPlateformUsernameGet

> StatsIdPlateformIdGet200Response statsPlateformUsernameGet(plateform, username)

Get user&#39;s stats by username

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';
let defaultClient = FortniteRestApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FortniteRestApi.StatsApi();
let plateform = "plateform_example"; // String | Playing plateform, can be xb1, ps4 or pc
let username = "username_example"; // String | Player username
apiInstance.statsPlateformUsernameGet(plateform, username, (error, data, response) => {
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
 **plateform** | **String**| Playing plateform, can be xb1, ps4 or pc | 
 **username** | **String**| Player username | 

### Return type

[**StatsIdPlateformIdGet200Response**](StatsIdPlateformIdGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

