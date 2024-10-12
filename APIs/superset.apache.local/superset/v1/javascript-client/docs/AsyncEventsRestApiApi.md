# Superset.AsyncEventsRestApiApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asyncEventGet**](AsyncEventsRestApiApi.md#asyncEventGet) | **GET** /async_event/ | 



## asyncEventGet

> AsyncEventGet200Response asyncEventGet(opts)



Reads off of the Redis events stream, using the user&#39;s JWT token and optional query params for last event received.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AsyncEventsRestApiApi();
let opts = {
  'lastId': "lastId_example" // String | Last ID received by the client
};
apiInstance.asyncEventGet(opts, (error, data, response) => {
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
 **lastId** | **String**| Last ID received by the client | [optional] 

### Return type

[**AsyncEventGet200Response**](AsyncEventGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

