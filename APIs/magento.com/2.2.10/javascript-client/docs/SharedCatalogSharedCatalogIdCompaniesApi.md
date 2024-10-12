# MagentoB2B.SharedCatalogSharedCatalogIdCompaniesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogCompanyManagementV1GetCompaniesGet**](SharedCatalogSharedCatalogIdCompaniesApi.md#sharedCatalogCompanyManagementV1GetCompaniesGet) | **GET** /V1/sharedCatalog/{sharedCatalogId}/companies | sharedCatalog/{sharedCatalogId}/companies



## sharedCatalogCompanyManagementV1GetCompaniesGet

> String sharedCatalogCompanyManagementV1GetCompaniesGet(sharedCatalogId)

sharedCatalog/{sharedCatalogId}/companies

Return the list of company IDs for the companies assigned to the selected catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogSharedCatalogIdCompaniesApi();
let sharedCatalogId = 56; // Number | 
apiInstance.sharedCatalogCompanyManagementV1GetCompaniesGet(sharedCatalogId, (error, data, response) => {
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

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

