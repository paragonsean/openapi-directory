# TeamMemberApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteTeamMemberOfProject**](TeamMemberApi.md#deleteTeamMemberOfProject) | **DELETE** /v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers/{teammember_id} | Delete a team member for the specific project. |
| [**getTeamMemberListOfClientProject**](TeamMemberApi.md#getTeamMemberListOfClientProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/teamMembersOfClientProject | List team member of client project side. |
| [**getTeamMemberListOfProject**](TeamMemberApi.md#getTeamMemberListOfProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers | List team member of project. |
| [**postTeamMemberOfProject**](TeamMemberApi.md#postTeamMemberOfProject) | **POST** /1.1/workgroups/{workgroup_id}/projects/{project_id}/teammembers | Invite a team member or all the members of team template for the specific project. |
| [**v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost**](TeamMemberApi.md#v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers | Deprecated, please use 1.1 Version |


<a id="deleteTeamMemberOfProject"></a>
# **deleteTeamMemberOfProject**
> TeamMemberBaseInfVO deleteTeamMemberOfProject(workgroupId, projectId, teammemberId)

Delete a team member for the specific project.

Delete a team member for the specific project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String teammemberId = "teammemberId_example"; // String | 
    try {
      TeamMemberBaseInfVO result = apiInstance.deleteTeamMemberOfProject(workgroupId, projectId, teammemberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#deleteTeamMemberOfProject");
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
| **teammemberId** | **String**|  | |

### Return type

[**TeamMemberBaseInfVO**](TeamMemberBaseInfVO.md)

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

<a id="getTeamMemberListOfClientProject"></a>
# **getTeamMemberListOfClientProject**
> TeamMemberListVO getTeamMemberListOfClientProject(workgroupId, projectId)

List team member of client project side.

List team member of client project side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      TeamMemberListVO result = apiInstance.getTeamMemberListOfClientProject(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#getTeamMemberListOfClientProject");
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

### Return type

[**TeamMemberListVO**](TeamMemberListVO.md)

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

<a id="getTeamMemberListOfProject"></a>
# **getTeamMemberListOfProject**
> TeamMemberListVO getTeamMemberListOfProject(workgroupId, projectId)

List team member of project.

List team member of project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      TeamMemberListVO result = apiInstance.getTeamMemberListOfProject(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#getTeamMemberListOfProject");
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

### Return type

[**TeamMemberListVO**](TeamMemberListVO.md)

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

<a id="postTeamMemberOfProject"></a>
# **postTeamMemberOfProject**
> V1x1InvitedTeamMemberResultsVO postTeamMemberOfProject(workgroupId, projectId, teamMemberPO)

Invite a team member or all the members of team template for the specific project.

Invite a team member or all the members of team template for the specific project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    TeamMemberPO teamMemberPO = new TeamMemberPO(); // TeamMemberPO | 
    try {
      V1x1InvitedTeamMemberResultsVO result = apiInstance.postTeamMemberOfProject(workgroupId, projectId, teamMemberPO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#postTeamMemberOfProject");
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
| **teamMemberPO** | [**TeamMemberPO**](TeamMemberPO.md)|  | [optional] |

### Return type

[**V1x1InvitedTeamMemberResultsVO**](V1x1InvitedTeamMemberResultsVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost"></a>
# **v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost**
> TeamMemberBaseInfVO v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost(workgroupId, projectId, contactUserVO)

Deprecated, please use 1.1 Version

Deprecated, please use 1.1 Version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    ContactUserVO contactUserVO = new ContactUserVO(); // ContactUserVO | 
    try {
      TeamMemberBaseInfVO result = apiInstance.v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost(workgroupId, projectId, contactUserVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost");
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
| **contactUserVO** | [**ContactUserVO**](ContactUserVO.md)|  | [optional] |

### Return type

[**TeamMemberBaseInfVO**](TeamMemberBaseInfVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

