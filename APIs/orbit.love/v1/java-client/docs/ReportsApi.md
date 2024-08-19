# ReportsApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugReportsGet**](ReportsApi.md#workspaceSlugReportsGet) | **GET** /{workspace_slug}/reports | Get a workspace stats |


<a id="workspaceSlugReportsGet"></a>
# **workspaceSlugReportsGet**
> workspaceSlugReportsGet(workspaceSlug, startDate, endDate, relative, properties, activityType, type)

Get a workspace stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String startDate = "startDate_example"; // String | Filter activities after this date. Format: YYYY-MM-DD.
    String endDate = "endDate_example"; // String | Filter activities before this date. Format: YYYY-MM-DD.
    String relative = "relative_example"; // String | Relative timeframes. Format: this_<integer>_<period>, with period in [days, weeks, months, years]. For example, this_30_days.
    String properties = "properties_example"; // String | 
    String activityType = "activityType_example"; // String | 
    String type = "type_example"; // String | Deprecated in favor of the activity_type parameter.
    try {
      apiInstance.workspaceSlugReportsGet(workspaceSlug, startDate, endDate, relative, properties, activityType, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#workspaceSlugReportsGet");
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
| **workspaceSlug** | **String**|  | |
| **startDate** | **String**| Filter activities after this date. Format: YYYY-MM-DD. | [optional] |
| **endDate** | **String**| Filter activities before this date. Format: YYYY-MM-DD. | [optional] |
| **relative** | **String**| Relative timeframes. Format: this_&lt;integer&gt;_&lt;period&gt;, with period in [days, weeks, months, years]. For example, this_30_days. | [optional] |
| **properties** | **String**|  | [optional] |
| **activityType** | **String**|  | [optional] |
| **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

