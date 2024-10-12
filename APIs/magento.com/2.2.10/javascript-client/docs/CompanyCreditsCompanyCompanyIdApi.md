# MagentoB2B.CompanyCreditsCompanyCompanyIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet**](CompanyCreditsCompanyCompanyIdApi.md#companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet) | **GET** /V1/companyCredits/company/{companyId} | companyCredits/company/{companyId}



## companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet

> CompanyCreditDataCreditLimitInterface companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet(companyId)

companyCredits/company/{companyId}

Returns data on the credit limit for a specified company.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCreditsCompanyCompanyIdApi();
let companyId = 56; // Number | 
apiInstance.companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet(companyId, (error, data, response) => {
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

[**CompanyCreditDataCreditLimitInterface**](CompanyCreditDataCreditLimitInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

