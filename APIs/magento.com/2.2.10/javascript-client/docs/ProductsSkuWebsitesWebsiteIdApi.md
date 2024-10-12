# MagentoB2B.ProductsSkuWebsitesWebsiteIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete**](ProductsSkuWebsitesWebsiteIdApi.md#catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/{sku}/websites/{websiteId} | products/{sku}/websites/{websiteId}



## catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete

> Boolean catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete(sku, websiteId)

products/{sku}/websites/{websiteId}

Remove the website assignment from the product by product sku

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuWebsitesWebsiteIdApi();
let sku = "sku_example"; // String | 
let websiteId = 56; // Number | 
apiInstance.catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete(sku, websiteId, (error, data, response) => {
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
 **websiteId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

