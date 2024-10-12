# RandomLovecraft.SentencesApi

All URIs are relative to *https://randomlovecraft.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSentences**](SentencesApi.md#getSentences) | **GET** /sentences | A random sentence
[**getSentencesFromBook**](SentencesApi.md#getSentencesFromBook) | **GET** /books/{id}/sentences | Random sentences from a specific book
[**getSpecificSentence**](SentencesApi.md#getSpecificSentence) | **GET** /sentences/{id} | A specific sentence



## getSentences

> GetSentencesFromBook200Response getSentences(opts)

A random sentence



### Example

```javascript
import RandomLovecraft from 'random_lovecraft';

let apiInstance = new RandomLovecraft.SentencesApi();
let opts = {
  'limit': 1 // Number | 
};
apiInstance.getSentences(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 1]

### Return type

[**GetSentencesFromBook200Response**](GetSentencesFromBook200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSentencesFromBook

> GetSentencesFromBook200Response getSentencesFromBook(id, opts)

Random sentences from a specific book



### Example

```javascript
import RandomLovecraft from 'random_lovecraft';

let apiInstance = new RandomLovecraft.SentencesApi();
let id = "id_example"; // String | Book ID
let opts = {
  'limit': 1 // Number | 
};
apiInstance.getSentencesFromBook(id, opts, (error, data, response) => {
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
 **id** | **String**| Book ID | 
 **limit** | **Number**|  | [optional] [default to 1]

### Return type

[**GetSentencesFromBook200Response**](GetSentencesFromBook200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSpecificSentence

> GetSpecificSentence200Response getSpecificSentence(id)

A specific sentence



### Example

```javascript
import RandomLovecraft from 'random_lovecraft';

let apiInstance = new RandomLovecraft.SentencesApi();
let id = "id_example"; // String | Sentence ID
apiInstance.getSpecificSentence(id, (error, data, response) => {
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
 **id** | **String**| Sentence ID | 

### Return type

[**GetSpecificSentence200Response**](GetSpecificSentence200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

