# Covid19DataApi.CountryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDailyReportAllCountries**](CountryApi.md#getDailyReportAllCountries) | **GET** /report/country/all | getDailyReportAllCountries
[**getDailyReportByCountryCode**](CountryApi.md#getDailyReportByCountryCode) | **GET** /report/country/code | getDailyReportByCountryCode
[**getDailyReportByCountryName**](CountryApi.md#getDailyReportByCountryName) | **GET** /report/country/name | getDailyReportByCountryName
[**getLatestAllCountries**](CountryApi.md#getLatestAllCountries) | **GET** /country/all | getLatestAllCountries
[**getLatestCountryDataByCode**](CountryApi.md#getLatestCountryDataByCode) | **GET** /country/code | getLatestCountryDataByCode
[**getLatestCountryDataByName**](CountryApi.md#getLatestCountryDataByName) | **GET** /country | getLatestCountryDataByName



## getDailyReportAllCountries

> [GetDailyReportAllCountries200ResponseInner] getDailyReportAllCountries(date, opts)

getDailyReportAllCountries

Get daily report for all countries. Date is mandatory parametar. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.CountryApi();
let date = "date_example"; // String | Date of the report.
let opts = {
  'dateFormat': "'YYYY-MM-DD'", // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
  'format': "'json'" // String | Format of the response
};
apiInstance.getDailyReportAllCountries(date, opts, (error, data, response) => {
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
 **date** | **String**| Date of the report. | 
 **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to &#39;YYYY-MM-DD&#39;]
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetDailyReportAllCountries200ResponseInner]**](GetDailyReportAllCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getDailyReportByCountryCode

> [GetDailyReportAllCountries200ResponseInner] getDailyReportByCountryCode(code, date, opts)

getDailyReportByCountryCode

Get daily report for specific country. Country code and date are mandatory in parametars. Country code is in ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.CountryApi();
let code = "code_example"; // String | Country code. Country code is by ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type.
let date = "date_example"; // String | Date of the report.
let opts = {
  'dateFormat': "'YYYY-MM-DD'", // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
  'format': "'json'" // String | Format of the response
};
apiInstance.getDailyReportByCountryCode(code, date, opts, (error, data, response) => {
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
 **code** | **String**| Country code. Country code is by ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type. | 
 **date** | **String**| Date of the report. | 
 **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to &#39;YYYY-MM-DD&#39;]
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetDailyReportAllCountries200ResponseInner]**](GetDailyReportAllCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getDailyReportByCountryName

> [GetDailyReportAllCountries200ResponseInner] getDailyReportByCountryName(name, date, opts)

getDailyReportByCountryName

Get daily report for specific country. Country name and date are mandatory in parametars. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.CountryApi();
let name = "name_example"; // String | Country name.
let date = "date_example"; // String | Date of the report.
let opts = {
  'dateFormat': "'YYYY-MM-DD'", // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
  'format': "'json'" // String | Format of the response
};
apiInstance.getDailyReportByCountryName(name, date, opts, (error, data, response) => {
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
 **name** | **String**| Country name. | 
 **date** | **String**| Date of the report. | 
 **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to &#39;YYYY-MM-DD&#39;]
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetDailyReportAllCountries200ResponseInner]**](GetDailyReportAllCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLatestAllCountries

> [GetLatestCountryDataByName200ResponseInner] getLatestAllCountries(opts)

getLatestAllCountries

Get latest data from all countries.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.CountryApi();
let opts = {
  'format': "'json'" // String | Format of the response
};
apiInstance.getLatestAllCountries(opts, (error, data, response) => {
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

[**[GetLatestCountryDataByName200ResponseInner]**](GetLatestCountryDataByName200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLatestCountryDataByCode

> [GetLatestCountryDataByName200ResponseInner] getLatestCountryDataByCode(code, opts)

getLatestCountryDataByCode

Get latest data for specific country. Country code and format are in parametars. Country code is in ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.CountryApi();
let code = "code_example"; // String | Country code
let opts = {
  'format': "'json'" // String | Format of the response
};
apiInstance.getLatestCountryDataByCode(code, opts, (error, data, response) => {
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
 **code** | **String**| Country code | 
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetLatestCountryDataByName200ResponseInner]**](GetLatestCountryDataByName200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLatestCountryDataByName

> [GetLatestCountryDataByName200ResponseInner] getLatestCountryDataByName(name, opts)

getLatestCountryDataByName

Get latest data for specific country. Country name and format are in parametars.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.CountryApi();
let name = "name_example"; // String | Name of the country
let opts = {
  'format': "'json'" // String | Format of the response
};
apiInstance.getLatestCountryDataByName(name, opts, (error, data, response) => {
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
 **name** | **String**| Name of the country | 
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetLatestCountryDataByName200ResponseInner]**](GetLatestCountryDataByName200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

