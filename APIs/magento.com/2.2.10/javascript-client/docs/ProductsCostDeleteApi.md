# MagentoB2B.ProductsCostDeleteApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCostStorageV1DeletePost**](ProductsCostDeleteApi.md#catalogCostStorageV1DeletePost) | **POST** /V1/products/cost-delete | products/cost-delete



## catalogCostStorageV1DeletePost

> Boolean catalogCostStorageV1DeletePost(opts)

products/cost-delete

Delete product cost. In case of at least one of skus is not found exception will be thrown. If error occurred during the delete exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsCostDeleteApi();
let opts = {
  'catalogBasePriceStorageV1GetPostRequest': new MagentoB2B.CatalogBasePriceStorageV1GetPostRequest() // CatalogBasePriceStorageV1GetPostRequest | 
};
apiInstance.catalogCostStorageV1DeletePost(opts, (error, data, response) => {
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
 **catalogBasePriceStorageV1GetPostRequest** | [**CatalogBasePriceStorageV1GetPostRequest**](CatalogBasePriceStorageV1GetPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

