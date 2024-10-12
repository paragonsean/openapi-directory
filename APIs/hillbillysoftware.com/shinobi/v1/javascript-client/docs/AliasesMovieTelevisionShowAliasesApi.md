# Shinobiapi.AliasesMovieTelevisionShowAliasesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aliasesByIDGet**](AliasesMovieTelevisionShowAliasesApi.md#aliasesByIDGet) | **GET** /Aliases/ByID/{AccessToken}/{imdbID} | Get known aliases for Movies or Television shows from passed imdbID
[**aliasesGet**](AliasesMovieTelevisionShowAliasesApi.md#aliasesGet) | **GET** /Aliases/ByName/{AccessToken}/{Title} | Get known aliases for Movies or Television shows



## aliasesByIDGet

> [Aliases] aliasesByIDGet(accessToken, imdbID)

Get known aliases for Movies or Television shows from passed imdbID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.AliasesMovieTelevisionShowAliasesApi();
let accessToken = "accessToken_example"; // String | 
let imdbID = "imdbID_example"; // String | 
apiInstance.aliasesByIDGet(accessToken, imdbID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **imdbID** | **String**|  | 

### Return type

[**[Aliases]**](Aliases.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## aliasesGet

> [Aliases] aliasesGet(accessToken, title)

Get known aliases for Movies or Television shows

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.AliasesMovieTelevisionShowAliasesApi();
let accessToken = "accessToken_example"; // String | 
let title = "title_example"; // String | Title of movie or television show
apiInstance.aliasesGet(accessToken, title, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **title** | **String**| Title of movie or television show | 

### Return type

[**[Aliases]**](Aliases.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

