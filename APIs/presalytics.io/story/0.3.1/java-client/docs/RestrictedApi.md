# RestrictedApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**collaboratorsPost**](RestrictedApi.md#collaboratorsPost) | **POST** /collaborators | Collborators: Bulk Update (Admin Only) |


<a id="collaboratorsPost"></a>
# **collaboratorsPost**
> List&lt;PermissionType&gt; collaboratorsPost(collaboratorBulkUpdateRequest)

Collborators: Bulk Update (Admin Only)

Allows for bulk updates on collaborator metadata.  Restricted to internal admins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestrictedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    RestrictedApi apiInstance = new RestrictedApi(defaultClient);
    CollaboratorBulkUpdateRequest collaboratorBulkUpdateRequest = new CollaboratorBulkUpdateRequest(); // CollaboratorBulkUpdateRequest | parameters to identify an update a collaborator across multiple stories
    try {
      List<PermissionType> result = apiInstance.collaboratorsPost(collaboratorBulkUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictedApi#collaboratorsPost");
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
| **collaboratorBulkUpdateRequest** | [**CollaboratorBulkUpdateRequest**](CollaboratorBulkUpdateRequest.md)| parameters to identify an update a collaborator across multiple stories | |

### Return type

[**List&lt;PermissionType&gt;**](PermissionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of all possible permission types |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

