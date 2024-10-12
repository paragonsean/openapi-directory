# ReplicationApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disablePerLocationPause**](ReplicationApi.md#disablePerLocationPause) | **POST** /replication/location_pause/disable | Resume replication from specified source clusters |
| [**enablePerLocationPause**](ReplicationApi.md#enablePerLocationPause) | **POST** /replication/location_pause/enable | Pause replication from specified source clusters |


<a id="disablePerLocationPause"></a>
# **disablePerLocationPause**
> disablePerLocationPause(disablePerLocationPause)

Resume replication from specified source clusters

A single Rubrik cluster can be the replication target for multiple source Rubrik clusters. For each source cluster specified, this resumes replication from that source cluster to the target cluster. This call must be made on the target cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReplicationApi apiInstance = new ReplicationApi(defaultClient);
    DisablePerLocationPause disablePerLocationPause = new DisablePerLocationPause(); // DisablePerLocationPause | A configuration value that specifies which source clusters resume replication. Snapshots taken before or during the replication pause can be skipped. 
    try {
      apiInstance.disablePerLocationPause(disablePerLocationPause);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationApi#disablePerLocationPause");
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
| **disablePerLocationPause** | [**DisablePerLocationPause**](DisablePerLocationPause.md)| A configuration value that specifies which source clusters resume replication. Snapshots taken before or during the replication pause can be skipped.  | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully resumed replication from all specified source clusters.  |  -  |

<a id="enablePerLocationPause"></a>
# **enablePerLocationPause**
> enablePerLocationPause(enablePerLocationPause)

Pause replication from specified source clusters

A single Rubrik cluster can be the replication target for multiple source Rubrik clusters. For each source cluster specified, this pauses replication from that source cluster to the target cluster. This call must be made on the target cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReplicationApi apiInstance = new ReplicationApi(defaultClient);
    EnablePerLocationPause enablePerLocationPause = new EnablePerLocationPause(); // EnablePerLocationPause | A configuration value that specifies which source clusters pause replication. Replication jobs can be canceled immediately or be allowed to finish. 
    try {
      apiInstance.enablePerLocationPause(enablePerLocationPause);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationApi#enablePerLocationPause");
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
| **enablePerLocationPause** | [**EnablePerLocationPause**](EnablePerLocationPause.md)| A configuration value that specifies which source clusters pause replication. Replication jobs can be canceled immediately or be allowed to finish.  | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully paused replication from all specified source clusters.  |  -  |

