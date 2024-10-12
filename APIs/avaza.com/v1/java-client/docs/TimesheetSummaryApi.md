# TimesheetSummaryApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timesheetSummaryGet**](TimesheetSummaryApi.md#timesheetSummaryGet) | **GET** /api/TimesheetSummary | Gets Basic Summary of Timesheet Statistics |


<a id="timesheetSummaryGet"></a>
# **timesheetSummaryGet**
> TimesheetSummaryResult timesheetSummaryGet(modelGroupBy, modelEntryDateFrom, modelEntryDateTo, modelUserID, modelProjectID, modelIsBillable, modelIsInvoiced)

Gets Basic Summary of Timesheet Statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetSummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetSummaryApi apiInstance = new TimesheetSummaryApi(defaultClient);
    List<String> modelGroupBy = Arrays.asList(); // List<String> | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Customer\", \"Project\", \"Category\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".
    OffsetDateTime modelEntryDateFrom = OffsetDateTime.now(); // OffsetDateTime | (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
    OffsetDateTime modelEntryDateTo = OffsetDateTime.now(); // OffsetDateTime | (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
    List<Integer> modelUserID = Arrays.asList(); // List<Integer> | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.
    Integer modelProjectID = 56; // Integer | (Optional) Filter by Project
    Boolean modelIsBillable = true; // Boolean | (Optional) Filter by the billable status of Timesheets.
    Boolean modelIsInvoiced = true; // Boolean | (Optional) Filter for timesheets by whether they have been Invoiced or not.
    try {
      TimesheetSummaryResult result = apiInstance.timesheetSummaryGet(modelGroupBy, modelEntryDateFrom, modelEntryDateTo, modelUserID, modelProjectID, modelIsBillable, modelIsInvoiced);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetSummaryApi#timesheetSummaryGet");
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
| **modelGroupBy** | [**List&lt;String&gt;**](String.md)| (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;Category\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. | [optional] |
| **modelEntryDateFrom** | **OffsetDateTime**| (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00 | [optional] |
| **modelEntryDateTo** | **OffsetDateTime**| (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00 | [optional] |
| **modelUserID** | [**List&lt;Integer&gt;**](Integer.md)| (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. | [optional] |
| **modelProjectID** | **Integer**| (Optional) Filter by Project | [optional] |
| **modelIsBillable** | **Boolean**| (Optional) Filter by the billable status of Timesheets. | [optional] |
| **modelIsInvoiced** | **Boolean**| (Optional) Filter for timesheets by whether they have been Invoiced or not. | [optional] |

### Return type

[**TimesheetSummaryResult**](TimesheetSummaryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

