# RedirectionIo.AgentFlushRequestApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agentFlushRequestsPost**](AgentFlushRequestApi.md#agentFlushRequestsPost) | **POST** /agent-flush-requests | Creates a AgentFlushRequest resource.
[**postLogsPost**](AgentFlushRequestApi.md#postLogsPost) | **POST** /post-logs | Creates a AgentFlushRequest resource.



## agentFlushRequestsPost

> AgentFlushRequest agentFlushRequestsPost(opts)

Creates a AgentFlushRequest resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.AgentFlushRequestApi();
let opts = {
  'agentFlushRequest': new RedirectionIo.AgentFlushRequest() // AgentFlushRequest | The new AgentFlushRequest resource
};
apiInstance.agentFlushRequestsPost(opts, (error, data, response) => {
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
 **agentFlushRequest** | [**AgentFlushRequest**](AgentFlushRequest.md)| The new AgentFlushRequest resource | [optional] 

### Return type

[**AgentFlushRequest**](AgentFlushRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postLogsPost

> AgentFlushRequest postLogsPost(opts)

Creates a AgentFlushRequest resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.AgentFlushRequestApi();
let opts = {
  'agentFlushRequest': new RedirectionIo.AgentFlushRequest() // AgentFlushRequest | The new AgentFlushRequest resource
};
apiInstance.postLogsPost(opts, (error, data, response) => {
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
 **agentFlushRequest** | [**AgentFlushRequest**](AgentFlushRequest.md)| The new AgentFlushRequest resource | [optional] 

### Return type

[**AgentFlushRequest**](AgentFlushRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

