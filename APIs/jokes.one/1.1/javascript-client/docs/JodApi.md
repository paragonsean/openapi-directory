# JokesOneApi.JodApi

All URIs are relative to *https://api.jokes.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jodCategoriesGet**](JodApi.md#jodCategoriesGet) | **GET** /jod/categories | 
[**jodGet**](JodApi.md#jodGet) | **GET** /jod | 



## jodCategoriesGet

> jodCategoriesGet()



Gets a list of &#x60;Joke of the Day&#x60; Categories. 

### Example

```javascript
import JokesOneApi from 'jokes_one_api';
let defaultClient = JokesOneApi.ApiClient.instance;
// Configure API key authorization: X-JokesOne-Api-Secret
let X-JokesOne-Api-Secret = defaultClient.authentications['X-JokesOne-Api-Secret'];
X-JokesOne-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-JokesOne-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new JokesOneApi.JodApi();
apiInstance.jodCategoriesGet((error, data, response) => {
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

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jodGet

> JokeOfTheDayResponse jodGet(opts)



Gets &#x60;Joke of the Day&#x60;. Optional &#x60;category&#x60; param determines the category of returned joke of the day 

### Example

```javascript
import JokesOneApi from 'jokes_one_api';
let defaultClient = JokesOneApi.ApiClient.instance;
// Configure API key authorization: X-JokesOne-Api-Secret
let X-JokesOne-Api-Secret = defaultClient.authentications['X-JokesOne-Api-Secret'];
X-JokesOne-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-JokesOne-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new JokesOneApi.JodApi();
let opts = {
  'category': "category_example" // String | JOD Category
};
apiInstance.jodGet(opts, (error, data, response) => {
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
 **category** | **String**| JOD Category | [optional] 

### Return type

[**JokeOfTheDayResponse**](JokeOfTheDayResponse.md)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

