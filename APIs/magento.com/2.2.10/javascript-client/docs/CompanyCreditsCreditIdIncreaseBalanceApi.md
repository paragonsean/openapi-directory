# MagentoB2B.CompanyCreditsCreditIdIncreaseBalanceApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditCreditBalanceManagementV1IncreasePost**](CompanyCreditsCreditIdIncreaseBalanceApi.md#companyCreditCreditBalanceManagementV1IncreasePost) | **POST** /V1/companyCredits/{creditId}/increaseBalance | companyCredits/{creditId}/increaseBalance



## companyCreditCreditBalanceManagementV1IncreasePost

> Boolean companyCreditCreditBalanceManagementV1IncreasePost(creditId, opts)

companyCredits/{creditId}/increaseBalance

Increases the company credit with an Allocate, Update, Refund, Revert, or Reimburse transaction. This transaction decreases company&#39;s outstanding balance and increases company&#39;s available credit.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCreditsCreditIdIncreaseBalanceApi();
let creditId = 56; // Number | 
let opts = {
  'companyCreditCreditBalanceManagementV1DecreasePostRequest': new MagentoB2B.CompanyCreditCreditBalanceManagementV1DecreasePostRequest() // CompanyCreditCreditBalanceManagementV1DecreasePostRequest | 
};
apiInstance.companyCreditCreditBalanceManagementV1IncreasePost(creditId, opts, (error, data, response) => {
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
 **companyCreditCreditBalanceManagementV1DecreasePostRequest** | [**CompanyCreditCreditBalanceManagementV1DecreasePostRequest**](CompanyCreditCreditBalanceManagementV1DecreasePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

