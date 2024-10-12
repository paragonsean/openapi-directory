# EtMdbRestApiV1.FilmographyTypeApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filmographyTypeSearchRead**](FilmographyTypeApi.md#filmographyTypeSearchRead) | **GET** /api/v1/filmography-type/search/{filmography_description} | Return filmography type search result



## filmographyTypeSearchRead

> filmographyTypeSearchRead(filmographyDescription)

Return filmography type search result

Return filmography type search result  ### Response Class (Status 200)  * __{filmography_description}__: Used as a key word to search filmography types  For more details on how filmography types are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.FilmographyTypeApi();
let filmographyDescription = "filmographyDescription_example"; // String | 
apiInstance.filmographyTypeSearchRead(filmographyDescription, (error, data, response) => {
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
 **filmographyDescription** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

