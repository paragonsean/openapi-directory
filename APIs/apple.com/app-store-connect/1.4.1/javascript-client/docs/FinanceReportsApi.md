# AppStoreConnectApi.FinanceReportsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**financeReportsGetCollection**](FinanceReportsApi.md#financeReportsGetCollection) | **GET** /v1/financeReports | 



## financeReportsGetCollection

> File financeReportsGetCollection(filterRegionCode, filterReportDate, filterReportType, filterVendorNumber)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.FinanceReportsApi();
let filterRegionCode = ["null"]; // [String] | filter by attribute 'regionCode'
let filterReportDate = ["null"]; // [String] | filter by attribute 'reportDate'
let filterReportType = ["null"]; // [String] | filter by attribute 'reportType'
let filterVendorNumber = ["null"]; // [String] | filter by attribute 'vendorNumber'
apiInstance.financeReportsGetCollection(filterRegionCode, filterReportDate, filterReportType, filterVendorNumber, (error, data, response) => {
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
 **filterRegionCode** | [**[String]**](String.md)| filter by attribute &#39;regionCode&#39; | 
 **filterReportDate** | [**[String]**](String.md)| filter by attribute &#39;reportDate&#39; | 
 **filterReportType** | [**[String]**](String.md)| filter by attribute &#39;reportType&#39; | 
 **filterVendorNumber** | [**[String]**](String.md)| filter by attribute &#39;vendorNumber&#39; | 

### Return type

**File**

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: gzip, application/json

