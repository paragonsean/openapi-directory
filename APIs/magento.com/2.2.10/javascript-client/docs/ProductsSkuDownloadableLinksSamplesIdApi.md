# MagentoB2B.ProductsSkuDownloadableLinksSamplesIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadableSampleRepositoryV1SavePut**](ProductsSkuDownloadableLinksSamplesIdApi.md#downloadableSampleRepositoryV1SavePut) | **PUT** /V1/products/{sku}/downloadable-links/samples/{id} | products/{sku}/downloadable-links/samples/{id}



## downloadableSampleRepositoryV1SavePut

> Number downloadableSampleRepositoryV1SavePut(sku, id, opts)

products/{sku}/downloadable-links/samples/{id}

Update downloadable sample of the given product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuDownloadableLinksSamplesIdApi();
let sku = "sku_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'downloadableSampleRepositoryV1SavePostRequest': new MagentoB2B.DownloadableSampleRepositoryV1SavePostRequest() // DownloadableSampleRepositoryV1SavePostRequest | 
};
apiInstance.downloadableSampleRepositoryV1SavePut(sku, id, opts, (error, data, response) => {
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
 **sku** | **String**|  | 
 **id** | **String**|  | 
 **downloadableSampleRepositoryV1SavePostRequest** | [**DownloadableSampleRepositoryV1SavePostRequest**](DownloadableSampleRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

