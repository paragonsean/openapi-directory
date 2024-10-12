# 1ForgeFinanceApis.FinanceApi

All URIs are relative to *https://1forge.com/forex-quotes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotesGet_0**](FinanceApi.md#quotesGet_0) | **GET** /quotes | Get quotes for all symbols
[**symbolsGet_0**](FinanceApi.md#symbolsGet_0) | **GET** /symbols | Get a list of symbols for which we provide real-time quotes



## quotesGet_0

> quotesGet_0()

Get quotes for all symbols

Get quotes

### Example

```javascript
import 1ForgeFinanceApis from '1_forge_finance_apis';

let apiInstance = new 1ForgeFinanceApis.FinanceApi();
apiInstance.quotesGet_0((error, data, response) => {
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


## symbolsGet_0

> [String] symbolsGet_0()

Get a list of symbols for which we provide real-time quotes

Symbol List

### Example

```javascript
import 1ForgeFinanceApis from '1_forge_finance_apis';

let apiInstance = new 1ForgeFinanceApis.FinanceApi();
apiInstance.symbolsGet_0((error, data, response) => {
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

