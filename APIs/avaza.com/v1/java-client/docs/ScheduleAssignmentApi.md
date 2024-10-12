# ScheduleAssignmentApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scheduleAssignmentGet**](ScheduleAssignmentApi.md#scheduleAssignmentGet) | **GET** /api/ScheduleAssignment | Gets list of Schedule Assignments. |


<a id="scheduleAssignmentGet"></a>
# **scheduleAssignmentGet**
> ScheduleAssignmentList scheduleAssignmentGet(updatedAfter, scheduleDateFrom, scheduleDateTo, scheduleSeriesID, userID, userEmail, pageSize, pageNumber, sort)

Gets list of Schedule Assignments.

Schedule assignments are per-day, and link to a parent Schedule Series.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScheduleAssignmentApi apiInstance = new ScheduleAssignmentApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to records updated after the specified date
    OffsetDateTime scheduleDateFrom = OffsetDateTime.now(); // OffsetDateTime | Filter for schedule assignement  that are  on or after a specific date
    OffsetDateTime scheduleDateTo = OffsetDateTime.now(); // OffsetDateTime | Filter for schedules that are on or before a specific date
    Long scheduleSeriesID = 56L; // Long | Filter to records for a particular Schedule Series
    Integer userID = 56; // Integer | The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries.
    String userEmail = "userEmail_example"; // String | The email of the user who has been scheduled
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\"
    try {
      ScheduleAssignmentList result = apiInstance.scheduleAssignmentGet(updatedAfter, scheduleDateFrom, scheduleDateTo, scheduleSeriesID, userID, userEmail, pageSize, pageNumber, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleAssignmentApi#scheduleAssignmentGet");
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
| **updatedAfter** | **OffsetDateTime**| Limit results to records updated after the specified date | [optional] |
| **scheduleDateFrom** | **OffsetDateTime**| Filter for schedule assignement  that are  on or after a specific date | [optional] |
| **scheduleDateTo** | **OffsetDateTime**| Filter for schedules that are on or before a specific date | [optional] |
| **scheduleSeriesID** | **Long**| Filter to records for a particular Schedule Series | [optional] |
| **userID** | **Integer**| The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. | [optional] |
| **userEmail** | **String**| The email of the user who has been scheduled | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] |

### Return type

[**ScheduleAssignmentList**](ScheduleAssignmentList.md)

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

