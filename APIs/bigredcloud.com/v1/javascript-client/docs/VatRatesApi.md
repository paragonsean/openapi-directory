# BigRedCloudApi.VatRatesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vatRatesGet**](VatRatesApi.md#vatRatesGet) | **GET** /v1/vatRates | Returns a list of company&#39;s Vat Rates. Supports OData querying protocol.  Filtering is allowed by \&quot;vatCategoryId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.



## vatRatesGet

> PageResultVatRateDto vatRatesGet()

Returns a list of company&#39;s Vat Rates. Supports OData querying protocol.  Filtering is allowed by \&quot;vatCategoryId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.VatRatesApi();
apiInstance.vatRatesGet((error, data, response) => {
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

[**PageResultVatRateDto**](PageResultVatRateDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

