# BigRedCloudApi.CompanySettingsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companySettingsGet**](CompanySettingsApi.md#companySettingsGet) | **GET** /v1/companySettings | Returns a list of company settings. Supports OData querying protocol.  Filtering is forbidden.



## companySettingsGet

> PageResultCompanySettingDto companySettingsGet()

Returns a list of company settings. Supports OData querying protocol.  Filtering is forbidden.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CompanySettingsApi();
apiInstance.companySettingsGet((error, data, response) => {
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

[**PageResultCompanySettingDto**](PageResultCompanySettingDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

