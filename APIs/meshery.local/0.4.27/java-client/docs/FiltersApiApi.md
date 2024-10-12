# FiltersApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteMesheryFilter**](FiltersApiApi.md#idDeleteMesheryFilter) | **DELETE** /api/filter/{id} | Handle Delete for a Meshery Filter |
| [**idGetFilterFile**](FiltersApiApi.md#idGetFilterFile) | **GET** /api/filter | Handle GET request for all filters |
| [**idGetFilterFiles**](FiltersApiApi.md#idGetFilterFiles) | **GET** /api/filter/file/{id} | Handle GET request for filter file with given id |
| [**idGetMesheryFilter**](FiltersApiApi.md#idGetMesheryFilter) | **GET** /api/filter/{id} | Handle GET request for a Meshery Filter |
| [**idPostFilterFile**](FiltersApiApi.md#idPostFilterFile) | **POST** /api/filter | Handle POST requests for Meshery Filters |


<a id="idDeleteMesheryFilter"></a>
# **idDeleteMesheryFilter**
> idDeleteMesheryFilter(id)

Handle Delete for a Meshery Filter

Deletes a meshery filter with ID: id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    FiltersApiApi apiInstance = new FiltersApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      apiInstance.idDeleteMesheryFilter(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApiApi#idDeleteMesheryFilter");
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

<a id="idGetFilterFile"></a>
# **idGetFilterFile**
> FiltersAPIResponse idGetFilterFile()

Handle GET request for all filters

Returns all the Meshery Filters saved by the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    FiltersApiApi apiInstance = new FiltersApiApi(defaultClient);
    try {
      FiltersAPIResponse result = apiInstance.idGetFilterFile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApiApi#idGetFilterFile");
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

[**FiltersAPIResponse**](FiltersAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all meshery filters |  -  |

<a id="idGetFilterFiles"></a>
# **idGetFilterFiles**
> MesheryFilter idGetFilterFiles(id)

Handle GET request for filter file with given id

Returns the Meshery Filter file saved by the current user with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    FiltersApiApi apiInstance = new FiltersApiApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    try {
      MesheryFilter result = apiInstance.idGetFilterFiles(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApiApi#idGetFilterFiles");
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
| **id** | **String**| Automatically added | |

### Return type

[**MesheryFilter**](MesheryFilter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single meshery filter |  -  |

<a id="idGetMesheryFilter"></a>
# **idGetMesheryFilter**
> MesheryFilter idGetMesheryFilter(id)

Handle GET request for a Meshery Filter

Fetches the Meshery Filter with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    FiltersApiApi apiInstance = new FiltersApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      MesheryFilter result = apiInstance.idGetMesheryFilter(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApiApi#idGetMesheryFilter");
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

[**MesheryFilter**](MesheryFilter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single meshery filter |  -  |

<a id="idPostFilterFile"></a>
# **idPostFilterFile**
> MesheryFilter idPostFilterFile()

Handle POST requests for Meshery Filters

Used to save/update a Meshery Filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    FiltersApiApi apiInstance = new FiltersApiApi(defaultClient);
    try {
      MesheryFilter result = apiInstance.idPostFilterFile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApiApi#idPostFilterFile");
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

[**MesheryFilter**](MesheryFilter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single meshery filter |  -  |

