# MagentoB2B.CompanyCreditsHistoryHistoryIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCreditCreditHistoryManagementV1UpdatePut**](CompanyCreditsHistoryHistoryIdApi.md#companyCreditCreditHistoryManagementV1UpdatePut) | **PUT** /V1/companyCredits/history/{historyId} | companyCredits/history/{historyId}



## companyCreditCreditHistoryManagementV1UpdatePut

> Boolean companyCreditCreditHistoryManagementV1UpdatePut(historyId, opts)

companyCredits/history/{historyId}

Update the PO Number and/or comment for a Reimburse transaction.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyCreditsHistoryHistoryIdApi();
let historyId = 56; // Number | 
let opts = {
  'companyCreditCreditHistoryManagementV1UpdatePutRequest': new MagentoB2B.CompanyCreditCreditHistoryManagementV1UpdatePutRequest() // CompanyCreditCreditHistoryManagementV1UpdatePutRequest | 
};
apiInstance.companyCreditCreditHistoryManagementV1UpdatePut(historyId, opts, (error, data, response) => {
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
 **historyId** | **Number**|  | 
 **companyCreditCreditHistoryManagementV1UpdatePutRequest** | [**CompanyCreditCreditHistoryManagementV1UpdatePutRequest**](CompanyCreditCreditHistoryManagementV1UpdatePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

