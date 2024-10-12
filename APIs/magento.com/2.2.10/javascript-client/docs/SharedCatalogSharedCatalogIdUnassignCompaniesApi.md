# MagentoB2B.SharedCatalogSharedCatalogIdUnassignCompaniesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogCompanyManagementV1UnassignCompaniesPost**](SharedCatalogSharedCatalogIdUnassignCompaniesApi.md#sharedCatalogCompanyManagementV1UnassignCompaniesPost) | **POST** /V1/sharedCatalog/{sharedCatalogId}/unassignCompanies | sharedCatalog/{sharedCatalogId}/unassignCompanies



## sharedCatalogCompanyManagementV1UnassignCompaniesPost

> Boolean sharedCatalogCompanyManagementV1UnassignCompaniesPost(sharedCatalogId, opts)

sharedCatalog/{sharedCatalogId}/unassignCompanies

Unassign companies from a shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogSharedCatalogIdUnassignCompaniesApi();
let sharedCatalogId = 56; // Number | 
let opts = {
  'sharedCatalogCompanyManagementV1AssignCompaniesPostRequest': new MagentoB2B.SharedCatalogCompanyManagementV1AssignCompaniesPostRequest() // SharedCatalogCompanyManagementV1AssignCompaniesPostRequest | 
};
apiInstance.sharedCatalogCompanyManagementV1UnassignCompaniesPost(sharedCatalogId, opts, (error, data, response) => {
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
 **sharedCatalogId** | **Number**|  | 
 **sharedCatalogCompanyManagementV1AssignCompaniesPostRequest** | [**SharedCatalogCompanyManagementV1AssignCompaniesPostRequest**](SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

