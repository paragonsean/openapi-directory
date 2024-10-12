# PaylocityApi.CompanyCodesApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllCompanyCodesAndDescriptionsByResource**](CompanyCodesApi.md#getAllCompanyCodesAndDescriptionsByResource) | **GET** /v2/companies/{companyId}/codes/{codeResource} | Get All Company Codes



## getAllCompanyCodesAndDescriptionsByResource

> [CompanyCodes] getAllCompanyCodesAndDescriptionsByResource(companyId, codeResource)

Get All Company Codes

Get All Company Codes for the selected company and resource

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.CompanyCodesApi();
let companyId = "companyId_example"; // String | Company Id
let codeResource = "codeResource_example"; // String | Type of Company Code. Common values costcenter1, costcenter2, costcenter3, deductions, earnings, taxes, paygrade, positions.
apiInstance.getAllCompanyCodesAndDescriptionsByResource(companyId, codeResource, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **codeResource** | **String**| Type of Company Code. Common values costcenter1, costcenter2, costcenter3, deductions, earnings, taxes, paygrade, positions. | 

### Return type

[**[CompanyCodes]**](CompanyCodes.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

