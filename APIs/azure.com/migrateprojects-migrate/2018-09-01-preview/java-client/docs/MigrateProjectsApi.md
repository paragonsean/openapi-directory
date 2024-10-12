# MigrateProjectsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**migrateProjectsDeleteMigrateProject**](MigrateProjectsApi.md#migrateProjectsDeleteMigrateProject) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Delete the migrate project |
| [**migrateProjectsGetMigrateProject**](MigrateProjectsApi.md#migrateProjectsGetMigrateProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Method to get a migrate project. |
| [**migrateProjectsPatchMigrateProject**](MigrateProjectsApi.md#migrateProjectsPatchMigrateProject) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Update migrate project. |
| [**migrateProjectsPutMigrateProject**](MigrateProjectsApi.md#migrateProjectsPutMigrateProject) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName} | Method to create or update a migrate project. |
| [**migrateProjectsRefreshMigrateProjectSummary**](MigrateProjectsApi.md#migrateProjectsRefreshMigrateProjectSummary) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/refreshSummary | Refresh the summary of the migrate project. |
| [**migrateProjectsRegisterTool**](MigrateProjectsApi.md#migrateProjectsRegisterTool) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/registerTool | Registers a tool with the migrate project. |


<a id="migrateProjectsDeleteMigrateProject"></a>
# **migrateProjectsDeleteMigrateProject**
> migrateProjectsDeleteMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, acceptLanguage)

Delete the migrate project

Delete the migrate project. Deleting non-existent project is a no-operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrateProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrateProjectsApi apiInstance = new MigrateProjectsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.migrateProjectsDeleteMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrateProjectsApi#migrateProjectsDeleteMigrateProject");
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

<a id="migrateProjectsGetMigrateProject"></a>
# **migrateProjectsGetMigrateProject**
> MigrateProject migrateProjectsGetMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion)

Method to get a migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrateProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrateProjectsApi apiInstance = new MigrateProjectsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    try {
      MigrateProject result = apiInstance.migrateProjectsGetMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrateProjectsApi#migrateProjectsGetMigrateProject");
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

[**MigrateProject**](MigrateProject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="migrateProjectsPatchMigrateProject"></a>
# **migrateProjectsPatchMigrateProject**
> MigrateProject migrateProjectsPatchMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, acceptLanguage)

Update migrate project.

Update a migrate project with specified name. Supports partial updates, for example only tags can be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrateProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrateProjectsApi apiInstance = new MigrateProjectsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    MigrateProject body = new MigrateProject(); // MigrateProject | Body with migrate project details.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      MigrateProject result = apiInstance.migrateProjectsPatchMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrateProjectsApi#migrateProjectsPatchMigrateProject");
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
| **body** | [**MigrateProject**](MigrateProject.md)| Body with migrate project details. | |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**MigrateProject**](MigrateProject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="migrateProjectsPutMigrateProject"></a>
# **migrateProjectsPutMigrateProject**
> MigrateProject migrateProjectsPutMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, acceptLanguage)

Method to create or update a migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrateProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrateProjectsApi apiInstance = new MigrateProjectsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    MigrateProject body = new MigrateProject(); // MigrateProject | Body with migrate project details.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      MigrateProject result = apiInstance.migrateProjectsPutMigrateProject(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, body, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrateProjectsApi#migrateProjectsPutMigrateProject");
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
| **body** | [**MigrateProject**](MigrateProject.md)| Body with migrate project details. | |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**MigrateProject**](MigrateProject.md)

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

<a id="migrateProjectsRefreshMigrateProjectSummary"></a>
# **migrateProjectsRefreshMigrateProjectSummary**
> RefreshSummaryResult migrateProjectsRefreshMigrateProjectSummary(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input)

Refresh the summary of the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrateProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrateProjectsApi apiInstance = new MigrateProjectsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    RefreshSummaryInput input = new RefreshSummaryInput(); // RefreshSummaryInput | The goal input which needs to be refreshed.
    try {
      RefreshSummaryResult result = apiInstance.migrateProjectsRefreshMigrateProjectSummary(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrateProjectsApi#migrateProjectsRefreshMigrateProjectSummary");
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
| **input** | [**RefreshSummaryInput**](RefreshSummaryInput.md)| The goal input which needs to be refreshed. | |

### Return type

[**RefreshSummaryResult**](RefreshSummaryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="migrateProjectsRegisterTool"></a>
# **migrateProjectsRegisterTool**
> RegistrationResult migrateProjectsRegisterTool(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input, acceptLanguage)

Registers a tool with the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrateProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrateProjectsApi apiInstance = new MigrateProjectsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    RegisterToolInput input = new RegisterToolInput(); // RegisterToolInput | Input containing the name of the tool to be registered.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      RegistrationResult result = apiInstance.migrateProjectsRegisterTool(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, input, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrateProjectsApi#migrateProjectsRegisterTool");
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
| **input** | [**RegisterToolInput**](RegisterToolInput.md)| Input containing the name of the tool to be registered. | |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**RegistrationResult**](RegistrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

