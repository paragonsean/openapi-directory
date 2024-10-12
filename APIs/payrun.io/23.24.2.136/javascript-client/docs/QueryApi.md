# PayRunIo.QueryApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQueryResponse**](QueryApi.md#getQueryResponse) | **POST** /Query | Get the query result



## getQueryResponse

> File getQueryResponse(authorization, apiVersion, query)

Get the query result

Get the results for the specified query

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.QueryApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let query = new PayRunIo.Query(); // Query | The query object to be executed against the application data.
apiInstance.getQueryResponse(authorization, apiVersion, query, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **query** | [**Query**](Query.md)| The query object to be executed against the application data. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

