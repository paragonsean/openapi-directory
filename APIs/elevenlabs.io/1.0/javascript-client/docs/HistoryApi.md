# ElevenLabsApiDocumentation.HistoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteHistoryItemV1HistoryHistoryItemIdDelete**](HistoryApi.md#deleteHistoryItemV1HistoryHistoryItemIdDelete) | **DELETE** /v1/history/{history_item_id} | Delete History Item
[**deleteHistoryItemsV1HistoryDeletePost**](HistoryApi.md#deleteHistoryItemsV1HistoryDeletePost) | **POST** /v1/history/delete | Delete History Items
[**downloadHistoryItemsV1HistoryDownloadPost**](HistoryApi.md#downloadHistoryItemsV1HistoryDownloadPost) | **POST** /v1/history/download | Download History Items
[**getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet**](HistoryApi.md#getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet) | **GET** /v1/history/{history_item_id}/audio | Get Audio From History Item
[**getGeneratedItemsV1HistoryGet**](HistoryApi.md#getGeneratedItemsV1HistoryGet) | **GET** /v1/history | Get Generated Items



## deleteHistoryItemV1HistoryHistoryItemIdDelete

> Object deleteHistoryItemV1HistoryHistoryItemIdDelete(historyItemId, opts)

Delete History Item

Delete a history item by its ID

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.HistoryApi();
let historyItemId = "VW7YKqPnjY4h39yTbx2L"; // String | History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.deleteHistoryItemV1HistoryHistoryItemIdDelete(historyItemId, opts, (error, data, response) => {
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
 **historyItemId** | **String**| History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs. | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteHistoryItemsV1HistoryDeletePost

> Object deleteHistoryItemsV1HistoryDeletePost(bodyDeleteHistoryItemsV1HistoryDeletePost, opts)

Delete History Items

Delete a number of history items by their IDs.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.HistoryApi();
let bodyDeleteHistoryItemsV1HistoryDeletePost = new ElevenLabsApiDocumentation.BodyDeleteHistoryItemsV1HistoryDeletePost(); // BodyDeleteHistoryItemsV1HistoryDeletePost | 
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.deleteHistoryItemsV1HistoryDeletePost(bodyDeleteHistoryItemsV1HistoryDeletePost, opts, (error, data, response) => {
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
 **bodyDeleteHistoryItemsV1HistoryDeletePost** | [**BodyDeleteHistoryItemsV1HistoryDeletePost**](BodyDeleteHistoryItemsV1HistoryDeletePost.md)|  | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadHistoryItemsV1HistoryDownloadPost

> downloadHistoryItemsV1HistoryDownloadPost(bodyDownloadHistoryItemsV1HistoryDownloadPost, opts)

Download History Items

Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.HistoryApi();
let bodyDownloadHistoryItemsV1HistoryDownloadPost = new ElevenLabsApiDocumentation.BodyDownloadHistoryItemsV1HistoryDownloadPost(); // BodyDownloadHistoryItemsV1HistoryDownloadPost | 
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.downloadHistoryItemsV1HistoryDownloadPost(bodyDownloadHistoryItemsV1HistoryDownloadPost, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyDownloadHistoryItemsV1HistoryDownloadPost** | [**BodyDownloadHistoryItemsV1HistoryDownloadPost**](BodyDownloadHistoryItemsV1HistoryDownloadPost.md)|  | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet

> getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet(historyItemId, opts)

Get Audio From History Item

Returns the audio of an history item.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.HistoryApi();
let historyItemId = "VW7YKqPnjY4h39yTbx2L"; // String | History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getAudioFromHistoryItemV1HistoryHistoryItemIdAudioGet(historyItemId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **historyItemId** | **String**| History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs. | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/mpeg, application/json


## getGeneratedItemsV1HistoryGet

> GetHistoryResponseModel getGeneratedItemsV1HistoryGet(opts)

Get Generated Items

Returns metadata about all your generated audio.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.HistoryApi();
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getGeneratedItemsV1HistoryGet(opts, (error, data, response) => {
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
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

[**GetHistoryResponseModel**](GetHistoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

