# ElevenLabsApiDocumentation.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserInfoV1UserGet**](UserApi.md#getUserInfoV1UserGet) | **GET** /v1/user | Get User Info
[**getUserSubscriptionInfoV1UserSubscriptionGet**](UserApi.md#getUserSubscriptionInfoV1UserSubscriptionGet) | **GET** /v1/user/subscription | Get User Subscription Info



## getUserInfoV1UserGet

> UserResponseModel getUserInfoV1UserGet(opts)

Get User Info

Gets information about the user

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.UserApi();
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getUserInfoV1UserGet(opts, (error, data, response) => {
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
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

[**UserResponseModel**](UserResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserSubscriptionInfoV1UserSubscriptionGet

> ExtendedSubscriptionResponseModel getUserSubscriptionInfoV1UserSubscriptionGet(opts)

Get User Subscription Info

Gets extended information about the users subscription

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.UserApi();
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getUserSubscriptionInfoV1UserSubscriptionGet(opts, (error, data, response) => {
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
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

[**ExtendedSubscriptionResponseModel**](ExtendedSubscriptionResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

