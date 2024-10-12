# AdministrationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**administrationEntityGet**](AdministrationApi.md#administrationEntityGet) | **GET** /administration/entity | Get all organizations |
| [**administrationEntityIdDelete**](AdministrationApi.md#administrationEntityIdDelete) | **DELETE** /administration/entity/{id} | Delete organization |
| [**administrationEntityPost**](AdministrationApi.md#administrationEntityPost) | **POST** /administration/entity | Create organization |
| [**administrationEntityPut**](AdministrationApi.md#administrationEntityPut) | **PUT** /administration/entity | Pause organization |
| [**administrationFileToJsonPost**](AdministrationApi.md#administrationFileToJsonPost) | **POST** /administration/file-to-json | Transform data file to JSON format |
| [**administrationModelEntityIdGet**](AdministrationApi.md#administrationModelEntityIdGet) | **GET** /administration/model/{entityId} | Get Models for Organization |
| [**administrationModelEntityIdPost**](AdministrationApi.md#administrationModelEntityIdPost) | **POST** /administration/model/{entityId} | Register new forecasting model |
| [**administrationModelGet**](AdministrationApi.md#administrationModelGet) | **GET** /administration/model | Get all common Models |
| [**administrationModelPost**](AdministrationApi.md#administrationModelPost) | **POST** /administration/model | Register new forecasting model |
| [**administrationPlanningLevelEntityIdIdDelete**](AdministrationApi.md#administrationPlanningLevelEntityIdIdDelete) | **DELETE** /administration/planning-level/{entityId}/{id} | Delete planning level |
| [**administrationPlanningLevelLockPost**](AdministrationApi.md#administrationPlanningLevelLockPost) | **POST** /administration/planning-level/lock | Lock planning level |
| [**administrationTokenPost**](AdministrationApi.md#administrationTokenPost) | **POST** /administration/token | Issue a token |
| [**administrationUserEntityIdGet**](AdministrationApi.md#administrationUserEntityIdGet) | **GET** /administration/user/{entityId} | Get all users |
| [**administrationUserEntityIdIdDelete**](AdministrationApi.md#administrationUserEntityIdIdDelete) | **DELETE** /administration/user/{entityId}/{id} | Delete user |
| [**administrationUserLockPut**](AdministrationApi.md#administrationUserLockPut) | **PUT** /administration/user/lock | Lock user |
| [**administrationUserPost**](AdministrationApi.md#administrationUserPost) | **POST** /administration/user | Create user |
| [**administrationUserPut**](AdministrationApi.md#administrationUserPut) | **PUT** /administration/user | Update user |


<a id="administrationEntityGet"></a>
# **administrationEntityGet**
> List&lt;EntityResponse&gt; administrationEntityGet(token)

Get all organizations

This is an iCUE only endpoint or Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      List<EntityResponse> result = apiInstance.administrationEntityGet(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationEntityGet");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

[**List&lt;EntityResponse&gt;**](EntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationEntityIdDelete"></a>
# **administrationEntityIdDelete**
> administrationEntityIdDelete(id, token)

Delete organization

This is an iCUE only endpoint or Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    Integer id = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.administrationEntityIdDelete(id, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationEntityIdDelete");
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
| **id** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="administrationEntityPost"></a>
# **administrationEntityPost**
> UUID administrationEntityPost(token, newEntityRequest)

Create organization

This is an iCUE only endpoint or Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    NewEntityRequest newEntityRequest = new NewEntityRequest(); // NewEntityRequest | 
    try {
      UUID result = apiInstance.administrationEntityPost(token, newEntityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationEntityPost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **newEntityRequest** | [**NewEntityRequest**](NewEntityRequest.md)|  | [optional] |

### Return type

[**UUID**](UUID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationEntityPut"></a>
# **administrationEntityPut**
> administrationEntityPut(token, toggleRequest)

Pause organization

This is an iCUE only endpoint or Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    ToggleRequest toggleRequest = new ToggleRequest(); // ToggleRequest | 
    try {
      apiInstance.administrationEntityPut(token, toggleRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationEntityPut");
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
| **token** | **String**| User Authentication Token | [optional] |
| **toggleRequest** | [**ToggleRequest**](ToggleRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationFileToJsonPost"></a>
# **administrationFileToJsonPost**
> JsonForecastResponse administrationFileToJsonPost(_file, periodicity, token)

Transform data file to JSON format

Transform data file to JSON format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    File _file = new File("/path/to/file"); // File | 
    Integer periodicity = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      JsonForecastResponse result = apiInstance.administrationFileToJsonPost(_file, periodicity, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationFileToJsonPost");
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
| **_file** | **File**|  | |
| **periodicity** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

### Return type

[**JsonForecastResponse**](JsonForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationModelEntityIdGet"></a>
# **administrationModelEntityIdGet**
> List&lt;MethodDto&gt; administrationModelEntityIdGet(entityId, token)

Get Models for Organization

Returns models registered for Organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    Integer entityId = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      List<MethodDto> result = apiInstance.administrationModelEntityIdGet(entityId, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationModelEntityIdGet");
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
| **entityId** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

### Return type

[**List&lt;MethodDto&gt;**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationModelEntityIdPost"></a>
# **administrationModelEntityIdPost**
> MethodDto administrationModelEntityIdPost(entityId, token, newModelRequest)

Register new forecasting model

Register new forecasting model for single organziation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    Integer entityId = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    NewModelRequest newModelRequest = new NewModelRequest(); // NewModelRequest | 
    try {
      MethodDto result = apiInstance.administrationModelEntityIdPost(entityId, token, newModelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationModelEntityIdPost");
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
| **entityId** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |
| **newModelRequest** | [**NewModelRequest**](NewModelRequest.md)|  | [optional] |

### Return type

[**MethodDto**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationModelGet"></a>
# **administrationModelGet**
> List&lt;MethodDto&gt; administrationModelGet(token)

Get all common Models

Returns models that are common for all Organizations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      List<MethodDto> result = apiInstance.administrationModelGet(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationModelGet");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

[**List&lt;MethodDto&gt;**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationModelPost"></a>
# **administrationModelPost**
> MethodDto administrationModelPost(token, newModelRequest)

Register new forecasting model

Register new forecasting model for all organziations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    NewModelRequest newModelRequest = new NewModelRequest(); // NewModelRequest | 
    try {
      MethodDto result = apiInstance.administrationModelPost(token, newModelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationModelPost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **newModelRequest** | [**NewModelRequest**](NewModelRequest.md)|  | [optional] |

### Return type

[**MethodDto**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationPlanningLevelEntityIdIdDelete"></a>
# **administrationPlanningLevelEntityIdIdDelete**
> administrationPlanningLevelEntityIdIdDelete(entityId, id, token)

Delete planning level

Delete planning level. This is an Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    Integer entityId = 56; // Integer | 
    Integer id = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.administrationPlanningLevelEntityIdIdDelete(entityId, id, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationPlanningLevelEntityIdIdDelete");
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
| **entityId** | **Integer**|  | |
| **id** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="administrationPlanningLevelLockPost"></a>
# **administrationPlanningLevelLockPost**
> administrationPlanningLevelLockPost(token)

Lock planning level

Lock planning level against modification. This is an Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.administrationPlanningLevelLockPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationPlanningLevelLockPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="administrationTokenPost"></a>
# **administrationTokenPost**
> UUID administrationTokenPost(token, newTokenRequest)

Issue a token

This is an iCUE only endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    NewTokenRequest newTokenRequest = new NewTokenRequest(); // NewTokenRequest | 
    try {
      UUID result = apiInstance.administrationTokenPost(token, newTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationTokenPost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **newTokenRequest** | [**NewTokenRequest**](NewTokenRequest.md)|  | [optional] |

### Return type

[**UUID**](UUID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationUserEntityIdGet"></a>
# **administrationUserEntityIdGet**
> administrationUserEntityIdGet(entityId, token)

Get all users

Get all users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    Integer entityId = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.administrationUserEntityIdGet(entityId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationUserEntityIdGet");
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
| **entityId** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="administrationUserEntityIdIdDelete"></a>
# **administrationUserEntityIdIdDelete**
> administrationUserEntityIdIdDelete(entityId, id, token)

Delete user

Delete user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    Integer entityId = 56; // Integer | 
    Integer id = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.administrationUserEntityIdIdDelete(entityId, id, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationUserEntityIdIdDelete");
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
| **entityId** | **Integer**|  | |
| **id** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="administrationUserLockPut"></a>
# **administrationUserLockPut**
> administrationUserLockPut(token, toggleUserRequest)

Lock user

After lock user won&#39;t be able to use iCUE API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    ToggleUserRequest toggleUserRequest = new ToggleUserRequest(); // ToggleUserRequest | 
    try {
      apiInstance.administrationUserLockPut(token, toggleUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationUserLockPut");
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
| **token** | **String**| User Authentication Token | [optional] |
| **toggleUserRequest** | [**ToggleUserRequest**](ToggleUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationUserPost"></a>
# **administrationUserPost**
> UUID administrationUserPost(token, newUserRequest)

Create user

Create new user for entity/organization. This can be done by entity administrator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    NewUserRequest newUserRequest = new NewUserRequest(); // NewUserRequest | 
    try {
      UUID result = apiInstance.administrationUserPost(token, newUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationUserPost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **newUserRequest** | [**NewUserRequest**](NewUserRequest.md)|  | [optional] |

### Return type

[**UUID**](UUID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="administrationUserPut"></a>
# **administrationUserPut**
> administrationUserPut(token)

Update user

Update user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AdministrationApi apiInstance = new AdministrationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.administrationUserPut(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationApi#administrationUserPut");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

