# SetlistFmApi.Class10UserUserIdApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10UserUserIdGetUserGET**](Class10UserUserIdApi.md#resource10UserUserIdGetUserGET) | **GET** /1.0/user/{userId} | Get a user by userId.



## resource10UserUserIdGetUserGET

> JsonUser resource10UserUserIdGetUserGET(userId)

Get a user by userId.

Get a user by userId. (deprecated)  Note: This endpoint always returns a result, even if the user doesn&#39;t exist

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10UserUserIdApi();
let userId = "userId_example"; // String | the user's userId
apiInstance.resource10UserUserIdGetUserGET(userId, (error, data, response) => {
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
 **userId** | **String**| the user&#39;s userId | 

### Return type

[**JsonUser**](JsonUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

