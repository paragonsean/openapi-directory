# MagentoB2B.CompanyRoleIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyRoleRepositoryV1SavePut**](CompanyRoleIdApi.md#companyRoleRepositoryV1SavePut) | **PUT** /V1/company/role/{id} | company/role/{id}



## companyRoleRepositoryV1SavePut

> CompanyDataRoleInterface companyRoleRepositoryV1SavePut(id, opts)

company/role/{id}

Create or update a role for a selected company.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyRoleIdApi();
let id = "id_example"; // String | 
let opts = {
  'companyRoleRepositoryV1SavePostRequest': new MagentoB2B.CompanyRoleRepositoryV1SavePostRequest() // CompanyRoleRepositoryV1SavePostRequest | 
};
apiInstance.companyRoleRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **companyRoleRepositoryV1SavePostRequest** | [**CompanyRoleRepositoryV1SavePostRequest**](CompanyRoleRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CompanyDataRoleInterface**](CompanyDataRoleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

