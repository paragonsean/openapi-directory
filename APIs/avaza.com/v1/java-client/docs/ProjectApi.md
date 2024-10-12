# ProjectApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectGet**](ProjectApi.md#projectGet) | **GET** /api/Project | Gets list of Projects |
| [**projectGetByID**](ProjectApi.md#projectGetByID) | **GET** /api/Project/{id} | Gets Project by Project ID |
| [**projectLookup**](ProjectApi.md#projectLookup) | **GET** /api/Project/Lookup | Gets minimal list of active Projects for the current user |
| [**projectPost**](ProjectApi.md#projectPost) | **POST** /api/Project | Create a Project |
| [**projectPut**](ProjectApi.md#projectPut) | **PUT** /api/Project | Update an Project |


<a id="projectGet"></a>
# **projectGet**
> ProjectList projectGet(updatedAfter, pageSize, pageNumber, sort, timesheetUserID, includeArchived)

Gets list of Projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Only show project records updated after a certain date (UTC)
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | A column to sort on. Current possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\"
    Integer timesheetUserID = 56; // Integer | Filter to the projects that the supplied UserID can add timesheets to
    Boolean includeArchived = true; // Boolean | Include Archived Projects in the results
    try {
      ProjectList result = apiInstance.projectGet(updatedAfter, pageSize, pageNumber, sort, timesheetUserID, includeArchived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#projectGet");
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
| **updatedAfter** | **OffsetDateTime**| Only show project records updated after a certain date (UTC) | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **sort** | **String**| A column to sort on. Current possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] |
| **timesheetUserID** | **Integer**| Filter to the projects that the supplied UserID can add timesheets to | [optional] |
| **includeArchived** | **Boolean**| Include Archived Projects in the results | [optional] |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="projectGetByID"></a>
# **projectGetByID**
> ProjectDetails projectGetByID(id)

Gets Project by Project ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    Long id = 56L; // Long | Project ID number
    try {
      ProjectDetails result = apiInstance.projectGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#projectGetByID");
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
| **id** | **Long**| Project ID number | |

### Return type

[**ProjectDetails**](ProjectDetails.md)

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
| **404** | Not Found |  -  |

<a id="projectLookup"></a>
# **projectLookup**
> ProjectDropdownList projectLookup(pageSize, pageNumber, timesheetUserID, companyIDFK, search)

Gets minimal list of active Projects for the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    Integer timesheetUserID = 56; // Integer | Optionally Filter to the projects that the supplied UserID can add timesheets to
    Integer companyIDFK = 56; // Integer | Optionally Filter for a specific Company ID
    String search = "search_example"; // String | Search string to match against Project title and Customer name
    try {
      ProjectDropdownList result = apiInstance.projectLookup(pageSize, pageNumber, timesheetUserID, companyIDFK, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#projectLookup");
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
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **timesheetUserID** | **Integer**| Optionally Filter to the projects that the supplied UserID can add timesheets to | [optional] |
| **companyIDFK** | **Integer**| Optionally Filter for a specific Company ID | [optional] |
| **search** | **String**| Search string to match against Project title and Customer name | [optional] |

### Return type

[**ProjectDropdownList**](ProjectDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="projectPost"></a>
# **projectPost**
> ProjectDetails projectPost(model)

Create a Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    NewProjectModel model = new NewProjectModel(); // NewProjectModel | 
    try {
      ProjectDetails result = apiInstance.projectPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#projectPost");
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
| **model** | [**NewProjectModel**](NewProjectModel.md)|  | |

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="projectPut"></a>
# **projectPut**
> ProjectDetails projectPut(model)

Update an Project

Update a Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    UpdateProjectModel model = new UpdateProjectModel(); // UpdateProjectModel | 
    try {
      ProjectDetails result = apiInstance.projectPut(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#projectPut");
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
| **model** | [**UpdateProjectModel**](UpdateProjectModel.md)|  | |

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

