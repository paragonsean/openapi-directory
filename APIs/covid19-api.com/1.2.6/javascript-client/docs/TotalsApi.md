# Covid19DataApi.TotalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDailyReportTotals**](TotalsApi.md#getDailyReportTotals) | **GET** /report/totals | getDailyReportTotals
[**getLatestTotals**](TotalsApi.md#getLatestTotals) | **GET** /totals | getLatestTotals



## getDailyReportTotals

> [GetDailyReportTotals200ResponseInner] getDailyReportTotals(opts)

getDailyReportTotals

Get daily report data for whole world.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.TotalsApi();
let opts = {
  'date': "date_example", // String | Date of the report. If you don't put this field all dates will be returned.
  'dateFormat': "'YYYY-MM-DD'", // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
  'format': "'json'" // String | Format of the response. If you don't put this field JSON will be response format.
};
apiInstance.getDailyReportTotals(opts, (error, data, response) => {
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
 **date** | **String**| Date of the report. If you don&#39;t put this field all dates will be returned. | [optional] 
 **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to &#39;YYYY-MM-DD&#39;]
 **format** | **String**| Format of the response. If you don&#39;t put this field JSON will be response format. | [optional] [default to &#39;json&#39;]

### Return type

[**[GetDailyReportTotals200ResponseInner]**](GetDailyReportTotals200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLatestTotals

> [GetLatestTotals200ResponseInner] getLatestTotals(opts)

getLatestTotals

Get latest data for whole world.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.TotalsApi();
let opts = {
  'format': "'json'" // String | Format of the response
};
apiInstance.getLatestTotals(opts, (error, data, response) => {
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
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetLatestTotals200ResponseInner]**](GetLatestTotals200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

