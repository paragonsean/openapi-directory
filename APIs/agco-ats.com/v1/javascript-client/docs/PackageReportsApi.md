# AgcoApi.PackageReportsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2ClientsClientIDPackageReportsPut**](PackageReportsApi.md#apiV2ClientsClientIDPackageReportsPut) | **PUT** /api/v2/Clients/{ClientID}/PackageReports | Submit a package report
[**packageReportsBatch**](PackageReportsApi.md#packageReportsBatch) | **PUT** /api/v2/Clients/{ClientID}/PackageReports/Batch | Submit a batch of package reports
[**packageReportsDefault**](PackageReportsApi.md#packageReportsDefault) | **GET** /api/v2/Clients/{ClientID}/PackageReports | Get the package reports for a client.



## apiV2ClientsClientIDPackageReportsPut

> apiV2ClientsClientIDPackageReportsPut(clientID, updateSystemModelsPackageReport)

Submit a package report

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageReportsApi();
let clientID = "clientID_example"; // String | The Client ID
let updateSystemModelsPackageReport = new AgcoApi.UpdateSystemModelsPackageReport(); // UpdateSystemModelsPackageReport | The Package Report
apiInstance.apiV2ClientsClientIDPackageReportsPut(clientID, updateSystemModelsPackageReport, (error, data, response) => {
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
 **clientID** | **String**| The Client ID | 
 **updateSystemModelsPackageReport** | [**UpdateSystemModelsPackageReport**](UpdateSystemModelsPackageReport.md)| The Package Report | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## packageReportsBatch

> packageReportsBatch(clientID, updateSystemModelsPackageReport)

Submit a batch of package reports

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageReportsApi();
let clientID = "clientID_example"; // String | The Client ID
let updateSystemModelsPackageReport = [new AgcoApi.UpdateSystemModelsPackageReport()]; // [UpdateSystemModelsPackageReport] | The Package Reports
apiInstance.packageReportsBatch(clientID, updateSystemModelsPackageReport, (error, data, response) => {
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
 **clientID** | **String**| The Client ID | 
 **updateSystemModelsPackageReport** | [**[UpdateSystemModelsPackageReport]**](UpdateSystemModelsPackageReport.md)| The Package Reports | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## packageReportsDefault

> [UpdateSystemModelsPackageReport] packageReportsDefault(clientID)

Get the package reports for a client.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageReportsApi();
let clientID = "clientID_example"; // String | The Client ID
apiInstance.packageReportsDefault(clientID, (error, data, response) => {
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
 **clientID** | **String**| The Client ID | 

### Return type

[**[UpdateSystemModelsPackageReport]**](UpdateSystemModelsPackageReport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

