# MagentoB2B.SharedCatalogIdAssignProductsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogProductManagementV1AssignProductsPost**](SharedCatalogIdAssignProductsApi.md#sharedCatalogProductManagementV1AssignProductsPost) | **POST** /V1/sharedCatalog/{id}/assignProducts | sharedCatalog/{id}/assignProducts



## sharedCatalogProductManagementV1AssignProductsPost

> Boolean sharedCatalogProductManagementV1AssignProductsPost(id, opts)

sharedCatalog/{id}/assignProducts

Add products into the shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdAssignProductsApi();
let id = 56; // Number | 
let opts = {
  'sharedCatalogProductManagementV1AssignProductsPostRequest': new MagentoB2B.SharedCatalogProductManagementV1AssignProductsPostRequest() // SharedCatalogProductManagementV1AssignProductsPostRequest | 
};
apiInstance.sharedCatalogProductManagementV1AssignProductsPost(id, opts, (error, data, response) => {
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
 **sharedCatalogProductManagementV1AssignProductsPostRequest** | [**SharedCatalogProductManagementV1AssignProductsPostRequest**](SharedCatalogProductManagementV1AssignProductsPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

