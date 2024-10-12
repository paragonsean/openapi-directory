# PublicApi.ProvisioningJobsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provisioningjobsJobIdGet**](ProvisioningJobsApi.md#provisioningjobsJobIdGet) | **GET** /provisioningjobs/{jobId} | Detail of a provisioning job



## provisioningjobsJobIdGet

> ProvisioningJobInfo provisioningjobsJobIdGet(jobId, jobId2)

Detail of a provisioning job

Provisioning failures may occur. Contact support in the event of a failure or wait for error resolution.&lt;br /&gt;  Do NOT retry provisioning until the job reports finished or cancelled.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.ProvisioningJobsApi();
let jobId = "jobId_example"; // String | 
let jobId2 = "jobId_example"; // String | Automatically added
apiInstance.provisioningjobsJobIdGet(jobId, jobId2, (error, data, response) => {
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
 **jobId** | **String**|  | 
 **jobId2** | **String**| Automatically added | 

### Return type

[**ProvisioningJobInfo**](ProvisioningJobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

