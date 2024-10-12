# MagentoB2B.CmsBlockApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmsBlockRepositoryV1SavePost**](CmsBlockApi.md#cmsBlockRepositoryV1SavePost) | **POST** /V1/cmsBlock | cmsBlock



## cmsBlockRepositoryV1SavePost

> CmsDataBlockInterface cmsBlockRepositoryV1SavePost(opts)

cmsBlock

Save block.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsBlockApi();
let opts = {
  'cmsBlockRepositoryV1SavePostRequest': new MagentoB2B.CmsBlockRepositoryV1SavePostRequest() // CmsBlockRepositoryV1SavePostRequest | 
};
apiInstance.cmsBlockRepositoryV1SavePost(opts, (error, data, response) => {
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
 **cmsBlockRepositoryV1SavePostRequest** | [**CmsBlockRepositoryV1SavePostRequest**](CmsBlockRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

