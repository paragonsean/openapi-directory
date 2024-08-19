# SearchLyApiV1.SongApi

All URIs are relative to *https://searchly.asuarez.dev/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**srcSearchlyApiV1ControllersSongSearch**](SongApi.md#srcSearchlyApiV1ControllersSongSearch) | **GET** /song/search | API endpoint to search songs from the database given a query



## srcSearchlyApiV1ControllersSongSearch

> APIResponseSong srcSearchlyApiV1ControllersSongSearch(query)

API endpoint to search songs from the database given a query

Endpoint for an end-user client to search songs from the database given a String query.  If you want to run the /song/search operation, you can do so via an HTTP GET command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/song/search &#x60;&#x60;&#x60; 

### Example

```javascript
import SearchLyApiV1 from 'search_ly_api_v1';

let apiInstance = new SearchLyApiV1.SongApi();
let query = "Miley Cyrus"; // String | Query.
apiInstance.srcSearchlyApiV1ControllersSongSearch(query, (error, data, response) => {
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
 **query** | **String**| Query. | 

### Return type

[**APIResponseSong**](APIResponseSong.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/text

