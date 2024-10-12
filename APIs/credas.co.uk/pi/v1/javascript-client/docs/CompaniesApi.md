# CredasApi.CompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompany**](CompaniesApi.md#getCompany) | **GET** /api/companies/{companyId} | 
[**searchCompany**](CompaniesApi.md#searchCompany) | **POST** /api/companies | Searches for a company based on its Company Number and returns its details.



## getCompany

> CredasApiModelsCompaniesCompanyDetail getCompany(companyId, apikey)



### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.CompaniesApi();
let companyId = "companyId_example"; // String | 
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getCompany(companyId, apikey, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsCompaniesCompanyDetail**](CredasApiModelsCompaniesCompanyDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## searchCompany

> CredasApiModelsCompaniesCompanyDetail searchCompany(apikey, opts)

Searches for a company based on its Company Number and returns its details.

If a company appears multiple times within the structure, it will only be detailed in full (i.e. with significant ownership details) in its first instance. Subsequent instances will be               marked as duplicates.              Whilst duplicate instances of companies can and will be identified, it is not possible to categorically identify duplicated people.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.CompaniesApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'companyNumber': "companyNumber_example" // String | The company registration number of the company that should be searched.
};
apiInstance.searchCompany(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **companyNumber** | **String**| The company registration number of the company that should be searched. | [optional] 

### Return type

[**CredasApiModelsCompaniesCompanyDetail**](CredasApiModelsCompaniesCompanyDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

