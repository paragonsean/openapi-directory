# DaniWebConnectApi.MarkdownApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markdownEmoticonsGet**](MarkdownApi.md#markdownEmoticonsGet) | **GET** /markdown/emoticons | 
[**markdownPost**](MarkdownApi.md#markdownPost) | **POST** /markdown | 



## markdownEmoticonsGet

> EndpointGetMarkdownEmoticons markdownEmoticonsGet()



### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MarkdownApi();
apiInstance.markdownEmoticonsGet((error, data, response) => {
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

[**EndpointGetMarkdownEmoticons**](EndpointGetMarkdownEmoticons.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## markdownPost

> EndpointPostMarkdown markdownPost(textRaw, opts)



### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MarkdownApi();
let textRaw = "textRaw_example"; // String | 
let opts = {
  'textEmoticons': false // Boolean | 
};
apiInstance.markdownPost(textRaw, opts, (error, data, response) => {
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
 **textRaw** | **String**|  | 
 **textEmoticons** | **Boolean**|  | [optional] [default to false]

### Return type

[**EndpointPostMarkdown**](EndpointPostMarkdown.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

