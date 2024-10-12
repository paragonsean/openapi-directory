# MagentoB2B.CompanyCreditsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditCreditLimitRepositoryV1SavePut**](CompanyCreditsIdApi.md#companyCreditCreditLimitRepositoryV1SavePut) | **PUT** /V1/companyCredits/{id} | companyCredits/{id}



## companyCreditCreditLimitRepositoryV1SavePut

> CompanyCreditDataCreditLimitInterface companyCreditCreditLimitRepositoryV1SavePut(id, opts)

companyCredits/{id}

Update the following company credit attributes: credit currency, credit limit and setting to exceed credit.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCreditsIdApi();
let id = "id_example"; // String | 
let opts = {
  'companyCreditCreditLimitRepositoryV1SavePutRequest': new MagentoB2B.CompanyCreditCreditLimitRepositoryV1SavePutRequest() // CompanyCreditCreditLimitRepositoryV1SavePutRequest | 
};
apiInstance.companyCreditCreditLimitRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **companyCreditCreditLimitRepositoryV1SavePutRequest** | [**CompanyCreditCreditLimitRepositoryV1SavePutRequest**](CompanyCreditCreditLimitRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**CompanyCreditDataCreditLimitInterface**](CompanyCreditDataCreditLimitInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

