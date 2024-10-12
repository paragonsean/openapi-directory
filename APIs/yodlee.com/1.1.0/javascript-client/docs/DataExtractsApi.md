# YodleeCoreApis.DataExtractsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataExtractsEvents**](DataExtractsApi.md#getDataExtractsEvents) | **GET** /dataExtracts/events | Get Events
[**getDataExtractsUserData**](DataExtractsApi.md#getDataExtractsUserData) | **GET** /dataExtracts/userData | Get userData



## getDataExtractsEvents

> DataExtractsEventResponse getDataExtractsEvents(eventName, fromDate, toDate)

Get Events

The get extracts events service is used to learn about occurrences of data extract related events. This service currently supports only the DATA_UPDATES event.&lt;br&gt;Passing the event name as DATA_UPDATES provides information about users for whom data has been modified in the system for the specified time range. To learn more, please refer to the &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/DataExtracts\&quot;&gt;dataExtracts&lt;/a&gt; page.&lt;br&gt;You can retrieve data in increments of no more than 60 minutes over the period of the last 7 days from today&#39;s date.&lt;br&gt;This service is only invoked with either admin access token or a cobrand session.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.DataExtractsApi();
let eventName = "eventName_example"; // String | Event Name
let fromDate = "fromDate_example"; // String | From DateTime (YYYY-MM-DDThh:mm:ssZ)
let toDate = "toDate_example"; // String | To DateTime (YYYY-MM-DDThh:mm:ssZ)
apiInstance.getDataExtractsEvents(eventName, fromDate, toDate, (error, data, response) => {
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
 **eventName** | **String**| Event Name | 
 **fromDate** | **String**| From DateTime (YYYY-MM-DDThh:mm:ssZ) | 
 **toDate** | **String**| To DateTime (YYYY-MM-DDThh:mm:ssZ) | 

### Return type

[**DataExtractsEventResponse**](DataExtractsEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getDataExtractsUserData

> DataExtractsUserDataResponse getDataExtractsUserData(fromDate, loginName, toDate)

Get userData

The get user data service is used to get a user&#39;s modified data for a particular period of time for accounts, transactions, holdings, and provider account information.&lt;br&gt;The time difference between fromDate and toDate fields cannot be more than 60 minutes.&lt;br&gt;By default, pagination is available for the transaction entity in this API. In the first response, the API will retrieve 500 transactions along with other data. The response header will provide a link to retrieve the next set of transactions.&lt;br&gt;In the response body of the first API response, totalTransactionsCount indicates the total number of transactions the API will retrieve for the user.&lt;br&gt;This service is only invoked with either admin access token or a cobrand session.&lt;br/&gt;Refer to &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/DataExtracts\&quot;&gt;dataExtracts&lt;/a&gt; page for more information.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.DataExtractsApi();
let fromDate = "fromDate_example"; // String | From DateTime (YYYY-MM-DDThh:mm:ssZ)
let loginName = "loginName_example"; // String | Login Name
let toDate = "toDate_example"; // String | To DateTime (YYYY-MM-DDThh:mm:ssZ)
apiInstance.getDataExtractsUserData(fromDate, loginName, toDate, (error, data, response) => {
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
 **fromDate** | **String**| From DateTime (YYYY-MM-DDThh:mm:ssZ) | 
 **loginName** | **String**| Login Name | 
 **toDate** | **String**| To DateTime (YYYY-MM-DDThh:mm:ssZ) | 

### Return type

[**DataExtractsUserDataResponse**](DataExtractsUserDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

