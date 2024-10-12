# MagentoB2B.ProductsMediaTypesAttributeSetNameApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductMediaAttributeManagementV1GetListGet**](ProductsMediaTypesAttributeSetNameApi.md#catalogProductMediaAttributeManagementV1GetListGet) | **GET** /V1/products/media/types/{attributeSetName} | products/media/types/{attributeSetName}



## catalogProductMediaAttributeManagementV1GetListGet

> [CatalogDataProductAttributeInterface] catalogProductMediaAttributeManagementV1GetListGet(attributeSetName)

products/media/types/{attributeSetName}

Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsMediaTypesAttributeSetNameApi();
let attributeSetName = "attributeSetName_example"; // String | 
apiInstance.catalogProductMediaAttributeManagementV1GetListGet(attributeSetName, (error, data, response) => {
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
 **attributeSetName** | **String**|  | 

### Return type

[**[CatalogDataProductAttributeInterface]**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

