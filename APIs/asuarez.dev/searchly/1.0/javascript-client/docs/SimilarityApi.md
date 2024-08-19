# SearchLyApiV1.SimilarityApi

All URIs are relative to *https://searchly.asuarez.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**srcSearchlyApiV1ControllersSimilarityByContent**](SimilarityApi.md#srcSearchlyApiV1ControllersSimilarityByContent) | **POST** /similarity/by_content | API endpoint to search similarity using content
[**srcSearchlyApiV1ControllersSimilarityBySong**](SimilarityApi.md#srcSearchlyApiV1ControllersSimilarityBySong) | **GET** /similarity/by_song | API endpoint to search similarity using a song identifier



## srcSearchlyApiV1ControllersSimilarityByContent

> APIResponseSimilarity srcSearchlyApiV1ControllersSimilarityByContent(srcSearchlyApiV1ControllersSimilarityByContentRequest)

API endpoint to search similarity using content

Endpoint for an end-user client to search similarity by content.  If you want to run the /similarity/by_content operation, you can do so via an HTTP POST command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/similarity/by_content &#x60;&#x60;&#x60; 

### Example

```javascript
import SearchLyApiV1 from 'search_ly_api_v1';

let apiInstance = new SearchLyApiV1.SimilarityApi();
let srcSearchlyApiV1ControllersSimilarityByContentRequest = new SearchLyApiV1.SrcSearchlyApiV1ControllersSimilarityByContentRequest(); // SrcSearchlyApiV1ControllersSimilarityByContentRequest | Body wrapper for the request.
apiInstance.srcSearchlyApiV1ControllersSimilarityByContent(srcSearchlyApiV1ControllersSimilarityByContentRequest, (error, data, response) => {
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
 **srcSearchlyApiV1ControllersSimilarityByContentRequest** | [**SrcSearchlyApiV1ControllersSimilarityByContentRequest**](SrcSearchlyApiV1ControllersSimilarityByContentRequest.md)| Body wrapper for the request. | 

### Return type

[**APIResponseSimilarity**](APIResponseSimilarity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/text


## srcSearchlyApiV1ControllersSimilarityBySong

> APIResponseSimilarity srcSearchlyApiV1ControllersSimilarityBySong(songId)

API endpoint to search similarity using a song identifier

Endpoint for an end-user client to search similarity by song identifier.  If you want to run the /similarity/by_song operation, you can do so via an HTTP GET command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/similarity/by_song &#x60;&#x60;&#x60; 

### Example

```javascript
import SearchLyApiV1 from 'search_ly_api_v1';

let apiInstance = new SearchLyApiV1.SimilarityApi();
let songId = 234; // Number | Song identifier.
apiInstance.srcSearchlyApiV1ControllersSimilarityBySong(songId, (error, data, response) => {
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
 **songId** | **Number**| Song identifier. | 

### Return type

[**APIResponseSimilarity**](APIResponseSimilarity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/text

