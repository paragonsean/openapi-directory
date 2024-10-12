# LogsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logsGetLog**](LogsApi.md#logsGetLog) | **GET** /api/v2/Logs/{ID} | Get a log by ID |
| [**logsGetLogs**](LogsApi.md#logsGetLogs) | **GET** /api/v2/Logs | Get the API System logs, most recent first. |
| [**logsPostLog**](LogsApi.md#logsPostLog) | **POST** /api/v2/Logs | Add a Log entry |


<a id="logsGetLog"></a>
# **logsGetLog**
> APIModelsLog logsGetLog(ID)

Get a log by ID

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String ID = "ID_example"; // String | The Log ID
    try {
      APIModelsLog result = apiInstance.logsGetLog(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsGetLog");
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
| **ID** | **String**| The Log ID | |

### Return type

[**APIModelsLog**](APIModelsLog.md)

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

<a id="logsGetLogs"></a>
# **logsGetLogs**
> APIPagedResponseAPIModelsLog logsGetLogs(limit, offset)

Get the API System logs, most recent first.

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LogsApi apiInstance = new LogsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsLog result = apiInstance.logsGetLogs(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsGetLogs");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsLog**](APIPagedResponseAPIModelsLog.md)

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

<a id="logsPostLog"></a>
# **logsPostLog**
> String logsPostLog(message)

Add a Log entry

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String message = "message_example"; // String | Message to enter into the log
    try {
      String result = apiInstance.logsPostLog(message);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsPostLog");
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
| **message** | **String**| Message to enter into the log | |

### Return type

**String**

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

