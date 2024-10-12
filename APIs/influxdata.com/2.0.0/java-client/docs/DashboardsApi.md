# DashboardsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDashboardsID**](DashboardsApi.md#deleteDashboardsID) | **DELETE** /dashboards/{dashboardID} | Delete a dashboard |
| [**deleteDashboardsIDCellsID_0**](DashboardsApi.md#deleteDashboardsIDCellsID_0) | **DELETE** /dashboards/{dashboardID}/cells/{cellID} | Delete a dashboard cell |
| [**deleteDashboardsIDLabelsID**](DashboardsApi.md#deleteDashboardsIDLabelsID) | **DELETE** /dashboards/{dashboardID}/labels/{labelID} | Delete a label from a dashboard |
| [**deleteDashboardsIDMembersID**](DashboardsApi.md#deleteDashboardsIDMembersID) | **DELETE** /dashboards/{dashboardID}/members/{userID} | Remove a member from a dashboard |
| [**deleteDashboardsIDOwnersID**](DashboardsApi.md#deleteDashboardsIDOwnersID) | **DELETE** /dashboards/{dashboardID}/owners/{userID} | Remove an owner from a dashboard |
| [**getDashboards**](DashboardsApi.md#getDashboards) | **GET** /dashboards | List all dashboards |
| [**getDashboardsID**](DashboardsApi.md#getDashboardsID) | **GET** /dashboards/{dashboardID} | Retrieve a Dashboard |
| [**getDashboardsIDCellsIDView_0**](DashboardsApi.md#getDashboardsIDCellsIDView_0) | **GET** /dashboards/{dashboardID}/cells/{cellID}/view | Retrieve the view for a cell |
| [**getDashboardsIDLabels**](DashboardsApi.md#getDashboardsIDLabels) | **GET** /dashboards/{dashboardID}/labels | List all labels for a dashboard |
| [**getDashboardsIDMembers**](DashboardsApi.md#getDashboardsIDMembers) | **GET** /dashboards/{dashboardID}/members | List all dashboard members |
| [**getDashboardsIDOwners**](DashboardsApi.md#getDashboardsIDOwners) | **GET** /dashboards/{dashboardID}/owners | List all dashboard owners |
| [**patchDashboardsID**](DashboardsApi.md#patchDashboardsID) | **PATCH** /dashboards/{dashboardID} | Update a dashboard |
| [**patchDashboardsIDCellsIDView_0**](DashboardsApi.md#patchDashboardsIDCellsIDView_0) | **PATCH** /dashboards/{dashboardID}/cells/{cellID}/view | Update the view for a cell |
| [**patchDashboardsIDCellsID_0**](DashboardsApi.md#patchDashboardsIDCellsID_0) | **PATCH** /dashboards/{dashboardID}/cells/{cellID} | Update the non-positional information related to a cell |
| [**postDashboards**](DashboardsApi.md#postDashboards) | **POST** /dashboards | Create a dashboard |
| [**postDashboardsIDCells_0**](DashboardsApi.md#postDashboardsIDCells_0) | **POST** /dashboards/{dashboardID}/cells | Create a dashboard cell |
| [**postDashboardsIDLabels**](DashboardsApi.md#postDashboardsIDLabels) | **POST** /dashboards/{dashboardID}/labels | Add a label to a dashboard |
| [**postDashboardsIDMembers**](DashboardsApi.md#postDashboardsIDMembers) | **POST** /dashboards/{dashboardID}/members | Add a member to a dashboard |
| [**postDashboardsIDOwners**](DashboardsApi.md#postDashboardsIDOwners) | **POST** /dashboards/{dashboardID}/owners | Add an owner to a dashboard |
| [**putDashboardsIDCells_0**](DashboardsApi.md#putDashboardsIDCells_0) | **PUT** /dashboards/{dashboardID}/cells | Replace cells in a dashboard |


<a id="deleteDashboardsID"></a>
# **deleteDashboardsID**
> deleteDashboardsID(dashboardID, zapTraceSpan)

Delete a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDashboardsID(dashboardID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#deleteDashboardsID");
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
| **204** | Delete has been accepted |  -  |
| **404** | Dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteDashboardsIDCellsID_0"></a>
# **deleteDashboardsIDCellsID_0**
> deleteDashboardsIDCellsID_0(dashboardID, cellID, zapTraceSpan)

Delete a dashboard cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to delete.
    String cellID = "cellID_example"; // String | The ID of the cell to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDashboardsIDCellsID_0(dashboardID, cellID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#deleteDashboardsIDCellsID_0");
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

<a id="deleteDashboardsIDLabelsID"></a>
# **deleteDashboardsIDLabelsID**
> deleteDashboardsIDLabelsID(dashboardID, labelID, zapTraceSpan)

Delete a label from a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String labelID = "labelID_example"; // String | The ID of the label to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDashboardsIDLabelsID(dashboardID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#deleteDashboardsIDLabelsID");
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
| **labelID** | **String**| The ID of the label to delete. | |
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
| **204** | Delete has been accepted |  -  |
| **404** | Dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteDashboardsIDMembersID"></a>
# **deleteDashboardsIDMembersID**
> deleteDashboardsIDMembersID(userID, dashboardID, zapTraceSpan)

Remove a member from a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the member to remove.
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDashboardsIDMembersID(userID, dashboardID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#deleteDashboardsIDMembersID");
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
| **userID** | **String**| The ID of the member to remove. | |
| **dashboardID** | **String**| The dashboard ID. | |
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
| **204** | Member removed |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteDashboardsIDOwnersID"></a>
# **deleteDashboardsIDOwnersID**
> deleteDashboardsIDOwnersID(userID, dashboardID, zapTraceSpan)

Remove an owner from a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the owner to remove.
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDashboardsIDOwnersID(userID, dashboardID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#deleteDashboardsIDOwnersID");
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
| **userID** | **String**| The ID of the owner to remove. | |
| **dashboardID** | **String**| The dashboard ID. | |
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
| **204** | Owner removed |  -  |
| **0** | Unexpected error |  -  |

<a id="getDashboards"></a>
# **getDashboards**
> Dashboards getDashboards(zapTraceSpan, offset, limit, descending, owner, sortBy, id, orgID, org)

List all dashboards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Integer offset = 56; // Integer | 
    Integer limit = 20; // Integer | 
    Boolean descending = false; // Boolean | 
    String owner = "owner_example"; // String | A user identifier. Returns only dashboards where this user has the `owner` role.
    String sortBy = "ID"; // String | The column to sort by.
    List<String> id = Arrays.asList(); // List<String> | A list of dashboard identifiers. Returns only the listed dashboards. If both `id` and `owner` are specified, only `id` is used.
    String orgID = "orgID_example"; // String | The identifier of the organization.
    String org = "org_example"; // String | The name of the organization.
    try {
      Dashboards result = apiInstance.getDashboards(zapTraceSpan, offset, limit, descending, owner, sortBy, id, orgID, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#getDashboards");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **descending** | **Boolean**|  | [optional] [default to false] |
| **owner** | **String**| A user identifier. Returns only dashboards where this user has the &#x60;owner&#x60; role. | [optional] |
| **sortBy** | **String**| The column to sort by. | [optional] [enum: ID, CreatedAt, UpdatedAt] |
| **id** | [**List&lt;String&gt;**](String.md)| A list of dashboard identifiers. Returns only the listed dashboards. If both &#x60;id&#x60; and &#x60;owner&#x60; are specified, only &#x60;id&#x60; is used. | [optional] |
| **orgID** | **String**| The identifier of the organization. | [optional] |
| **org** | **String**| The name of the organization. | [optional] |

### Return type

[**Dashboards**](Dashboards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All dashboards |  -  |
| **0** | Unexpected error |  -  |

<a id="getDashboardsID"></a>
# **getDashboardsID**
> PostDashboards201Response getDashboardsID(dashboardID, zapTraceSpan, include)

Retrieve a Dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String include = "properties"; // String | Includes the cell view properties in the response if set to `properties`
    try {
      PostDashboards201Response result = apiInstance.getDashboardsID(dashboardID, zapTraceSpan, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#getDashboardsID");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **include** | **String**| Includes the cell view properties in the response if set to &#x60;properties&#x60; | [optional] [enum: properties] |

### Return type

[**PostDashboards201Response**](PostDashboards201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve a single dashboard |  -  |
| **404** | Dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getDashboardsIDCellsIDView_0"></a>
# **getDashboardsIDCellsIDView_0**
> View getDashboardsIDCellsIDView_0(dashboardID, cellID, zapTraceSpan)

Retrieve the view for a cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String cellID = "cellID_example"; // String | The cell ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      View result = apiInstance.getDashboardsIDCellsIDView_0(dashboardID, cellID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#getDashboardsIDCellsIDView_0");
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

<a id="getDashboardsIDLabels"></a>
# **getDashboardsIDLabels**
> LabelsResponse getDashboardsIDLabels(dashboardID, zapTraceSpan)

List all labels for a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getDashboardsIDLabels(dashboardID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#getDashboardsIDLabels");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all labels for a dashboard |  -  |
| **0** | Unexpected error |  -  |

<a id="getDashboardsIDMembers"></a>
# **getDashboardsIDMembers**
> ResourceMembers getDashboardsIDMembers(dashboardID, zapTraceSpan)

List all dashboard members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMembers result = apiInstance.getDashboardsIDMembers(dashboardID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#getDashboardsIDMembers");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of users who have member privileges for a dashboard |  -  |
| **0** | Unexpected error |  -  |

<a id="getDashboardsIDOwners"></a>
# **getDashboardsIDOwners**
> ResourceOwners getDashboardsIDOwners(dashboardID, zapTraceSpan)

List all dashboard owners

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwners result = apiInstance.getDashboardsIDOwners(dashboardID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#getDashboardsIDOwners");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of users who have owner privileges for a dashboard |  -  |
| **0** | Unexpected error |  -  |

<a id="patchDashboardsID"></a>
# **patchDashboardsID**
> Dashboard patchDashboardsID(dashboardID, patchDashboardRequest, zapTraceSpan)

Update a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    PatchDashboardRequest patchDashboardRequest = new PatchDashboardRequest(); // PatchDashboardRequest | Patching of a dashboard
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Dashboard result = apiInstance.patchDashboardsID(dashboardID, patchDashboardRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#patchDashboardsID");
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
| **patchDashboardRequest** | [**PatchDashboardRequest**](PatchDashboardRequest.md)| Patching of a dashboard | |
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
| **200** | Updated dashboard |  -  |
| **404** | Dashboard not found |  -  |
| **0** | Unexpected error |  -  |

<a id="patchDashboardsIDCellsIDView_0"></a>
# **patchDashboardsIDCellsIDView_0**
> View patchDashboardsIDCellsIDView_0(dashboardID, cellID, view, zapTraceSpan)

Update the view for a cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String cellID = "cellID_example"; // String | The ID of the cell to update.
    View view = new View(); // View | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      View result = apiInstance.patchDashboardsIDCellsIDView_0(dashboardID, cellID, view, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#patchDashboardsIDCellsIDView_0");
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

<a id="patchDashboardsIDCellsID_0"></a>
# **patchDashboardsIDCellsID_0**
> Cell patchDashboardsIDCellsID_0(dashboardID, cellID, cellUpdate, zapTraceSpan)

Update the non-positional information related to a cell

Updates the non positional information related to a cell. Updates to a single cell&#39;s positional data could cause grid conflicts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    String cellID = "cellID_example"; // String | The ID of the cell to update.
    CellUpdate cellUpdate = new CellUpdate(); // CellUpdate | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Cell result = apiInstance.patchDashboardsIDCellsID_0(dashboardID, cellID, cellUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#patchDashboardsIDCellsID_0");
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

<a id="postDashboards"></a>
# **postDashboards**
> PostDashboards201Response postDashboards(createDashboardRequest, zapTraceSpan)

Create a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    CreateDashboardRequest createDashboardRequest = new CreateDashboardRequest(); // CreateDashboardRequest | Dashboard to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      PostDashboards201Response result = apiInstance.postDashboards(createDashboardRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#postDashboards");
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
| **createDashboardRequest** | [**CreateDashboardRequest**](CreateDashboardRequest.md)| Dashboard to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**PostDashboards201Response**](PostDashboards201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added dashboard |  -  |
| **0** | Unexpected error |  -  |

<a id="postDashboardsIDCells_0"></a>
# **postDashboardsIDCells_0**
> Cell postDashboardsIDCells_0(dashboardID, createCell, zapTraceSpan)

Create a dashboard cell

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    CreateCell createCell = new CreateCell(); // CreateCell | Cell that will be added
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Cell result = apiInstance.postDashboardsIDCells_0(dashboardID, createCell, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#postDashboardsIDCells_0");
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

<a id="postDashboardsIDLabels"></a>
# **postDashboardsIDLabels**
> LabelResponse postDashboardsIDLabels(dashboardID, labelMapping, zapTraceSpan)

Add a label to a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postDashboardsIDLabels(dashboardID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#postDashboardsIDLabels");
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
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The label added to the dashboard |  -  |
| **0** | Unexpected error |  -  |

<a id="postDashboardsIDMembers"></a>
# **postDashboardsIDMembers**
> ResourceMember postDashboardsIDMembers(dashboardID, addResourceMemberRequestBody, zapTraceSpan)

Add a member to a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMember result = apiInstance.postDashboardsIDMembers(dashboardID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#postDashboardsIDMembers");
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
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added to dashboard members |  -  |
| **0** | Unexpected error |  -  |

<a id="postDashboardsIDOwners"></a>
# **postDashboardsIDOwners**
> ResourceOwner postDashboardsIDOwners(dashboardID, addResourceMemberRequestBody, zapTraceSpan)

Add an owner to a dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The dashboard ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwner result = apiInstance.postDashboardsIDOwners(dashboardID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#postDashboardsIDOwners");
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
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added to dashboard owners |  -  |
| **0** | Unexpected error |  -  |

<a id="putDashboardsIDCells_0"></a>
# **putDashboardsIDCells_0**
> Dashboard putDashboardsIDCells_0(dashboardID, cell, zapTraceSpan)

Replace cells in a dashboard

Replaces all cells in a dashboard. This is used primarily to update the positional information of all cells.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
    List<Cell> cell = Arrays.asList(); // List<Cell> | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Dashboard result = apiInstance.putDashboardsIDCells_0(dashboardID, cell, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#putDashboardsIDCells_0");
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

