# Gitlab.CiApi

All URIs are relative to *https://gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postV3CiLint**](CiApi.md#postV3CiLint) | **POST** /v3/ci/lint | Validation of .gitlab-ci.yml content



## postV3CiLint

> postV3CiLint(postV3CiLintRequest)

Validation of .gitlab-ci.yml content

Validation of .gitlab-ci.yml content

### Example

```javascript
import Gitlab from 'gitlab';
let defaultClient = Gitlab.ApiClient.instance;
// Configure API key authorization: private_token_query
let private_token_query = defaultClient.authentications['private_token_query'];
private_token_query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_query.apiKeyPrefix = 'Token';
// Configure API key authorization: private_token_header
let private_token_header = defaultClient.authentications['private_token_header'];
private_token_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_header.apiKeyPrefix = 'Token';

let apiInstance = new Gitlab.CiApi();
let postV3CiLintRequest = new Gitlab.PostV3CiLintRequest(); // PostV3CiLintRequest | 
apiInstance.postV3CiLint(postV3CiLintRequest, (error, data, response) => {
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
 **postV3CiLintRequest** | [**PostV3CiLintRequest**](PostV3CiLintRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

