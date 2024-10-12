# SnippetsApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteV3SnippetsId**](SnippetsApi.md#deleteV3SnippetsId) | **DELETE** /v3/snippets/{id} | Remove snippet |
| [**getV3Snippets**](SnippetsApi.md#getV3Snippets) | **GET** /v3/snippets | Get a snippets list for authenticated user |
| [**getV3SnippetsId**](SnippetsApi.md#getV3SnippetsId) | **GET** /v3/snippets/{id} | Get a single snippet |
| [**getV3SnippetsIdRaw**](SnippetsApi.md#getV3SnippetsIdRaw) | **GET** /v3/snippets/{id}/raw | Get a raw snippet |
| [**getV3SnippetsPublic**](SnippetsApi.md#getV3SnippetsPublic) | **GET** /v3/snippets/public | List all public snippets current_user has access to |
| [**postV3Snippets**](SnippetsApi.md#postV3Snippets) | **POST** /v3/snippets | Create new snippet |
| [**putV3SnippetsId**](SnippetsApi.md#putV3SnippetsId) | **PUT** /v3/snippets/{id} | Update an existing snippet |


<a id="deleteV3SnippetsId"></a>
# **deleteV3SnippetsId**
> PersonalSnippet deleteV3SnippetsId(id)

Remove snippet

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer id = 56; // Integer | The ID of a snippet
    try {
      PersonalSnippet result = apiInstance.deleteV3SnippetsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#deleteV3SnippetsId");
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
| **id** | **Integer**| The ID of a snippet | |

### Return type

[**PersonalSnippet**](PersonalSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Remove snippet |  -  |

<a id="getV3Snippets"></a>
# **getV3Snippets**
> PersonalSnippet getV3Snippets(page, perPage)

Get a snippets list for authenticated user

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      PersonalSnippet result = apiInstance.getV3Snippets(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#getV3Snippets");
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
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**PersonalSnippet**](PersonalSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a snippets list for authenticated user |  -  |

<a id="getV3SnippetsId"></a>
# **getV3SnippetsId**
> PersonalSnippet getV3SnippetsId(id)

Get a single snippet

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer id = 56; // Integer | The ID of a snippet
    try {
      PersonalSnippet result = apiInstance.getV3SnippetsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#getV3SnippetsId");
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
| **id** | **Integer**| The ID of a snippet | |

### Return type

[**PersonalSnippet**](PersonalSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single snippet |  -  |

<a id="getV3SnippetsIdRaw"></a>
# **getV3SnippetsIdRaw**
> getV3SnippetsIdRaw(id)

Get a raw snippet

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer id = 56; // Integer | The ID of a snippet
    try {
      apiInstance.getV3SnippetsIdRaw(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#getV3SnippetsIdRaw");
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
| **id** | **Integer**| The ID of a snippet | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a raw snippet |  -  |

<a id="getV3SnippetsPublic"></a>
# **getV3SnippetsPublic**
> PersonalSnippet getV3SnippetsPublic(page, perPage)

List all public snippets current_user has access to

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      PersonalSnippet result = apiInstance.getV3SnippetsPublic(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#getV3SnippetsPublic");
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
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**PersonalSnippet**](PersonalSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all public snippets current_user has access to |  -  |

<a id="postV3Snippets"></a>
# **postV3Snippets**
> PersonalSnippet postV3Snippets(postV3SnippetsRequest)

Create new snippet

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    PostV3SnippetsRequest postV3SnippetsRequest = new PostV3SnippetsRequest(); // PostV3SnippetsRequest | 
    try {
      PersonalSnippet result = apiInstance.postV3Snippets(postV3SnippetsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#postV3Snippets");
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
| **postV3SnippetsRequest** | [**PostV3SnippetsRequest**](PostV3SnippetsRequest.md)|  | |

### Return type

[**PersonalSnippet**](PersonalSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create new snippet |  -  |

<a id="putV3SnippetsId"></a>
# **putV3SnippetsId**
> PersonalSnippet putV3SnippetsId(id, putV3SnippetsIdRequest)

Update an existing snippet

This feature was introduced in GitLab 8.15.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    SnippetsApi apiInstance = new SnippetsApi(defaultClient);
    Integer id = 56; // Integer | The ID of a snippet
    PutV3SnippetsIdRequest putV3SnippetsIdRequest = new PutV3SnippetsIdRequest(); // PutV3SnippetsIdRequest | 
    try {
      PersonalSnippet result = apiInstance.putV3SnippetsId(id, putV3SnippetsIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetsApi#putV3SnippetsId");
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
| **id** | **Integer**| The ID of a snippet | |
| **putV3SnippetsIdRequest** | [**PutV3SnippetsIdRequest**](PutV3SnippetsIdRequest.md)|  | [optional] |

### Return type

[**PersonalSnippet**](PersonalSnippet.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update an existing snippet |  -  |

