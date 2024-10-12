# Reverb.CuratedSetsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**curatedSetsSlugGet**](CuratedSetsApi.md#curatedSetsSlugGet) | **GET** /curated_sets/{slug} | 



## curatedSetsSlugGet

> curatedSetsSlugGet(slug)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CuratedSetsApi();
let slug = "slug_example"; // String | 
apiInstance.curatedSetsSlugGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

