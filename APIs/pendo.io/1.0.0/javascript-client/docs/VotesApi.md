# PendoFeedbackApi.VotesApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**votesGet**](VotesApi.md#votesGet) | **GET** /votes | 
[**votesPost**](VotesApi.md#votesPost) | **POST** /votes | update specified votes for a User



## votesGet

> [Vote] votesGet(opts)



### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.VotesApi();
let opts = {
  'userId': 56, // Number | Include only votes by User that voted on a feature.
  'featureId': 56, // Number | Include only votes for Feature with this Feature ID
  'positive': true, // Boolean | Include only votes that are positive
  'negative': true, // Boolean | Include only votes that are negative
  'offset': 3.4, // Number | Offset to start at
  'limit': 3.4 // Number | Limit the number of records returned
};
apiInstance.votesGet(opts, (error, data, response) => {
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
 **userId** | **Number**| Include only votes by User that voted on a feature. | [optional] 
 **featureId** | **Number**| Include only votes for Feature with this Feature ID | [optional] 
 **positive** | **Boolean**| Include only votes that are positive | [optional] 
 **negative** | **Boolean**| Include only votes that are negative | [optional] 
 **offset** | **Number**| Offset to start at | [optional] 
 **limit** | **Number**| Limit the number of records returned | [optional] 

### Return type

[**[Vote]**](Vote.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## votesPost

> votesPost(data)

update specified votes for a User

Automatically subscribes/unsubscribes the User to the specifed feature depending on the quantity value

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.VotesApi();
let data = new PendoFeedbackApi.VotesPostRequest(); // VotesPostRequest | 
apiInstance.votesPost(data, (error, data, response) => {
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
 **data** | [**VotesPostRequest**](VotesPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

