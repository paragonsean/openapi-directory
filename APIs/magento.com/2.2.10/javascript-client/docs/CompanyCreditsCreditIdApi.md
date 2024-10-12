# MagentoB2B.CompanyCreditsCreditIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditCreditLimitRepositoryV1GetGet**](CompanyCreditsCreditIdApi.md#companyCreditCreditLimitRepositoryV1GetGet) | **GET** /V1/companyCredits/{creditId} | companyCredits/{creditId}



## companyCreditCreditLimitRepositoryV1GetGet

> CompanyCreditDataCreditLimitInterface companyCreditCreditLimitRepositoryV1GetGet(creditId, opts)

companyCredits/{creditId}

Returns data on the credit limit for a specified credit limit ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCreditsCreditIdApi();
let creditId = 56; // Number | 
let opts = {
  'reload': true // Boolean | [optional]
};
apiInstance.companyCreditCreditLimitRepositoryV1GetGet(creditId, opts, (error, data, response) => {
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
 **creditId** | **Number**|  | 
 **reload** | **Boolean**| [optional] | [optional] 

### Return type

[**CompanyCreditDataCreditLimitInterface**](CompanyCreditDataCreditLimitInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

