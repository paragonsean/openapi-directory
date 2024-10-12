# MagentoB2B.ProductsSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductRepositoryV1DeleteByIdDelete**](ProductsSkuApi.md#catalogProductRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/{sku} | products/{sku}
[**catalogProductRepositoryV1GetGet**](ProductsSkuApi.md#catalogProductRepositoryV1GetGet) | **GET** /V1/products/{sku} | products/{sku}
[**catalogProductRepositoryV1SavePut**](ProductsSkuApi.md#catalogProductRepositoryV1SavePut) | **PUT** /V1/products/{sku} | products/{sku}



## catalogProductRepositoryV1DeleteByIdDelete

> Boolean catalogProductRepositoryV1DeleteByIdDelete(sku)

products/{sku}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuApi();
let sku = "sku_example"; // String | 
apiInstance.catalogProductRepositoryV1DeleteByIdDelete(sku, (error, data, response) => {
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

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductRepositoryV1GetGet

> CatalogDataProductInterface catalogProductRepositoryV1GetGet(sku, opts)

products/{sku}

Get info about product by product SKU

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuApi();
let sku = "sku_example"; // String | 
let opts = {
  'editMode': true, // Boolean | 
  'storeId': 56, // Number | 
  'forceReload': true // Boolean | 
};
apiInstance.catalogProductRepositoryV1GetGet(sku, opts, (error, data, response) => {
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
 **editMode** | **Boolean**|  | [optional] 
 **storeId** | **Number**|  | [optional] 
 **forceReload** | **Boolean**|  | [optional] 

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductRepositoryV1SavePut

> CatalogDataProductInterface catalogProductRepositoryV1SavePut(sku, opts)

products/{sku}

Create product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuApi();
let sku = "sku_example"; // String | 
let opts = {
  'catalogProductRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductRepositoryV1SavePostRequest() // CatalogProductRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductRepositoryV1SavePut(sku, opts, (error, data, response) => {
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
 **catalogProductRepositoryV1SavePostRequest** | [**CatalogProductRepositoryV1SavePostRequest**](CatalogProductRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

