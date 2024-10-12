# OpenTargetsPlatformRestApi.SearchApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSearch_0**](SearchApi.md#getSearch_0) | **GET** /platform/public/search | Search for a disease or a target



## getSearch_0

> getSearch_0(q, opts)

Search for a disease or a target

This method allows you to look for gene or diseases of interest using a free text search, replicating the functionality of the search box on our homepage. It should be used to identify the best match for a disease or target of interest, rather than gathering a specific set of evidence. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.SearchApi();
let q = "q_example"; // String | A full text query.
let opts = {
  'size': "size_example", // String | Maximum amount of results to return. Defaults to 10, max is 10000.
  'from': "from_example", // String | How many initial results should be skipped. Defaults to 0.
  'filter': "filter_example" // String | Restrict the search to the type requested. Eg. `target` or `disease`.
};
apiInstance.getSearch_0(q, opts, (error, data, response) => {
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
 **q** | **String**| A full text query. | 
 **size** | **String**| Maximum amount of results to return. Defaults to 10, max is 10000. | [optional] 
 **from** | **String**| How many initial results should be skipped. Defaults to 0. | [optional] 
 **filter** | **String**| Restrict the search to the type requested. Eg. &#x60;target&#x60; or &#x60;disease&#x60;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

