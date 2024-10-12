# ProjectTimesheetCategoryApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectTimesheetCategoryGet**](ProjectTimesheetCategoryApi.md#projectTimesheetCategoryGet) | **GET** /api/ProjectTimesheetCategory | Gets list of Project Timesheet Categories |
| [**projectTimesheetCategoryPost**](ProjectTimesheetCategoryApi.md#projectTimesheetCategoryPost) | **POST** /api/ProjectTimesheetCategory | Assign a TimeSheetCategory to a Project. |


<a id="projectTimesheetCategoryGet"></a>
# **projectTimesheetCategoryGet**
> ProjectTimesheetCategoryList projectTimesheetCategoryGet(projectID)

Gets list of Project Timesheet Categories

The default sort order is by isBillable desc, Name asc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectTimesheetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectTimesheetCategoryApi apiInstance = new ProjectTimesheetCategoryApi(defaultClient);
    Integer projectID = 56; // Integer | Get categories filtered by ProjectID
    try {
      ProjectTimesheetCategoryList result = apiInstance.projectTimesheetCategoryGet(projectID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectTimesheetCategoryApi#projectTimesheetCategoryGet");
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
| **projectID** | **Integer**| Get categories filtered by ProjectID | [optional] |

### Return type

[**ProjectTimesheetCategoryList**](ProjectTimesheetCategoryList.md)

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

<a id="projectTimesheetCategoryPost"></a>
# **projectTimesheetCategoryPost**
> ProjectTimesheetCategoryDetails projectTimesheetCategoryPost(model)

Assign a TimeSheetCategory to a Project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectTimesheetCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectTimesheetCategoryApi apiInstance = new ProjectTimesheetCategoryApi(defaultClient);
    AssignProjectTimesheetCategory model = new AssignProjectTimesheetCategory(); // AssignProjectTimesheetCategory | 
    try {
      ProjectTimesheetCategoryDetails result = apiInstance.projectTimesheetCategoryPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectTimesheetCategoryApi#projectTimesheetCategoryPost");
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
| **model** | [**AssignProjectTimesheetCategory**](AssignProjectTimesheetCategory.md)|  | |

### Return type

[**ProjectTimesheetCategoryDetails**](ProjectTimesheetCategoryDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

