# MagentoB2B.SharedCatalogIdUnassignProductsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogProductManagementV1UnassignProductsPost**](SharedCatalogIdUnassignProductsApi.md#sharedCatalogProductManagementV1UnassignProductsPost) | **POST** /V1/sharedCatalog/{id}/unassignProducts | sharedCatalog/{id}/unassignProducts



## sharedCatalogProductManagementV1UnassignProductsPost

> Boolean sharedCatalogProductManagementV1UnassignProductsPost(id, opts)

sharedCatalog/{id}/unassignProducts

Remove the specified products from the shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdUnassignProductsApi();
let id = 56; // Number | 
let opts = {
  'sharedCatalogProductManagementV1AssignProductsPostRequest': new MagentoB2B.SharedCatalogProductManagementV1AssignProductsPostRequest() // SharedCatalogProductManagementV1AssignProductsPostRequest | 
};
apiInstance.sharedCatalogProductManagementV1UnassignProductsPost(id, opts, (error, data, response) => {
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

