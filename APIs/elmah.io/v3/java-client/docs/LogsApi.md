# LogsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logsCreate**](LogsApi.md#logsCreate) | **POST** /v3/logs | Create a new log. |
| [**logsDiagnose**](LogsApi.md#logsDiagnose) | **GET** /v3/logs/{id}/_diagnose | Help diagnose logging problems. |
| [**logsDisable**](LogsApi.md#logsDisable) | **POST** /v3/logs/{id}/_disable | Disable a log by its ID. |
| [**logsEnable**](LogsApi.md#logsEnable) | **POST** /v3/logs/{id}/_enable | Enable a log by its ID. |
| [**logsGet**](LogsApi.md#logsGet) | **GET** /v3/logs/{id} | Fetch a log by its ID. |
| [**logsGetAll**](LogsApi.md#logsGetAll) | **GET** /v3/logs | Fetch a list of logs. |


<a id="logsCreate"></a>
# **logsCreate**
> CreateLogResult logsCreate(createLog)

Create a new log.

Required permission: &#x60;logs_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    CreateLog createLog = new CreateLog(); // CreateLog | The log object to create.
    try {
      CreateLogResult result = apiInstance.logsCreate(createLog);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsCreate");
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
| **createLog** | [**CreateLog**](CreateLog.md)| The log object to create. | [optional] |

### Return type

[**CreateLogResult**](CreateLogResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Log where successfully created. |  -  |
| **400** | Something wrong with the parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="logsDiagnose"></a>
# **logsDiagnose**
> List&lt;String&gt; logsDiagnose(id)

Help diagnose logging problems.

Required permission: &#x60;messages_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String id = "id_example"; // String | The ID of the log to diagnose.
    try {
      List<String> result = apiInstance.logsDiagnose(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsDiagnose");
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
| **id** | **String**| The ID of the log to diagnose. | |

### Return type

**List&lt;String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log was diagnosed. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="logsDisable"></a>
# **logsDisable**
> logsDisable(id)

Disable a log by its ID.

Required permission: &#x60;logs_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String id = "id_example"; // String | The ID of the log to disable.
    try {
      apiInstance.logsDisable(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsDisable");
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
| **id** | **String**| The ID of the log to disable. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log was disabled. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="logsEnable"></a>
# **logsEnable**
> logsEnable(id)

Enable a log by its ID.

Required permission: &#x60;logs_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String id = "id_example"; // String | The ID of the log to enable.
    try {
      apiInstance.logsEnable(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsEnable");
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
| **id** | **String**| The ID of the log to enable. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log was enabled. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="logsGet"></a>
# **logsGet**
> Log logsGet(id)

Fetch a log by its ID.

Required permission: &#x60;logs_read&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String id = "id_example"; // String | The ID of the log to fetch.
    try {
      Log result = apiInstance.logsGet(id);
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
| **id** | **String**| The ID of the log to fetch. | |

### Return type

[**Log**](Log.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for log successful. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="logsGetAll"></a>
# **logsGetAll**
> List&lt;Log&gt; logsGetAll()

Fetch a list of logs.

Required permission: &#x60;logs_read&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    try {
      List<Log> result = apiInstance.logsGetAll();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsGetAll");
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

[**List&lt;Log&gt;**](Log.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for logs successful. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

