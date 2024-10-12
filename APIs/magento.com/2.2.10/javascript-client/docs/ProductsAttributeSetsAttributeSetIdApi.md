# MagentoB2B.ProductsAttributeSetsAttributeSetIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogAttributeSetRepositoryV1DeleteByIdDelete**](ProductsAttributeSetsAttributeSetIdApi.md#catalogAttributeSetRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/attribute-sets/{attributeSetId} | products/attribute-sets/{attributeSetId}
[**catalogAttributeSetRepositoryV1GetGet**](ProductsAttributeSetsAttributeSetIdApi.md#catalogAttributeSetRepositoryV1GetGet) | **GET** /V1/products/attribute-sets/{attributeSetId} | products/attribute-sets/{attributeSetId}
[**catalogAttributeSetRepositoryV1SavePut**](ProductsAttributeSetsAttributeSetIdApi.md#catalogAttributeSetRepositoryV1SavePut) | **PUT** /V1/products/attribute-sets/{attributeSetId} | products/attribute-sets/{attributeSetId}



## catalogAttributeSetRepositoryV1DeleteByIdDelete

> Boolean catalogAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId)

products/attribute-sets/{attributeSetId}

Remove attribute set by given ID

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdApi();
let attributeSetId = 56; // Number | 
apiInstance.catalogAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId, (error, data, response) => {
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
 **attributeSetId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogAttributeSetRepositoryV1GetGet

> EavDataAttributeSetInterface catalogAttributeSetRepositoryV1GetGet(attributeSetId)

products/attribute-sets/{attributeSetId}

Retrieve attribute set information based on given ID

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdApi();
let attributeSetId = 56; // Number | 
apiInstance.catalogAttributeSetRepositoryV1GetGet(attributeSetId, (error, data, response) => {
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
 **attributeSetId** | **Number**|  | 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogAttributeSetRepositoryV1SavePut

> EavDataAttributeSetInterface catalogAttributeSetRepositoryV1SavePut(attributeSetId, opts)

products/attribute-sets/{attributeSetId}

Save attribute set data

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdApi();
let attributeSetId = "attributeSetId_example"; // String | 
let opts = {
  'eavAttributeSetRepositoryV1SavePutRequest': new MagentoB2B.EavAttributeSetRepositoryV1SavePutRequest() // EavAttributeSetRepositoryV1SavePutRequest | 
};
apiInstance.catalogAttributeSetRepositoryV1SavePut(attributeSetId, opts, (error, data, response) => {
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
 **attributeSetId** | **String**|  | 
 **eavAttributeSetRepositoryV1SavePutRequest** | [**EavAttributeSetRepositoryV1SavePutRequest**](EavAttributeSetRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

