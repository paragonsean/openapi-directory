# EtMdbRestApiV1.GenreTypeApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genreTypeSearchRead**](GenreTypeApi.md#genreTypeSearchRead) | **GET** /api/v1/genre-type/search/{genre_description} | Return genre type search result



## genreTypeSearchRead

> genreTypeSearchRead(genreDescription)

Return genre type search result

Return genre type search result  ### Response Class (Status 200)  * __{genre_description}__: Used as a key word to search genre types  For more details on how genre types are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.GenreTypeApi();
let genreDescription = "genreDescription_example"; // String | 
apiInstance.genreTypeSearchRead(genreDescription, (error, data, response) => {
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
 **genreDescription** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

