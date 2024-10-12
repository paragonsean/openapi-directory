# MusixmatchApi.SnippetApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trackSnippetGetGet**](SnippetApi.md#trackSnippetGetGet) | **GET** /track.snippet.get | 



## trackSnippetGetGet

> TrackSnippetGetGet200Response trackSnippetGetGet(trackId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.SnippetApi();
let trackId = "trackId_example"; // String | The musiXmatch track id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example" // String | jsonp callback
};
apiInstance.trackSnippetGetGet(trackId, opts, (error, data, response) => {
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
 **trackId** | **String**| The musiXmatch track id | 
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 

### Return type

[**TrackSnippetGetGet200Response**](TrackSnippetGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

