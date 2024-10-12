# LetMcApiV2FreeTier1.CompanyControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyControllerGetCompany**](CompanyControllerApi.md#companyControllerGetCompany) | **GET** /v2/tier1/{shortName}/company | Information about a specific company



## companyControllerGetCompany

> CompanyModel companyControllerGetCompany(shortName)

Information about a specific company

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.CompanyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
apiInstance.companyControllerGetCompany(shortName, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 

### Return type

[**CompanyModel**](CompanyModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

