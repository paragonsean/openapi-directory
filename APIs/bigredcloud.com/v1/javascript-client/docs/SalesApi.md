# BigRedCloudApi.SalesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesGet**](SalesApi.md#salesGet) | **GET** /v1/sales | Returns a list of company&#39;s Sales Entries, Sales Invoices and Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.



## salesGet

> PageResultSalesQueryDto salesGet()

Returns a list of company&#39;s Sales Entries, Sales Invoices and Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesApi();
apiInstance.salesGet((error, data, response) => {
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

[**PageResultSalesQueryDto**](PageResultSalesQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

