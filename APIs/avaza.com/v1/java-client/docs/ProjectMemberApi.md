# ProjectMemberApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectMemberGet**](ProjectMemberApi.md#projectMemberGet) | **GET** /api/ProjectMember | Gets list of Project Members |
| [**projectMemberPost**](ProjectMemberApi.md#projectMemberPost) | **POST** /api/ProjectMember | Assign a user as a Member of a Project |
| [**projectMemberPut**](ProjectMemberApi.md#projectMemberPut) | **PUT** /api/ProjectMember | Update a Member of a Project |


<a id="projectMemberGet"></a>
# **projectMemberGet**
> ProjectMemberList projectMemberGet(projectID, userID)

Gets list of Project Members

Include at least one of ProjectID or UserID parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectMemberApi apiInstance = new ProjectMemberApi(defaultClient);
    Integer projectID = 56; // Integer | Get Project members filtered by ProjectID
    Integer userID = 56; // Integer | Get Project members filtered by UserID
    try {
      ProjectMemberList result = apiInstance.projectMemberGet(projectID, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectMemberApi#projectMemberGet");
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
| **projectID** | **Integer**| Get Project members filtered by ProjectID | [optional] |
| **userID** | **Integer**| Get Project members filtered by UserID | [optional] |

### Return type

[**ProjectMemberList**](ProjectMemberList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="projectMemberPost"></a>
# **projectMemberPost**
> ProjectMemberDetails projectMemberPost(model)

Assign a user as a Member of a Project

the Amount columns for Cost, Budget, Rates should be specified as a decimal. Financial amounts assume the currency of the Customer company. Budget units depend on the Budget method set on the Project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectMemberApi apiInstance = new ProjectMemberApi(defaultClient);
    NewProjectMember model = new NewProjectMember(); // NewProjectMember | 
    try {
      ProjectMemberDetails result = apiInstance.projectMemberPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectMemberApi#projectMemberPost");
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
| **model** | [**NewProjectMember**](NewProjectMember.md)|  | |

### Return type

[**ProjectMemberDetails**](ProjectMemberDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="projectMemberPut"></a>
# **projectMemberPut**
> ProjectMemberDetails projectMemberPut(model)

Update a Member of a Project

Fields are only updated if their field name is in the FieldsToUpdate string collection. The Amount columns for Cost, Budget, Rates if specified should be a decimal. Financial amounts assume the currency of the parent Company. Budget units depend on the Budget method set on the Project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectMemberApi apiInstance = new ProjectMemberApi(defaultClient);
    UpdateProjectMember model = new UpdateProjectMember(); // UpdateProjectMember | 
    try {
      ProjectMemberDetails result = apiInstance.projectMemberPut(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectMemberApi#projectMemberPut");
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
| **model** | [**UpdateProjectMember**](UpdateProjectMember.md)|  | |

### Return type

[**ProjectMemberDetails**](ProjectMemberDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

