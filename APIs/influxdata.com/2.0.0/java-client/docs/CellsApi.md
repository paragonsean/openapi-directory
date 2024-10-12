# CellsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDashboardsIDCellsID**](CellsApi.md#deleteDashboardsIDCellsID) | **DELETE** /dashboards/{dashboardID}/cells/{cellID} | Delete a dashboard cell |
| [**getDashboardsIDCellsIDView**](CellsApi.md#getDashboardsIDCellsIDView) | **GET** /dashboards/{dashboardID}/cells/{cellID}/view | Retrieve the view for a cell |
| [**patchDashboardsIDCellsID**](CellsApi.md#patchDashboardsIDCellsID) | **PATCH** /dashboards/{dashboardID}/cells/{cellID} | Update the non-positional information related to a cell |
| [**patchDashboardsIDCellsIDView**](CellsApi.md#patchDashboardsIDCellsIDView) | **PATCH** /dashboards/{dashboardID}/cells/{cellID}/view | Update the view for a cell |
| [**postDashboardsIDCells**](CellsApi.md#postDashboardsIDCells) | **POST** /dashboards/{dashboardID}/cells | Create a dashboard cell |
| [**putDashboardsIDCells**](CellsApi.md#putDashboardsIDCells) | **PUT** /dashboards/{dashboardID}/cells | Replace cells in a dashboard |


<a id="deleteDashboardsIDCellsID"></a>
# **deleteDashboardsIDCellsID**
> deleteDashboardsIDCellsID(dashboardID, cellID, zapTraceSpan)

Delete a dashboard cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CellsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CellsApi apiInstance = new CellsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to delete.
    String cellID = "cellID_example"; // String | The ID of the cell to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDashboardsIDCellsID(dashboardID, cellID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling CellsApi#deleteDashboardsIDCellsID");
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
| **dashboardID** | **String**| The ID of the dashboard to delete. | |
| **cellID** | **String**| The ID of the cell to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Cell successfully deleted |  -  |
| **404** | Cell or dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getDashboardsIDCellsIDView"></a>
# **getDashboardsIDCellsIDView**
> View getDashboardsIDCellsIDView(dashboardID, cellID, zapTraceSpan)

Retrieve the view for a cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CellsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CellsApi apiInstance = new CellsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String cellID = "cellID_example"; // String | The cell ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      View result = apiInstance.getDashboardsIDCellsIDView(dashboardID, cellID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CellsApi#getDashboardsIDCellsIDView");
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

<a id="patchDashboardsIDCellsID"></a>
# **patchDashboardsIDCellsID**
> Cell patchDashboardsIDCellsID(dashboardID, cellID, cellUpdate, zapTraceSpan)

Update the non-positional information related to a cell

Updates the non positional information related to a cell. Updates to a single cell&#39;s positional data could cause grid conflicts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CellsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CellsApi apiInstance = new CellsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String cellID = "cellID_example"; // String | The ID of the cell to update.
    CellUpdate cellUpdate = new CellUpdate(); // CellUpdate | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Cell result = apiInstance.patchDashboardsIDCellsID(dashboardID, cellID, cellUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CellsApi#patchDashboardsIDCellsID");
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
| **cellUpdate** | [**CellUpdate**](CellUpdate.md)|  | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Cell**](Cell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated dashboard cell |  -  |
| **404** | Cell or dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="patchDashboardsIDCellsIDView"></a>
# **patchDashboardsIDCellsIDView**
> View patchDashboardsIDCellsIDView(dashboardID, cellID, view, zapTraceSpan)

Update the view for a cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CellsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CellsApi apiInstance = new CellsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String cellID = "cellID_example"; // String | The ID of the cell to update.
    View view = new View(); // View | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      View result = apiInstance.patchDashboardsIDCellsIDView(dashboardID, cellID, view, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CellsApi#patchDashboardsIDCellsIDView");
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

<a id="postDashboardsIDCells"></a>
# **postDashboardsIDCells**
> Cell postDashboardsIDCells(dashboardID, createCell, zapTraceSpan)

Create a dashboard cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CellsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CellsApi apiInstance = new CellsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    CreateCell createCell = new CreateCell(); // CreateCell | Cell that will be added
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Cell result = apiInstance.postDashboardsIDCells(dashboardID, createCell, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CellsApi#postDashboardsIDCells");
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
| **createCell** | [**CreateCell**](CreateCell.md)| Cell that will be added | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Cell**](Cell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cell successfully added |  -  |
| **404** | Dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="putDashboardsIDCells"></a>
# **putDashboardsIDCells**
> Dashboard putDashboardsIDCells(dashboardID, cell, zapTraceSpan)

Replace cells in a dashboard

Replaces all cells in a dashboard. This is used primarily to update the positional information of all cells.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CellsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    CellsApi apiInstance = new CellsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    List<Cell> cell = Arrays.asList(); // List<Cell> | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Dashboard result = apiInstance.putDashboardsIDCells(dashboardID, cell, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CellsApi#putDashboardsIDCells");
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
| **cell** | [**List&lt;Cell&gt;**](Cell.md)|  | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Replaced dashboard cells |  -  |
| **404** | Dashboard not found |  -  |
| **0** | Unexpected error |  -  |

