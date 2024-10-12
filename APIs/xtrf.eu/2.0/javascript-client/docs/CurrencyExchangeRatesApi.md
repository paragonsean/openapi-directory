# XtrfHomePortalApi.CurrencyExchangeRatesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createExchangeRate**](CurrencyExchangeRatesApi.md#createExchangeRate) | **POST** /dictionaries/currency/{isoCode}/exchangeRate | Adding currency exchange rates.
[**getByIsoCode**](CurrencyExchangeRatesApi.md#getByIsoCode) | **GET** /dictionaries/currency/{isoCode}/exchangeRate | Returns currency exchange rates.



## createExchangeRate

> createExchangeRate(isoCode, currencyHistoryDTO)

Adding currency exchange rates.

Adding currency exchange rates via API

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.CurrencyExchangeRatesApi();
let isoCode = "isoCode_example"; // String | iso code, https://www.xe.com/iso4217.php
let currencyHistoryDTO = /home-api/assets/examples/dictionaries/currency/createExchangeRate.json#requestBody; // CurrencyHistoryDTO | Adding new currency exchange rates
apiInstance.createExchangeRate(isoCode, currencyHistoryDTO, (error, data, response) => {
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
 **isoCode** | **String**| iso code, https://www.xe.com/iso4217.php | 
 **currencyHistoryDTO** | [**CurrencyHistoryDTO**](CurrencyHistoryDTO.md)| Adding new currency exchange rates | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getByIsoCode

> CurrencyHistoryDTO getByIsoCode(isoCode)

Returns currency exchange rates.

Returns currency exchange rates.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.CurrencyExchangeRatesApi();
let isoCode = "isoCode_example"; // String | iso code, https://www.xe.com/iso4217.php
apiInstance.getByIsoCode(isoCode, (error, data, response) => {
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
 **isoCode** | **String**| iso code, https://www.xe.com/iso4217.php | 

### Return type

[**CurrencyHistoryDTO**](CurrencyHistoryDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

