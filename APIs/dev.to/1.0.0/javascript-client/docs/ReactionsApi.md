# ForemApiV1.ReactionsApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiReactionsPost**](ReactionsApi.md#apiReactionsPost) | **POST** /api/reactions | create reaction
[**apiReactionsTogglePost**](ReactionsApi.md#apiReactionsTogglePost) | **POST** /api/reactions/toggle | toggle reaction



## apiReactionsPost

> apiReactionsPost(category, reactableId, reactableType)

create reaction

This endpoint allows the client to create a reaction to a specified reactable (eg, Article, Comment, or User). For examples:         * \&quot;Like\&quot;ing an Article will create a new \&quot;like\&quot; Reaction from the user for that Articles         * \&quot;Like\&quot;ing that Article a second time will return the previous \&quot;like\&quot;

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.ReactionsApi();
let category = "category_example"; // String | 
let reactableId = 56; // Number | 
let reactableType = "reactableType_example"; // String | 
apiInstance.apiReactionsPost(category, reactableId, reactableType, (error, data, response) => {
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
 **category** | **String**|  | 
 **reactableId** | **Number**|  | 
 **reactableType** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiReactionsTogglePost

> apiReactionsTogglePost(category, reactableId, reactableType)

toggle reaction

This endpoint allows the client to toggle the user&#39;s reaction to a specified reactable (eg, Article, Comment, or User). For examples:         * \&quot;Like\&quot;ing an Article will create a new \&quot;like\&quot; Reaction from the user for that Articles         * \&quot;Like\&quot;ing that Article a second time will remove the \&quot;like\&quot; from the user

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.ReactionsApi();
let category = "category_example"; // String | 
let reactableId = 56; // Number | 
let reactableType = "reactableType_example"; // String | 
apiInstance.apiReactionsTogglePost(category, reactableId, reactableType, (error, data, response) => {
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
 **category** | **String**|  | 
 **reactableId** | **Number**|  | 
 **reactableType** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

