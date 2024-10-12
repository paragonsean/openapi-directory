# MusixmatchApi.SubtitleApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matcherSubtitleGetGet**](SubtitleApi.md#matcherSubtitleGetGet) | **GET** /matcher.subtitle.get | 
[**trackSubtitleGetGet**](SubtitleApi.md#trackSubtitleGetGet) | **GET** /track.subtitle.get | 



## matcherSubtitleGetGet

> MatcherSubtitleGetGet200Response matcherSubtitleGetGet(opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.SubtitleApi();
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'qTrack': "qTrack_example", // String | The song title
  'qArtist': "qArtist_example", // String |  The song artist
  'fSubtitleLength': 3.4, // Number | Filter by subtitle length in seconds
  'fSubtitleLengthMaxDeviation': 3.4 // Number | Max deviation for a subtitle length in seconds
};
apiInstance.matcherSubtitleGetGet(opts, (error, data, response) => {
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
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **qTrack** | **String**| The song title | [optional] 
 **qArtist** | **String**|  The song artist | [optional] 
 **fSubtitleLength** | **Number**| Filter by subtitle length in seconds | [optional] 
 **fSubtitleLengthMaxDeviation** | **Number**| Max deviation for a subtitle length in seconds | [optional] 

### Return type

[**MatcherSubtitleGetGet200Response**](MatcherSubtitleGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trackSubtitleGetGet

> MatcherSubtitleGetGet200Response trackSubtitleGetGet(trackId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.SubtitleApi();
let trackId = "trackId_example"; // String | The musiXmatch track id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example" // String | jsonp callback
};
apiInstance.trackSubtitleGetGet(trackId, opts, (error, data, response) => {
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

[**MatcherSubtitleGetGet200Response**](MatcherSubtitleGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

