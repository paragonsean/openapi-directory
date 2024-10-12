# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**readDependenciesV1EnCoreWebSmDependenciesPost**](DefaultApi.md#readDependenciesV1EnCoreWebSmDependenciesPost) | **POST** /v1/en_core_web_sm/dependencies | Read Dependencies |
| [**readEntitiesV1EnCoreWebSmEntitiesPost**](DefaultApi.md#readEntitiesV1EnCoreWebSmEntitiesPost) | **POST** /v1/en_core_web_sm/entities | Read Entities |
| [**readRootV1EnCoreWebSmGet**](DefaultApi.md#readRootV1EnCoreWebSmGet) | **GET** /v1/en_core_web_sm/ | Read Root |
| [**readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost**](DefaultApi.md#readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost) | **POST** /v1/en_core_web_sm/sentence-dependencies | Read Sentence Dependencies |
| [**readVersionV1EnCoreWebSmVersionGet**](DefaultApi.md#readVersionV1EnCoreWebSmVersionGet) | **GET** /v1/en_core_web_sm/version | Read Version |


<a id="readDependenciesV1EnCoreWebSmDependenciesPost"></a>
# **readDependenciesV1EnCoreWebSmDependenciesPost**
> DependenciesOut readDependenciesV1EnCoreWebSmDependenciesPost(userRequestIn)

Read Dependencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UserRequestIn userRequestIn = new UserRequestIn(); // UserRequestIn | 
    try {
      DependenciesOut result = apiInstance.readDependenciesV1EnCoreWebSmDependenciesPost(userRequestIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#readDependenciesV1EnCoreWebSmDependenciesPost");
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
| **userRequestIn** | [**UserRequestIn**](UserRequestIn.md)|  | |

### Return type

[**DependenciesOut**](DependenciesOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="readEntitiesV1EnCoreWebSmEntitiesPost"></a>
# **readEntitiesV1EnCoreWebSmEntitiesPost**
> EntitiesOut readEntitiesV1EnCoreWebSmEntitiesPost(userRequestIn)

Read Entities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UserRequestIn userRequestIn = new UserRequestIn(); // UserRequestIn | 
    try {
      EntitiesOut result = apiInstance.readEntitiesV1EnCoreWebSmEntitiesPost(userRequestIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#readEntitiesV1EnCoreWebSmEntitiesPost");
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
| **userRequestIn** | [**UserRequestIn**](UserRequestIn.md)|  | |

### Return type

[**EntitiesOut**](EntitiesOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="readRootV1EnCoreWebSmGet"></a>
# **readRootV1EnCoreWebSmGet**
> Object readRootV1EnCoreWebSmGet()

Read Root

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Object result = apiInstance.readRootV1EnCoreWebSmGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#readRootV1EnCoreWebSmGet");
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

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost"></a>
# **readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost**
> SentenceDependenciesOut readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost(userRequestIn)

Read Sentence Dependencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UserRequestIn userRequestIn = new UserRequestIn(); // UserRequestIn | 
    try {
      SentenceDependenciesOut result = apiInstance.readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost(userRequestIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost");
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
| **userRequestIn** | [**UserRequestIn**](UserRequestIn.md)|  | |

### Return type

[**SentenceDependenciesOut**](SentenceDependenciesOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="readVersionV1EnCoreWebSmVersionGet"></a>
# **readVersionV1EnCoreWebSmVersionGet**
> VersionOut readVersionV1EnCoreWebSmVersionGet()

Read Version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      VersionOut result = apiInstance.readVersionV1EnCoreWebSmVersionGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#readVersionV1EnCoreWebSmVersionGet");
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

[**VersionOut**](VersionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

