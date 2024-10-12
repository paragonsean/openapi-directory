# ApiDatumboxCom.MetricsApi

All URIs are relative to *http://api.datumbox.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentSimilarity**](MetricsApi.md#documentSimilarity) | **POST** /1.0/DocumentSimilarity.json | Estimates the similarity between 2 Documents



## documentSimilarity

> documentSimilarity(apiKey, opts)

Estimates the similarity between 2 Documents

The Document Similarity function estimates the degree of similarity between two documents. It can be used to detect duplicate webpages or detect plagiarism.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.MetricsApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'copy': "copy_example", // String | The second text. It should not contain HTML tags.
  'original': "original_example" // String | The first text. It should not contain HTML tags.
};
apiInstance.documentSimilarity(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **copy** | **String**| The second text. It should not contain HTML tags. | [optional] 
 **original** | **String**| The first text. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

