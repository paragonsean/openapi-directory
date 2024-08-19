# TechniquesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTechnique**](TechniquesApi.md#createTechnique) | **PUT** /techniques | Create technique |
| [**deleteTechnique**](TechniquesApi.md#deleteTechnique) | **DELETE** /techniques/{techniqueId}/{techniqueVersion} | Delete technique |
| [**getTechniqueAllVersion**](TechniquesApi.md#getTechniqueAllVersion) | **GET** /techniques/{techniqueId} | Technique metadata by ID |
| [**getTechniqueAllVersionId**](TechniquesApi.md#getTechniqueAllVersionId) | **GET** /techniques/{techniqueId}/{techniqueVersion} | Technique metadata by version and ID |
| [**getTechniquesResources**](TechniquesApi.md#getTechniquesResources) | **GET** /techniques/{techniqueId}/{techniqueVersion}/resources | Technique&#39;s resources |
| [**listTechniqueVersionDirectives**](TechniquesApi.md#listTechniqueVersionDirectives) | **GET** /techniques/{techniqueId}/{techniqueVersion}/directives | List all directives based on a version of a technique |
| [**listTechniques**](TechniquesApi.md#listTechniques) | **GET** /techniques | List all techniques |
| [**listTechniquesDirectives**](TechniquesApi.md#listTechniquesDirectives) | **GET** /techniques/{techniqueId}/directives | List all directives based on a technique |
| [**listTechniquesVersions**](TechniquesApi.md#listTechniquesVersions) | **GET** /techniques/versions | List versions |
| [**methods**](TechniquesApi.md#methods) | **GET** /methods | List methods |
| [**reloadMethods**](TechniquesApi.md#reloadMethods) | **POST** /methods/reload | Reload methods |
| [**techniqueCategories**](TechniquesApi.md#techniqueCategories) | **GET** /techniques/categories | List categories |
| [**techniqueRevisions**](TechniquesApi.md#techniqueRevisions) | **GET** /techniques/{techniqueId}/{techniqueVersion}/revisions | Technique&#39;s revisions |
| [**techniques**](TechniquesApi.md#techniques) | **POST** /techniques/reload | Reload techniques |
| [**updateTechnique**](TechniquesApi.md#updateTechnique) | **POST** /techniques/{techniqueId}/{techniqueVersion} | Update technique |


<a id="createTechnique"></a>
# **createTechnique**
> CreateTechnique200Response createTechnique(editorTechnique)

Create technique

Create a new technique in Rudder from a technique in the technique editor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    List<EditorTechnique> editorTechnique = Arrays.asList(); // List<EditorTechnique> | 
    try {
      CreateTechnique200Response result = apiInstance.createTechnique(editorTechnique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#createTechnique");
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
| **editorTechnique** | [**List&lt;EditorTechnique&gt;**](EditorTechnique.md)|  | |

### Return type

[**CreateTechnique200Response**](CreateTechnique200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Versions information |  -  |

<a id="deleteTechnique"></a>
# **deleteTechnique**
> DeleteTechnique200Response deleteTechnique(techniqueId, techniqueVersion)

Delete technique

Delete a technique from technique editor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    String techniqueVersion = "6.0"; // String | Technique version
    try {
      DeleteTechnique200Response result = apiInstance.deleteTechnique(techniqueId, techniqueVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#deleteTechnique");
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
| **techniqueId** | **String**| Technique ID | |
| **techniqueVersion** | **String**| Technique version | |

### Return type

[**DeleteTechnique200Response**](DeleteTechnique200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletion information |  -  |

<a id="getTechniqueAllVersion"></a>
# **getTechniqueAllVersion**
> GetTechniqueAllVersion200Response getTechniqueAllVersion(techniqueId)

Technique metadata by ID

Get each Technique&#39;s versions with their metadata by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    try {
      GetTechniqueAllVersion200Response result = apiInstance.getTechniqueAllVersion(techniqueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#getTechniqueAllVersion");
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
| **techniqueId** | **String**| Technique ID | |

### Return type

[**GetTechniqueAllVersion200Response**](GetTechniqueAllVersion200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Techniques information |  -  |

<a id="getTechniqueAllVersionId"></a>
# **getTechniqueAllVersionId**
> GetTechniqueAllVersion200Response getTechniqueAllVersionId(techniqueId, techniqueVersion)

Technique metadata by version and ID

Get Technique metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    String techniqueVersion = "6.0"; // String | Technique version
    try {
      GetTechniqueAllVersion200Response result = apiInstance.getTechniqueAllVersionId(techniqueId, techniqueVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#getTechniqueAllVersionId");
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
| **techniqueId** | **String**| Technique ID | |
| **techniqueVersion** | **String**| Technique version | |

### Return type

[**GetTechniqueAllVersion200Response**](GetTechniqueAllVersion200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Techniques information |  -  |

<a id="getTechniquesResources"></a>
# **getTechniquesResources**
> GetTechniquesResources200Response getTechniquesResources(techniqueId, techniqueVersion)

Technique&#39;s resources

Get currently deployed resources of a technique

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    String techniqueVersion = "6.0"; // String | Technique version
    try {
      GetTechniquesResources200Response result = apiInstance.getTechniquesResources(techniqueId, techniqueVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#getTechniquesResources");
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
| **techniqueId** | **String**| Technique ID | |
| **techniqueVersion** | **String**| Technique version | |

### Return type

[**GetTechniquesResources200Response**](GetTechniquesResources200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resources information |  -  |

<a id="listTechniqueVersionDirectives"></a>
# **listTechniqueVersionDirectives**
> ListTechniqueVersionDirectives200Response listTechniqueVersionDirectives(techniqueId, techniqueVersion)

List all directives based on a version of a technique

List all directives based on a version of a technique

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    String techniqueVersion = "6.0"; // String | Technique version
    try {
      ListTechniqueVersionDirectives200Response result = apiInstance.listTechniqueVersionDirectives(techniqueId, techniqueVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#listTechniqueVersionDirectives");
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
| **techniqueId** | **String**| Technique ID | |
| **techniqueVersion** | **String**| Technique version | |

### Return type

[**ListTechniqueVersionDirectives200Response**](ListTechniqueVersionDirectives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Techniques information |  -  |

<a id="listTechniques"></a>
# **listTechniques**
> ListTechniques200Response listTechniques()

List all techniques

List all technique with their versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    try {
      ListTechniques200Response result = apiInstance.listTechniques();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#listTechniques");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListTechniques200Response**](ListTechniques200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Techniques information |  -  |

<a id="listTechniquesDirectives"></a>
# **listTechniquesDirectives**
> ListTechniquesDirectives200Response listTechniquesDirectives(techniqueId)

List all directives based on a technique

List all directives based on all version of a technique

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    try {
      ListTechniquesDirectives200Response result = apiInstance.listTechniquesDirectives(techniqueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#listTechniquesDirectives");
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
| **techniqueId** | **String**| Technique ID | |

### Return type

[**ListTechniquesDirectives200Response**](ListTechniquesDirectives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Techniques information |  -  |

<a id="listTechniquesVersions"></a>
# **listTechniquesVersions**
> ListTechniquesVersions200Response listTechniquesVersions()

List versions

List all techniques version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    try {
      ListTechniquesVersions200Response result = apiInstance.listTechniquesVersions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#listTechniquesVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListTechniquesVersions200Response**](ListTechniquesVersions200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Versions information |  -  |

<a id="methods"></a>
# **methods**
> Methods200Response methods()

List methods

Get all generic methods metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    try {
      Methods200Response result = apiInstance.methods();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#methods");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Methods200Response**](Methods200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Methods information |  -  |

<a id="reloadMethods"></a>
# **reloadMethods**
> Methods200Response reloadMethods()

Reload methods

Reload methods metadata from file system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    try {
      Methods200Response result = apiInstance.reloadMethods();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#reloadMethods");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Methods200Response**](Methods200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Methods information |  -  |

<a id="techniqueCategories"></a>
# **techniqueCategories**
> TechniqueCategories200Response techniqueCategories()

List categories

Get all technique categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    try {
      TechniqueCategories200Response result = apiInstance.techniqueCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#techniqueCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TechniqueCategories200Response**](TechniqueCategories200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Categories information |  -  |

<a id="techniqueRevisions"></a>
# **techniqueRevisions**
> TechniqueRevisions200Response techniqueRevisions(techniqueId, techniqueVersion)

Technique&#39;s revisions

Get revisions for given technique

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    String techniqueVersion = "6.0"; // String | Technique version
    try {
      TechniqueRevisions200Response result = apiInstance.techniqueRevisions(techniqueId, techniqueVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#techniqueRevisions");
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
| **techniqueId** | **String**| Technique ID | |
| **techniqueVersion** | **String**| Technique version | |

### Return type

[**TechniqueRevisions200Response**](TechniqueRevisions200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Versions information |  -  |

<a id="techniques"></a>
# **techniques**
> ListTechniques200Response techniques()

Reload techniques

Reload all techniques metadata from file system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    try {
      ListTechniques200Response result = apiInstance.techniques();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#techniques");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListTechniques200Response**](ListTechniques200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Techniques information |  -  |

<a id="updateTechnique"></a>
# **updateTechnique**
> CreateTechnique200Response updateTechnique(techniqueId, techniqueVersion, editorTechnique)

Update technique

Update technique created with technique editor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TechniquesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    TechniquesApi apiInstance = new TechniquesApi(defaultClient);
    String techniqueId = "userManagement"; // String | Technique ID
    String techniqueVersion = "6.0"; // String | Technique version
    List<EditorTechnique> editorTechnique = Arrays.asList(); // List<EditorTechnique> | 
    try {
      CreateTechnique200Response result = apiInstance.updateTechnique(techniqueId, techniqueVersion, editorTechnique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TechniquesApi#updateTechnique");
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
| **techniqueId** | **String**| Technique ID | |
| **techniqueVersion** | **String**| Technique version | |
| **editorTechnique** | [**List&lt;EditorTechnique&gt;**](EditorTechnique.md)|  | |

### Return type

[**CreateTechnique200Response**](CreateTechnique200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Versions information |  -  |

