# Authentication.DefaultApi

All URIs are relative to *https://api.personio.de/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authPost**](DefaultApi.md#authPost) | **POST** /auth | 



## authPost

> AuthenticationTokenResponse authPost(clientId, clientSecret)



Request Authentication Token

### Example

```javascript
import Authentication from 'authentication';

let apiInstance = new Authentication.DefaultApi();
let clientId = "clientId_example"; // String | Client id of the downloaded credentials file
let clientSecret = "clientSecret_example"; // String | Client secret of the downloaded credentials file
apiInstance.authPost(clientId, clientSecret, (error, data, response) => {
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
 **clientId** | **String**| Client id of the downloaded credentials file | 
 **clientSecret** | **String**| Client secret of the downloaded credentials file | 

### Return type

[**AuthenticationTokenResponse**](AuthenticationTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

