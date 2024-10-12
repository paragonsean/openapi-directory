# FactsApi.RandomFactsApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factCategoriesGet**](RandomFactsApi.md#factCategoriesGet) | **GET** /fact/categories | 
[**factGet**](RandomFactsApi.md#factGet) | **GET** /fact | 
[**factRandomGet**](RandomFactsApi.md#factRandomGet) | **GET** /fact/random | 
[**factSearchGet**](RandomFactsApi.md#factSearchGet) | **GET** /fact/search | 



## factCategoriesGet

> factCategoriesGet(opts)



Get a random Fact.

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.RandomFactsApi();
let opts = {
  'start': 56 // Number | start
};
apiInstance.factCategoriesGet(opts, (error, data, response) => {
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
 **start** | **Number**| start | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factGet

> factGet(opts)



Get a Fact belonging to the id.

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.RandomFactsApi();
let opts = {
  'id': "id_example" // String | ID of the fact to fetch
};
apiInstance.factGet(opts, (error, data, response) => {
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
 **id** | **String**| ID of the fact to fetch | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factRandomGet

> factRandomGet(opts)



Get a random Fact for a given category(optional) and subcategory(optional).

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.RandomFactsApi();
let opts = {
  'category': "category_example", // String | Category to get the fact from
  'subcategory': "subcategory_example" // String | Sub Category to get the fact from
};
apiInstance.factRandomGet(opts, (error, data, response) => {
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
 **category** | **String**| Category to get the fact from | [optional] 
 **subcategory** | **String**| Sub Category to get the fact from | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factSearchGet

> factSearchGet(opts)



Search for random Fact which has the text in the query, for a given category(optional) and subcategory(optional).

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.RandomFactsApi();
let opts = {
  'query': "query_example", // String | Text to search for in the facts
  'category': "category_example", // String | Category to get the fact from
  'subcategory': "subcategory_example" // String | Sub Category to get the fact from
};
apiInstance.factSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Text to search for in the facts | [optional] 
 **category** | **String**| Category to get the fact from | [optional] 
 **subcategory** | **String**| Sub Category to get the fact from | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

