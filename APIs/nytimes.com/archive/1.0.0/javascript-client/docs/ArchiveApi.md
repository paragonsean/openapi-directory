# ArchiveApi.ArchiveApi

All URIs are relative to *http://api.nytimes.com/svc/archive/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**yearMonthJsonGet**](ArchiveApi.md#yearMonthJsonGet) | **GET** /{year}/{month}.json | Archive API



## yearMonthJsonGet

> YearMonthJsonGet200Response yearMonthJsonGet(year, month)

Archive API

The Archive API provides lists of NYT articles by month going back to 1851.  Simply pass in the year and month you want and it returns a JSON object with all articles for that month. 

### Example

```javascript
import ArchiveApi from 'archive_api';
let defaultClient = ArchiveApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new ArchiveApi.ArchiveApi();
let year = 56; // Number | The year (e.g. 2016).
let month = 56; // Number | The month number (e.g. 1 for January).
apiInstance.yearMonthJsonGet(year, month, (error, data, response) => {
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
 **year** | **Number**| The year (e.g. 2016). | 
 **month** | **Number**| The month number (e.g. 1 for January). | 

### Return type

[**YearMonthJsonGet200Response**](YearMonthJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

