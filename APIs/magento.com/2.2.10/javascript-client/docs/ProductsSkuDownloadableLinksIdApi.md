# MagentoB2B.ProductsSkuDownloadableLinksIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadableLinkRepositoryV1SavePut**](ProductsSkuDownloadableLinksIdApi.md#downloadableLinkRepositoryV1SavePut) | **PUT** /V1/products/{sku}/downloadable-links/{id} | products/{sku}/downloadable-links/{id}



## downloadableLinkRepositoryV1SavePut

> Number downloadableLinkRepositoryV1SavePut(sku, id, opts)

products/{sku}/downloadable-links/{id}

Update downloadable link of the given product (link type and its resources cannot be changed)

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuDownloadableLinksIdApi();
let sku = "sku_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'downloadableLinkRepositoryV1SavePostRequest': new MagentoB2B.DownloadableLinkRepositoryV1SavePostRequest() // DownloadableLinkRepositoryV1SavePostRequest | 
};
apiInstance.downloadableLinkRepositoryV1SavePut(sku, id, opts, (error, data, response) => {
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
 **downloadableLinkRepositoryV1SavePostRequest** | [**DownloadableLinkRepositoryV1SavePostRequest**](DownloadableLinkRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

