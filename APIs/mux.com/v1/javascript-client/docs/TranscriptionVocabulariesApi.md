# MuxApi.TranscriptionVocabulariesApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTranscriptionVocabulary**](TranscriptionVocabulariesApi.md#createTranscriptionVocabulary) | **POST** /video/v1/transcription-vocabularies | Create a Transcription Vocabulary
[**deleteTranscriptionVocabulary**](TranscriptionVocabulariesApi.md#deleteTranscriptionVocabulary) | **DELETE** /video/v1/transcription-vocabularies/{TRANSCRIPTION_VOCABULARY_ID} | Delete a Transcription Vocabulary
[**getTranscriptionVocabulary**](TranscriptionVocabulariesApi.md#getTranscriptionVocabulary) | **GET** /video/v1/transcription-vocabularies/{TRANSCRIPTION_VOCABULARY_ID} | Retrieve a Transcription Vocabulary
[**listTranscriptionVocabularies**](TranscriptionVocabulariesApi.md#listTranscriptionVocabularies) | **GET** /video/v1/transcription-vocabularies | List Transcription Vocabularies
[**updateTranscriptionVocabulary**](TranscriptionVocabulariesApi.md#updateTranscriptionVocabulary) | **PUT** /video/v1/transcription-vocabularies/{TRANSCRIPTION_VOCABULARY_ID} | Update a Transcription Vocabulary



## createTranscriptionVocabulary

> TranscriptionVocabularyResponse createTranscriptionVocabulary(createTranscriptionVocabularyRequest)

Create a Transcription Vocabulary

Create a new Transcription Vocabulary.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.TranscriptionVocabulariesApi();
let createTranscriptionVocabularyRequest = {"name":"Mux API Vocabulary","phrases":["Mux","Live Stream","Playback ID","video encoding"]}; // CreateTranscriptionVocabularyRequest | 
apiInstance.createTranscriptionVocabulary(createTranscriptionVocabularyRequest, (error, data, response) => {
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
 **createTranscriptionVocabularyRequest** | [**CreateTranscriptionVocabularyRequest**](CreateTranscriptionVocabularyRequest.md)|  | 

### Return type

[**TranscriptionVocabularyResponse**](TranscriptionVocabularyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTranscriptionVocabulary

> deleteTranscriptionVocabulary(TRANSCRIPTION_VOCABULARY_ID)

Delete a Transcription Vocabulary

Deletes a Transcription Vocabulary. The Transcription Vocabulary&#39;s ID will be disassociated from any live streams using it. Transcription Vocabularies can be deleted while associated live streams are active. However, the words and phrases in the deleted Transcription Vocabulary will remain attached to those streams while they are active.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.TranscriptionVocabulariesApi();
let TRANSCRIPTION_VOCABULARY_ID = "TRANSCRIPTION_VOCABULARY_ID_example"; // String | The ID of the Transcription Vocabulary.
apiInstance.deleteTranscriptionVocabulary(TRANSCRIPTION_VOCABULARY_ID, (error, data, response) => {
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
 **TRANSCRIPTION_VOCABULARY_ID** | **String**| The ID of the Transcription Vocabulary. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTranscriptionVocabulary

> TranscriptionVocabularyResponse getTranscriptionVocabulary(TRANSCRIPTION_VOCABULARY_ID)

Retrieve a Transcription Vocabulary

Retrieves the details of a Transcription Vocabulary that has previously been created. Supply the unique Transcription Vocabulary ID and Mux will return the corresponding Transcription Vocabulary information. The same information is returned when creating a Transcription Vocabulary.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.TranscriptionVocabulariesApi();
let TRANSCRIPTION_VOCABULARY_ID = "TRANSCRIPTION_VOCABULARY_ID_example"; // String | The ID of the Transcription Vocabulary.
apiInstance.getTranscriptionVocabulary(TRANSCRIPTION_VOCABULARY_ID, (error, data, response) => {
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
 **TRANSCRIPTION_VOCABULARY_ID** | **String**| The ID of the Transcription Vocabulary. | 

### Return type

[**TranscriptionVocabularyResponse**](TranscriptionVocabularyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscriptionVocabularies

> ListTranscriptionVocabulariesResponse listTranscriptionVocabularies(opts)

List Transcription Vocabularies

List all Transcription Vocabularies.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.TranscriptionVocabulariesApi();
let opts = {
  'limit': 10, // Number | Number of items to include in the response
  'page': 1 // Number | Offset by this many pages, of the size of `limit`
};
apiInstance.listTranscriptionVocabularies(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 10]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListTranscriptionVocabulariesResponse**](ListTranscriptionVocabulariesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTranscriptionVocabulary

> TranscriptionVocabularyResponse updateTranscriptionVocabulary(TRANSCRIPTION_VOCABULARY_ID, updateTranscriptionVocabularyRequest)

Update a Transcription Vocabulary

Updates the details of a previously-created Transcription Vocabulary. Updates to Transcription Vocabularies are allowed while associated live streams are active. However, updates will not be applied to those streams while they are active.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.TranscriptionVocabulariesApi();
let TRANSCRIPTION_VOCABULARY_ID = "TRANSCRIPTION_VOCABULARY_ID_example"; // String | The ID of the Transcription Vocabulary.
let updateTranscriptionVocabularyRequest = {"name":"Mux API Vocabulary - Updated","phrases":["Mux","Live Stream","RTMP","Stream Key"]}; // UpdateTranscriptionVocabularyRequest | 
apiInstance.updateTranscriptionVocabulary(TRANSCRIPTION_VOCABULARY_ID, updateTranscriptionVocabularyRequest, (error, data, response) => {
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
 **TRANSCRIPTION_VOCABULARY_ID** | **String**| The ID of the Transcription Vocabulary. | 
 **updateTranscriptionVocabularyRequest** | [**UpdateTranscriptionVocabularyRequest**](UpdateTranscriptionVocabularyRequest.md)|  | 

### Return type

[**TranscriptionVocabularyResponse**](TranscriptionVocabularyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

