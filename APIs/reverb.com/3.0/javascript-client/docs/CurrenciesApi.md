# Reverb.CurrenciesApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currenciesDisplayGet**](CurrenciesApi.md#currenciesDisplayGet) | **GET** /currencies/display | List of supported display currencies for browsing listings
[**currenciesListingGet**](CurrenciesApi.md#currenciesListingGet) | **GET** /currencies/listing | List of supported listing currencies for shops



## currenciesDisplayGet

> currenciesDisplayGet()

List of supported display currencies for browsing listings

List of supported display currencies for browsing listings

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CurrenciesApi();
apiInstance.currenciesDisplayGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## currenciesListingGet

> currenciesListingGet()

List of supported listing currencies for shops

List of supported listing currencies for shops

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CurrenciesApi();
apiInstance.currenciesListingGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

