# IntegrationAccountAssembliesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountAssembliesCreateOrUpdate**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName} |  |
| [**integrationAccountAssembliesDelete**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName} |  |
| [**integrationAccountAssembliesGet**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName} |  |
| [**integrationAccountAssembliesList**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies |  |
| [**integrationAccountAssembliesListContentCallbackUrl**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName}/listContentCallbackUrl |  |


<a id="integrationAccountAssembliesCreateOrUpdate"></a>
# **integrationAccountAssembliesCreateOrUpdate**
> AssemblyDefinition integrationAccountAssembliesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, assemblyArtifact)



Create or update an assembly for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAssembliesApi apiInstance = new IntegrationAccountAssembliesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    AssemblyDefinition assemblyArtifact = new AssemblyDefinition(); // AssemblyDefinition | The assembly artifact.
    try {
      AssemblyDefinition result = apiInstance.integrationAccountAssembliesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, assemblyArtifact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAssembliesApi#integrationAccountAssembliesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **assemblyArtifactName** | **String**| The assembly artifact name. | |
| **apiVersion** | **String**| The API version. | |
| **assemblyArtifact** | [**AssemblyDefinition**](AssemblyDefinition.md)| The assembly artifact. | |

### Return type

[**AssemblyDefinition**](AssemblyDefinition.md)

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

<a id="integrationAccountAssembliesDelete"></a>
# **integrationAccountAssembliesDelete**
> integrationAccountAssembliesDelete(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion)



Delete an assembly for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAssembliesApi apiInstance = new IntegrationAccountAssembliesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountAssembliesDelete(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAssembliesApi#integrationAccountAssembliesDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **assemblyArtifactName** | **String**| The assembly artifact name. | |
| **apiVersion** | **String**| The API version. | |

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
| **204** | No Content |  -  |

<a id="integrationAccountAssembliesGet"></a>
# **integrationAccountAssembliesGet**
> AssemblyDefinition integrationAccountAssembliesGet(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion)



Get an assembly for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAssembliesApi apiInstance = new IntegrationAccountAssembliesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      AssemblyDefinition result = apiInstance.integrationAccountAssembliesGet(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAssembliesApi#integrationAccountAssembliesGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **assemblyArtifactName** | **String**| The assembly artifact name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**AssemblyDefinition**](AssemblyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="integrationAccountAssembliesList"></a>
# **integrationAccountAssembliesList**
> AssemblyCollection integrationAccountAssembliesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



List the assemblies for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAssembliesApi apiInstance = new IntegrationAccountAssembliesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      AssemblyCollection result = apiInstance.integrationAccountAssembliesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAssembliesApi#integrationAccountAssembliesList");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**AssemblyCollection**](AssemblyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="integrationAccountAssembliesListContentCallbackUrl"></a>
# **integrationAccountAssembliesListContentCallbackUrl**
> WorkflowTriggerCallbackUrl integrationAccountAssembliesListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion)



Get the content callback url for an integration account assembly.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAssembliesApi apiInstance = new IntegrationAccountAssembliesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowTriggerCallbackUrl result = apiInstance.integrationAccountAssembliesListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAssembliesApi#integrationAccountAssembliesListContentCallbackUrl");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **assemblyArtifactName** | **String**| The assembly artifact name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

