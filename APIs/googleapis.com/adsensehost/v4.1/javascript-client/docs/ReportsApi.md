# AdSenseHostApi.ReportsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adsensehostReportsGenerate**](ReportsApi.md#adsensehostReportsGenerate) | **GET** /reports | 



## adsensehostReportsGenerate

> Report adsensehostReportsGenerate(startDate, endDate, opts)



Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify \&quot;alt&#x3D;csv\&quot; as a query parameter.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.ReportsApi();
let startDate = "startDate_example"; // String | Start of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
let endDate = "endDate_example"; // String | End of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'dimension': ["null"], // [String] | Dimensions to base the report on.
  'filter': ["null"], // [String] | Filters to be run on the report.
  'locale': "locale_example", // String | Optional locale to use for translating report output to a local language. Defaults to \"en_US\" if not specified.
  'maxResults': 56, // Number | The maximum number of rows of report data to return.
  'metric': ["null"], // [String] | Numeric columns to include in the report.
  'sort': ["null"], // [String] | The name of a dimension or metric to sort the resulting report on, optionally prefixed with \"+\" to sort ascending or \"-\" to sort descending. If no prefix is specified, the column is sorted ascending.
  'startIndex': 56 // Number | Index of the first row of report data to return.
};
apiInstance.adsensehostReportsGenerate(startDate, endDate, opts, (error, data, response) => {
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
 **startDate** | **String**| Start of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | 
 **endDate** | **String**| End of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **dimension** | [**[String]**](String.md)| Dimensions to base the report on. | [optional] 
 **filter** | [**[String]**](String.md)| Filters to be run on the report. | [optional] 
 **locale** | **String**| Optional locale to use for translating report output to a local language. Defaults to \&quot;en_US\&quot; if not specified. | [optional] 
 **maxResults** | **Number**| The maximum number of rows of report data to return. | [optional] 
 **metric** | [**[String]**](String.md)| Numeric columns to include in the report. | [optional] 
 **sort** | [**[String]**](String.md)| The name of a dimension or metric to sort the resulting report on, optionally prefixed with \&quot;+\&quot; to sort ascending or \&quot;-\&quot; to sort descending. If no prefix is specified, the column is sorted ascending. | [optional] 
 **startIndex** | **Number**| Index of the first row of report data to return. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

