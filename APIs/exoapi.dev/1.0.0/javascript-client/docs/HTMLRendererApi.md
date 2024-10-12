# ExoApi.HTMLRendererApi

All URIs are relative to *https://api.exoapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**htmlRendererPost**](HTMLRendererApi.md#htmlRendererPost) | **POST** /html-renderer | 



## htmlRendererPost

> File htmlRendererPost(htmlRendererPostRequest)



Generate high-quality PDF documents or images from HTML

### Example

```javascript
import ExoApi from 'exo_api';
let defaultClient = ExoApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExoApi.HTMLRendererApi();
let htmlRendererPostRequest = new ExoApi.HtmlRendererPostRequest(); // HtmlRendererPostRequest | 
apiInstance.htmlRendererPost(htmlRendererPostRequest, (error, data, response) => {
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
 **htmlRendererPostRequest** | [**HtmlRendererPostRequest**](HtmlRendererPostRequest.md)|  | 

### Return type

**File**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, image/png, application/json

