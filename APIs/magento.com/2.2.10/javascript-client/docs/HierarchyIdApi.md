# MagentoB2B.HierarchyIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCompanyHierarchyV1GetCompanyHierarchyGet**](HierarchyIdApi.md#companyCompanyHierarchyV1GetCompanyHierarchyGet) | **GET** /V1/hierarchy/{id} | hierarchy/{id}



## companyCompanyHierarchyV1GetCompanyHierarchyGet

> [CompanyDataHierarchyInterface] companyCompanyHierarchyV1GetCompanyHierarchyGet(id)

hierarchy/{id}

Returns the list of teams and company users in the company structure.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.HierarchyIdApi();
let id = 56; // Number | 
apiInstance.companyCompanyHierarchyV1GetCompanyHierarchyGet(id, (error, data, response) => {
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

[**[CompanyDataHierarchyInterface]**](CompanyDataHierarchyInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

