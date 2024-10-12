# Pims.SeriesApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllSeries**](SeriesApi.md#fetchAllSeries) | **GET** /series | Find all series
[**fetchOneSeries**](SeriesApi.md#fetchOneSeries) | **GET** /series/{series_id} | Get one series by ID



## fetchAllSeries

> [SeriesEntity] fetchAllSeries(opts)

Find all series

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.SeriesApi();
let opts = {
  'label': "label_example", // String | Find only the venues whose label contains this value.
  'fromDate': new Date("2013-10-20"), // Date | Find only the series starting after this date.
  'toDate': new Date("2013-10-20"), // Date | Find only the series ending before this date.
  'type': "type_example", // String | Find only the series whose type is equal to this value.
  'sort': "'first_date'", // String | Sort the series in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllSeries(opts, (error, data, response) => {
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
 **label** | **String**| Find only the venues whose label contains this value. | [optional] 
 **fromDate** | **Date**| Find only the series starting after this date. | [optional] 
 **toDate** | **Date**| Find only the series ending before this date. | [optional] 
 **type** | **String**| Find only the series whose type is equal to this value. | [optional] 
 **sort** | **String**| Sort the series in the corresponding order. | [optional] [default to &#39;first_date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[SeriesEntity]**](SeriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneSeries

> SeriesEntity fetchOneSeries(seriesId, opts)

Get one series by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.SeriesApi();
let seriesId = 56; // Number | ID of the targeted series.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOneSeries(seriesId, opts, (error, data, response) => {
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
 **seriesId** | **Number**| ID of the targeted series. | 
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**SeriesEntity**](SeriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

