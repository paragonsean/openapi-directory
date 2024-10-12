# UebermapsApiEndpoints.AuthenticationApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticationPost**](AuthenticationApi.md#authenticationPost) | **POST** /authentication | Sign in user



## authenticationPost

> UserFullProfile authenticationPost(user)

Sign in user

Sign in user. Wrap authentication parameters in [user].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AuthenticationApi();
let user = new UebermapsApiEndpoints.UserAuthentication(); // UserAuthentication | user authentication attributes
apiInstance.authenticationPost(user, (error, data, response) => {
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
 **user** | [**UserAuthentication**](UserAuthentication.md)| user authentication attributes | 

### Return type

[**UserFullProfile**](UserFullProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

