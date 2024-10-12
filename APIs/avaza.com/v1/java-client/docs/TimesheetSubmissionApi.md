# TimesheetSubmissionApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timesheetSubmissionPost**](TimesheetSubmissionApi.md#timesheetSubmissionPost) | **POST** /api/TimesheetSubmission | Submit Timesheets for Approval. |


<a id="timesheetSubmissionPost"></a>
# **timesheetSubmissionPost**
> Object timesheetSubmissionPost(sendNotifications, wholeWeekOf, wholeDayOf, userID)

Submit Timesheets for Approval.

Either provide a a specific Day (WholeDayOf) or any day in a Week (WholeWeekOf) to submit all draft timesheets in that day or week

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetSubmissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetSubmissionApi apiInstance = new TimesheetSubmissionApi(defaultClient);
    Boolean sendNotifications = true; // Boolean | Send email alerts to timesheet approvers. Defaults to true
    OffsetDateTime wholeWeekOf = OffsetDateTime.now(); // OffsetDateTime | A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range.
    OffsetDateTime wholeDayOf = OffsetDateTime.now(); // OffsetDateTime | A date (yyyy-MM-dd) to submit all timesheets on this day
    Integer userID = 56; // Integer | The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users.
    try {
      Object result = apiInstance.timesheetSubmissionPost(sendNotifications, wholeWeekOf, wholeDayOf, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetSubmissionApi#timesheetSubmissionPost");
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
| **sendNotifications** | **Boolean**| Send email alerts to timesheet approvers. Defaults to true | [optional] |
| **wholeWeekOf** | **OffsetDateTime**| A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range. | [optional] |
| **wholeDayOf** | **OffsetDateTime**| A date (yyyy-MM-dd) to submit all timesheets on this day | [optional] |
| **userID** | **Integer**| The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users. | [optional] |

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

