# MagentoB2B.CmsPageIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmsPageRepositoryV1SavePut**](CmsPageIdApi.md#cmsPageRepositoryV1SavePut) | **PUT** /V1/cmsPage/{id} | cmsPage/{id}



## cmsPageRepositoryV1SavePut

> CmsDataPageInterface cmsPageRepositoryV1SavePut(id, opts)

cmsPage/{id}

Save page.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsPageIdApi();
let id = "id_example"; // String | 
let opts = {
  'cmsPageRepositoryV1SavePostRequest': new MagentoB2B.CmsPageRepositoryV1SavePostRequest() // CmsPageRepositoryV1SavePostRequest | 
};
apiInstance.cmsPageRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **cmsPageRepositoryV1SavePostRequest** | [**CmsPageRepositoryV1SavePostRequest**](CmsPageRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

