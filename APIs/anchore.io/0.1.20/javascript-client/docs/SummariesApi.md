# AnchoreEngineApiServer.SummariesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listImagetags**](SummariesApi.md#listImagetags) | **GET** /summaries/imagetags | List all visible image digests and tags



## listImagetags

> [AnchoreImageTagSummary] listImagetags(opts)

List all visible image digests and tags

List all image tags visible to the user

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.SummariesApi();
let opts = {
  'imageStatus': ["null"], // [String] | Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listImagetags(opts, (error, data, response) => {
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
 **imageStatus** | [**[String]**](String.md)| Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[AnchoreImageTagSummary]**](AnchoreImageTagSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

