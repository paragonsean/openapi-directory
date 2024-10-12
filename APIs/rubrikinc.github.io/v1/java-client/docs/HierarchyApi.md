# HierarchyApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkHierarchySlaConflictsV1**](HierarchyApi.md#bulkHierarchySlaConflictsV1) | **POST** /hierarchy/bulk_sla_conflicts | Retrieve the list of descendant objects with SLA conflicts in bulk |


<a id="bulkHierarchySlaConflictsV1"></a>
# **bulkHierarchySlaConflictsV1**
> BulkSlaConflictsSummary bulkHierarchySlaConflictsV1(hierarchyObjectIds)

Retrieve the list of descendant objects with SLA conflicts in bulk

Retrieve the list of descendant objects with an explicitly configured SLA domain, or inherit an SLA domain from a different parent for each managed ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HierarchyApi;

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

    HierarchyApi apiInstance = new HierarchyApi(defaultClient);
    HierarchyObjectIds hierarchyObjectIds = new HierarchyObjectIds(); // HierarchyObjectIds | List of hierarchy object IDs.
    try {
      BulkSlaConflictsSummary result = apiInstance.bulkHierarchySlaConflictsV1(hierarchyObjectIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HierarchyApi#bulkHierarchySlaConflictsV1");
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
| **hierarchyObjectIds** | [**HierarchyObjectIds**](HierarchyObjectIds.md)| List of hierarchy object IDs. | |

### Return type

[**BulkSlaConflictsSummary**](BulkSlaConflictsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of SLA domain conflict summaries for the specified managed IDs.  |  -  |

