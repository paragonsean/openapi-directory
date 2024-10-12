# DefaultTitle.DefaultApi

All URIs are relative to *https://modelpubsub.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV10SafeUnsafeImageWithTagsPost**](DefaultApi.md#apiV10SafeUnsafeImageWithTagsPost) | **POST** /api-v1.0/SafeUnsafeImageWithTags | 



## apiV10SafeUnsafeImageWithTagsPost

> InlineResponse200 apiV10SafeUnsafeImageWithTagsPost(opts)



Auto generated using Swagger Inspector

### Example

```javascript
import DefaultTitle from 'default_title';

let apiInstance = new DefaultTitle.DefaultApi();
let opts = {
  'apiv10SafeUnsafeImageWithTagsBody': new DefaultTitle.Apiv10SafeUnsafeImageWithTagsBody() // Apiv10SafeUnsafeImageWithTagsBody | 
};
apiInstance.apiV10SafeUnsafeImageWithTagsPost(opts, (error, data, response) => {
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
 **apiv10SafeUnsafeImageWithTagsBody** | [**Apiv10SafeUnsafeImageWithTagsBody**](Apiv10SafeUnsafeImageWithTagsBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

