# Shipstation.DefaultApi

All URIs are relative to *https://polls.apiblueprint.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createANewQuestion**](DefaultApi.md#createANewQuestion) | **POST** /questions | Create a New Question
[**listAllQuestions**](DefaultApi.md#listAllQuestions) | **GET** /questions | List All Questions



## createANewQuestion

> createANewQuestion(opts)

Create a New Question

You may create your own question using this action. It takes a JSON object containing a question and a collection of answers in the form of choices.

### Example

```javascript
import Shipstation from 'shipstation';

let apiInstance = new Shipstation.DefaultApi();
let opts = {
  'createANewQuestionRequest': new Shipstation.CreateANewQuestionRequest() // CreateANewQuestionRequest | 
};
apiInstance.createANewQuestion(opts, (error, data, response) => {
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
 **createANewQuestionRequest** | [**CreateANewQuestionRequest**](CreateANewQuestionRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAllQuestions

> listAllQuestions()

List All Questions



### Example

```javascript
import Shipstation from 'shipstation';

let apiInstance = new Shipstation.DefaultApi();
apiInstance.listAllQuestions((error, data, response) => {
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
- **Accept**: application/json

