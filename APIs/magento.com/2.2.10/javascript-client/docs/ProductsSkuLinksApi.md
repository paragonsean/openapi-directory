# MagentoB2B.ProductsSkuLinksApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductLinkManagementV1SetProductLinksPost**](ProductsSkuLinksApi.md#catalogProductLinkManagementV1SetProductLinksPost) | **POST** /V1/products/{sku}/links | products/{sku}/links
[**catalogProductLinkRepositoryV1SavePut**](ProductsSkuLinksApi.md#catalogProductLinkRepositoryV1SavePut) | **PUT** /V1/products/{sku}/links | products/{sku}/links



## catalogProductLinkManagementV1SetProductLinksPost

> Boolean catalogProductLinkManagementV1SetProductLinksPost(sku, opts)

products/{sku}/links

Assign a product link to another product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuLinksApi();
let sku = "sku_example"; // String | 
let opts = {
  'catalogProductLinkManagementV1SetProductLinksPostRequest': new MagentoB2B.CatalogProductLinkManagementV1SetProductLinksPostRequest() // CatalogProductLinkManagementV1SetProductLinksPostRequest | 
};
apiInstance.catalogProductLinkManagementV1SetProductLinksPost(sku, opts, (error, data, response) => {
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
 **catalogProductLinkManagementV1SetProductLinksPostRequest** | [**CatalogProductLinkManagementV1SetProductLinksPostRequest**](CatalogProductLinkManagementV1SetProductLinksPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## catalogProductLinkRepositoryV1SavePut

> Boolean catalogProductLinkRepositoryV1SavePut(sku, opts)

products/{sku}/links

Save product link

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuLinksApi();
let sku = "sku_example"; // String | 
let opts = {
  'catalogProductLinkRepositoryV1SavePutRequest': new MagentoB2B.CatalogProductLinkRepositoryV1SavePutRequest() // CatalogProductLinkRepositoryV1SavePutRequest | 
};
apiInstance.catalogProductLinkRepositoryV1SavePut(sku, opts, (error, data, response) => {
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
 **catalogProductLinkRepositoryV1SavePutRequest** | [**CatalogProductLinkRepositoryV1SavePutRequest**](CatalogProductLinkRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

