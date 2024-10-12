# BigRedCloudApi.AnalysisCategoriesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysisCategoriesGet**](AnalysisCategoriesApi.md#analysisCategoriesGet) | **GET** /v1/analysisCategories | Returns a list of company&#39;s Analysis Categories. Supports OData querying protocol.  Filtering is allowed by \&quot;categoryTypeId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.



## analysisCategoriesGet

> PageResultAnalysisCategoryDto analysisCategoriesGet()

Returns a list of company&#39;s Analysis Categories. Supports OData querying protocol.  Filtering is allowed by \&quot;categoryTypeId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.AnalysisCategoriesApi();
apiInstance.analysisCategoriesGet((error, data, response) => {
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

[**PageResultAnalysisCategoryDto**](PageResultAnalysisCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

