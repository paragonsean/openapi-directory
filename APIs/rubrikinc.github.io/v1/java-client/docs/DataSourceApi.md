# DataSourceApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkDeleteSnapshots**](DataSourceApi.md#bulkDeleteSnapshots) | **POST** /data_source/snapshot/bulk_delete | Bulk delete all snapshots for the given objects |
| [**bulkDeleteSnapshotsForObject**](DataSourceApi.md#bulkDeleteSnapshotsForObject) | **POST** /data_source/{id}/snapshot/bulk_delete | Bulk delete specified snapshots for the given object |
| [**expiredCustomRetentionSnapshots**](DataSourceApi.md#expiredCustomRetentionSnapshots) | **GET** /data_source/{id}/expired_custom_retention_snapshots | Returns a list of snapshots that have expired according to their snapshot-level SLA Domain assignments  |


<a id="bulkDeleteSnapshots"></a>
# **bulkDeleteSnapshots**
> bulkDeleteSnapshots(bulkDeleteSnapshotsConfig)

Bulk delete all snapshots for the given objects

This endpoint deletes all snapshots from all locations for the objects with the IDs specified by the &#39;objectIds&#39; parameter. API returning success does not guarantee that the snapshots will be expired. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourceApi;

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

    DataSourceApi apiInstance = new DataSourceApi(defaultClient);
    BulkDeleteSnapshotsConfig bulkDeleteSnapshotsConfig = new BulkDeleteSnapshotsConfig(); // BulkDeleteSnapshotsConfig | A list of object IDs. 
    try {
      apiInstance.bulkDeleteSnapshots(bulkDeleteSnapshotsConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourceApi#bulkDeleteSnapshots");
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
| **bulkDeleteSnapshotsConfig** | [**BulkDeleteSnapshotsConfig**](BulkDeleteSnapshotsConfig.md)| A list of object IDs.  | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK on success, success doesn&#39;t imply all snapshots will be deleted.  |  -  |
| **422** | Returned if delete API fails. |  -  |

<a id="bulkDeleteSnapshotsForObject"></a>
# **bulkDeleteSnapshotsForObject**
> bulkDeleteSnapshotsForObject(id, bulkDeleteObjectSnapshotsConfig)

Bulk delete specified snapshots for the given object

Bulk deletion of the snapshots specified by a list of snapshot IDs for a given object. Object type is required. Location ID is optional. API returning success does not guarantee that the snapshot will be expired. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourceApi;

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

    DataSourceApi apiInstance = new DataSourceApi(defaultClient);
    String id = "id_example"; // String | ID of the object.
    BulkDeleteObjectSnapshotsConfig bulkDeleteObjectSnapshotsConfig = new BulkDeleteObjectSnapshotsConfig(); // BulkDeleteObjectSnapshotsConfig | A list of snapshot IDs specifying snapshots to delete. Optionally specifies a location ID. Snapshot deletion is global when the location ID is absent. 
    try {
      apiInstance.bulkDeleteSnapshotsForObject(id, bulkDeleteObjectSnapshotsConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourceApi#bulkDeleteSnapshotsForObject");
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
| **id** | **String**| ID of the object. | |
| **bulkDeleteObjectSnapshotsConfig** | [**BulkDeleteObjectSnapshotsConfig**](BulkDeleteObjectSnapshotsConfig.md)| A list of snapshot IDs specifying snapshots to delete. Optionally specifies a location ID. Snapshot deletion is global when the location ID is absent.  | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK on success, success doesn&#39;t imply all snapshots will be deleted.  |  -  |
| **422** | Returned if delete API fails. |  -  |

<a id="expiredCustomRetentionSnapshots"></a>
# **expiredCustomRetentionSnapshots**
> ExpiredCustomRetentionSnapshots expiredCustomRetentionSnapshots(id)

Returns a list of snapshots that have expired according to their snapshot-level SLA Domain assignments 

Gets a list of the snapshots of a specified data source that have expired according to the snapshot-level SLA Domain assignments. This list does not include remote snapshots. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourceApi;

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

    DataSourceApi apiInstance = new DataSourceApi(defaultClient);
    String id = "id_example"; // String | The object ID.
    try {
      ExpiredCustomRetentionSnapshots result = apiInstance.expiredCustomRetentionSnapshots(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourceApi#expiredCustomRetentionSnapshots");
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
| **id** | **String**| The object ID. | |

### Return type

[**ExpiredCustomRetentionSnapshots**](ExpiredCustomRetentionSnapshots.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array containing information of snapshots which have been expired due to snapshot-level SLA Domain assignments.  |  -  |
| **422** | The API call has failed. |  -  |

