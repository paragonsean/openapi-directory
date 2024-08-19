# ActiveDocumentationForV1.ChargesApi

All URIs are relative to *https://api.idtbeyond.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iatuChargesReportsAllCsvGet**](ChargesApi.md#iatuChargesReportsAllCsvGet) | **GET** /iatu/charges/reports/all.csv | List of account charges in CSV
[**iatuChargesReportsAllGet**](ChargesApi.md#iatuChargesReportsAllGet) | **GET** /iatu/charges/reports/all | List of account charges in JSON



## iatuChargesReportsAllCsvGet

> iatuChargesReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account charges in CSV

Returns charges by date range in CSV.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.ChargesApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let dateFrom = "'2016-01-28'"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
let dateTo = "'2016-01-28'"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
apiInstance.iatuChargesReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo, (error, data, response) => {
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


## iatuChargesReportsAllGet

> iatuChargesReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account charges in JSON

Returns charges by date range.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.ChargesApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let dateFrom = "'2016-01-28'"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
let dateTo = "'2016-01-28'"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
apiInstance.iatuChargesReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo, (error, data, response) => {
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

