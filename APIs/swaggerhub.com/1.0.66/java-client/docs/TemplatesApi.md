# TemplatesApi

All URIs are relative to *https://api.swaggerhub.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteTemplate**](TemplatesApi.md#deleteTemplate) | **DELETE** /templates/{owner}/{templateId} | Delete a template |
| [**deleteTemplateVersion**](TemplatesApi.md#deleteTemplateVersion) | **DELETE** /templates/{owner}/{templateId}/{version} | Delete a particular version of a template |
| [**forkTemplate**](TemplatesApi.md#forkTemplate) | **POST** /templates/{owner}/{templateId}/{version}/fork | Create a fork for a template |
| [**getTemplateComments**](TemplatesApi.md#getTemplateComments) | **GET** /templates/{owner}/{templateId}/{version}/comments | Return the list of comments for a template |
| [**getTemplateDefinition**](TemplatesApi.md#getTemplateDefinition) | **GET** /templates/{owner}/{templateId}/{version} | Retrieve a template definition |
| [**getTemplateLifecycleSettings**](TemplatesApi.md#getTemplateLifecycleSettings) | **GET** /templates/{owner}/{templateId}/{version}/settings/lifecycle | Retrieve lifecycle settings for a template |
| [**getTemplatePrivateSettings**](TemplatesApi.md#getTemplatePrivateSettings) | **GET** /templates/{owner}/{templateId}/{version}/settings/private | Retrieve visibility settings for a template |
| [**getTemplateVersions**](TemplatesApi.md#getTemplateVersions) | **GET** /templates/{owner}/{templateId} | Retrieve an APIs.json listing for all template versions for an owner and template |
| [**getTemplates**](TemplatesApi.md#getTemplates) | **GET** /templates | Retrieve a list of templates for an owner |
| [**renameTemplate**](TemplatesApi.md#renameTemplate) | **POST** /templates/{owner}/{templateId}/rename | Rename a template |
| [**saveTemplateDefinition**](TemplatesApi.md#saveTemplateDefinition) | **POST** /templates/{owner}/{templateId} | Create or update a template |
| [**searchApisAndDomains_1**](TemplatesApi.md#searchApisAndDomains_1) | **GET** /specs | Retrieve a list of currently defined APIs, domains, and templates in APIs.json format |
| [**setTemplateLifecycleSettings**](TemplatesApi.md#setTemplateLifecycleSettings) | **PUT** /templates/{owner}/{templateId}/{version}/settings/lifecycle | Update lifecycle settings for a template |
| [**setTemplatePrivateSettings**](TemplatesApi.md#setTemplatePrivateSettings) | **PUT** /templates/{owner}/{templateId}/{version}/settings/private | Update visibility settings for a template |
| [**updateTemplateComments**](TemplatesApi.md#updateTemplateComments) | **POST** /templates/{owner}/{templateId}/{version}/comments/batch | Update the list of comments for a template |


<a id="deleteTemplate"></a>
# **deleteTemplate**
> deleteTemplate(owner, templateId)

Delete a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    try {
      apiInstance.deleteTemplate(owner, templateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#deleteTemplate");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Template successfully deleted |  -  |
| **403** | Access denied |  -  |
| **409** | Template has published versions, and cannot be deleted |  -  |

<a id="deleteTemplateVersion"></a>
# **deleteTemplateVersion**
> deleteTemplateVersion(owner, templateId, version)

Delete a particular version of a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    try {
      apiInstance.deleteTemplateVersion(owner, templateId, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#deleteTemplateVersion");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Template version successfully deleted |  -  |
| **403** | Access denied |  -  |
| **409** | Selected template version is either published or the only version, and cannot be deleted |  -  |

<a id="forkTemplate"></a>
# **forkTemplate**
> forkTemplate(owner, templateId, version, body)

Create a fork for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    ForkVersion body = new ForkVersion(); // ForkVersion | Fork version information
    try {
      apiInstance.forkTemplate(owner, templateId, version, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#forkTemplate");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |
| **body** | [**ForkVersion**](ForkVersion.md)| Fork version information | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Template fork successfully created |  -  |
| **400** | Request body invalid |  -  |
| **403** | Access denied |  -  |
| **409** | Conflict with existing template |  -  |

<a id="getTemplateComments"></a>
# **getTemplateComments**
> List&lt;ClosableComment&gt; getTemplateComments(owner, templateId, version)

Return the list of comments for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    try {
      List<ClosableComment> result = apiInstance.getTemplateComments(owner, templateId, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateComments");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |

### Return type

[**List&lt;ClosableComment&gt;**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments for the template |  -  |
| **204** | No comments found for the template |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | Template not found |  -  |

<a id="getTemplateDefinition"></a>
# **getTemplateDefinition**
> Object getTemplateDefinition(owner, templateId, version, flatten)

Retrieve a template definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    Boolean flatten = false; // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    try {
      Object result = apiInstance.getTemplateDefinition(owner, templateId, version, flatten);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateDefinition");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |
| **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false] |

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The template in requested format (YAML or JSON) |  -  |
| **404** | Template not found |  -  |

<a id="getTemplateLifecycleSettings"></a>
# **getTemplateLifecycleSettings**
> LifecycleSettings getTemplateLifecycleSettings(owner, templateId, version)

Retrieve lifecycle settings for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    try {
      LifecycleSettings result = apiInstance.getTemplateLifecycleSettings(owner, templateId, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateLifecycleSettings");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |

### Return type

[**LifecycleSettings**](LifecycleSettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lifecycle settings for the specified template |  -  |
| **404** | Template not found |  -  |

<a id="getTemplatePrivateSettings"></a>
# **getTemplatePrivateSettings**
> VisibilitySettings getTemplatePrivateSettings(owner, templateId, version)

Retrieve visibility settings for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    try {
      VisibilitySettings result = apiInstance.getTemplatePrivateSettings(owner, templateId, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplatePrivateSettings");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |

### Return type

[**VisibilitySettings**](VisibilitySettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visibility settings for the template |  -  |
| **404** | Template not found |  -  |

<a id="getTemplateVersions"></a>
# **getTemplateVersions**
> ApisJson getTemplateVersions(owner, templateId)

Retrieve an APIs.json listing for all template versions for an owner and template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    try {
      ApisJson result = apiInstance.getTemplateVersions(owner, templateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateVersions");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of template versions in APIs.json format |  -  |
| **404** | Template not found |  -  |

<a id="getTemplates"></a>
# **getTemplates**
> TemplateWrapper getTemplates(owner)

Retrieve a list of templates for an owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | Owner name
    try {
      TemplateWrapper result = apiInstance.getTemplates(owner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplates");
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
| **owner** | **String**| Owner name | [optional] |

### Return type

[**TemplateWrapper**](TemplateWrapper.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template wrapper |  -  |

<a id="renameTemplate"></a>
# **renameTemplate**
> renameTemplate(owner, templateId, newName)

Rename a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String newName = "newName_example"; // String | New name
    try {
      apiInstance.renameTemplate(owner, templateId, newName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#renameTemplate");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **newName** | **String**| New name | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template successfully renamed |  -  |
| **400** | Invalid request |  -  |
| **403** | Access denied |  -  |
| **409** | API, domain, and template with the new name already exist |  -  |

<a id="saveTemplateDefinition"></a>
# **saveTemplateDefinition**
> saveTemplateDefinition(owner, templateId, body, isPrivate, version, force, projectName)

Create or update a template

Saves the provided template definition; the owner must match the token owner. The version will be extracted from the template definitions itself.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String body = "body_example"; // String | The template definition
    Boolean isPrivate = false; // Boolean | Defines whether the API or template has to be private
    String version = "version_example"; // String | Template version to create or update. If omitted, the version will be taken from the `info.version` field in the definition.
    Boolean force = true; // Boolean | Force update
    String projectName = "projectName_example"; // String | The project to add the API, domain, or template to
    try {
      apiInstance.saveTemplateDefinition(owner, templateId, body, isPrivate, version, force, projectName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#saveTemplateDefinition");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **body** | **String**| The template definition | |
| **isPrivate** | **Boolean**| Defines whether the API or template has to be private | [optional] [default to false] |
| **version** | **String**| Template version to create or update. If omitted, the version will be taken from the &#x60;info.version&#x60; field in the definition. | [optional] |
| **force** | **Boolean**| Force update | [optional] |
| **projectName** | **String**| The project to add the API, domain, or template to | [optional] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template successfully saved |  -  |
| **201** | New template successfully saved |  -  |
| **205** | Template successfully saved, and should be reloaded |  -  |
| **400** | Template definition invalid |  -  |
| **403** | Access denied |  -  |
| **409** | Cannot overwrite a template version |  -  |
| **415** | Invalid content type |  -  |

<a id="searchApisAndDomains_1"></a>
# **searchApisAndDomains_1**
> ApisJson searchApisAndDomains_1(specType, visibility, state, owner, query, page, limit, sort, order)

Retrieve a list of currently defined APIs, domains, and templates in APIs.json format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String specType = "API"; // String | Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates 
    String visibility = "PUBLIC"; // String | The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE 
    String state = "ALL"; // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
    String owner = "owner_example"; // String | API or domain owner. Can be username or organization name. Case-sensitive.
    String query = "query_example"; // String | Free text query to match
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
    String order = "ASC"; // String | Sort order
    try {
      ApisJson result = apiInstance.searchApisAndDomains_1(specType, visibility, state, owner, query, page, limit, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#searchApisAndDomains_1");
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
| **specType** | **String**| Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates  | [optional] [default to ANY] [enum: API, DOMAIN, TEMPLATE, ANY] |
| **visibility** | **String**| The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE  | [optional] [default to ANY] [enum: PUBLIC, PRIVATE, ANY] |
| **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to ALL] [enum: ALL, PUBLISHED, UNPUBLISHED] |
| **owner** | **String**| API or domain owner. Can be username or organization name. Case-sensitive. | [optional] |
| **query** | **String**| Free text query to match | [optional] |
| **page** | **Integer**| Page to return | [optional] [default to 0] |
| **limit** | **Integer**| Number of results per page (1 .. 100) | [optional] [default to 10] |
| **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to NAME] [enum: NAME, UPDATED, CREATED, OWNER, BEST_MATCH, TITLE] |
| **order** | **String**| Sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of APIs, domains, and templates in APIs.json format |  -  |

<a id="setTemplateLifecycleSettings"></a>
# **setTemplateLifecycleSettings**
> setTemplateLifecycleSettings(owner, templateId, version, body, force)

Update lifecycle settings for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    LifecycleSettings body = new LifecycleSettings(); // LifecycleSettings | Fork version information
    Boolean force = true; // Boolean | Force update
    try {
      apiInstance.setTemplateLifecycleSettings(owner, templateId, version, body, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#setTemplateLifecycleSettings");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |
| **body** | [**LifecycleSettings**](LifecycleSettings.md)| Fork version information | |
| **force** | **Boolean**| Force update | [optional] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lifecycle settings successfully stored |  -  |
| **400** | Request body invalid |  -  |
| **403** | Access denied |  -  |
| **404** | Template not found |  -  |

<a id="setTemplatePrivateSettings"></a>
# **setTemplatePrivateSettings**
> setTemplatePrivateSettings(owner, templateId, version, body)

Update visibility settings for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    VisibilitySettings body = new VisibilitySettings(); // VisibilitySettings | Private settings
    try {
      apiInstance.setTemplatePrivateSettings(owner, templateId, version, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#setTemplatePrivateSettings");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |
| **body** | [**VisibilitySettings**](VisibilitySettings.md)| Private settings | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visibility setting updated |  -  |
| **400** | Request body invalid |  -  |
| **403** | Access denied |  -  |
| **404** | Template not found |  -  |

<a id="updateTemplateComments"></a>
# **updateTemplateComments**
> updateTemplateComments(owner, templateId, version, body)

Update the list of comments for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String owner = "owner_example"; // String | API, domain, or template owner identifier (case-sensitive)
    String templateId = "templateId_example"; // String | Template identifier
    String version = "version_example"; // String | Version identifier
    CommentsBatch body = new CommentsBatch(); // CommentsBatch | 
    try {
      apiInstance.updateTemplateComments(owner, templateId, version, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#updateTemplateComments");
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
| **owner** | **String**| API, domain, or template owner identifier (case-sensitive) | |
| **templateId** | **String**| Template identifier | |
| **version** | **String**| Version identifier | |
| **body** | [**CommentsBatch**](CommentsBatch.md)|  | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments successfully updated |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | Template, comment, or reply not found |  -  |

