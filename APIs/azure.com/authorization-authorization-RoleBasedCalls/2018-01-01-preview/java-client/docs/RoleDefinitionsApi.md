# RoleDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**roleDefinitionsCreateOrUpdate**](RoleDefinitionsApi.md#roleDefinitionsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} |  |
| [**roleDefinitionsDelete**](RoleDefinitionsApi.md#roleDefinitionsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} |  |
| [**roleDefinitionsGet**](RoleDefinitionsApi.md#roleDefinitionsGet) | **GET** /{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} |  |
| [**roleDefinitionsList**](RoleDefinitionsApi.md#roleDefinitionsList) | **GET** /{scope}/providers/Microsoft.Authorization/roleDefinitions |  |


<a id="roleDefinitionsCreateOrUpdate"></a>
# **roleDefinitionsCreateOrUpdate**
> RoleDefinition roleDefinitionsCreateOrUpdate(scope, roleDefinitionId, apiVersion, roleDefinition)



Creates or updates a role definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleDefinitionsApi apiInstance = new RoleDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role definition.
    String roleDefinitionId = "roleDefinitionId_example"; // String | The ID of the role definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    RoleDefinition roleDefinition = new RoleDefinition(); // RoleDefinition | The values for the role definition.
    try {
      RoleDefinition result = apiInstance.roleDefinitionsCreateOrUpdate(scope, roleDefinitionId, apiVersion, roleDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleDefinitionsApi#roleDefinitionsCreateOrUpdate");
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
| **scope** | **String**| The scope of the role definition. | |
| **roleDefinitionId** | **String**| The ID of the role definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **roleDefinition** | [**RoleDefinition**](RoleDefinition.md)| The values for the role definition. | |

### Return type

[**RoleDefinition**](RoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK - Returns information about the role definition. |  -  |

<a id="roleDefinitionsDelete"></a>
# **roleDefinitionsDelete**
> RoleDefinition roleDefinitionsDelete(scope, roleDefinitionId, apiVersion)



Deletes a role definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleDefinitionsApi apiInstance = new RoleDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role definition.
    String roleDefinitionId = "roleDefinitionId_example"; // String | The ID of the role definition to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RoleDefinition result = apiInstance.roleDefinitionsDelete(scope, roleDefinitionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleDefinitionsApi#roleDefinitionsDelete");
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
| **scope** | **String**| The scope of the role definition. | |
| **roleDefinitionId** | **String**| The ID of the role definition to delete. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RoleDefinition**](RoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the role definition. |  -  |

<a id="roleDefinitionsGet"></a>
# **roleDefinitionsGet**
> RoleDefinition roleDefinitionsGet(scope, roleDefinitionId, apiVersion)



Get role definition by name (GUID).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleDefinitionsApi apiInstance = new RoleDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role definition.
    String roleDefinitionId = "roleDefinitionId_example"; // String | The ID of the role definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RoleDefinition result = apiInstance.roleDefinitionsGet(scope, roleDefinitionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleDefinitionsApi#roleDefinitionsGet");
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
| **scope** | **String**| The scope of the role definition. | |
| **roleDefinitionId** | **String**| The ID of the role definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RoleDefinition**](RoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the role definition. |  -  |

<a id="roleDefinitionsList"></a>
# **roleDefinitionsList**
> RoleDefinitionListResult roleDefinitionsList(scope, apiVersion, $filter)



Get all role definitions that are applicable at scope and above.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleDefinitionsApi apiInstance = new RoleDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use atScopeAndBelow filter to search below the given scope as well.
    try {
      RoleDefinitionListResult result = apiInstance.roleDefinitionsList(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleDefinitionsApi#roleDefinitionsList");
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
| **scope** | **String**| The scope of the role definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. Use atScopeAndBelow filter to search below the given scope as well. | [optional] |

### Return type

[**RoleDefinitionListResult**](RoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of role definitions. |  -  |

