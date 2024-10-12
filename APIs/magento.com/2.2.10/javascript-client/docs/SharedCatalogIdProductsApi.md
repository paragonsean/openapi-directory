# MagentoB2B.SharedCatalogIdProductsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogProductManagementV1GetProductsGet**](SharedCatalogIdProductsApi.md#sharedCatalogProductManagementV1GetProductsGet) | **GET** /V1/sharedCatalog/{id}/products | sharedCatalog/{id}/products



## sharedCatalogProductManagementV1GetProductsGet

> [String] sharedCatalogProductManagementV1GetProductsGet(id)

sharedCatalog/{id}/products

Return the list of product SKUs in the selected shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdProductsApi();
let id = 56; // Number | 
apiInstance.sharedCatalogProductManagementV1GetProductsGet(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

