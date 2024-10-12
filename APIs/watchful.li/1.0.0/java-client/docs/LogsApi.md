# LogsApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLogById**](LogsApi.md#deleteLogById) | **DELETE** /logs/{id} | Delete a specific log |
| [**getExportLogs**](LogsApi.md#getExportLogs) | **GET** /logs/export | Get a CSV or PDF file contain the list of logs |
| [**getFieldsLogs**](LogsApi.md#getFieldsLogs) | **GET** /logs/metadata | Get the list of fields |
| [**getTypesLogs**](LogsApi.md#getTypesLogs) | **GET** /logs/types | Get the list of log types |
| [**logsGet**](LogsApi.md#logsGet) | **GET** /logs | Get a list of logs |


<a id="deleteLogById"></a>
# **deleteLogById**
> String deleteLogById(id)

Delete a specific log

Delete a specific log

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    LogsApi apiInstance = new LogsApi(defaultClient);
    Long id = 56L; // Long | ID of log that needs to be deleted
    try {
      String result = apiInstance.deleteLogById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#deleteLogById");
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
| **id** | **Long**| ID of log that needs to be deleted | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log correctly deleted |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getExportLogs"></a>
# **getExportLogs**
> getExportLogs(format, site, filterType, search, startdate, enddate, limit, startid)

Get a CSV or PDF file contain the list of logs

Returns a file contain the list of logs

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String format = "csv"; // String | Format of exported file (PDF or CSV)
    Long site = 56L; // Long | Site id of the log
    String filterType = ""; // String | Type of the log
    String search = "search_example"; // String | Do a 'LIKE' search, you can also use '%'
    String startdate = "startdate_example"; // String | Logs after this date, format YYYY-MM-DD HH:MM:SS
    String enddate = "enddate_example"; // String | Logs before this date, format YYYY-MM-DD HH:MM:SS
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long startid = 56L; // Long | Start of the return (default 0)
    try {
      apiInstance.getExportLogs(format, site, filterType, search, startdate, enddate, limit, startid);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#getExportLogs");
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
| **format** | **String**| Format of exported file (PDF or CSV) | [enum: csv, pdf] |
| **site** | **Long**| Site id of the log | [optional] |
| **filterType** | **String**| Type of the log | [optional] [enum: , plugin_sends_error, curlerror, modified_file, word_not_in_homepage, file_not_exists, update_available, new_extension, deleted_extension, extension_not_saved, modified_value_files, custom] |
| **search** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **startdate** | **String**| Logs after this date, format YYYY-MM-DD HH:MM:SS | [optional] |
| **enddate** | **String**| Logs before this date, format YYYY-MM-DD HH:MM:SS | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **startid** | **Long**| Start of the return (default 0) | [optional] |

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
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |

<a id="getFieldsLogs"></a>
# **getFieldsLogs**
> String getFieldsLogs()

Get the list of fields

Returns a list of fields

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    LogsApi apiInstance = new LogsApi(defaultClient);
    try {
      String result = apiInstance.getFieldsLogs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#getFieldsLogs");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getTypesLogs"></a>
# **getTypesLogs**
> String getTypesLogs()

Get the list of log types

Returns a list of log types

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    LogsApi apiInstance = new LogsApi(defaultClient);
    try {
      String result = apiInstance.getTypesLogs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#getTypesLogs");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="logsGet"></a>
# **logsGet**
> Log logsGet(logType, logEntry, from, to, fields, limit, limitstart, order)

Get a list of logs

Returns a list of logs

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String logType = ""; // String | Type of the log
    String logEntry = "logEntry_example"; // String | Do a 'LIKE' search, you can also use '%'
    String from = "from_example"; // String | Logs after this date, format YYYY-MM-DD HH:MM:SS
    String to = "to_example"; // String | Logs before this date, format YYYY-MM-DD HH:MM:SS
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Log result = apiInstance.logsGet(logType, logEntry, from, to, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsGet");
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
| **logType** | **String**| Type of the log | [optional] [enum: , plugin_sends_error, curlerror, modified_file, word_not_in_homepage, file_not_exists, update_available, new_extension, deleted_extension, extension_not_saved, modified_value_files, custom] |
| **logEntry** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **from** | **String**| Logs after this date, format YYYY-MM-DD HH:MM:SS | [optional] |
| **to** | **String**| Logs before this date, format YYYY-MM-DD HH:MM:SS | [optional] |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |

