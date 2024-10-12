# 1ForgeFinanceApis.QuotesApi

All URIs are relative to *https://1forge.com/forex-quotes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotesGet_1**](QuotesApi.md#quotesGet_1) | **GET** /quotes | Get quotes for all symbols
[**symbolsGet_1**](QuotesApi.md#symbolsGet_1) | **GET** /symbols | Get a list of symbols for which we provide real-time quotes



## quotesGet_1

> quotesGet_1()

Get quotes for all symbols

Get quotes

### Example

```javascript
import 1ForgeFinanceApis from '1_forge_finance_apis';

let apiInstance = new 1ForgeFinanceApis.QuotesApi();
apiInstance.quotesGet_1((error, data, response) => {
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


## symbolsGet_1

> [String] symbolsGet_1()

Get a list of symbols for which we provide real-time quotes

Symbol List

### Example

```javascript
import 1ForgeFinanceApis from '1_forge_finance_apis';

let apiInstance = new 1ForgeFinanceApis.QuotesApi();
apiInstance.symbolsGet_1((error, data, response) => {
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

