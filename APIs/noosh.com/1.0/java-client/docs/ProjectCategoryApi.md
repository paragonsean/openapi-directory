# ProjectCategoryApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProjectCategoryList**](ProjectCategoryApi.md#getProjectCategoryList) | **GET** /v1/workgroups/{workgroup_id}/projectCategory | List the project categories |
| [**getProjectCategoryListOfClient**](ProjectCategoryApi.md#getProjectCategoryListOfClient) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectCategory | List the project categories of client side |


<a id="getProjectCategoryList"></a>
# **getProjectCategoryList**
> ProjectCategoryListVO getProjectCategoryList(workgroupId)

List the project categories

List the project categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectCategoryApi apiInstance = new ProjectCategoryApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ProjectCategoryListVO result = apiInstance.getProjectCategoryList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectCategoryApi#getProjectCategoryList");
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

[**ProjectCategoryListVO**](ProjectCategoryListVO.md)

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

<a id="getProjectCategoryListOfClient"></a>
# **getProjectCategoryListOfClient**
> ProjectCategoryListVO getProjectCategoryListOfClient(workgroupId, clientWorkgroupId)

List the project categories of client side

List the project categories of client side

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectCategoryApi apiInstance = new ProjectCategoryApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String clientWorkgroupId = "clientWorkgroupId_example"; // String | 
    try {
      ProjectCategoryListVO result = apiInstance.getProjectCategoryListOfClient(workgroupId, clientWorkgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectCategoryApi#getProjectCategoryListOfClient");
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

[**ProjectCategoryListVO**](ProjectCategoryListVO.md)

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
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

