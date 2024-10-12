# FunGeneratorsApi.TriviaApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triviaCategoriesGet**](TriviaApi.md#triviaCategoriesGet) | **GET** /trivia/categories | 
[**triviaDelete**](TriviaApi.md#triviaDelete) | **DELETE** /trivia | 
[**triviaGet**](TriviaApi.md#triviaGet) | **GET** /trivia | 
[**triviaPut**](TriviaApi.md#triviaPut) | **PUT** /trivia | 
[**triviaRandomGet**](TriviaApi.md#triviaRandomGet) | **GET** /trivia/random | 
[**triviaSearchGet**](TriviaApi.md#triviaSearchGet) | **GET** /trivia/search | 



## triviaCategoriesGet

> triviaCategoriesGet(opts)



Get a random Trivia.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.TriviaApi();
let opts = {
  'start': 56 // Number | start
};
apiInstance.triviaCategoriesGet(opts, (error, data, response) => {
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


## triviaDelete

> triviaDelete(id)



Create a random Trivia entry.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.TriviaApi();
let id = "id_example"; // String | Trivia ID
apiInstance.triviaDelete(id, (error, data, response) => {
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
 **id** | **String**| Trivia ID | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## triviaGet

> triviaGet(opts)



Get a Trivia entry for a given id. Retrieves a trivia question and answer based on the id.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.TriviaApi();
let opts = {
  'id': "id_example" // String | ID of the trivia to fetch
};
apiInstance.triviaGet(opts, (error, data, response) => {
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
 **id** | **String**| ID of the trivia to fetch | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## triviaPut

> triviaPut(question, category, answer)



Create a random Trivia entry.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.TriviaApi();
let question = "question_example"; // String | Trivia Question
let category = "category_example"; // String | Category of the trivia
let answer = "answer_example"; // String | Answer(s) to the trivia question
apiInstance.triviaPut(question, category, answer, (error, data, response) => {
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
 **question** | **String**| Trivia Question | 
 **category** | **String**| Category of the trivia | 
 **answer** | **String**| Answer(s) to the trivia question | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## triviaRandomGet

> triviaRandomGet(opts)



Get a random trivia for a given category(optional)

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.TriviaApi();
let opts = {
  'category': "category_example" // String | Category to get the trivia from
};
apiInstance.triviaRandomGet(opts, (error, data, response) => {
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
 **category** | **String**| Category to get the trivia from | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## triviaSearchGet

> triviaSearchGet(opts)



Search for random trivia which has the text in the query, for a given category(optional).

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.TriviaApi();
let opts = {
  'query': "query_example", // String | Text to search for in the trivia
  'category': "category_example" // String | Category to get the trivia from
};
apiInstance.triviaSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Text to search for in the trivia | [optional] 
 **category** | **String**| Category to get the trivia from | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

