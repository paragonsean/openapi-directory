# LogsApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logDelete**](LogsApi.md#logDelete) | **DELETE** /log |  |
| [**logGet**](LogsApi.md#logGet) | **GET** /log |  |
| [**logIdDelete**](LogsApi.md#logIdDelete) | **DELETE** /log/{id} |  |


<a id="logDelete"></a>
# **logDelete**
> logDelete()



delete all log messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    LogsApi apiInstance = new LogsApi(defaultClient);
    try {
      apiInstance.logDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **204** | log messages successfully |  -  |

<a id="logGet"></a>
# **logGet**
> List&lt;LogEntry&gt; logGet(startindex, count, subject, type)



get a list of slicebox log messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    LogsApi apiInstance = new LogsApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of log messages
    Long count = 20L; // Long | size of returned slice of log messages
    String subject = "subject_example"; // String | log subject to filter results by
    String type = "type_example"; // String | log type (DEFAULT, INFO, WARN, ERROR) to filter results by
    try {
      List<LogEntry> result = apiInstance.logGet(startindex, count, subject, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logGet");
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
| **startindex** | **Long**| start index of returned slice of log messages | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of log messages | [optional] [default to 20] |
| **subject** | **String**| log subject to filter results by | [optional] |
| **type** | **String**| log type (DEFAULT, INFO, WARN, ERROR) to filter results by | [optional] |

### Return type

[**List&lt;LogEntry&gt;**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | log messages |  -  |

<a id="logIdDelete"></a>
# **logIdDelete**
> logIdDelete(id)



Delete the log entry with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    LogsApi apiInstance = new LogsApi(defaultClient);
    Long id = 56L; // Long | ID of log entry
    try {
      apiInstance.logIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logIdDelete");
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
| **id** | **Long**| ID of log entry | |

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
| **204** | log entry deleted |  -  |

