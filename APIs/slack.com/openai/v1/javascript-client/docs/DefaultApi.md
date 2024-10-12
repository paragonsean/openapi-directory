# SlackAiPlugin.DefaultApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aiAlphaSearchMessages**](DefaultApi.md#aiAlphaSearchMessages) | **POST** /ai.alpha.search.messages | 



## aiAlphaSearchMessages

> AiAlphaSearchMessages200Response aiAlphaSearchMessages(searchRequest)



Search for messages matching a query

### Example

```javascript
import SlackAiPlugin from 'slack_ai_plugin';

let apiInstance = new SlackAiPlugin.DefaultApi();
let searchRequest = new SlackAiPlugin.SearchRequest(); // SearchRequest | 
apiInstance.aiAlphaSearchMessages(searchRequest, (error, data, response) => {
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
 **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**AiAlphaSearchMessages200Response**](AiAlphaSearchMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

