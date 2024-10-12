# TwilioBulkexports.BulkexportsV1JobApi

All URIs are relative to *https://bulkexports.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteJob**](BulkexportsV1JobApi.md#deleteJob) | **DELETE** /v1/Exports/Jobs/{JobSid} | 
[**fetchJob**](BulkexportsV1JobApi.md#fetchJob) | **GET** /v1/Exports/Jobs/{JobSid} | 



## deleteJob

> deleteJob(jobSid)





### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1JobApi();
let jobSid = "jobSid_example"; // String | The unique string that that we created to identify the Bulk Export job
apiInstance.deleteJob(jobSid, (error, data, response) => {
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
 **jobSid** | **String**| The unique string that that we created to identify the Bulk Export job | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchJob

> BulkexportsV1ExportJob fetchJob(jobSid)





### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1JobApi();
let jobSid = "jobSid_example"; // String | The unique string that that we created to identify the Bulk Export job
apiInstance.fetchJob(jobSid, (error, data, response) => {
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
 **jobSid** | **String**| The unique string that that we created to identify the Bulk Export job | 

### Return type

[**BulkexportsV1ExportJob**](BulkexportsV1ExportJob.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

