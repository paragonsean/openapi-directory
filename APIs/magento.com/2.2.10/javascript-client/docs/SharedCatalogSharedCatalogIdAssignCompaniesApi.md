# MagentoB2B.SharedCatalogSharedCatalogIdAssignCompaniesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogCompanyManagementV1AssignCompaniesPost**](SharedCatalogSharedCatalogIdAssignCompaniesApi.md#sharedCatalogCompanyManagementV1AssignCompaniesPost) | **POST** /V1/sharedCatalog/{sharedCatalogId}/assignCompanies | sharedCatalog/{sharedCatalogId}/assignCompanies



## sharedCatalogCompanyManagementV1AssignCompaniesPost

> Boolean sharedCatalogCompanyManagementV1AssignCompaniesPost(sharedCatalogId, opts)

sharedCatalog/{sharedCatalogId}/assignCompanies

Assign companies to a shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogSharedCatalogIdAssignCompaniesApi();
let sharedCatalogId = 56; // Number | 
let opts = {
  'sharedCatalogCompanyManagementV1AssignCompaniesPostRequest': new MagentoB2B.SharedCatalogCompanyManagementV1AssignCompaniesPostRequest() // SharedCatalogCompanyManagementV1AssignCompaniesPostRequest | 
};
apiInstance.sharedCatalogCompanyManagementV1AssignCompaniesPost(sharedCatalogId, opts, (error, data, response) => {
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

