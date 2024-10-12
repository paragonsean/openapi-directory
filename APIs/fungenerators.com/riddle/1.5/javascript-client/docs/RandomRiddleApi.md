# FunGeneratorsApi.RandomRiddleApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**riddleRandomGet**](RandomRiddleApi.md#riddleRandomGet) | **GET** /riddle/random | 
[**riddleSearchGet**](RandomRiddleApi.md#riddleSearchGet) | **GET** /riddle/search | 



## riddleRandomGet

> riddleRandomGet(opts)



Get a random riddle for a given category(optional)

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.RandomRiddleApi();
let opts = {
  'category': "category_example" // String | Category to get the riddle from
};
apiInstance.riddleRandomGet(opts, (error, data, response) => {
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
 **category** | **String**| Category to get the riddle from | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## riddleSearchGet

> riddleSearchGet(opts)



Search for random riddle which has the text in the query, for a given category(optional).

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.RandomRiddleApi();
let opts = {
  'query': "query_example", // String | Text to search for in the riddle
  'category': "category_example" // String | Category to get the riddle from
};
apiInstance.riddleSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Text to search for in the riddle | [optional] 
 **category** | **String**| Category to get the riddle from | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

