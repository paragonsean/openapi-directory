# BioLinkApi.GenomeFeaturesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFeaturesWithinResource**](GenomeFeaturesApi.md#getFeaturesWithinResource) | **GET** /genome/features/within/{build}/{reference}/{begin}/{end} | Returns list of matches



## getFeaturesWithinResource

> [SequenceFeature] getFeaturesWithinResource(build, reference, begin, end)

Returns list of matches

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.GenomeFeaturesApi();
let build = "build_example"; // String | 
let reference = "reference_example"; // String | 
let begin = "begin_example"; // String | 
let end = "end_example"; // String | 
apiInstance.getFeaturesWithinResource(build, reference, begin, end, (error, data, response) => {
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
 **build** | **String**|  | 
 **reference** | **String**|  | 
 **begin** | **String**|  | 
 **end** | **String**|  | 

### Return type

[**[SequenceFeature]**](SequenceFeature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

