# SchedulerApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**executeDestinationCheckConnection**](SchedulerApi.md#executeDestinationCheckConnection) | **POST** /v1/scheduler/destinations/check_connection | Run check connection for a given destination configuration |
| [**executeSourceCheckConnection**](SchedulerApi.md#executeSourceCheckConnection) | **POST** /v1/scheduler/sources/check_connection | Run check connection for a given source configuration |
| [**executeSourceDiscoverSchema**](SchedulerApi.md#executeSourceDiscoverSchema) | **POST** /v1/scheduler/sources/discover_schema | Run discover schema for a given source a source configuration |


<a id="executeDestinationCheckConnection"></a>
# **executeDestinationCheckConnection**
> CheckConnectionRead executeDestinationCheckConnection(destinationCoreConfig)

Run check connection for a given destination configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    DestinationCoreConfig destinationCoreConfig = new DestinationCoreConfig(); // DestinationCoreConfig | 
    try {
      CheckConnectionRead result = apiInstance.executeDestinationCheckConnection(destinationCoreConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#executeDestinationCheckConnection");
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
| **destinationCoreConfig** | [**DestinationCoreConfig**](DestinationCoreConfig.md)|  | |

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **422** | Input failed validation |  -  |

<a id="executeSourceCheckConnection"></a>
# **executeSourceCheckConnection**
> CheckConnectionRead executeSourceCheckConnection(sourceCoreConfig)

Run check connection for a given source configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    SourceCoreConfig sourceCoreConfig = new SourceCoreConfig(); // SourceCoreConfig | 
    try {
      CheckConnectionRead result = apiInstance.executeSourceCheckConnection(sourceCoreConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#executeSourceCheckConnection");
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
| **sourceCoreConfig** | [**SourceCoreConfig**](SourceCoreConfig.md)|  | |

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **422** | Input failed validation |  -  |

<a id="executeSourceDiscoverSchema"></a>
# **executeSourceDiscoverSchema**
> SourceDiscoverSchemaRead executeSourceDiscoverSchema(sourceCoreConfig)

Run discover schema for a given source a source configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    SourceCoreConfig sourceCoreConfig = new SourceCoreConfig(); // SourceCoreConfig | 
    try {
      SourceDiscoverSchemaRead result = apiInstance.executeSourceDiscoverSchema(sourceCoreConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#executeSourceDiscoverSchema");
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
| **sourceCoreConfig** | [**SourceCoreConfig**](SourceCoreConfig.md)|  | |

### Return type

[**SourceDiscoverSchemaRead**](SourceDiscoverSchemaRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **422** | Input failed validation |  -  |

