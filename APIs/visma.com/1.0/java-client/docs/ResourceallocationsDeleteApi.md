# ResourceallocationsDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceAllocationsDeleteResourceAllocation**](ResourceallocationsDeleteApi.md#resourceAllocationsDeleteResourceAllocation) | **DELETE** /v1/resourceallocations/{guid} | Delete an resource allocation |
| [**roleAllocationsDeleteRoleAllocation**](ResourceallocationsDeleteApi.md#roleAllocationsDeleteRoleAllocation) | **DELETE** /v1/roleallocations/{guid} | Delete a role allocation. |


<a id="resourceAllocationsDeleteResourceAllocation"></a>
# **resourceAllocationsDeleteResourceAllocation**
> resourceAllocationsDeleteResourceAllocation(guid)

Delete an resource allocation

Returns: No Content (204) if succeeded. Not found (404) if resource allocation can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceallocationsDeleteApi apiInstance = new ResourceallocationsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the resource allocation to delete
    try {
      apiInstance.resourceAllocationsDeleteResourceAllocation(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsDeleteApi#resourceAllocationsDeleteResourceAllocation");
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
| **guid** | **String**| ID of the resource allocation to delete | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="roleAllocationsDeleteRoleAllocation"></a>
# **roleAllocationsDeleteRoleAllocation**
> roleAllocationsDeleteRoleAllocation(guid)

Delete a role allocation.

Returns: No Content (204) if succeeded. Not found (404) if role can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceallocationsDeleteApi apiInstance = new ResourceallocationsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the role allocation to delete.
    try {
      apiInstance.roleAllocationsDeleteRoleAllocation(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsDeleteApi#roleAllocationsDeleteRoleAllocation");
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
| **guid** | **String**| ID for the role allocation to delete. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

