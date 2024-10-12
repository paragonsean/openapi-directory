# AttemptApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**saveStats**](AttemptApi.md#saveStats) | **POST** /v1/attempt/save_stats | For worker to set sync stats of a running attempt. |
| [**saveSyncConfig**](AttemptApi.md#saveSyncConfig) | **POST** /v1/attempt/save_sync_config | For worker to save the AttemptSyncConfig for an attempt. |
| [**setWorkflowInAttempt**](AttemptApi.md#setWorkflowInAttempt) | **POST** /v1/attempt/set_workflow_in_attempt | For worker to register the workflow id in attempt. |


<a id="saveStats"></a>
# **saveStats**
> InternalOperationResult saveStats(saveStatsRequestBody)

For worker to set sync stats of a running attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    AttemptApi apiInstance = new AttemptApi(defaultClient);
    SaveStatsRequestBody saveStatsRequestBody = new SaveStatsRequestBody(); // SaveStatsRequestBody | 
    try {
      InternalOperationResult result = apiInstance.saveStats(saveStatsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttemptApi#saveStats");
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
| **saveStatsRequestBody** | [**SaveStatsRequestBody**](SaveStatsRequestBody.md)|  | |

### Return type

[**InternalOperationResult**](InternalOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="saveSyncConfig"></a>
# **saveSyncConfig**
> InternalOperationResult saveSyncConfig(saveAttemptSyncConfigRequestBody)

For worker to save the AttemptSyncConfig for an attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    AttemptApi apiInstance = new AttemptApi(defaultClient);
    SaveAttemptSyncConfigRequestBody saveAttemptSyncConfigRequestBody = new SaveAttemptSyncConfigRequestBody(); // SaveAttemptSyncConfigRequestBody | 
    try {
      InternalOperationResult result = apiInstance.saveSyncConfig(saveAttemptSyncConfigRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttemptApi#saveSyncConfig");
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
| **saveAttemptSyncConfigRequestBody** | [**SaveAttemptSyncConfigRequestBody**](SaveAttemptSyncConfigRequestBody.md)|  | |

### Return type

[**InternalOperationResult**](InternalOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="setWorkflowInAttempt"></a>
# **setWorkflowInAttempt**
> InternalOperationResult setWorkflowInAttempt(setWorkflowInAttemptRequestBody)

For worker to register the workflow id in attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    AttemptApi apiInstance = new AttemptApi(defaultClient);
    SetWorkflowInAttemptRequestBody setWorkflowInAttemptRequestBody = new SetWorkflowInAttemptRequestBody(); // SetWorkflowInAttemptRequestBody | 
    try {
      InternalOperationResult result = apiInstance.setWorkflowInAttempt(setWorkflowInAttemptRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttemptApi#setWorkflowInAttempt");
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
| **setWorkflowInAttemptRequestBody** | [**SetWorkflowInAttemptRequestBody**](SetWorkflowInAttemptRequestBody.md)|  | |

### Return type

[**InternalOperationResult**](InternalOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

