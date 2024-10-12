# SpaceTradersApi.AgentsApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMyAgent**](AgentsApi.md#getMyAgent) | **GET** /my/agent | My Agent Details



## getMyAgent

> GetMyAgent200Response getMyAgent()

My Agent Details

Fetch your agent&#39;s details.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.AgentsApi();
apiInstance.getMyAgent((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMyAgent200Response**](GetMyAgent200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

