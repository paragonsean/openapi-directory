# BigRedCloudApi.CompanySetupConfigApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companySetupConfigGet**](CompanySetupConfigApi.md#companySetupConfigGet) | **GET** /v1/companySetupConfig | Returns the company configuration settings.
[**companySetupConfigGetCompanyOptions**](CompanySetupConfigApi.md#companySetupConfigGetCompanyOptions) | **GET** /v1/companySetupConfig/getCompanyOptions | Returns the company option setting.
[**companySetupConfigGetFinancialYear**](CompanySetupConfigApi.md#companySetupConfigGetFinancialYear) | **GET** /v1/companySetupConfig/getFinancialYear | Returns the financial year.



## companySetupConfigGet

> CompanySetupConfigViewModel companySetupConfigGet()

Returns the company configuration settings.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CompanySetupConfigApi();
apiInstance.companySetupConfigGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanySetupConfigViewModel**](CompanySetupConfigViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companySetupConfigGetCompanyOptions

> CompanyOptionDto companySetupConfigGetCompanyOptions()

Returns the company option setting.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CompanySetupConfigApi();
apiInstance.companySetupConfigGetCompanyOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyOptionDto**](CompanyOptionDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companySetupConfigGetFinancialYear

> FinancialYearDto companySetupConfigGetFinancialYear()

Returns the financial year.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CompanySetupConfigApi();
apiInstance.companySetupConfigGetFinancialYear((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**FinancialYearDto**](FinancialYearDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

