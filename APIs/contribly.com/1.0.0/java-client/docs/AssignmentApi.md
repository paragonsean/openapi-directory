# AssignmentApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignmentsGet**](AssignmentApi.md#assignmentsGet) | **GET** /assignments | List assignments |
| [**assignmentsIdDelete**](AssignmentApi.md#assignmentsIdDelete) | **DELETE** /assignments/{id} | Delete this assignment and all of it&#39;s contributions |
| [**assignmentsIdGet**](AssignmentApi.md#assignmentsIdGet) | **GET** /assignments/{id} | Get a single assigment by id |
| [**assignmentsPost**](AssignmentApi.md#assignmentsPost) | **POST** /assignments | Create a new assignment |


<a id="assignmentsGet"></a>
# **assignmentsGet**
> List&lt;Assignment&gt; assignmentsGet(ownedBy, page, pageSize, q, urlWords, open, alwaysOpen, tag, name)

List assignments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String ownedBy = "ownedBy_example"; // String | Restrict results to assignments owned by this user.
    Integer page = 56; // Integer | Pagination page
    Integer pageSize = 56; // Integer | Pagination page size
    String q = "q_example"; // String | Restrict results to assignments whose name or description matches this keyword.
    String urlWords = "urlWords_example"; // String | Select an assignment by urlWords.
    Boolean open = true; // Boolean | Select open or closed assignments
    Boolean alwaysOpen = true; // Boolean | Select assignments with no closing date.
    String tag = "tag_example"; // String | Restrict results to assignments which are tagged with this tag.
    String name = "name_example"; // String | Restrict results to the assignment (or potentially assignments) with this exact name
    try {
      List<Assignment> result = apiInstance.assignmentsGet(ownedBy, page, pageSize, q, urlWords, open, alwaysOpen, tag, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsGet");
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
| **ownedBy** | **String**| Restrict results to assignments owned by this user. | [optional] |
| **page** | **Integer**| Pagination page | [optional] |
| **pageSize** | **Integer**| Pagination page size | [optional] |
| **q** | **String**| Restrict results to assignments whose name or description matches this keyword. | [optional] |
| **urlWords** | **String**| Select an assignment by urlWords. | [optional] |
| **open** | **Boolean**| Select open or closed assignments | [optional] |
| **alwaysOpen** | **Boolean**| Select assignments with no closing date. | [optional] |
| **tag** | **String**| Restrict results to assignments which are tagged with this tag. | [optional] |
| **name** | **String**| Restrict results to the assignment (or potentially assignments) with this exact name | [optional] |

### Return type

[**List&lt;Assignment&gt;**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of assignments |  * X-total-count - Total number of matching users <br>  |

<a id="assignmentsIdDelete"></a>
# **assignmentsIdDelete**
> assignmentsIdDelete(id)

Delete this assignment and all of it&#39;s contributions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String id = "id_example"; // String | Id of the assignment to return
    try {
      apiInstance.assignmentsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsIdDelete");
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
| **id** | **String**| Id of the assignment to return | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Assignment deleted |  -  |
| **403** | Not permitted to delete this assignment. |  -  |
| **404** | Not found |  -  |

<a id="assignmentsIdGet"></a>
# **assignmentsIdGet**
> Assignment assignmentsIdGet(id)

Get a single assigment by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String id = "id_example"; // String | Id of the assignment to return
    try {
      Assignment result = apiInstance.assignmentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsIdGet");
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
| **id** | **String**| Id of the assignment to return | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Assignment found |  -  |
| **404** | Not found |  -  |

<a id="assignmentsPost"></a>
# **assignmentsPost**
> Assignment assignmentsPost(assignmentSubmission)

Create a new assignment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    AssignmentSubmission assignmentSubmission = new AssignmentSubmission(); // AssignmentSubmission | Assignment object to be created
    try {
      Assignment result = apiInstance.assignmentsPost(assignmentSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsPost");
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
| **assignmentSubmission** | [**AssignmentSubmission**](AssignmentSubmission.md)| Assignment object to be created | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Assignment created |  -  |
| **400** | The new assignment vailed to validate. Check the response body for details. |  -  |
| **500** | Failed to create the new assignment due to an unexpected error. |  -  |

