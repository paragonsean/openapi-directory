# DeactivationReasonApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeactivationReasonList**](DeactivationReasonApi.md#getDeactivationReasonList) | **GET** /v1/workgroups/{workgroup_id}/deactivationReasons | List all deactivation reasons |


<a id="getDeactivationReasonList"></a>
# **getDeactivationReasonList**
> DeactivationReasonListVO getDeactivationReasonList(workgroupId)

List all deactivation reasons

List all deactivation reasons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeactivationReasonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    DeactivationReasonApi apiInstance = new DeactivationReasonApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      DeactivationReasonListVO result = apiInstance.getDeactivationReasonList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeactivationReasonApi#getDeactivationReasonList");
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
| **workgroupId** | **String**|  | |

### Return type

[**DeactivationReasonListVO**](DeactivationReasonListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

