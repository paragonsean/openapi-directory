# MagentoB2B.ProductsSkuOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete**](ProductsSkuOptionsOptionIdApi.md#catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete) | **DELETE** /V1/products/{sku}/options/{optionId} | products/{sku}/options/{optionId}
[**catalogProductCustomOptionRepositoryV1GetGet**](ProductsSkuOptionsOptionIdApi.md#catalogProductCustomOptionRepositoryV1GetGet) | **GET** /V1/products/{sku}/options/{optionId} | products/{sku}/options/{optionId}



## catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete

> Boolean catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete(sku, optionId)

products/{sku}/options/{optionId}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuOptionsOptionIdApi();
let sku = "sku_example"; // String | 
let optionId = 56; // Number | 
apiInstance.catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete(sku, optionId, (error, data, response) => {
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
 **optionId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductCustomOptionRepositoryV1GetGet

> CatalogDataProductCustomOptionInterface catalogProductCustomOptionRepositoryV1GetGet(sku, optionId)

products/{sku}/options/{optionId}

Get custom option for a specific product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuOptionsOptionIdApi();
let sku = "sku_example"; // String | 
let optionId = 56; // Number | 
apiInstance.catalogProductCustomOptionRepositoryV1GetGet(sku, optionId, (error, data, response) => {
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
 **optionId** | **Number**|  | 

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

