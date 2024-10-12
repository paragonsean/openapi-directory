# AuthentiqApi.LoginApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pushLoginRequest**](LoginApi.md#pushLoginRequest) | **POST** /login | 



## pushLoginRequest

> PushLoginRequest200Response pushLoginRequest(callback, pushToken)



push sign-in request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.LoginApi();
let callback = "callback_example"; // String | URI App will connect to
let pushToken = new AuthentiqApi.PushToken(); // PushToken | Push Token.
apiInstance.pushLoginRequest(callback, pushToken, (error, data, response) => {
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
 **callback** | **String**| URI App will connect to | 
 **pushToken** | [**PushToken**](PushToken.md)| Push Token. | 

### Return type

[**PushLoginRequest200Response**](PushLoginRequest200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*

