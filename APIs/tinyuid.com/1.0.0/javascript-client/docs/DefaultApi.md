# TinyUidCom.DefaultApi

All URIs are relative to *https://tinyuid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1ShortenPost**](DefaultApi.md#v1ShortenPost) | **POST** /v1/shorten | Create short link



## v1ShortenPost

> V1ShortenPost200Response v1ShortenPost(url)

Create short link

### Example

```javascript
import TinyUidCom from 'tiny_uid_com';

let apiInstance = new TinyUidCom.DefaultApi();
let url = "url_example"; // String | Link
apiInstance.v1ShortenPost(url, (error, data, response) => {
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
 **url** | **String**| Link | 

### Return type

[**V1ShortenPost200Response**](V1ShortenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

