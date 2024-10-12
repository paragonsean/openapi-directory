# EtMdbRestApiV1.MovieCastApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**movieCastSearchRead**](MovieCastApi.md#movieCastSearchRead) | **GET** /api/v1/movie-cast/search/{movie_title} | Return movie cast search result
[**movieCastSearchallRead**](MovieCastApi.md#movieCastSearchallRead) | **GET** /api/v1/movie-cast/searchall/{param} | Return movie cast search result



## movieCastSearchRead

> movieCastSearchRead(movieTitle)

Return movie cast search result

Return movie cast search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie cast * You can use both Amharic or English charset/font to search  For more details on how movie casts are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.MovieCastApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.movieCastSearchRead(movieTitle, (error, data, response) => {
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


## movieCastSearchallRead

> movieCastSearchallRead(param)

Return movie cast search result

Return movie cast search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or * character name  For more details on how movie casts are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.MovieCastApi();
let param = "param_example"; // String | 
apiInstance.movieCastSearchallRead(param, (error, data, response) => {
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
 **param** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

