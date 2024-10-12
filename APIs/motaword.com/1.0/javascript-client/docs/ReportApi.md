# MotaWordApi.ReportApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateQAReport**](ReportApi.md#generateQAReport) | **POST** /reports/qa | Generate a QA report for given filter
[**getFilterContents**](ReportApi.md#getFilterContents) | **POST** /reports/filter | Returns available options for selected timeframe.
[**getLanguagePairsReport**](ReportApi.md#getLanguagePairsReport) | **POST** /reports/language-pairs | Language pairs report
[**getProjectsReport**](ReportApi.md#getProjectsReport) | **POST** /reports/projects | Projects report
[**getUsersReport**](ReportApi.md#getUsersReport) | **POST** /reports/users | Company users report



## generateQAReport

> QaWarnings generateQAReport(opts)

Generate a QA report for given filter

Generate a QA report for given filter

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ReportApi();
let opts = {
  'qaFilter': new MotaWordApi.QaFilter() // QaFilter | 
};
apiInstance.generateQAReport(opts, (error, data, response) => {
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
 **qaFilter** | [**QaFilter**](QaFilter.md)|  | [optional] 

### Return type

[**QaWarnings**](QaWarnings.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFilterContents

> FilterContents getFilterContents(opts)

Returns available options for selected timeframe.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ReportApi();
let opts = {
  'filterDates': new MotaWordApi.FilterDates() // FilterDates | 
};
apiInstance.getFilterContents(opts, (error, data, response) => {
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
 **filterDates** | [**FilterDates**](FilterDates.md)|  | [optional] 

### Return type

[**FilterContents**](FilterContents.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLanguagePairsReport

> LanguagePairsReport getLanguagePairsReport(opts)

Language pairs report

View translation reports for each language pair with translations under your account. You can view company-wide language pairs if you have the user permission.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ReportApi();
let opts = {
  'reportFilter': new MotaWordApi.ReportFilter() // ReportFilter | 
};
apiInstance.getLanguagePairsReport(opts, (error, data, response) => {
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
 **reportFilter** | [**ReportFilter**](ReportFilter.md)|  | [optional] 

### Return type

[**LanguagePairsReport**](LanguagePairsReport.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getProjectsReport

> ProjectList getProjectsReport(opts)

Projects report

View projects under your account, with advanced filtering. You can view company-wide projects if you have the user permission.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ReportApi();
let opts = {
  'reportFilter': new MotaWordApi.ReportFilter() // ReportFilter | 
};
apiInstance.getProjectsReport(opts, (error, data, response) => {
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
 **reportFilter** | [**ReportFilter**](ReportFilter.md)|  | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUsersReport

> UsersReport getUsersReport(opts)

Company users report

View translation reports for each user under your company account. You need the permission to view users in your company.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ReportApi();
let opts = {
  'reportFilter': new MotaWordApi.ReportFilter() // ReportFilter | 
};
apiInstance.getUsersReport(opts, (error, data, response) => {
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
 **reportFilter** | [**ReportFilter**](ReportFilter.md)|  | [optional] 

### Return type

[**UsersReport**](UsersReport.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

