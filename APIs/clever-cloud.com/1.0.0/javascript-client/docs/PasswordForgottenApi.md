# CleverCloudApi.PasswordForgottenApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPasswordForgottenKey_0**](PasswordForgottenApi.md#getPasswordForgottenKey_0) | **GET** /password_forgotten/{key} | 
[**getPasswordForgotten_0**](PasswordForgottenApi.md#getPasswordForgotten_0) | **GET** /password_forgotten | 
[**postPasswordForgottenKey_0**](PasswordForgottenApi.md#postPasswordForgottenKey_0) | **POST** /password_forgotten/{key} | 
[**postPasswordForgotten_0**](PasswordForgottenApi.md#postPasswordForgotten_0) | **POST** /password_forgotten | 



## getPasswordForgottenKey_0

> getPasswordForgottenKey_0(key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PasswordForgottenApi();
let key = "key_example"; // String | 
apiInstance.getPasswordForgottenKey_0(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPasswordForgotten_0

> getPasswordForgotten_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PasswordForgottenApi();
apiInstance.getPasswordForgotten_0((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postPasswordForgottenKey_0

> postPasswordForgottenKey_0(key, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PasswordForgottenApi();
let key = "key_example"; // String | 
let opts = {
  'pass': "pass_example", // String | 
  'pass2': "pass2_example" // String | 
};
apiInstance.postPasswordForgottenKey_0(key, opts, (error, data, response) => {
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
 **key** | **String**|  | 
 **pass** | **String**|  | [optional] 
 **pass2** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postPasswordForgotten_0

> postPasswordForgotten_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PasswordForgottenApi();
let opts = {
  'login': "login_example", // String | 
  'dropTokens': "dropTokens_example", // String | 
  'testerPass': "testerPass_example" // String | 
};
apiInstance.postPasswordForgotten_0(opts, (error, data, response) => {
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
 **login** | **String**|  | [optional] 
 **dropTokens** | **String**|  | [optional] 
 **testerPass** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

