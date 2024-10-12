# SnapshotApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSnapshotStorageStatsV1**](SnapshotApi.md#getSnapshotStorageStatsV1) | **GET** /snapshot/{id}/storage/stats | Returns storage stats for a snapshot |


<a id="getSnapshotStorageStatsV1"></a>
# **getSnapshotStorageStatsV1**
> SnapshotStorageStats getSnapshotStorageStatsV1(id)

Returns storage stats for a snapshot

Returns the storage statistics for a snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotApi;

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

    SnapshotApi apiInstance = new SnapshotApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a snapshot object.
    try {
      SnapshotStorageStats result = apiInstance.getSnapshotStorageStatsV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotApi#getSnapshotStorageStatsV1");
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
| **id** | **String**| ID assigned to a snapshot object. | |

### Return type

[**SnapshotStorageStats**](SnapshotStorageStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns storage stats for a snapshot. |  -  |

