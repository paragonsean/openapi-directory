# FunGeneratorsApi.PrivateRiddlesApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**riddleDelete**](PrivateRiddlesApi.md#riddleDelete) | **DELETE** /riddle | 
[**riddleGet**](PrivateRiddlesApi.md#riddleGet) | **GET** /riddle | 
[**riddlePost**](PrivateRiddlesApi.md#riddlePost) | **POST** /riddle | 
[**riddlePut**](PrivateRiddlesApi.md#riddlePut) | **PUT** /riddle | 



## riddleDelete

> riddleDelete(id)



Create a random Riddle entry.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.PrivateRiddlesApi();
let id = "id_example"; // String | Riddle ID
apiInstance.riddleDelete(id, (error, data, response) => {
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
 **id** | **String**| Riddle ID | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## riddleGet

> riddleGet(opts)



Get a Riddle entry for a given id. Retrieves a riddle question and answer based on the id.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.PrivateRiddlesApi();
let opts = {
  'id': "id_example" // String | ID of the riddle to fetch
};
apiInstance.riddleGet(opts, (error, data, response) => {
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
 **id** | **String**| ID of the riddle to fetch | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## riddlePost

> riddlePost(question, category, answer)



Create a random Riddle entry. Same as &#39;PUT&#39; but can be used when some of the client libraries don&#39;t support &#39;PUT&#39;.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.PrivateRiddlesApi();
let question = "question_example"; // String | Riddle Question
let category = "category_example"; // String | Category of the riddle
let answer = "answer_example"; // String | Answer(s) to the riddle question
apiInstance.riddlePost(question, category, answer, (error, data, response) => {
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
 **question** | **String**| Riddle Question | 
 **category** | **String**| Category of the riddle | 
 **answer** | **String**| Answer(s) to the riddle question | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## riddlePut

> riddlePut(question, category, answer)



Create a random Riddle entry.

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.PrivateRiddlesApi();
let question = "question_example"; // String | Riddle Question
let category = "category_example"; // String | Category of the riddle
let answer = "answer_example"; // String | Answer(s) to the riddle question
apiInstance.riddlePut(question, category, answer, (error, data, response) => {
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
 **question** | **String**| Riddle Question | 
 **category** | **String**| Category of the riddle | 
 **answer** | **String**| Answer(s) to the riddle question | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

