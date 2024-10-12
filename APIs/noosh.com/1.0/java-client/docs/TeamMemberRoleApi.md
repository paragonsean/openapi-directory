# TeamMemberRoleApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMemberRoles**](TeamMemberRoleApi.md#getMemberRoles) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/memberroles/{user_id} | List all the role options for the user |


<a id="getMemberRoles"></a>
# **getMemberRoles**
> RoleListVO getMemberRoles(workgroupId, projectId, userId)

List all the role options for the user

List all the role options for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberRoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TeamMemberRoleApi apiInstance = new TeamMemberRoleApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      RoleListVO result = apiInstance.getMemberRoles(workgroupId, projectId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberRoleApi#getMemberRoles");
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
| **projectId** | **String**|  | |
| **userId** | **String**|  | |

### Return type

[**RoleListVO**](RoleListVO.md)

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

