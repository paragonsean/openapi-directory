# ReportsApi.DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCallLogs**](DefaultApi.md#getCallLogs) | **GET** /accounts/{account_id}/call-logs | Retrieve call logs for your account



## getCallLogs

> CallLogsHalResponse getCallLogs(accountId, startgte, startlte, pageSize, page, opts)

Retrieve call logs for your account

Retrieve call logs for your account

### Example

```javascript
import ReportsApi from 'reports_api';
let defaultClient = ReportsApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ReportsApi.DefaultApi();
let accountId = "913874"; // String | The Vonage Business Cloud account ID
let startgte = "2019-01-01 00:00:00"; // String | Filter records by start date (greater equal or equal to)
let startlte = "2019-01-01 00:00:00"; // String | Filter records by start date (less equal or equal to)
let pageSize = 10; // Number | Number of records per page
let page = 10; // Number | Current page number
let opts = {
  'endgte': "2019-01-01 00:00:00", // String | Filter records by end date (greater equal or equal to)
  'endlte': "2019-01-01 00:00:00", // String | Filter records by end date (less equal or equal to)
  'to': "17325550100", // String | Filter by called number
  'from': "17325550100", // String | Filter by source number
  'sourceUser': "sourceUser_example", // String | Filter by source user
  'destinationUser': "destinationUser_example", // String | Filter by destination user
  'direction': "Inbound" // String | Filter by call direction.
};
apiInstance.getCallLogs(accountId, startgte, startlte, pageSize, page, opts, (error, data, response) => {
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
 **accountId** | **String**| The Vonage Business Cloud account ID | 
 **startgte** | **String**| Filter records by start date (greater equal or equal to) | 
 **startlte** | **String**| Filter records by start date (less equal or equal to) | 
 **pageSize** | **Number**| Number of records per page | [default to 10]
 **page** | **Number**| Current page number | [default to 0]
 **endgte** | **String**| Filter records by end date (greater equal or equal to) | [optional] 
 **endlte** | **String**| Filter records by end date (less equal or equal to) | [optional] 
 **to** | **String**| Filter by called number | [optional] 
 **from** | **String**| Filter by source number | [optional] 
 **sourceUser** | **String**| Filter by source user | [optional] 
 **destinationUser** | **String**| Filter by destination user | [optional] 
 **direction** | **String**| Filter by call direction. | [optional] 

### Return type

[**CallLogsHalResponse**](CallLogsHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

