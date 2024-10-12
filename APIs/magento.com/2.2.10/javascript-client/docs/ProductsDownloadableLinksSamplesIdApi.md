# MagentoB2B.ProductsDownloadableLinksSamplesIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadableSampleRepositoryV1DeleteDelete**](ProductsDownloadableLinksSamplesIdApi.md#downloadableSampleRepositoryV1DeleteDelete) | **DELETE** /V1/products/downloadable-links/samples/{id} | products/downloadable-links/samples/{id}



## downloadableSampleRepositoryV1DeleteDelete

> Boolean downloadableSampleRepositoryV1DeleteDelete(id)

products/downloadable-links/samples/{id}

Delete downloadable sample

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsDownloadableLinksSamplesIdApi();
let id = 56; // Number | 
apiInstance.downloadableSampleRepositoryV1DeleteDelete(id, (error, data, response) => {
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

