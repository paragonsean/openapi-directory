# QnAMakerRuntimeClient.KnowledgebasesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**runtimeGenerateAnswer**](KnowledgebasesApi.md#runtimeGenerateAnswer) | **POST** /knowledgebases/{kbId}/generateAnswer | GenerateAnswer call to query the knowledgebase.
[**runtimeTrain**](KnowledgebasesApi.md#runtimeTrain) | **POST** /knowledgebases/{kbId}/train | Train call to add suggestions to the knowledgebase.



## runtimeGenerateAnswer

> QnASearchResultList runtimeGenerateAnswer(kbId, generateAnswerPayload)

GenerateAnswer call to query the knowledgebase.

### Example

```javascript
import QnAMakerRuntimeClient from 'qn_a_maker_runtime_client';
let defaultClient = QnAMakerRuntimeClient.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerRuntimeClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
let generateAnswerPayload = new QnAMakerRuntimeClient.QueryDTO(); // QueryDTO | Post body of the request.
apiInstance.runtimeGenerateAnswer(kbId, generateAnswerPayload, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 
 **generateAnswerPayload** | [**QueryDTO**](QueryDTO.md)| Post body of the request. | 

### Return type

[**QnASearchResultList**](QnASearchResultList.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## runtimeTrain

> runtimeTrain(kbId, trainPayload)

Train call to add suggestions to the knowledgebase.

### Example

```javascript
import QnAMakerRuntimeClient from 'qn_a_maker_runtime_client';
let defaultClient = QnAMakerRuntimeClient.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerRuntimeClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
let trainPayload = new QnAMakerRuntimeClient.FeedbackRecordsDTO(); // FeedbackRecordsDTO | Post body of the request.
apiInstance.runtimeTrain(kbId, trainPayload, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 
 **trainPayload** | [**FeedbackRecordsDTO**](FeedbackRecordsDTO.md)| Post body of the request. | 

### Return type

null (empty response body)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

