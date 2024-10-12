# ActivityRunsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityRunsGetActivityRun**](ActivityRunsApi.md#activityRunsGetActivityRun) | **GET** /api/v2/activityRuns/{activityRunID} | Get an ActivityRun by ID |
| [**activityRunsGetActivityRunStatus**](ActivityRunsApi.md#activityRunsGetActivityRunStatus) | **GET** /api/v2/activityRuns/{activityRunID}/status | Get the ActivityRunStatus of an ActivityRun |
| [**activityRunsGetActivityRuns**](ActivityRunsApi.md#activityRunsGetActivityRuns) | **GET** /api/v2/activityRuns | Get ActivityRuns |
| [**activityRunsPutActivityRun**](ActivityRunsApi.md#activityRunsPutActivityRun) | **PUT** /api/v2/activityRuns/{activityRunID} | Update an ActivityRun |
| [**activityRunsPutActivityRunStatus**](ActivityRunsApi.md#activityRunsPutActivityRunStatus) | **PUT** /api/v2/activityRuns/{activityRunID}/status | Update the ActivityRunStatus of an ActivityRun |


<a id="activityRunsGetActivityRun"></a>
# **activityRunsGetActivityRun**
> BuildSystemSharedDTOActivityRun activityRunsGetActivityRun(activityRunID)

Get an ActivityRun by ID

Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,              an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivityRunsApi apiInstance = new ActivityRunsApi(defaultClient);
    Integer activityRunID = 56; // Integer | The ID of the ActivityRun to get.
    try {
      BuildSystemSharedDTOActivityRun result = apiInstance.activityRunsGetActivityRun(activityRunID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityRunsApi#activityRunsGetActivityRun");
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
| **activityRunID** | **Integer**| The ID of the ActivityRun to get. | |

### Return type

[**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="activityRunsGetActivityRunStatus"></a>
# **activityRunsGetActivityRunStatus**
> BuildSystemSharedDTOActivityRunStatus activityRunsGetActivityRunStatus(activityRunID)

Get the ActivityRunStatus of an ActivityRun

Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivityRunsApi apiInstance = new ActivityRunsApi(defaultClient);
    Integer activityRunID = 56; // Integer | The ID of the ActivityRun to get ActivityRunStatus for.
    try {
      BuildSystemSharedDTOActivityRunStatus result = apiInstance.activityRunsGetActivityRunStatus(activityRunID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityRunsApi#activityRunsGetActivityRunStatus");
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
| **activityRunID** | **Integer**| The ID of the ActivityRun to get ActivityRunStatus for. | |

### Return type

[**BuildSystemSharedDTOActivityRunStatus**](BuildSystemSharedDTOActivityRunStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="activityRunsGetActivityRuns"></a>
# **activityRunsGetActivityRuns**
> APIPagedResponseBuildSystemSharedDTOActivityRun activityRunsGetActivityRuns(limit, offset, status)

Get ActivityRuns

Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.                If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivityRunsApi apiInstance = new ActivityRunsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    String status = "Ready"; // String | Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.              If not specified, the default status filter is “InProgress”.
    try {
      APIPagedResponseBuildSystemSharedDTOActivityRun result = apiInstance.activityRunsGetActivityRuns(limit, offset, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityRunsApi#activityRunsGetActivityRuns");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **status** | **String**| Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.              If not specified, the default status filter is “InProgress”. | [optional] [enum: Ready, InProgress, Succeeded, Cancelled, Failed] |

### Return type

[**APIPagedResponseBuildSystemSharedDTOActivityRun**](APIPagedResponseBuildSystemSharedDTOActivityRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="activityRunsPutActivityRun"></a>
# **activityRunsPutActivityRun**
> activityRunsPutActivityRun(activityRunID, buildSystemSharedDTOActivityRun)

Update an ActivityRun

Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivityRunsApi apiInstance = new ActivityRunsApi(defaultClient);
    Integer activityRunID = 56; // Integer | The ID of the ActivityRun to update ActivityRunStatus for.
    BuildSystemSharedDTOActivityRun buildSystemSharedDTOActivityRun = new BuildSystemSharedDTOActivityRun(); // BuildSystemSharedDTOActivityRun | The updated ActivityRun.
    try {
      apiInstance.activityRunsPutActivityRun(activityRunID, buildSystemSharedDTOActivityRun);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityRunsApi#activityRunsPutActivityRun");
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
| **activityRunID** | **Integer**| The ID of the ActivityRun to update ActivityRunStatus for. | |
| **buildSystemSharedDTOActivityRun** | [**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)| The updated ActivityRun. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="activityRunsPutActivityRunStatus"></a>
# **activityRunsPutActivityRunStatus**
> activityRunsPutActivityRunStatus(activityRunID, buildSystemSharedDTOActivityRunStatus)

Update the ActivityRunStatus of an ActivityRun

Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivityRunsApi apiInstance = new ActivityRunsApi(defaultClient);
    Integer activityRunID = 56; // Integer | The ID of the ActivityRun to update ActivityRunStatus for.
    BuildSystemSharedDTOActivityRunStatus buildSystemSharedDTOActivityRunStatus = new BuildSystemSharedDTOActivityRunStatus(); // BuildSystemSharedDTOActivityRunStatus | The updated ActivityRunStatus.
    try {
      apiInstance.activityRunsPutActivityRunStatus(activityRunID, buildSystemSharedDTOActivityRunStatus);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityRunsApi#activityRunsPutActivityRunStatus");
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
| **activityRunID** | **Integer**| The ID of the ActivityRun to update ActivityRunStatus for. | |
| **buildSystemSharedDTOActivityRunStatus** | [**BuildSystemSharedDTOActivityRunStatus**](BuildSystemSharedDTOActivityRunStatus.md)| The updated ActivityRunStatus. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

