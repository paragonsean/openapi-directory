# ProvisioningJobsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**provisioningjobsJobIdGet**](ProvisioningJobsApi.md#provisioningjobsJobIdGet) | **GET** /provisioningjobs/{jobId} | Detail of a provisioning job |


<a id="provisioningjobsJobIdGet"></a>
# **provisioningjobsJobIdGet**
> ProvisioningJobInfo provisioningjobsJobIdGet(jobId, jobId2)

Detail of a provisioning job

Provisioning failures may occur. Contact support in the event of a failure or wait for error resolution.&lt;br /&gt;  Do NOT retry provisioning until the job reports finished or cancelled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    ProvisioningJobsApi apiInstance = new ProvisioningJobsApi(defaultClient);
    UUID jobId = UUID.randomUUID(); // UUID | 
    String jobId2 = "jobId_example"; // String | Automatically added
    try {
      ProvisioningJobInfo result = apiInstance.provisioningjobsJobIdGet(jobId, jobId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningJobsApi#provisioningjobsJobIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jobId** | **UUID**|  | |
| **jobId2** | **String**| Automatically added | |

### Return type

[**ProvisioningJobInfo**](ProvisioningJobInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

