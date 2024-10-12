# PatternsApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteDeployPattern**](PatternsApiApi.md#idDeleteDeployPattern) | **DELETE** /api/pattern/deploy | Handle DELETE request for Pattern Deploy |
| [**idDeleteMesheryPattern**](PatternsApiApi.md#idDeleteMesheryPattern) | **DELETE** /api/pattern/{id} | Handle Delete for a Meshery Pattern |
| [**idGETOAMMesheryPattern**](PatternsApiApi.md#idGETOAMMesheryPattern) | **GET** /api/oam/{type} | Handles the get requests for the OAM objects |
| [**idGetMesheryPattern**](PatternsApiApi.md#idGetMesheryPattern) | **GET** /api/pattern/{id} | Handle GET for a Meshery Pattern |
| [**idGetPatternFiles**](PatternsApiApi.md#idGetPatternFiles) | **GET** /api/pattern | Handle GET request for patterns |
| [**idPOSTOAMMesheryPattern**](PatternsApiApi.md#idPOSTOAMMesheryPattern) | **POST** /api/oam/{type} | Handles registering OMA objects |
| [**idPostDeployPattern**](PatternsApiApi.md#idPostDeployPattern) | **POST** /api/pattern/deploy | Handle POST request for Pattern Deploy |
| [**idPostPatternFile**](PatternsApiApi.md#idPostPatternFile) | **POST** /api/pattern | Handle POST requests for patterns |


<a id="idDeleteDeployPattern"></a>
# **idDeleteDeployPattern**
> idDeleteDeployPattern()

Handle DELETE request for Pattern Deploy

Delete a deployed pattern with the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    try {
      apiInstance.idDeleteDeployPattern();
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idDeleteDeployPattern");
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

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idDeleteMesheryPattern"></a>
# **idDeleteMesheryPattern**
> idDeleteMesheryPattern(id)

Handle Delete for a Meshery Pattern

Deletes a meshery pattern with ID: id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      apiInstance.idDeleteMesheryPattern(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idDeleteMesheryPattern");
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
| **id** | **UUID**| id for a specific | |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGETOAMMesheryPattern"></a>
# **idGETOAMMesheryPattern**
> idGETOAMMesheryPattern(type)

Handles the get requests for the OAM objects

Getting list of workloads/traits/scopes  {type} being of either trait, scope, workload; registration of adapter capabilities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    String type = "type_example"; // String | Automatically added
    try {
      apiInstance.idGETOAMMesheryPattern(type);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idGETOAMMesheryPattern");
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
| **type** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetMesheryPattern"></a>
# **idGetMesheryPattern**
> MesheryPattern idGetMesheryPattern(id)

Handle GET for a Meshery Pattern

Fetches the pattern with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      MesheryPattern result = apiInstance.idGetMesheryPattern(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idGetMesheryPattern");
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
| **id** | **UUID**| id for a specific | |

### Return type

[**MesheryPattern**](MesheryPattern.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single meshery pattern |  -  |

<a id="idGetPatternFiles"></a>
# **idGetPatternFiles**
> PatternsAPIResponse idGetPatternFiles()

Handle GET request for patterns

Returns the list of all the patterns saved by the current user This will return all the patterns with their details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    try {
      PatternsAPIResponse result = apiInstance.idGetPatternFiles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idGetPatternFiles");
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

[**PatternsAPIResponse**](PatternsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all meshery patterns |  -  |

<a id="idPOSTOAMMesheryPattern"></a>
# **idPOSTOAMMesheryPattern**
> idPOSTOAMMesheryPattern(type)

Handles registering OMA objects

Adding a workload/trait/scope  {type} being of either trait, scope, workload; registration of adapter capabilities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    String type = "type_example"; // String | Automatically added
    try {
      apiInstance.idPOSTOAMMesheryPattern(type);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idPOSTOAMMesheryPattern");
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
| **type** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idPostDeployPattern"></a>
# **idPostDeployPattern**
> idPostDeployPattern(uploadYamlYmlFile)

Handle POST request for Pattern Deploy

Deploy an attached pattern with the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    File uploadYamlYmlFile = new File("/path/to/file"); // File | 
    try {
      apiInstance.idPostDeployPattern(uploadYamlYmlFile);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idPostDeployPattern");
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
| **uploadYamlYmlFile** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idPostPatternFile"></a>
# **idPostPatternFile**
> MesheryPattern idPostPatternFile()

Handle POST requests for patterns

Edit/update a meshery pattern

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PatternsApiApi apiInstance = new PatternsApiApi(defaultClient);
    try {
      MesheryPattern result = apiInstance.idPostPatternFile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApiApi#idPostPatternFile");
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

[**MesheryPattern**](MesheryPattern.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single meshery pattern |  -  |

