# UrlboxApi.DefaultApi

All URIs are relative to *https://api.urlbox.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**renderSync**](DefaultApi.md#renderSync) | **POST** /v1/render/sync | Render a URL as an image or video



## renderSync

> RenderResponse renderSync(renderRequest)

Render a URL as an image or video

### Example

```javascript
import UrlboxApi from 'urlbox_api';
let defaultClient = UrlboxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: SecretKey
let SecretKey = defaultClient.authentications['SecretKey'];
SecretKey.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UrlboxApi.DefaultApi();
let renderRequest = new UrlboxApi.RenderRequest(); // RenderRequest | 
apiInstance.renderSync(renderRequest, (error, data, response) => {
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
 **renderRequest** | [**RenderRequest**](RenderRequest.md)|  | 

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

