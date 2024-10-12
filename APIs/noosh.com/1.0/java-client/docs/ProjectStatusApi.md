# ProjectStatusApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProjectStatus**](ProjectStatusApi.md#getProjectStatus) | **GET** /v1/workgroups/{workgroup_id}/projectStatus | List the project status |
| [**getProjectStatusOfClient**](ProjectStatusApi.md#getProjectStatusOfClient) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectStatus | List the project status of client |


<a id="getProjectStatus"></a>
# **getProjectStatus**
> ProjectStatusListVO getProjectStatus(workgroupId)

List the project status

List the project status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectStatusApi apiInstance = new ProjectStatusApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ProjectStatusListVO result = apiInstance.getProjectStatus(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusApi#getProjectStatus");
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

[**ProjectStatusListVO**](ProjectStatusListVO.md)

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

<a id="getProjectStatusOfClient"></a>
# **getProjectStatusOfClient**
> ProjectStatusListVO getProjectStatusOfClient(workgroupId, clientWorkgroupId)

List the project status of client

List the project status of client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectStatusApi apiInstance = new ProjectStatusApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String clientWorkgroupId = "clientWorkgroupId_example"; // String | 
    try {
      ProjectStatusListVO result = apiInstance.getProjectStatusOfClient(workgroupId, clientWorkgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusApi#getProjectStatusOfClient");
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
| **clientWorkgroupId** | **String**|  | |

### Return type

[**ProjectStatusListVO**](ProjectStatusListVO.md)

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

