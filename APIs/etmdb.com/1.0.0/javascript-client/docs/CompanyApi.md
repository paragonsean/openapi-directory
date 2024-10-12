# EtMdbRestApiV1.CompanyApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companySearchRead**](CompanyApi.md#companySearchRead) | **GET** /api/v1/company/search/{company_name} | Return company search result



## companySearchRead

> companySearchRead(companyName)

Return company search result

Return company search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search companies,  For more details on how companies are listed [see here][ref]. [ref]: https://etmdb.com/en/company-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CompanyApi();
let companyName = "companyName_example"; // String | 
apiInstance.companySearchRead(companyName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

