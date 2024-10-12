# MagentoB2B.CompanyRoleRoleIdUsersApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyAclV1GetUsersByRoleIdGet**](CompanyRoleRoleIdUsersApi.md#companyAclV1GetUsersByRoleIdGet) | **GET** /V1/company/role/{roleId}/users | company/role/{roleId}/users



## companyAclV1GetUsersByRoleIdGet

> [CustomerDataCustomerInterface] companyAclV1GetUsersByRoleIdGet(roleId)

company/role/{roleId}/users

View the list of company users assigned to a specified role.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyRoleRoleIdUsersApi();
let roleId = 56; // Number | 
apiInstance.companyAclV1GetUsersByRoleIdGet(roleId, (error, data, response) => {
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
 **roleId** | **Number**|  | 

### Return type

[**[CustomerDataCustomerInterface]**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

