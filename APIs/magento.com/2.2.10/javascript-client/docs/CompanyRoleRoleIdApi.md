# MagentoB2B.CompanyRoleRoleIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyRoleRepositoryV1DeleteDelete**](CompanyRoleRoleIdApi.md#companyRoleRepositoryV1DeleteDelete) | **DELETE** /V1/company/role/{roleId} | company/role/{roleId}
[**companyRoleRepositoryV1GetGet**](CompanyRoleRoleIdApi.md#companyRoleRepositoryV1GetGet) | **GET** /V1/company/role/{roleId} | company/role/{roleId}



## companyRoleRepositoryV1DeleteDelete

> Boolean companyRoleRepositoryV1DeleteDelete(roleId)

company/role/{roleId}

Delete a role.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyRoleRoleIdApi();
let roleId = 56; // Number | 
apiInstance.companyRoleRepositoryV1DeleteDelete(roleId, (error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## companyRoleRepositoryV1GetGet

> CompanyDataRoleInterface companyRoleRepositoryV1GetGet(roleId)

company/role/{roleId}

Returns the list of permissions for a specified role.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyRoleRoleIdApi();
let roleId = 56; // Number | 
apiInstance.companyRoleRepositoryV1GetGet(roleId, (error, data, response) => {
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

[**CompanyDataRoleInterface**](CompanyDataRoleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

