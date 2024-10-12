# MagentoB2B.ProductsAttributesAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeRepositoryV1DeleteByIdDelete**](ProductsAttributesAttributeCodeApi.md#catalogProductAttributeRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/attributes/{attributeCode} | products/attributes/{attributeCode}
[**catalogProductAttributeRepositoryV1GetGet**](ProductsAttributesAttributeCodeApi.md#catalogProductAttributeRepositoryV1GetGet) | **GET** /V1/products/attributes/{attributeCode} | products/attributes/{attributeCode}
[**catalogProductAttributeRepositoryV1SavePut**](ProductsAttributesAttributeCodeApi.md#catalogProductAttributeRepositoryV1SavePut) | **PUT** /V1/products/attributes/{attributeCode} | products/attributes/{attributeCode}



## catalogProductAttributeRepositoryV1DeleteByIdDelete

> Boolean catalogProductAttributeRepositoryV1DeleteByIdDelete(attributeCode)

products/attributes/{attributeCode}

Delete Attribute by id

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesAttributeCodeApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.catalogProductAttributeRepositoryV1DeleteByIdDelete(attributeCode, (error, data, response) => {
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
 **attributeCode** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductAttributeRepositoryV1GetGet

> CatalogDataProductAttributeInterface catalogProductAttributeRepositoryV1GetGet(attributeCode)

products/attributes/{attributeCode}

Retrieve specific attribute

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesAttributeCodeApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.catalogProductAttributeRepositoryV1GetGet(attributeCode, (error, data, response) => {
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
 **attributeCode** | **String**|  | 

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductAttributeRepositoryV1SavePut

> CatalogDataProductAttributeInterface catalogProductAttributeRepositoryV1SavePut(attributeCode, opts)

products/attributes/{attributeCode}

Save attribute data

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesAttributeCodeApi();
let attributeCode = "attributeCode_example"; // String | 
let opts = {
  'catalogProductAttributeRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductAttributeRepositoryV1SavePostRequest() // CatalogProductAttributeRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductAttributeRepositoryV1SavePut(attributeCode, opts, (error, data, response) => {
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
 **attributeCode** | **String**|  | 
 **catalogProductAttributeRepositoryV1SavePostRequest** | [**CatalogProductAttributeRepositoryV1SavePostRequest**](CatalogProductAttributeRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

