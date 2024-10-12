# MagentoB2B.ProductsDownloadableLinksIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadableLinkRepositoryV1DeleteDelete**](ProductsDownloadableLinksIdApi.md#downloadableLinkRepositoryV1DeleteDelete) | **DELETE** /V1/products/downloadable-links/{id} | products/downloadable-links/{id}



## downloadableLinkRepositoryV1DeleteDelete

> Boolean downloadableLinkRepositoryV1DeleteDelete(id)

products/downloadable-links/{id}

Delete downloadable link

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsDownloadableLinksIdApi();
let id = 56; // Number | 
apiInstance.downloadableLinkRepositoryV1DeleteDelete(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

