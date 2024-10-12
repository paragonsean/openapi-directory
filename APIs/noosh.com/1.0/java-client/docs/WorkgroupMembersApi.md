# WorkgroupMembersApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWorkgroupMemberInfo**](WorkgroupMembersApi.md#getWorkgroupMemberInfo) | **GET** /v1/workgroups/{workgroup_id}/workgroupMembers/{user_id} | Workgroup Member Info |
| [**getWorkgroupMemberList**](WorkgroupMembersApi.md#getWorkgroupMemberList) | **GET** /v1/workgroups/{workgroup_id}/workgroupMembers | List the workgroup members |


<a id="getWorkgroupMemberInfo"></a>
# **getWorkgroupMemberInfo**
> UserDetailsExpandVO getWorkgroupMemberInfo(workgroupId, userId)

Workgroup Member Info

Workgroup Member Info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupMembersApi apiInstance = new WorkgroupMembersApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      UserDetailsExpandVO result = apiInstance.getWorkgroupMemberInfo(workgroupId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupMembersApi#getWorkgroupMemberInfo");
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
| **userId** | **String**|  | |

### Return type

[**UserDetailsExpandVO**](UserDetailsExpandVO.md)

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

<a id="getWorkgroupMemberList"></a>
# **getWorkgroupMemberList**
> WorkgroupMembersListVO getWorkgroupMemberList(workgroupId)

List the workgroup members

List the workgroup members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupMembersApi apiInstance = new WorkgroupMembersApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      WorkgroupMembersListVO result = apiInstance.getWorkgroupMemberList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupMembersApi#getWorkgroupMemberList");
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

[**WorkgroupMembersListVO**](WorkgroupMembersListVO.md)

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

