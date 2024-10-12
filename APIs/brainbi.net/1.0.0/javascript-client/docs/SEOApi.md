# Brainbi.SEOApi

All URIs are relative to *http://,*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seoLatestRankings**](SEOApi.md#seoLatestRankings) | **GET** /api/seo/ranking/latest | SEO Latest Rankings



## seoLatestRankings

> seoLatestRankings(opts)

SEO Latest Rankings

This resource lists all pricing rules that are currently saved in you account.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.SEOApi();
let opts = {
  '': "" // String | 
};
apiInstance.seoLatestRankings(opts, (error, data, response) => {
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
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

