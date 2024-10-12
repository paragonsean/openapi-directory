# PerformanceApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeletePerformanceProfile**](PerformanceApiApi.md#idDeletePerformanceProfile) | **DELETE** /api/user/performance/profiles/{id} | Handle Delete requests for performance profiles |
| [**idGETProfileResults**](PerformanceApiApi.md#idGETProfileResults) | **GET** /api/user/performance/profiles/{id}/results | Handle GET request for results of a profile |
| [**idGetAllPerformanceResults**](PerformanceApiApi.md#idGetAllPerformanceResults) | **GET** /api/user/performance/profiles/results | Handles GET requests for performance results |
| [**idGetPerformanceProfiles**](PerformanceApiApi.md#idGetPerformanceProfiles) | **GET** /api/user/performance/profiles | Handle GET requests for performance profiles |
| [**idGetSinglePerformanceProfile**](PerformanceApiApi.md#idGetSinglePerformanceProfile) | **GET** /api/user/performance/profiles/{id} | Handle GET requests for performance results of a profile |
| [**idRunPerformanceTest**](PerformanceApiApi.md#idRunPerformanceTest) | **GET** /api/user/performance/profiles/{id}/run | Handle GET request to run a performance test |
| [**idSavePerformanceProfile**](PerformanceApiApi.md#idSavePerformanceProfile) | **POST** /api/user/performance/profiles | Handle POST requests for saving performance profile |


<a id="idDeletePerformanceProfile"></a>
# **idDeletePerformanceProfile**
> idDeletePerformanceProfile(id)

Handle Delete requests for performance profiles

Deletes a performance profile with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      apiInstance.idDeletePerformanceProfile(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idDeletePerformanceProfile");
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

<a id="idGETProfileResults"></a>
# **idGETProfileResults**
> PerformanceResultsAPIResponse idGETProfileResults(id)

Handle GET request for results of a profile

Fetchs pages of results from Remote Provider for the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      PerformanceResultsAPIResponse result = apiInstance.idGETProfileResults(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idGETProfileResults");
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

[**PerformanceResultsAPIResponse**](PerformanceResultsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all performance results |  -  |

<a id="idGetAllPerformanceResults"></a>
# **idGetAllPerformanceResults**
> PerformanceResultsAPIResponse idGetAllPerformanceResults()

Handles GET requests for performance results

Returns pages of all the performance results from Remote Provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    try {
      PerformanceResultsAPIResponse result = apiInstance.idGetAllPerformanceResults();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idGetAllPerformanceResults");
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

[**PerformanceResultsAPIResponse**](PerformanceResultsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all performance results |  -  |

<a id="idGetPerformanceProfiles"></a>
# **idGetPerformanceProfiles**
> PerformanceProfilesAPIResponse idGetPerformanceProfiles()

Handle GET requests for performance profiles

Returns the list of all the performance profiles saved by the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    try {
      PerformanceProfilesAPIResponse result = apiInstance.idGetPerformanceProfiles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idGetPerformanceProfiles");
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

[**PerformanceProfilesAPIResponse**](PerformanceProfilesAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all the performance profiles |  -  |

<a id="idGetSinglePerformanceProfile"></a>
# **idGetSinglePerformanceProfile**
> PerformanceProfile idGetSinglePerformanceProfile(id)

Handle GET requests for performance results of a profile

Returns single performance profile with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      PerformanceProfile result = apiInstance.idGetSinglePerformanceProfile(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idGetSinglePerformanceProfile");
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

[**PerformanceProfile**](PerformanceProfile.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single performance profile |  -  |

<a id="idRunPerformanceTest"></a>
# **idRunPerformanceTest**
> idRunPerformanceTest(id)

Handle GET request to run a performance test

Runs the load test with the given parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    try {
      apiInstance.idRunPerformanceTest(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idRunPerformanceTest");
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

<a id="idSavePerformanceProfile"></a>
# **idSavePerformanceProfile**
> PerformanceProfile idSavePerformanceProfile(performanceProfileParameters)

Handle POST requests for saving performance profile

Save performance profile using the current provider&#39;s persistence mechanism

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerformanceApiApi apiInstance = new PerformanceApiApi(defaultClient);
    PerformanceProfileParameters performanceProfileParameters = new PerformanceProfileParameters(); // PerformanceProfileParameters | 
    try {
      PerformanceProfile result = apiInstance.idSavePerformanceProfile(performanceProfileParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceApiApi#idSavePerformanceProfile");
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
| **performanceProfileParameters** | [**PerformanceProfileParameters**](PerformanceProfileParameters.md)|  | [optional] |

### Return type

[**PerformanceProfile**](PerformanceProfile.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single performance profile |  -  |

