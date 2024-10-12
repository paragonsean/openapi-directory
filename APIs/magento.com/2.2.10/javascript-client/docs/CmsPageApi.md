# MagentoB2B.CmsPageApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmsPageRepositoryV1SavePost**](CmsPageApi.md#cmsPageRepositoryV1SavePost) | **POST** /V1/cmsPage | cmsPage



## cmsPageRepositoryV1SavePost

> CmsDataPageInterface cmsPageRepositoryV1SavePost(opts)

cmsPage

Save page.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsPageApi();
let opts = {
  'cmsPageRepositoryV1SavePostRequest': new MagentoB2B.CmsPageRepositoryV1SavePostRequest() // CmsPageRepositoryV1SavePostRequest | 
};
apiInstance.cmsPageRepositoryV1SavePost(opts, (error, data, response) => {
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
 **cmsPageRepositoryV1SavePostRequest** | [**CmsPageRepositoryV1SavePostRequest**](CmsPageRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

