# SolutionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**solutionsCleanupSolutionData**](SolutionsApi.md#solutionsCleanupSolutionData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}/cleanupData | Cleanup the solution data in the migrate project. |
| [**solutionsDeleteSolution**](SolutionsApi.md#solutionsDeleteSolution) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Delete the solution |
| [**solutionsEnumerateSolutions**](SolutionsApi.md#solutionsEnumerateSolutions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions | Gets the list of solutions in the migrate project. |
| [**solutionsGetConfig**](SolutionsApi.md#solutionsGetConfig) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}/getConfig | Gets the config for the solution in the migrate project. |
| [**solutionsGetSolution**](SolutionsApi.md#solutionsGetSolution) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Gets a solution in the migrate project. |
| [**solutionsPatchSolution**](SolutionsApi.md#solutionsPatchSolution) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Update solution. |
| [**solutionsPutSolution**](SolutionsApi.md#solutionsPutSolution) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName} | Creates a solution in the migrate project. |


<a id="solutionsCleanupSolutionData"></a>
# **solutionsCleanupSolutionData**
> solutionsCleanupSolutionData(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion)

Cleanup the solution data in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    try {
      apiInstance.solutionsCleanupSolutionData(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsCleanupSolutionData");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **solutionName** | **String**| Unique name of a migration solution within a migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="solutionsDeleteSolution"></a>
# **solutionsDeleteSolution**
> solutionsDeleteSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, acceptLanguage)

Delete the solution

Delete the solution. Deleting non-existent project is a no-operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.solutionsDeleteSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsDeleteSolution");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **solutionName** | **String**| Unique name of a migration solution within a migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="solutionsEnumerateSolutions"></a>
# **solutionsEnumerateSolutions**
> SolutionsCollection solutionsEnumerateSolutions(subscriptionId, resourceGroupName, migrateProjectName, apiVersion)

Gets the list of solutions in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    try {
      SolutionsCollection result = apiInstance.solutionsEnumerateSolutions(subscriptionId, resourceGroupName, migrateProjectName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsEnumerateSolutions");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |

### Return type

[**SolutionsCollection**](SolutionsCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="solutionsGetConfig"></a>
# **solutionsGetConfig**
> SolutionConfig solutionsGetConfig(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion)

Gets the config for the solution in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    try {
      SolutionConfig result = apiInstance.solutionsGetConfig(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsGetConfig");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **solutionName** | **String**| Unique name of a migration solution within a migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |

### Return type

[**SolutionConfig**](SolutionConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="solutionsGetSolution"></a>
# **solutionsGetSolution**
> Solution solutionsGetSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion)

Gets a solution in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    try {
      Solution result = apiInstance.solutionsGetSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsGetSolution");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **solutionName** | **String**| Unique name of a migration solution within a migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |

### Return type

[**Solution**](Solution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="solutionsPatchSolution"></a>
# **solutionsPatchSolution**
> Solution solutionsPatchSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput)

Update solution.

Update a solution with specified name. Supports partial updates, for example only tags can be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    Solution solutionInput = new Solution(); // Solution | The input for the solution.
    try {
      Solution result = apiInstance.solutionsPatchSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsPatchSolution");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **solutionName** | **String**| Unique name of a migration solution within a migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **solutionInput** | [**Solution**](Solution.md)| The input for the solution. | |

### Return type

[**Solution**](Solution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="solutionsPutSolution"></a>
# **solutionsPutSolution**
> Solution solutionsPutSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput)

Creates a solution in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SolutionsApi apiInstance = new SolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String solutionName = "solutionName_example"; // String | Unique name of a migration solution within a migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    Solution solutionInput = new Solution(); // Solution | The input for the solution.
    try {
      Solution result = apiInstance.solutionsPutSolution(subscriptionId, resourceGroupName, migrateProjectName, solutionName, apiVersion, solutionInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SolutionsApi#solutionsPutSolution");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **solutionName** | **String**| Unique name of a migration solution within a migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **solutionInput** | [**Solution**](Solution.md)| The input for the solution. | |

### Return type

[**Solution**](Solution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

