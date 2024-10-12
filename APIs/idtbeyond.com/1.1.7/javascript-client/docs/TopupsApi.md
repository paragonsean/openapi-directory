# ActiveDocumentationForV1.TopupsApi

All URIs are relative to *https://api.idtbeyond.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iatuTopupsPost**](TopupsApi.md#iatuTopupsPost) | **POST** /iatu/topups | Topup a mobile phone
[**iatuTopupsReportsAllCsvGet**](TopupsApi.md#iatuTopupsReportsAllCsvGet) | **GET** /iatu/topups/reports/all.csv | List of account topups in CSV
[**iatuTopupsReportsAllGet**](TopupsApi.md#iatuTopupsReportsAllGet) | **GET** /iatu/topups/reports/all | List of account topups in JSON
[**iatuTopupsReportsPost**](TopupsApi.md#iatuTopupsReportsPost) | **POST** /iatu/topups/reports | Search topups transactions
[**iatuTopupsReportsTotalsGet**](TopupsApi.md#iatuTopupsReportsTotalsGet) | **GET** /iatu/topups/reports/totals | Summary of account topups in JSON
[**iatuTopupsReversePost**](TopupsApi.md#iatuTopupsReversePost) | **POST** /iatu/topups/reverse | Reversal of a Topup



## iatuTopupsPost

> iatuTopupsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body)

Topup a mobile phone

Submits an IATU transaction request.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.TopupsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let body = new ActiveDocumentationForV1.Topups(); // Topups | Topups details
apiInstance.iatuTopupsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **body** | [**Topups**](Topups.md)| Topups details | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## iatuTopupsReportsAllCsvGet

> iatuTopupsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account topups in CSV

Returns topups by date range in CSV.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.TopupsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let dateFrom = "'2016-01-28'"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
let dateTo = "'2016-01-28'"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
apiInstance.iatuTopupsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **dateFrom** | **String**| The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to &#39;2016-01-28&#39;]
 **dateTo** | **String**| The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to &#39;2016-01-28&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iatuTopupsReportsAllGet

> iatuTopupsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account topups in JSON

Returns topups by date range.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.TopupsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let dateFrom = "'2016-01-28'"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
let dateTo = "'2016-01-28'"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
apiInstance.iatuTopupsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **dateFrom** | **String**| The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to &#39;2016-01-28&#39;]
 **dateTo** | **String**| The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to &#39;2016-01-28&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iatuTopupsReportsPost

> iatuTopupsReportsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body)

Search topups transactions

Search topups transactions, by date, with client_transaction_id or to_service_number. Use &#39;client_transaction_id&#39; to search by transaction number, or &#39;to_service_number&#39; to get transaction status.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.TopupsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let body = new ActiveDocumentationForV1.TopupsReports(); // TopupsReports | Topups reports request details
apiInstance.iatuTopupsReportsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **body** | [**TopupsReports**](TopupsReports.md)| Topups reports request details | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## iatuTopupsReportsTotalsGet

> iatuTopupsReportsTotalsGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

Summary of account topups in JSON

Returns topups totals by date range.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.TopupsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let dateFrom = "'2016-01-28'"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
let dateTo = "'2016-01-28'"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
apiInstance.iatuTopupsReportsTotalsGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **dateFrom** | **String**| The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to &#39;2016-01-28&#39;]
 **dateTo** | **String**| The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to &#39;2016-01-28&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iatuTopupsReversePost

> iatuTopupsReversePost(xIdtBeyondAppId, xIdtBeyondAppKey, body)

Reversal of a Topup

Occasionally, a carrier will not be able to successfully complete a topup request. In this case, we will attempt to automatically reverse the transaction for you, and return the money into your account. In the case when this is not possible, you may need to request a reverse on the transaction that has a status of &#39;transaction_status&#39; &#39;notredeemed&#39;.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.TopupsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let body = new ActiveDocumentationForV1.TopupsReversal(); // TopupsReversal | Topups details
apiInstance.iatuTopupsReversePost(xIdtBeyondAppId, xIdtBeyondAppKey, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **body** | [**TopupsReversal**](TopupsReversal.md)| Topups details | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

