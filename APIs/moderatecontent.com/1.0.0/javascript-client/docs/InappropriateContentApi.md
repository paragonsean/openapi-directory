# ImageModeration.InappropriateContentApi

All URIs are relative to *https://api.moderatecontent.com/moderate*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootGet**](InappropriateContentApi.md#rootGet) | **GET** / | Blocks images with nudity



## rootGet

> rootGet(url)

Blocks images with nudity

### Example

```javascript
import ImageModeration from 'image_moderation';

let apiInstance = new ImageModeration.InappropriateContentApi();
let url = "url_example"; // String | 
apiInstance.rootGet(url, (error, data, response) => {
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
 **url** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

