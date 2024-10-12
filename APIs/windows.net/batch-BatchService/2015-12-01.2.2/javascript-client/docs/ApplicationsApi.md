# BatchService.ApplicationsApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationGet**](ApplicationsApi.md#applicationGet) | **GET** /applications/{applicationId} | 
[**applicationList**](ApplicationsApi.md#applicationList) | **GET** /applications | 



## applicationGet

> ApplicationSummary applicationGet(applicationId, apiVersion, opts)



Gets information about the specified application.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ApplicationsApi();
let applicationId = "applicationId_example"; // String | The id of the application.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.applicationGet(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The id of the application. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**ApplicationSummary**](ApplicationSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationList

> ApplicationListResult applicationList(apiVersion, opts)



Lists all of the applications available in the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ApplicationsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'maxresults': 56, // Number | Sets the maximum number of items to return in the response.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.applicationList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **maxresults** | **Number**| Sets the maximum number of items to return in the response. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**ApplicationListResult**](ApplicationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

