# Gitlab.VersionApi

All URIs are relative to *https://gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getV3Version**](VersionApi.md#getV3Version) | **GET** /v3/version | Get the version information of the GitLab instance.



## getV3Version

> getV3Version()

Get the version information of the GitLab instance.

This feature was introduced in GitLab 8.13.

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

let apiInstance = new Gitlab.VersionApi();
apiInstance.getV3Version((error, data, response) => {
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

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

