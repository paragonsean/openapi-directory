# ScriptDeprecatedApi

All URIs are relative to *https://api.shop-pro.jp*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createScriptTag**](ScriptDeprecatedApi.md#createScriptTag) | **POST** /v1/script_tags.json | スクリプトタグの作成 |
| [**getScriptTag**](ScriptDeprecatedApi.md#getScriptTag) | **GET** /v1/script_tags/{scriptTagId}.json | スクリプトタグの取得 |
| [**getScriptTags**](ScriptDeprecatedApi.md#getScriptTags) | **GET** /v1/script_tags.json | スクリプトタグの取得 |
| [**updateScriptTag**](ScriptDeprecatedApi.md#updateScriptTag) | **PUT** /v1/script_tags/{scriptTagId}.json | スクリプトタグの更新 |
| [**v1ScriptTagsScriptTagIdJsonDelete**](ScriptDeprecatedApi.md#v1ScriptTagsScriptTagIdJsonDelete) | **DELETE** /v1/script_tags/{scriptTagId}.json | スクリプトタグの削除 |


<a id="createScriptTag"></a>
# **createScriptTag**
> CreateScriptTag200Response createScriptTag(createScriptTagRequest)

スクリプトタグの作成



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptDeprecatedApi apiInstance = new ScriptDeprecatedApi(defaultClient);
    CreateScriptTagRequest createScriptTagRequest = new CreateScriptTagRequest(); // CreateScriptTagRequest | 作成するスクリプトタグの情報
    try {
      CreateScriptTag200Response result = apiInstance.createScriptTag(createScriptTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptDeprecatedApi#createScriptTag");
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
| **createScriptTagRequest** | [**CreateScriptTagRequest**](CreateScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] |

### Return type

[**CreateScriptTag200Response**](CreateScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getScriptTag"></a>
# **getScriptTag**
> CreateScriptTag200Response getScriptTag(scriptTagId)

スクリプトタグの取得



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptDeprecatedApi apiInstance = new ScriptDeprecatedApi(defaultClient);
    Integer scriptTagId = 56; // Integer | スクリプトタグID
    try {
      CreateScriptTag200Response result = apiInstance.getScriptTag(scriptTagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptDeprecatedApi#getScriptTag");
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
| **scriptTagId** | **Integer**| スクリプトタグID | |

### Return type

[**CreateScriptTag200Response**](CreateScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getScriptTags"></a>
# **getScriptTags**
> GetScriptTags200Response getScriptTags()

スクリプトタグの取得



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptDeprecatedApi apiInstance = new ScriptDeprecatedApi(defaultClient);
    try {
      GetScriptTags200Response result = apiInstance.getScriptTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptDeprecatedApi#getScriptTags");
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

[**GetScriptTags200Response**](GetScriptTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateScriptTag"></a>
# **updateScriptTag**
> CreateScriptTag200Response updateScriptTag(scriptTagId, createScriptTagRequest)

スクリプトタグの更新



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptDeprecatedApi apiInstance = new ScriptDeprecatedApi(defaultClient);
    Integer scriptTagId = 56; // Integer | スクリプトタグID
    CreateScriptTagRequest createScriptTagRequest = new CreateScriptTagRequest(); // CreateScriptTagRequest | 作成するスクリプトタグの情報
    try {
      CreateScriptTag200Response result = apiInstance.updateScriptTag(scriptTagId, createScriptTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptDeprecatedApi#updateScriptTag");
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
| **scriptTagId** | **Integer**| スクリプトタグID | |
| **createScriptTagRequest** | [**CreateScriptTagRequest**](CreateScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] |

### Return type

[**CreateScriptTag200Response**](CreateScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="v1ScriptTagsScriptTagIdJsonDelete"></a>
# **v1ScriptTagsScriptTagIdJsonDelete**
> v1ScriptTagsScriptTagIdJsonDelete(scriptTagId)

スクリプトタグの削除



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptDeprecatedApi apiInstance = new ScriptDeprecatedApi(defaultClient);
    Integer scriptTagId = 56; // Integer | スクリプトタグID
    try {
      apiInstance.v1ScriptTagsScriptTagIdJsonDelete(scriptTagId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptDeprecatedApi#v1ScriptTagsScriptTagIdJsonDelete");
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
| **scriptTagId** | **Integer**| スクリプトタグID | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

