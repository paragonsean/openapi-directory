# TaskApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taskDelete**](TaskApi.md#taskDelete) | **DELETE** /api/Task | Delete a Task |
| [**taskGet**](TaskApi.md#taskGet) | **GET** /api/Task | Gets list of Tasks |
| [**taskGetByID**](TaskApi.md#taskGetByID) | **GET** /api/Task/{id} | Gets Task by Task ID |
| [**taskLookup**](TaskApi.md#taskLookup) | **GET** /api/Task/Lookup | Gets minimal list of Tasks for the current user |
| [**taskPost**](TaskApi.md#taskPost) | **POST** /api/Task | Create a Task |
| [**taskPut**](TaskApi.md#taskPut) | **PUT** /api/Task | Update a Task. |


<a id="taskDelete"></a>
# **taskDelete**
> Object taskDelete(taskID)

Delete a Task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TaskApi apiInstance = new TaskApi(defaultClient);
    Long taskID = 56L; // Long | 
    try {
      Object result = apiInstance.taskDelete(taskID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskDelete");
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
| **taskID** | **Long**|  | |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taskGet"></a>
# **taskGet**
> TaskList taskGet(updatedAfter, pageSize, pageNumber, sort, isComplete, projectID)

Gets list of Tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TaskApi apiInstance = new TaskApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Optional filter to records updated after a specific date.
    Integer pageSize = 56; // Integer | Number of items per page. Defaults to 20.
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1. Defaults to 1
    String sort = "sort_example"; // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\", \"SectionTitle\", \"Title\"
    Boolean isComplete = true; // Boolean | Optional filter to only display tasks linked to a Task Status where isComplete=false, or where isComplete=true
    Integer projectID = 56; // Integer | Optional filter to only display tasks belonging to a specific ProjectID
    try {
      TaskList result = apiInstance.taskGet(updatedAfter, pageSize, pageNumber, sort, isComplete, projectID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskGet");
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
| **updatedAfter** | **OffsetDateTime**| Optional filter to records updated after a specific date. | [optional] |
| **pageSize** | **Integer**| Number of items per page. Defaults to 20. | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. Defaults to 1 | [optional] |
| **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;, \&quot;SectionTitle\&quot;, \&quot;Title\&quot; | [optional] |
| **isComplete** | **Boolean**| Optional filter to only display tasks linked to a Task Status where isComplete&#x3D;false, or where isComplete&#x3D;true | [optional] |
| **projectID** | **Integer**| Optional filter to only display tasks belonging to a specific ProjectID | [optional] |

### Return type

[**TaskList**](TaskList.md)

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

<a id="taskGetByID"></a>
# **taskGetByID**
> TaskDetails taskGetByID(id)

Gets Task by Task ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TaskApi apiInstance = new TaskApi(defaultClient);
    Long id = 56L; // Long | Task ID number
    try {
      TaskDetails result = apiInstance.taskGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskGetByID");
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
| **id** | **Long**| Task ID number | |

### Return type

[**TaskDetails**](TaskDetails.md)

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

<a id="taskLookup"></a>
# **taskLookup**
> TaskDropdownList taskLookup(projectID, pageSize, pageNumber, hideCompleted, search)

Gets minimal list of Tasks for the current user

Groups Tasks by Section. Default sort is by Section Title followed by Task Title

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TaskApi apiInstance = new TaskApi(defaultClient);
    Integer projectID = 56; // Integer | (required) The ProjectID to use when filtering Tasks
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    Boolean hideCompleted = true; // Boolean | (optional) true/false to hide completed tasks. Defaults false
    String search = "search_example"; // String | (optional) Search string to match against Task title. Performs begins-with match
    try {
      TaskDropdownList result = apiInstance.taskLookup(projectID, pageSize, pageNumber, hideCompleted, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskLookup");
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
| **projectID** | **Integer**| (required) The ProjectID to use when filtering Tasks | |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **hideCompleted** | **Boolean**| (optional) true/false to hide completed tasks. Defaults false | [optional] |
| **search** | **String**| (optional) Search string to match against Task title. Performs begins-with match | [optional] |

### Return type

[**TaskDropdownList**](TaskDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taskPost"></a>
# **taskPost**
> TaskDetails taskPost(model)

Create a Task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TaskApi apiInstance = new TaskApi(defaultClient);
    NewTask model = new NewTask(); // NewTask | 
    try {
      TaskDetails result = apiInstance.taskPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskPost");
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
| **model** | [**NewTask**](NewTask.md)|  | |

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taskPut"></a>
# **taskPut**
> TaskDetails taskPut(model)

Update a Task.

Requires TaskID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TaskApi apiInstance = new TaskApi(defaultClient);
    UpdateTask model = new UpdateTask(); // UpdateTask | 
    try {
      TaskDetails result = apiInstance.taskPut(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskPut");
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
| **model** | [**UpdateTask**](UpdateTask.md)|  | |

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

