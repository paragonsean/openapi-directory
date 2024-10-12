# Betriebsstellen.DefaultApi

All URIs are relative to *https://api.deutschebahn.com/betriebsstellen/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**betriebsstellenAbbrevGet**](DefaultApi.md#betriebsstellenAbbrevGet) | **GET** /betriebsstellen/{abbrev} | Get information about a specific station or stop by abbrevation
[**betriebsstellenGet**](DefaultApi.md#betriebsstellenGet) | **GET** /betriebsstellen | Get information of stations matching a given text



## betriebsstellenAbbrevGet

> Station betriebsstellenAbbrevGet(abbrev)

Get information about a specific station or stop by abbrevation

Get information about a specific station or stop by abbrevation

### Example

```javascript
import Betriebsstellen from 'betriebsstellen';

let apiInstance = new Betriebsstellen.DefaultApi();
let abbrev = "abbrev_example"; // String | Station or stop abbrevation
apiInstance.betriebsstellenAbbrevGet(abbrev, (error, data, response) => {
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
 **abbrev** | **String**| Station or stop abbrevation | 

### Return type

[**Station**](Station.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## betriebsstellenGet

> [Station] betriebsstellenGet(opts)

Get information of stations matching a given text

Get all station and stop infos

### Example

```javascript
import Betriebsstellen from 'betriebsstellen';

let apiInstance = new Betriebsstellen.DefaultApi();
let opts = {
  'name': "name_example" // String | A station name or part of it
};
apiInstance.betriebsstellenGet(opts, (error, data, response) => {
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
 **name** | **String**| A station name or part of it | [optional] 

### Return type

[**[Station]**](Station.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

