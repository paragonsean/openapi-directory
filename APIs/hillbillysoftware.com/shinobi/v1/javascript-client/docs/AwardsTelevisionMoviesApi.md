# Shinobiapi.AwardsTelevisionMoviesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**awardsGet**](AwardsTelevisionMoviesApi.md#awardsGet) | **GET** /Awards/ByYear/{Year} | Gets all awards for requested year
[**awardsbyWinnerGet**](AwardsTelevisionMoviesApi.md#awardsbyWinnerGet) | **GET** /Awards/ByWinner/{AccessToken}/{Nominee} | Gets all awards by nominiee



## awardsGet

> [Awards] awardsGet(year)

Gets all awards for requested year

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.AwardsTelevisionMoviesApi();
let year = "year_example"; // String | 
apiInstance.awardsGet(year, (error, data, response) => {
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
 **year** | **String**|  | 

### Return type

[**[Awards]**](Awards.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## awardsbyWinnerGet

> [Awards] awardsbyWinnerGet(accessToken, nominee)

Gets all awards by nominiee

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.AwardsTelevisionMoviesApi();
let accessToken = "accessToken_example"; // String | 
let nominee = "nominee_example"; // String | 
apiInstance.awardsbyWinnerGet(accessToken, nominee, (error, data, response) => {
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
 **nominee** | **String**|  | 

### Return type

[**[Awards]**](Awards.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

