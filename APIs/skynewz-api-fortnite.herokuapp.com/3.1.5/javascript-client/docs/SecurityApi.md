# FortniteRestApi.SecurityApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauthTokenPost**](SecurityApi.md#oauthTokenPost) | **POST** /oauth/token | Get a Bearer token



## oauthTokenPost

> OauthTokenPost200Response oauthTokenPost(email, password)

Get a Bearer token

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';

let apiInstance = new FortniteRestApi.SecurityApi();
let email = "email_example"; // String | 
let password = "password_example"; // String | 
apiInstance.oauthTokenPost(email, password, (error, data, response) => {
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
 **email** | **String**|  | 
 **password** | **String**|  | 

### Return type

[**OauthTokenPost200Response**](OauthTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, application/json
- **Accept**: application/json

