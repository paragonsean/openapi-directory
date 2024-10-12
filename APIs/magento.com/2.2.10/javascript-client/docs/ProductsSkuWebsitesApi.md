# MagentoB2B.ProductsSkuWebsitesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductWebsiteLinkRepositoryV1SavePost**](ProductsSkuWebsitesApi.md#catalogProductWebsiteLinkRepositoryV1SavePost) | **POST** /V1/products/{sku}/websites | products/{sku}/websites
[**catalogProductWebsiteLinkRepositoryV1SavePut**](ProductsSkuWebsitesApi.md#catalogProductWebsiteLinkRepositoryV1SavePut) | **PUT** /V1/products/{sku}/websites | products/{sku}/websites



## catalogProductWebsiteLinkRepositoryV1SavePost

> Boolean catalogProductWebsiteLinkRepositoryV1SavePost(sku, opts)

products/{sku}/websites

Assign a product to the website

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuWebsitesApi();
let sku = "sku_example"; // String | 
let opts = {
  'catalogProductWebsiteLinkRepositoryV1SavePutRequest': new MagentoB2B.CatalogProductWebsiteLinkRepositoryV1SavePutRequest() // CatalogProductWebsiteLinkRepositoryV1SavePutRequest | 
};
apiInstance.catalogProductWebsiteLinkRepositoryV1SavePost(sku, opts, (error, data, response) => {
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
 **catalogProductWebsiteLinkRepositoryV1SavePutRequest** | [**CatalogProductWebsiteLinkRepositoryV1SavePutRequest**](CatalogProductWebsiteLinkRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## catalogProductWebsiteLinkRepositoryV1SavePut

> Boolean catalogProductWebsiteLinkRepositoryV1SavePut(sku, opts)

products/{sku}/websites

Assign a product to the website

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuWebsitesApi();
let sku = "sku_example"; // String | 
let opts = {
  'catalogProductWebsiteLinkRepositoryV1SavePutRequest': new MagentoB2B.CatalogProductWebsiteLinkRepositoryV1SavePutRequest() // CatalogProductWebsiteLinkRepositoryV1SavePutRequest | 
};
apiInstance.catalogProductWebsiteLinkRepositoryV1SavePut(sku, opts, (error, data, response) => {
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
 **catalogProductWebsiteLinkRepositoryV1SavePutRequest** | [**CatalogProductWebsiteLinkRepositoryV1SavePutRequest**](CatalogProductWebsiteLinkRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

