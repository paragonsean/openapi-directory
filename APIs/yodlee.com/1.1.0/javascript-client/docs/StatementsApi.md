# YodleeCoreApis.StatementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatements**](StatementsApi.md#getStatements) | **GET** /statements | Get Statements



## getStatements

> StatementResponse getStatements(opts)

Get Statements

The statements service is used to get the list of statement related information. &lt;br&gt;By default, all the latest statements of active and to be closed accounts are retrieved for the user. &lt;br&gt;Certain sites do not have both a statement date and a due date. When a fromDate is passed as an input, all the statements that have the due date on or after the passed date are retrieved. &lt;br&gt;For sites that do not have the due date, statements that have the statement date on or after the passed date are retrieved. &lt;br&gt;The default value of \&quot;isLatest\&quot; is true. To retrieve historical statements isLatest needs to be set to false.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.StatementsApi();
let opts = {
  'accountId': "accountId_example", // String | accountId
  'container': "container_example", // String | creditCard/loan/insurance
  'fromDate': "fromDate_example", // String | from date for statement retrieval (YYYY-MM-DD)
  'isLatest': "isLatest_example", // String | isLatest (true/false)
  'status': "status_example" // String | ACTIVE,TO_BE_CLOSED,CLOSED
};
apiInstance.getStatements(opts, (error, data, response) => {
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
 **accountId** | **String**| accountId | [optional] 
 **container** | **String**| creditCard/loan/insurance | [optional] 
 **fromDate** | **String**| from date for statement retrieval (YYYY-MM-DD) | [optional] 
 **isLatest** | **String**| isLatest (true/false) | [optional] 
 **status** | **String**| ACTIVE,TO_BE_CLOSED,CLOSED | [optional] 

### Return type

[**StatementResponse**](StatementResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

