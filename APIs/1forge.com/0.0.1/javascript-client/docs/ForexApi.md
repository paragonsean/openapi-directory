# 1ForgeFinanceApis.ForexApi

All URIs are relative to *https://1forge.com/forex-quotes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotesGet**](ForexApi.md#quotesGet) | **GET** /quotes | Get quotes for all symbols
[**symbolsGet**](ForexApi.md#symbolsGet) | **GET** /symbols | Get a list of symbols for which we provide real-time quotes



## quotesGet

> quotesGet()

Get quotes for all symbols

Get quotes

### Example

```javascript
import 1ForgeFinanceApis from '1_forge_finance_apis';

let apiInstance = new 1ForgeFinanceApis.ForexApi();
apiInstance.quotesGet((error, data, response) => {
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


## symbolsGet

> [String] symbolsGet()

Get a list of symbols for which we provide real-time quotes

Symbol List

### Example

```javascript
import 1ForgeFinanceApis from '1_forge_finance_apis';

let apiInstance = new 1ForgeFinanceApis.ForexApi();
apiInstance.symbolsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

