# ApisApi

All URIs are relative to *https://openapi.space/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteApi**](ApisApi.md#deleteApi) | **DELETE** /apis/{owner}/{api} | Deletes the specified API |
| [**deleteApiVersion**](ApisApi.md#deleteApiVersion) | **DELETE** /apis/{owner}/{api}/{version} | Deletes a particular version of the specified API |
| [**getApiVersions**](ApisApi.md#getApiVersions) | **GET** /apis/{owner}/{api} | Retrieves an API meta listing for all API versions for this owner and API |
| [**getJsonDefinition**](ApisApi.md#getJsonDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.json | Retrieves the Swagger definition for the specified API and version in JSON format |
| [**getOwnerApis**](ApisApi.md#getOwnerApis) | **GET** /apis/{owner} | Retrieves an API meta listing of all APIs defined for this owner |
| [**getYamlDefinition**](ApisApi.md#getYamlDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.yaml | Retrieves the Swagger definition for the specified API and version in YAML format |
| [**publishApiVersion**](ApisApi.md#publishApiVersion) | **POST** /apis/{owner}/{api}/{version} | Publish a particular version of the specified API |
| [**saveDefinition**](ApisApi.md#saveDefinition) | **POST** /apis/{owner}/{api} | Saves the provided Swagger definition |
| [**searchApis**](ApisApi.md#searchApis) | **GET** /apis | Retrieves a list of currently defined APIs in API meta list format. |


<a id="deleteApi"></a>
# **deleteApi**
> List&lt;APIMeta&gt; deleteApi(owner, api)

Deletes the specified API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    try {
      List<APIMeta> result = apiInstance.deleteApi(owner, api);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#deleteApi");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |

### Return type

[**List&lt;APIMeta&gt;**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the API was successfully deleted |  -  |
| **403** | access denied |  -  |
| **404** | specified API not found |  -  |

<a id="deleteApiVersion"></a>
# **deleteApiVersion**
> APIMeta deleteApiVersion(owner, api, version)

Deletes a particular version of the specified API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    String version = "version_example"; // String | version identifier
    try {
      APIMeta result = apiInstance.deleteApiVersion(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#deleteApiVersion");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |
| **version** | **String**| version identifier | |

### Return type

[**APIMeta**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the API version was successfully deleted |  -  |
| **403** | access denied |  -  |
| **404** | specified API not found |  -  |
| **409** | the API version is the only version of this API |  -  |

<a id="getApiVersions"></a>
# **getApiVersions**
> List&lt;APIMeta&gt; getApiVersions(owner, api)

Retrieves an API meta listing for all API versions for this owner and API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    try {
      List<APIMeta> result = apiInstance.getApiVersions(owner, api);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getApiVersions");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |

### Return type

[**List&lt;APIMeta&gt;**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of API versions in API meta format |  -  |

<a id="getJsonDefinition"></a>
# **getJsonDefinition**
> Object getJsonDefinition(owner, api, version)

Retrieves the Swagger definition for the specified API and version in JSON format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    String version = "version_example"; // String | version identifier
    try {
      Object result = apiInstance.getJsonDefinition(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getJsonDefinition");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |
| **version** | **String**| version identifier | |

### Return type

**Object**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the Swagger API in JSON format |  -  |
| **403** | access denied: api is private |  -  |
| **404** | specified API not found |  -  |

<a id="getOwnerApis"></a>
# **getOwnerApis**
> List&lt;APIMeta&gt; getOwnerApis(owner, sort, order)

Retrieves an API meta listing of all APIs defined for this owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String sort = "NAME"; // String | sort criteria or result set * NAME - * UPATED * CREATED * OWNER 
    String order = "ASC"; // String | sort order
    try {
      List<APIMeta> result = apiInstance.getOwnerApis(owner, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getOwnerApis");
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
| **owner** | **String**| API owner identifier | |
| **sort** | **String**| sort criteria or result set * NAME - * UPATED * CREATED * OWNER  | [optional] [default to NAME] [enum: NAME, UPDATED, CREATED, OWNER] |
| **order** | **String**| sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**List&lt;APIMeta&gt;**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of APIs in API meta list format |  -  |

<a id="getYamlDefinition"></a>
# **getYamlDefinition**
> Object getYamlDefinition(owner, api, version)

Retrieves the Swagger definition for the specified API and version in YAML format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    String version = "version_example"; // String | version identifier
    try {
      Object result = apiInstance.getYamlDefinition(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getYamlDefinition");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |
| **version** | **String**| version identifier | |

### Return type

**Object**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/vnd.yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the Swagger API in YAML format |  -  |
| **403** | access denied: api is private |  -  |
| **404** | specified API not found |  -  |

<a id="publishApiVersion"></a>
# **publishApiVersion**
> publishApiVersion(owner, api, version)

Publish a particular version of the specified API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    String version = "version_example"; // String | version identifier
    try {
      apiInstance.publishApiVersion(owner, api, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#publishApiVersion");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |
| **version** | **String**| version identifier | |

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
| **200** | the API version was successfully published |  -  |
| **403** | access denied |  -  |
| **404** | specified API not found |  -  |
| **409** | the API version is already published |  -  |

<a id="saveDefinition"></a>
# **saveDefinition**
> APIMeta saveDefinition(owner, api, definition, _private, force)

Saves the provided Swagger definition

Saves the provided Swagger definition; the owner must match the token owner. The version will be extracted from the Swagger definitions itself.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner identifier
    String api = "api_example"; // String | API identifier
    Object definition = null; // Object | the Swagger definition of this API
    Boolean _private = false; // Boolean | Defines whether the API has to be private
    Boolean force = false; // Boolean | force update
    try {
      APIMeta result = apiInstance.saveDefinition(owner, api, definition, _private, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#saveDefinition");
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
| **owner** | **String**| API owner identifier | |
| **api** | **String**| API identifier | |
| **definition** | **Object**| the Swagger definition of this API | |
| **_private** | **Boolean**| Defines whether the API has to be private | [optional] [default to false] |
| **force** | **Boolean**| force update | [optional] [default to false] |

### Return type

[**APIMeta**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the API was successfully saved |  -  |
| **201** | new API was successfully saved |  -  |
| **400** | the Swagger definition was invalid |  -  |
| **403** | the API is not owned by the user |  -  |
| **409** | can not overwrite a published API version without force&#x3D;true |  -  |
| **415** | invalid content type |  -  |

<a id="searchApis"></a>
# **searchApis**
> List&lt;APIMeta&gt; searchApis(query, limit, offset, sort, order)

Retrieves a list of currently defined APIs in API meta list format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://openapi.space/api/v1");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String query = "query_example"; // String | free text query to match
    Integer limit = 10; // Integer | the maximum number of APIs to return
    Integer offset = 0; // Integer | the offset where to start from when fetching a limited number of APIs
    String sort = "NAME"; // String | sort criteria or result set * NAME - * UPATED * CREATED * OWNER 
    String order = "ASC"; // String | sort order
    try {
      List<APIMeta> result = apiInstance.searchApis(query, limit, offset, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#searchApis");
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
| **query** | **String**| free text query to match | [optional] |
| **limit** | **Integer**| the maximum number of APIs to return | [optional] [default to 10] |
| **offset** | **Integer**| the offset where to start from when fetching a limited number of APIs | [optional] [default to 0] |
| **sort** | **String**| sort criteria or result set * NAME - * UPATED * CREATED * OWNER  | [optional] [default to NAME] [enum: NAME, UPDATED, CREATED, OWNER] |
| **order** | **String**| sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**List&lt;APIMeta&gt;**](APIMeta.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of APIs in API meta list format |  -  |

