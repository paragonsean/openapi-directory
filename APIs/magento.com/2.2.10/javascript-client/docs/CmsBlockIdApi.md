# MagentoB2B.CmsBlockIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmsBlockRepositoryV1SavePut**](CmsBlockIdApi.md#cmsBlockRepositoryV1SavePut) | **PUT** /V1/cmsBlock/{id} | cmsBlock/{id}



## cmsBlockRepositoryV1SavePut

> CmsDataBlockInterface cmsBlockRepositoryV1SavePut(id, opts)

cmsBlock/{id}

Save block.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsBlockIdApi();
let id = "id_example"; // String | 
let opts = {
  'cmsBlockRepositoryV1SavePostRequest': new MagentoB2B.CmsBlockRepositoryV1SavePostRequest() // CmsBlockRepositoryV1SavePostRequest | 
};
apiInstance.cmsBlockRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **cmsBlockRepositoryV1SavePostRequest** | [**CmsBlockRepositoryV1SavePostRequest**](CmsBlockRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

