# MagentoB2B.CompanyCompanyIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCompanyRepositoryV1DeleteByIdDelete**](CompanyCompanyIdApi.md#companyCompanyRepositoryV1DeleteByIdDelete) | **DELETE** /V1/company/{companyId} | company/{companyId}
[**companyCompanyRepositoryV1GetGet**](CompanyCompanyIdApi.md#companyCompanyRepositoryV1GetGet) | **GET** /V1/company/{companyId} | company/{companyId}
[**companyCompanyRepositoryV1SavePut**](CompanyCompanyIdApi.md#companyCompanyRepositoryV1SavePut) | **PUT** /V1/company/{companyId} | company/{companyId}



## companyCompanyRepositoryV1DeleteByIdDelete

> Boolean companyCompanyRepositoryV1DeleteByIdDelete(companyId)

company/{companyId}

Delete a company. Customers belonging to a company are not deleted with this request.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCompanyIdApi();
let companyId = 56; // Number | 
apiInstance.companyCompanyRepositoryV1DeleteByIdDelete(companyId, (error, data, response) => {
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
 **companyId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## companyCompanyRepositoryV1GetGet

> CompanyDataCompanyInterface companyCompanyRepositoryV1GetGet(companyId)

company/{companyId}

Returns company details.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCompanyIdApi();
let companyId = 56; // Number | 
apiInstance.companyCompanyRepositoryV1GetGet(companyId, (error, data, response) => {
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
 **companyId** | **Number**|  | 

### Return type

[**CompanyDataCompanyInterface**](CompanyDataCompanyInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## companyCompanyRepositoryV1SavePut

> CompanyDataCompanyInterface companyCompanyRepositoryV1SavePut(companyId, opts)

company/{companyId}

Create or update a company account.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCompanyIdApi();
let companyId = "companyId_example"; // String | 
let opts = {
  'companyCompanyRepositoryV1SavePostRequest': new MagentoB2B.CompanyCompanyRepositoryV1SavePostRequest() // CompanyCompanyRepositoryV1SavePostRequest | 
};
apiInstance.companyCompanyRepositoryV1SavePut(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companyCompanyRepositoryV1SavePostRequest** | [**CompanyCompanyRepositoryV1SavePostRequest**](CompanyCompanyRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CompanyDataCompanyInterface**](CompanyDataCompanyInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

