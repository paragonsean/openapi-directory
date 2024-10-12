# ResourceallocationsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceAllocationsPatchResourceAllocation**](ResourceallocationsWriteApi.md#resourceAllocationsPatchResourceAllocation) | **PATCH** /v1/resourceallocations/{guid} | Update (Patch) a resource allocation or a part of it |
| [**resourceAllocationsPostResourceAllocation**](ResourceallocationsWriteApi.md#resourceAllocationsPostResourceAllocation) | **POST** /v1/resourceallocations | Insert a resource allocation |
| [**roleAllocationsPatchRoleAllocation**](ResourceallocationsWriteApi.md#roleAllocationsPatchRoleAllocation) | **PATCH** /v1/roleallocations/{guid} | Update (Patch) a role allocation. |
| [**roleAllocationsPostRoleAllocation**](ResourceallocationsWriteApi.md#roleAllocationsPostRoleAllocation) | **POST** /v1/roleallocations | Insert a role allocation. |


<a id="resourceAllocationsPatchResourceAllocation"></a>
# **resourceAllocationsPatchResourceAllocation**
> List&lt;ResourceAllocationOutputModel&gt; resourceAllocationsPatchResourceAllocation(guid, patchOperation)

Update (Patch) a resource allocation or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsWriteApi;

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

    ResourceallocationsWriteApi apiInstance = new ResourceallocationsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the resource allocation
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ResourceAllocationModel
    try {
      List<ResourceAllocationOutputModel> result = apiInstance.resourceAllocationsPatchResourceAllocation(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsWriteApi#resourceAllocationsPatchResourceAllocation");
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
| **guid** | **String**| ID of the resource allocation | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ResourceAllocationModel | [optional] |

### Return type

[**List&lt;ResourceAllocationOutputModel&gt;**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated activities |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="resourceAllocationsPostResourceAllocation"></a>
# **resourceAllocationsPostResourceAllocation**
> ResourceAllocationOutputModel resourceAllocationsPostResourceAllocation(resourceAllocationInputModel)

Insert a resource allocation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsWriteApi;

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

    ResourceallocationsWriteApi apiInstance = new ResourceallocationsWriteApi(defaultClient);
    ResourceAllocationInputModel resourceAllocationInputModel = new ResourceAllocationInputModel(); // ResourceAllocationInputModel | ResourceAllocationInputModel
    try {
      ResourceAllocationOutputModel result = apiInstance.resourceAllocationsPostResourceAllocation(resourceAllocationInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsWriteApi#resourceAllocationsPostResourceAllocation");
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
| **resourceAllocationInputModel** | [**ResourceAllocationInputModel**](ResourceAllocationInputModel.md)| ResourceAllocationInputModel | [optional] |

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created resource allocation |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="roleAllocationsPatchRoleAllocation"></a>
# **roleAllocationsPatchRoleAllocation**
> List&lt;RoleAllocationOutputModel&gt; roleAllocationsPatchRoleAllocation(guid, patchOperation)

Update (Patch) a role allocation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsWriteApi;

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

    ResourceallocationsWriteApi apiInstance = new ResourceallocationsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the role allocation.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of RoleAllocationModel.
    try {
      List<RoleAllocationOutputModel> result = apiInstance.roleAllocationsPatchRoleAllocation(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsWriteApi#roleAllocationsPatchRoleAllocation");
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
| **guid** | **String**| ID of the role allocation. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of RoleAllocationModel. | [optional] |

### Return type

[**List&lt;RoleAllocationOutputModel&gt;**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RoleAllocationModel. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="roleAllocationsPostRoleAllocation"></a>
# **roleAllocationsPostRoleAllocation**
> RoleAllocationOutputModel roleAllocationsPostRoleAllocation(roleAllocationInputModel)

Insert a role allocation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsWriteApi;

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

    ResourceallocationsWriteApi apiInstance = new ResourceallocationsWriteApi(defaultClient);
    RoleAllocationInputModel roleAllocationInputModel = new RoleAllocationInputModel(); // RoleAllocationInputModel | Role allocation to insert.
    try {
      RoleAllocationOutputModel result = apiInstance.roleAllocationsPostRoleAllocation(roleAllocationInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsWriteApi#roleAllocationsPostRoleAllocation");
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
| **roleAllocationInputModel** | [**RoleAllocationInputModel**](RoleAllocationInputModel.md)| Role allocation to insert. | [optional] |

### Return type

[**RoleAllocationOutputModel**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | RoleAllocationModel. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

