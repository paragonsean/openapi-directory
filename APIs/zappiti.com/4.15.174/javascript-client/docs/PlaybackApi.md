# ZappitiPlayerApi.PlaybackApi

All URIs are relative to *http://192.168.1.5:8990*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lastMediaPost**](PlaybackApi.md#lastMediaPost) | **POST** /LastMedia | Get informations about last media playback
[**startVideoPost**](PlaybackApi.md#startVideoPost) | **POST** /StartVideo | Start the playback



## lastMediaPost

> LastMediaResult lastMediaPost(body)

Get informations about last media playback

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.PlaybackApi();
let body = new ZappitiPlayerApi.LastMediaRequest(); // LastMediaRequest | 
apiInstance.lastMediaPost(body, (error, data, response) => {
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
 **body** | [**LastMediaRequest**](LastMediaRequest.md)|  | 

### Return type

[**LastMediaResult**](LastMediaResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startVideoPost

> StartVideoResult startVideoPost(body)

Start the playback

Start the playback of the speficied video. 

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.PlaybackApi();
let body = new ZappitiPlayerApi.StartVideoRequest(); // StartVideoRequest | 
apiInstance.startVideoPost(body, (error, data, response) => {
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
 **body** | [**StartVideoRequest**](StartVideoRequest.md)|  | 

### Return type

[**StartVideoResult**](StartVideoResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

