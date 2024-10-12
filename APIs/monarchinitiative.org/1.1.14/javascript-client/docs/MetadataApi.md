# BioLinkApi.MetadataApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMetadataForDatasets**](MetadataApi.md#getMetadataForDatasets) | **GET** /metadata/datasets | Get metadata for all datasets from SciGraph



## getMetadataForDatasets

> getMetadataForDatasets()

Get metadata for all datasets from SciGraph

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MetadataApi();
apiInstance.getMetadataForDatasets((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

