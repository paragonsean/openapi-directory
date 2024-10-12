# EtMdbRestApiV1.WatchlistApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watchlistSearchRead**](WatchlistApi.md#watchlistSearchRead) | **GET** /api/v1/watchlist/search/{movie_title} | Return watchlist search result
[**watchlistSearchallRead**](WatchlistApi.md#watchlistSearchallRead) | **GET** /api/v1/watchlist/searchall/{param} | Return watchlist search result



## watchlistSearchRead

> watchlistSearchRead(movieTitle)

Return watchlist search result

Return watchlist search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies on watchlist * You can use both Amharic or English charset/font to search  For more details on how watchlist are listed [see here][ref]. [ref]: https://etmdb.com/en/movies/watchlist/id

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.WatchlistApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.watchlistSearchRead(movieTitle, (error, data, response) => {
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


## watchlistSearchallRead

> watchlistSearchallRead(param)

Return watchlist search result

Return watchlist search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or  For more details on how watchlist are listed [see here][ref]. [ref]: https://etmdb.com/en/movies/watchlist/id

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.WatchlistApi();
let param = "param_example"; // String | 
apiInstance.watchlistSearchallRead(param, (error, data, response) => {
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

