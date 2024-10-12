# RedirectionIo.AgentFlushAggregateRequestApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postAgentFlushAggregateRequestCollection**](AgentFlushAggregateRequestApi.md#postAgentFlushAggregateRequestCollection) | **POST** /agent-flush-aggregate-requests | Creates a AgentFlushAggregateRequest resource.



## postAgentFlushAggregateRequestCollection

> AgentFlushAggregateRequest postAgentFlushAggregateRequestCollection(opts)

Creates a AgentFlushAggregateRequest resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.AgentFlushAggregateRequestApi();
let opts = {
  'agentFlushAggregateRequest': new RedirectionIo.AgentFlushAggregateRequest() // AgentFlushAggregateRequest | The new AgentFlushAggregateRequest resource
};
apiInstance.postAgentFlushAggregateRequestCollection(opts, (error, data, response) => {
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
 **agentFlushAggregateRequest** | [**AgentFlushAggregateRequest**](AgentFlushAggregateRequest.md)| The new AgentFlushAggregateRequest resource | [optional] 

### Return type

[**AgentFlushAggregateRequest**](AgentFlushAggregateRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

