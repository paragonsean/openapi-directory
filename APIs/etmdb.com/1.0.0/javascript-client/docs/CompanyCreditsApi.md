# EtMdbRestApiV1.CompanyCreditsApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditsSearchRead**](CompanyCreditsApi.md#companyCreditsSearchRead) | **GET** /api/v1/company-credits/search/{movie_title} | Return company credits search result
[**companyCreditsSearchallRead**](CompanyCreditsApi.md#companyCreditsSearchallRead) | **GET** /api/v1/company-credits/searchall/{param} | Return company credits search result



## companyCreditsSearchRead

> companyCreditsSearchRead(movieTitle)

Return company credits search result

Return company credits search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search company credits for the movie * You can use both Amharic or English charset/font to search  For more details on how company credits are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CompanyCreditsApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.companyCreditsSearchRead(movieTitle, (error, data, response) => {
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


## companyCreditsSearchallRead

> companyCreditsSearchallRead(param)

Return company credits search result

Return company credits search result  ### Response Class (Status 200) __{param}__ argument can be * company name * movie title or * company credit description (such as production, cinematography, etc)  For more details on how company credits are listed [see here][ref]. [ref]: https://etmdb.com/en/company-list/company_name

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CompanyCreditsApi();
let param = "param_example"; // String | 
apiInstance.companyCreditsSearchallRead(param, (error, data, response) => {
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

