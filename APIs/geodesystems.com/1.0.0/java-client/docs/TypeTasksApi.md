# TypeTasksApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchTasks**](TypeTasksApi.md#searchTasks) | **GET** /repository/search/type/tasks | Search API for &#39;Tasks&#39; entry type |


<a id="searchTasks"></a>
# **searchTasks**
> searchTasks(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbTasksTitle, searchDbTasksPriority, searchDbTasksStatus, searchDbTasksComplete, searchDbTasksAssignedto, searchDbTasksStartdate, searchDbTasksEnddate)

Search API for &#39;Tasks&#39; entry type

API to search for entries of type Tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeTasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeTasksApi apiInstance = new TypeTasksApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchDbTasksTitle = "searchDbTasksTitle_example"; // String | Title
    String searchDbTasksPriority = "searchDbTasksPriority_example"; // String | Priority
    String searchDbTasksStatus = "searchDbTasksStatus_example"; // String | Status
    Double searchDbTasksComplete = 3.4D; // Double | % Complete
    String searchDbTasksAssignedto = "searchDbTasksAssignedto_example"; // String | Assigned To
    String searchDbTasksStartdate = "searchDbTasksStartdate_example"; // String | Start Date
    String searchDbTasksEnddate = "searchDbTasksEnddate_example"; // String | End Date
    try {
      apiInstance.searchTasks(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbTasksTitle, searchDbTasksPriority, searchDbTasksStatus, searchDbTasksComplete, searchDbTasksAssignedto, searchDbTasksStartdate, searchDbTasksEnddate);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeTasksApi#searchTasks");
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
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchDbTasksTitle** | **String**| Title | [optional] |
| **searchDbTasksPriority** | **String**| Priority | [optional] |
| **searchDbTasksStatus** | **String**| Status | [optional] |
| **searchDbTasksComplete** | **Double**| % Complete | [optional] |
| **searchDbTasksAssignedto** | **String**| Assigned To | [optional] |
| **searchDbTasksStartdate** | **String**| Start Date | [optional] |
| **searchDbTasksEnddate** | **String**| End Date | [optional] |

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
| **200** | No response was specified |  -  |

