# InterzoidGetCompanyNameMatchSimilarityKeyApi.CompanyNameSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcompanymatch**](CompanyNameSimilarityKeyApi.md#getcompanymatch) | **GET** /getcompanymatch | Gets a similarity key for matching purposes for company name data



## getcompanymatch

> Getcompanymatch200Response getcompanymatch(license, company)

Gets a similarity key for matching purposes for company name data

Gets a similarity key for matching purposes for company name data

### Example

```javascript
import InterzoidGetCompanyNameMatchSimilarityKeyApi from 'interzoid_get_company_name_match_similarity_key_api';

let apiInstance = new InterzoidGetCompanyNameMatchSimilarityKeyApi.CompanyNameSimilarityKeyApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let company = "company_example"; // String | Company name from which to generate similarity key
apiInstance.getcompanymatch(license, company, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **company** | **String**| Company name from which to generate similarity key | 

### Return type

[**Getcompanymatch200Response**](Getcompanymatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

