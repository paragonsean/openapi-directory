# JellyfinApi.SubtitleApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSubtitle**](SubtitleApi.md#deleteSubtitle) | **DELETE** /Videos/{itemId}/Subtitles/{index} | Deletes an external subtitle file.
[**downloadRemoteSubtitles**](SubtitleApi.md#downloadRemoteSubtitles) | **POST** /Items/{itemId}/RemoteSearch/Subtitles/{subtitleId} | Downloads a remote subtitle.
[**getFallbackFont**](SubtitleApi.md#getFallbackFont) | **GET** /FallbackFont/Fonts/{name} | Gets a fallback font file.
[**getFallbackFontList**](SubtitleApi.md#getFallbackFontList) | **GET** /FallbackFont/Fonts | Gets a list of available fallback font files.
[**getRemoteSubtitles**](SubtitleApi.md#getRemoteSubtitles) | **GET** /Providers/Subtitles/Subtitles/{id} | Gets the remote subtitles.
[**getSubtitle**](SubtitleApi.md#getSubtitle) | **GET** /Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/Stream.{format} | Gets subtitles in a specified format.
[**getSubtitlePlaylist**](SubtitleApi.md#getSubtitlePlaylist) | **GET** /Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8 | Gets an HLS subtitle playlist.
[**getSubtitleWithTicks**](SubtitleApi.md#getSubtitleWithTicks) | **GET** /Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/{startPositionTicks}/Stream.{format} | Gets subtitles in a specified format.
[**searchRemoteSubtitles**](SubtitleApi.md#searchRemoteSubtitles) | **GET** /Items/{itemId}/RemoteSearch/Subtitles/{language} | Search remote subtitles.
[**uploadSubtitle**](SubtitleApi.md#uploadSubtitle) | **POST** /Videos/{itemId}/Subtitles | Upload an external subtitle file.



## deleteSubtitle

> deleteSubtitle(itemId, index)

Deletes an external subtitle file.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item id.
let index = 56; // Number | The index of the subtitle file.
apiInstance.deleteSubtitle(itemId, index, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **index** | **Number**| The index of the subtitle file. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## downloadRemoteSubtitles

> downloadRemoteSubtitles(itemId, subtitleId)

Downloads a remote subtitle.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item id.
let subtitleId = "subtitleId_example"; // String | The subtitle id.
apiInstance.downloadRemoteSubtitles(itemId, subtitleId, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **subtitleId** | **String**| The subtitle id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFallbackFont

> File getFallbackFont(name)

Gets a fallback font file.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
let name = "name_example"; // String | The name of the fallback font file to get.
apiInstance.getFallbackFont(name, (error, data, response) => {
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
 **name** | **String**| The name of the fallback font file to get. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: font/*


## getFallbackFontList

> [FontFile] getFallbackFontList()

Gets a list of available fallback font files.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
apiInstance.getFallbackFontList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[FontFile]**](FontFile.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRemoteSubtitles

> File getRemoteSubtitles(id)

Gets the remote subtitles.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
let id = "id_example"; // String | The item id.
apiInstance.getRemoteSubtitles(id, (error, data, response) => {
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
 **id** | **String**| The item id. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/*


## getSubtitle

> File getSubtitle(itemId, mediaSourceId, index, format, opts)

Gets subtitles in a specified format.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item id.
let mediaSourceId = "mediaSourceId_example"; // String | The media source id.
let index = 56; // Number | The subtitle stream index.
let format = "format_example"; // String | The format of the returned subtitle.
let opts = {
  'endPositionTicks': 789, // Number | Optional. The end position of the subtitle in ticks.
  'copyTimestamps': false, // Boolean | Optional. Whether to copy the timestamps.
  'addVttTimeMap': false, // Boolean | Optional. Whether to add a VTT time map.
  'startPositionTicks': 0 // Number | Optional. The start position of the subtitle in ticks.
};
apiInstance.getSubtitle(itemId, mediaSourceId, index, format, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **mediaSourceId** | **String**| The media source id. | 
 **index** | **Number**| The subtitle stream index. | 
 **format** | **String**| The format of the returned subtitle. | 
 **endPositionTicks** | **Number**| Optional. The end position of the subtitle in ticks. | [optional] 
 **copyTimestamps** | **Boolean**| Optional. Whether to copy the timestamps. | [optional] [default to false]
 **addVttTimeMap** | **Boolean**| Optional. Whether to add a VTT time map. | [optional] [default to false]
 **startPositionTicks** | **Number**| Optional. The start position of the subtitle in ticks. | [optional] [default to 0]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/*


## getSubtitlePlaylist

> File getSubtitlePlaylist(itemId, index, mediaSourceId, segmentLength)

Gets an HLS subtitle playlist.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item id.
let index = 56; // Number | The subtitle stream index.
let mediaSourceId = "mediaSourceId_example"; // String | The media source id.
let segmentLength = 56; // Number | The subtitle segment length.
apiInstance.getSubtitlePlaylist(itemId, index, mediaSourceId, segmentLength, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **index** | **Number**| The subtitle stream index. | 
 **mediaSourceId** | **String**| The media source id. | 
 **segmentLength** | **Number**| The subtitle segment length. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-mpegURL


## getSubtitleWithTicks

> File getSubtitleWithTicks(itemId, mediaSourceId, index, startPositionTicks, format, opts)

Gets subtitles in a specified format.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item id.
let mediaSourceId = "mediaSourceId_example"; // String | The media source id.
let index = 56; // Number | The subtitle stream index.
let startPositionTicks = 789; // Number | Optional. The start position of the subtitle in ticks.
let format = "format_example"; // String | The format of the returned subtitle.
let opts = {
  'endPositionTicks': 789, // Number | Optional. The end position of the subtitle in ticks.
  'copyTimestamps': false, // Boolean | Optional. Whether to copy the timestamps.
  'addVttTimeMap': false // Boolean | Optional. Whether to add a VTT time map.
};
apiInstance.getSubtitleWithTicks(itemId, mediaSourceId, index, startPositionTicks, format, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **mediaSourceId** | **String**| The media source id. | 
 **index** | **Number**| The subtitle stream index. | 
 **startPositionTicks** | **Number**| Optional. The start position of the subtitle in ticks. | 
 **format** | **String**| The format of the returned subtitle. | 
 **endPositionTicks** | **Number**| Optional. The end position of the subtitle in ticks. | [optional] 
 **copyTimestamps** | **Boolean**| Optional. Whether to copy the timestamps. | [optional] [default to false]
 **addVttTimeMap** | **Boolean**| Optional. Whether to add a VTT time map. | [optional] [default to false]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/*


## searchRemoteSubtitles

> [RemoteSubtitleInfo] searchRemoteSubtitles(itemId, language, opts)

Search remote subtitles.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item id.
let language = "language_example"; // String | The language of the subtitles.
let opts = {
  'isPerfectMatch': true // Boolean | Optional. Only show subtitles which are a perfect match.
};
apiInstance.searchRemoteSubtitles(itemId, language, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **language** | **String**| The language of the subtitles. | 
 **isPerfectMatch** | **Boolean**| Optional. Only show subtitles which are a perfect match. | [optional] 

### Return type

[**[RemoteSubtitleInfo]**](RemoteSubtitleInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## uploadSubtitle

> uploadSubtitle(itemId, uploadSubtitleDto)

Upload an external subtitle file.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.SubtitleApi();
let itemId = "itemId_example"; // String | The item the subtitle belongs to.
let uploadSubtitleDto = new JellyfinApi.UploadSubtitleDto(); // UploadSubtitleDto | The request body.
apiInstance.uploadSubtitle(itemId, uploadSubtitleDto, (error, data, response) => {
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
 **itemId** | **String**| The item the subtitle belongs to. | 
 **uploadSubtitleDto** | [**UploadSubtitleDto**](UploadSubtitleDto.md)| The request body. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

