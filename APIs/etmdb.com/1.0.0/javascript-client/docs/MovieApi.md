# EtMdbRestApiV1.MovieApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**movieSearchRead**](MovieApi.md#movieSearchRead) | **GET** /api/v1/movie/search/{movie_title} | Return movie search result



## movieSearchRead

> movieSearchRead(movieTitle)

Return movie search result

Return movie search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies * You can use both Amharic or English charset/font to search  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.MovieApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.movieSearchRead(movieTitle, (error, data, response) => {
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
 **movieTitle** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

