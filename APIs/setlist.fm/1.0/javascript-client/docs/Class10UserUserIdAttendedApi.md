# SetlistFmApi.Class10UserUserIdAttendedApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10UserUserIdAttendedGetUserAttendedSetlistsGET**](Class10UserUserIdAttendedApi.md#resource10UserUserIdAttendedGetUserAttendedSetlistsGET) | **GET** /1.0/user/{userId}/attended | .



## resource10UserUserIdAttendedGetUserAttendedSetlistsGET

> JsonSetlists resource10UserUserIdAttendedGetUserAttendedSetlistsGET(userId, opts)

.

&lt;p&gt; Get a list of setlists of concerts attended by a user. &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10UserUserIdAttendedApi();
let userId = "userId_example"; // String | the user's userId
let opts = {
  'p': 1 // Number | the number of the result page
};
apiInstance.resource10UserUserIdAttendedGetUserAttendedSetlistsGET(userId, opts, (error, data, response) => {
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
 **p** | **Number**| the number of the result page | [optional] [default to 1]

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

