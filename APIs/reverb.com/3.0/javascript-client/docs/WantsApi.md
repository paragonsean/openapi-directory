# Reverb.WantsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wantsGet**](WantsApi.md#wantsGet) | **GET** /wants | A list of wanted items by the user
[**wantsIdDelete**](WantsApi.md#wantsIdDelete) | **DELETE** /wants/{id} | Unmark an item wanted.
[**wantsIdPut**](WantsApi.md#wantsIdPut) | **PUT** /wants/{id} | Mark an item wanted. Returns 200 on success or 422 on failure.



## wantsGet

> wantsGet()

A list of wanted items by the user

A list of wanted items by the user

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.WantsApi();
apiInstance.wantsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wantsIdDelete

> wantsIdDelete(id)

Unmark an item wanted.

Unmark an item wanted.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.WantsApi();
let id = "id_example"; // String | 
apiInstance.wantsIdDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wantsIdPut

> wantsIdPut(id)

Mark an item wanted. Returns 200 on success or 422 on failure.

Mark an item wanted. Returns 200 on success or 422 on failure.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.WantsApi();
let id = "id_example"; // String | 
apiInstance.wantsIdPut(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

