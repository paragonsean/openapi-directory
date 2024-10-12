# InternalApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrUpdateState_0**](InternalApi.md#createOrUpdateState_0) | **POST** /v1/state/create_or_update | Create or update the state for a connection. |
| [**getAttemptNormalizationStatusesForJob_0**](InternalApi.md#getAttemptNormalizationStatusesForJob_0) | **POST** /v1/jobs/get_normalization_status | Get normalization status to determine if we can bypass normalization phase |
| [**saveStats_0**](InternalApi.md#saveStats_0) | **POST** /v1/attempt/save_stats | For worker to set sync stats of a running attempt. |
| [**saveSyncConfig_0**](InternalApi.md#saveSyncConfig_0) | **POST** /v1/attempt/save_sync_config | For worker to save the AttemptSyncConfig for an attempt. |
| [**setWorkflowInAttempt_0**](InternalApi.md#setWorkflowInAttempt_0) | **POST** /v1/attempt/set_workflow_in_attempt | For worker to register the workflow id in attempt. |
| [**writeDiscoverCatalogResult_0**](InternalApi.md#writeDiscoverCatalogResult_0) | **POST** /v1/sources/write_discover_catalog_result | Should only called from worker, to write result from discover activity back to DB. |


<a id="createOrUpdateState_0"></a>
# **createOrUpdateState_0**
> ConnectionState createOrUpdateState_0(connectionStateCreateOrUpdate)

Create or update the state for a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    ConnectionStateCreateOrUpdate connectionStateCreateOrUpdate = new ConnectionStateCreateOrUpdate(); // ConnectionStateCreateOrUpdate | 
    try {
      ConnectionState result = apiInstance.createOrUpdateState_0(connectionStateCreateOrUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#createOrUpdateState_0");
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
| **connectionStateCreateOrUpdate** | [**ConnectionStateCreateOrUpdate**](ConnectionStateCreateOrUpdate.md)|  | |

### Return type

[**ConnectionState**](ConnectionState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getAttemptNormalizationStatusesForJob_0"></a>
# **getAttemptNormalizationStatusesForJob_0**
> AttemptNormalizationStatusReadList getAttemptNormalizationStatusesForJob_0(jobIdRequestBody)

Get normalization status to determine if we can bypass normalization phase

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    JobIdRequestBody jobIdRequestBody = new JobIdRequestBody(); // JobIdRequestBody | 
    try {
      AttemptNormalizationStatusReadList result = apiInstance.getAttemptNormalizationStatusesForJob_0(jobIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#getAttemptNormalizationStatusesForJob_0");
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
| **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | [optional] |

### Return type

[**AttemptNormalizationStatusReadList**](AttemptNormalizationStatusReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="saveStats_0"></a>
# **saveStats_0**
> InternalOperationResult saveStats_0(saveStatsRequestBody)

For worker to set sync stats of a running attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SaveStatsRequestBody saveStatsRequestBody = new SaveStatsRequestBody(); // SaveStatsRequestBody | 
    try {
      InternalOperationResult result = apiInstance.saveStats_0(saveStatsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#saveStats_0");
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

<a id="saveSyncConfig_0"></a>
# **saveSyncConfig_0**
> InternalOperationResult saveSyncConfig_0(saveAttemptSyncConfigRequestBody)

For worker to save the AttemptSyncConfig for an attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SaveAttemptSyncConfigRequestBody saveAttemptSyncConfigRequestBody = new SaveAttemptSyncConfigRequestBody(); // SaveAttemptSyncConfigRequestBody | 
    try {
      InternalOperationResult result = apiInstance.saveSyncConfig_0(saveAttemptSyncConfigRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#saveSyncConfig_0");
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

<a id="setWorkflowInAttempt_0"></a>
# **setWorkflowInAttempt_0**
> InternalOperationResult setWorkflowInAttempt_0(setWorkflowInAttemptRequestBody)

For worker to register the workflow id in attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SetWorkflowInAttemptRequestBody setWorkflowInAttemptRequestBody = new SetWorkflowInAttemptRequestBody(); // SetWorkflowInAttemptRequestBody | 
    try {
      InternalOperationResult result = apiInstance.setWorkflowInAttempt_0(setWorkflowInAttemptRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#setWorkflowInAttempt_0");
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

<a id="writeDiscoverCatalogResult_0"></a>
# **writeDiscoverCatalogResult_0**
> DiscoverCatalogResult writeDiscoverCatalogResult_0(sourceDiscoverSchemaWriteRequestBody)

Should only called from worker, to write result from discover activity back to DB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SourceDiscoverSchemaWriteRequestBody sourceDiscoverSchemaWriteRequestBody = new SourceDiscoverSchemaWriteRequestBody(); // SourceDiscoverSchemaWriteRequestBody | 
    try {
      DiscoverCatalogResult result = apiInstance.writeDiscoverCatalogResult_0(sourceDiscoverSchemaWriteRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#writeDiscoverCatalogResult_0");
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
| **sourceDiscoverSchemaWriteRequestBody** | [**SourceDiscoverSchemaWriteRequestBody**](SourceDiscoverSchemaWriteRequestBody.md)|  | |

### Return type

[**DiscoverCatalogResult**](DiscoverCatalogResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

