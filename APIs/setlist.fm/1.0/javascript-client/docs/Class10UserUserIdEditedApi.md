# SetlistFmApi.Class10UserUserIdEditedApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10UserUserIdEditedGetUserEditedSetlistsGET**](Class10UserUserIdEditedApi.md#resource10UserUserIdEditedGetUserEditedSetlistsGET) | **GET** /1.0/user/{userId}/edited | .



## resource10UserUserIdEditedGetUserEditedSetlistsGET

> JsonSetlists resource10UserUserIdEditedGetUserEditedSetlistsGET(userId, opts)

.

&lt;p&gt; Get a list of setlists of concerts edited by a user. The list contains the current version, not the version edited. &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10UserUserIdEditedApi();
let userId = "userId_example"; // String | the user's userId
let opts = {
  'p': 1 // Number | the number of the result page
};
apiInstance.resource10UserUserIdEditedGetUserEditedSetlistsGET(userId, opts, (error, data, response) => {
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

