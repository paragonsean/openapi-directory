# ActivityTypesApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugActivityTypesGet**](ActivityTypesApi.md#workspaceSlugActivityTypesGet) | **GET** /{workspace_slug}/activity_types | List all activity types for a workspace |


<a id="workspaceSlugActivityTypesGet"></a>
# **workspaceSlugActivityTypesGet**
> workspaceSlugActivityTypesGet(workspaceSlug)

List all activity types for a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    ActivityTypesApi apiInstance = new ActivityTypesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    try {
      apiInstance.workspaceSlugActivityTypesGet(workspaceSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityTypesApi#workspaceSlugActivityTypesGet");
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
| **workspaceSlug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

