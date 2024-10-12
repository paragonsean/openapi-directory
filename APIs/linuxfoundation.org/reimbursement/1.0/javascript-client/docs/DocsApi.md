# ReimbursementsApi.DocsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDoc**](DocsApi.md#getDoc) | **GET** /api-docs | Get swagger documentation



## getDoc

> getDoc()

Get swagger documentation

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';

let apiInstance = new ReimbursementsApi.DocsApi();
apiInstance.getDoc((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

