# ViewsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDashboardsIDCellsIDView_1**](ViewsApi.md#getDashboardsIDCellsIDView_1) | **GET** /dashboards/{dashboardID}/cells/{cellID}/view | Retrieve the view for a cell |
| [**patchDashboardsIDCellsIDView_1**](ViewsApi.md#patchDashboardsIDCellsIDView_1) | **PATCH** /dashboards/{dashboardID}/cells/{cellID}/view | Update the view for a cell |


<a id="getDashboardsIDCellsIDView_1"></a>
# **getDashboardsIDCellsIDView_1**
> View getDashboardsIDCellsIDView_1(dashboardID, cellID, zapTraceSpan)

Retrieve the view for a cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String cellID = "cellID_example"; // String | The cell ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      View result = apiInstance.getDashboardsIDCellsIDView_1(dashboardID, cellID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#getDashboardsIDCellsIDView_1");
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
| **dashboardID** | **String**| The dashboard ID. | |
| **cellID** | **String**| The cell ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A dashboard cells view |  -  |
| **404** | Cell or dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="patchDashboardsIDCellsIDView_1"></a>
# **patchDashboardsIDCellsIDView_1**
> View patchDashboardsIDCellsIDView_1(dashboardID, cellID, view, zapTraceSpan)

Update the view for a cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String cellID = "cellID_example"; // String | The ID of the cell to update.
    View view = new View(); // View | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      View result = apiInstance.patchDashboardsIDCellsIDView_1(dashboardID, cellID, view, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#patchDashboardsIDCellsIDView_1");
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
| **dashboardID** | **String**| The ID of the dashboard to update. | |
| **cellID** | **String**| The ID of the cell to update. | |
| **view** | [**View**](View.md)|  | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated cell view |  -  |
| **404** | Cell or dashboard not found |  -  |
| **0** | Unexpected error |  -  |

