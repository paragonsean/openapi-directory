# ScriptApi

All URIs are relative to *https://api.shop-pro.jp*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createShopScriptTag**](ScriptApi.md#createShopScriptTag) | **POST** /appstore/v1/script_tags.json | スクリプトタグの作成 |
| [**deleteScriptTag**](ScriptApi.md#deleteScriptTag) | **DELETE** /appstore/v1/script_tags/{scriptTagId}.json | スクリプトタグの削除 |
| [**getShopScriptTag**](ScriptApi.md#getShopScriptTag) | **GET** /appstore/v1/script_tags/{scriptTagId}.json | スクリプトタグの取得 |
| [**getShopScriptTags**](ScriptApi.md#getShopScriptTags) | **GET** /appstore/v1/script_tags.json | スクリプトタグの取得 |
| [**updateShopScriptTag**](ScriptApi.md#updateShopScriptTag) | **PUT** /appstore/v1/script_tags/{scriptTagId}.json | スクリプトタグの更新 |


<a id="createShopScriptTag"></a>
# **createShopScriptTag**
> CreateShopScriptTag200Response createShopScriptTag(createShopScriptTagRequest)

スクリプトタグの作成



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptApi apiInstance = new ScriptApi(defaultClient);
    CreateShopScriptTagRequest createShopScriptTagRequest = new CreateShopScriptTagRequest(); // CreateShopScriptTagRequest | 作成するスクリプトタグの情報
    try {
      CreateShopScriptTag200Response result = apiInstance.createShopScriptTag(createShopScriptTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptApi#createShopScriptTag");
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
| **createShopScriptTagRequest** | [**CreateShopScriptTagRequest**](CreateShopScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] |

### Return type

[**CreateShopScriptTag200Response**](CreateShopScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteScriptTag"></a>
# **deleteScriptTag**
> deleteScriptTag(scriptTagId)

スクリプトタグの削除



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptApi apiInstance = new ScriptApi(defaultClient);
    Integer scriptTagId = 56; // Integer | スクリプトタグID
    try {
      apiInstance.deleteScriptTag(scriptTagId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptApi#deleteScriptTag");
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

<a id="getShopScriptTag"></a>
# **getShopScriptTag**
> CreateShopScriptTag200Response getShopScriptTag(scriptTagId)

スクリプトタグの取得



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptApi apiInstance = new ScriptApi(defaultClient);
    Integer scriptTagId = 56; // Integer | スクリプトタグID
    try {
      CreateShopScriptTag200Response result = apiInstance.getShopScriptTag(scriptTagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptApi#getShopScriptTag");
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

[**CreateShopScriptTag200Response**](CreateShopScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getShopScriptTags"></a>
# **getShopScriptTags**
> GetShopScriptTags200Response getShopScriptTags()

スクリプトタグの取得



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptApi apiInstance = new ScriptApi(defaultClient);
    try {
      GetShopScriptTags200Response result = apiInstance.getShopScriptTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptApi#getShopScriptTags");
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

[**GetShopScriptTags200Response**](GetShopScriptTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateShopScriptTag"></a>
# **updateShopScriptTag**
> CreateShopScriptTag200Response updateShopScriptTag(scriptTagId, createShopScriptTagRequest)

スクリプトタグの更新



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptApi apiInstance = new ScriptApi(defaultClient);
    Integer scriptTagId = 56; // Integer | スクリプトタグID
    CreateShopScriptTagRequest createShopScriptTagRequest = new CreateShopScriptTagRequest(); // CreateShopScriptTagRequest | 作成するスクリプトタグの情報
    try {
      CreateShopScriptTag200Response result = apiInstance.updateShopScriptTag(scriptTagId, createShopScriptTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptApi#updateShopScriptTag");
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
| **createShopScriptTagRequest** | [**CreateShopScriptTagRequest**](CreateShopScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] |

### Return type

[**CreateShopScriptTag200Response**](CreateShopScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

