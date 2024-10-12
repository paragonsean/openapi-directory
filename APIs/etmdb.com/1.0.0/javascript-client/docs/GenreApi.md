# EtMdbRestApiV1.GenreApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genreSearchRead**](GenreApi.md#genreSearchRead) | **GET** /api/v1/genre/search/{movie_title} | Return movie genre search result
[**genreSearchallRead**](GenreApi.md#genreSearchallRead) | **GET** /api/v1/genre/searchall/{movie_genre_type} | Return movie genre search result



## genreSearchRead

> genreSearchRead(movieTitle)

Return movie genre search result

Return movie genre search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie genres * You can use both Amharic or English charset/font to search  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.GenreApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.genreSearchRead(movieTitle, (error, data, response) => {
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


## genreSearchallRead

> genreSearchallRead(movieGenreType)

Return movie genre search result

Return movie genre search result  ### Response Class (Status 200)  * __{movie_genre_type}__: Used as a key word to search movie genres  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.GenreApi();
let movieGenreType = "movieGenreType_example"; // String | 
apiInstance.genreSearchallRead(movieGenreType, (error, data, response) => {
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
 **movieGenreType** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

