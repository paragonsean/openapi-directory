# MagentoB2B.CompanyAssignRolesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyAclV1AssignRolesPut**](CompanyAssignRolesApi.md#companyAclV1AssignRolesPut) | **PUT** /V1/company/assignRoles | company/assignRoles



## companyAclV1AssignRolesPut

> Boolean companyAclV1AssignRolesPut(opts)

company/assignRoles

Change a role for a company user.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyAssignRolesApi();
let opts = {
  'companyAclV1AssignRolesPutRequest': new MagentoB2B.CompanyAclV1AssignRolesPutRequest() // CompanyAclV1AssignRolesPutRequest | 
};
apiInstance.companyAclV1AssignRolesPut(opts, (error, data, response) => {
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
 **companyAclV1AssignRolesPutRequest** | [**CompanyAclV1AssignRolesPutRequest**](CompanyAclV1AssignRolesPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

