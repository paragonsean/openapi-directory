# NativeAdsPublisherApi.AuthApi

All URIs are relative to *https://api.nativeads.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authDefaultLoginPost**](AuthApi.md#authDefaultLoginPost) | **POST** /auth/default/login | 



## authDefaultLoginPost

> AuthResponse authDefaultLoginPost(username, password)



Returns Native Ads Publisher API token

### Example

```javascript
import NativeAdsPublisherApi from 'native_ads_publisher_api';

let apiInstance = new NativeAdsPublisherApi.AuthApi();
let username = "username_example"; // String | Native Ads Publisher username
let password = "password_example"; // String | Native Ads Publisher password
apiInstance.authDefaultLoginPost(username, password, (error, data, response) => {
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
 **username** | **String**| Native Ads Publisher username | 
 **password** | **String**| Native Ads Publisher password | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

