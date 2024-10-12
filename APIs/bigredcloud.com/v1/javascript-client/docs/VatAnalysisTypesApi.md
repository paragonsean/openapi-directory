# BigRedCloudApi.VatAnalysisTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vatAnalysisTypesGet**](VatAnalysisTypesApi.md#vatAnalysisTypesGet) | **GET** /v1/vatAnalysisTypes | Returns a list of global Vat Analysis Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.



## vatAnalysisTypesGet

> PageResultVatAnalysisTypeDto vatAnalysisTypesGet()

Returns a list of global Vat Analysis Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.VatAnalysisTypesApi();
apiInstance.vatAnalysisTypesGet((error, data, response) => {
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

[**PageResultVatAnalysisTypeDto**](PageResultVatAnalysisTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

