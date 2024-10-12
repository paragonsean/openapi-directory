# MagentoB2B.ProductsAttributeSetsAttributesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeManagementV1AssignPost**](ProductsAttributeSetsAttributesApi.md#catalogProductAttributeManagementV1AssignPost) | **POST** /V1/products/attribute-sets/attributes | products/attribute-sets/attributes



## catalogProductAttributeManagementV1AssignPost

> Number catalogProductAttributeManagementV1AssignPost(opts)

products/attribute-sets/attributes

Assign attribute to attribute set

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributesApi();
let opts = {
  'catalogProductAttributeManagementV1AssignPostRequest': new MagentoB2B.CatalogProductAttributeManagementV1AssignPostRequest() // CatalogProductAttributeManagementV1AssignPostRequest | 
};
apiInstance.catalogProductAttributeManagementV1AssignPost(opts, (error, data, response) => {
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
 **catalogProductAttributeManagementV1AssignPostRequest** | [**CatalogProductAttributeManagementV1AssignPostRequest**](CatalogProductAttributeManagementV1AssignPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

