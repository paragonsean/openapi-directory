# MagentoB2B.CompanyCreditsCreditIdDecreaseBalanceApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditCreditBalanceManagementV1DecreasePost**](CompanyCreditsCreditIdDecreaseBalanceApi.md#companyCreditCreditBalanceManagementV1DecreasePost) | **POST** /V1/companyCredits/{creditId}/decreaseBalance | companyCredits/{creditId}/decreaseBalance



## companyCreditCreditBalanceManagementV1DecreasePost

> Boolean companyCreditCreditBalanceManagementV1DecreasePost(creditId, opts)

companyCredits/{creditId}/decreaseBalance

Decreases the company credit with an Update, Reimburse, or Purchase transaction. This transaction increases company&#39;s outstanding balance and decreases company&#39;s available credit.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCreditsCreditIdDecreaseBalanceApi();
let creditId = 56; // Number | 
let opts = {
  'companyCreditCreditBalanceManagementV1DecreasePostRequest': new MagentoB2B.CompanyCreditCreditBalanceManagementV1DecreasePostRequest() // CompanyCreditCreditBalanceManagementV1DecreasePostRequest | 
};
apiInstance.companyCreditCreditBalanceManagementV1DecreasePost(creditId, opts, (error, data, response) => {
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

