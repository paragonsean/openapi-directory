# FactsApi.FactOfTheDayApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factFodCategoriesGet**](FactOfTheDayApi.md#factFodCategoriesGet) | **GET** /fact/fod/categories | 
[**factFodGet**](FactOfTheDayApi.md#factFodGet) | **GET** /fact/fod | 



## factFodCategoriesGet

> factFodCategoriesGet()



Get the list of supported fact of the day categories.

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.FactOfTheDayApi();
apiInstance.factFodCategoriesGet((error, data, response) => {
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

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factFodGet

> factFodGet(opts)



Get fact of the day for the given category.

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.FactOfTheDayApi();
let opts = {
  'category': "category_example" // String | Category to get the fact of the day from. Must be one from the list returned from /fact/fod/categories
};
apiInstance.factFodGet(opts, (error, data, response) => {
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
 **category** | **String**| Category to get the fact of the day from. Must be one from the list returned from /fact/fod/categories | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

