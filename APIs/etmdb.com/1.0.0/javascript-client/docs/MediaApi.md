# EtMdbRestApiV1.MediaApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaSearchRead**](MediaApi.md#mediaSearchRead) | **GET** /api/v1/media/search/{movie_title} | Return movie media search result
[**mediaSearchallRead**](MediaApi.md#mediaSearchallRead) | **GET** /api/v1/media/searchall/{user} | Return cast media search result



## mediaSearchRead

> mediaSearchRead(movieTitle)

Return movie media search result

Return movie media search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search media for movies * You can use both Amharic or English charset/font to search  For more details on how media is listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.MediaApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.mediaSearchRead(movieTitle, (error, data, response) => {
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


## mediaSearchallRead

> mediaSearchallRead(user)

Return cast media search result

Return cast media search result  ### Response Class (Status 200) __{user}__ argument can be * artist first name * artist last name * artist username  For more details on how cast media is listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.MediaApi();
let user = "user_example"; // String | 
apiInstance.mediaSearchallRead(user, (error, data, response) => {
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
 **user** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

