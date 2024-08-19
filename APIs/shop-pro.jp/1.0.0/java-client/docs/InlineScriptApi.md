# InlineScriptApi

All URIs are relative to *https://api.shop-pro.jp*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInlineScriptTag**](InlineScriptApi.md#createInlineScriptTag) | **POST** /v1/inline_script_tags.json | インラインスクリプトタグの登録 |
| [**deleteInlineScriptTag**](InlineScriptApi.md#deleteInlineScriptTag) | **DELETE** /v1/inline_script_tags/{inlineScriptTagId}.json | インラインスクリプトタグの削除 |
| [**getInlineScriptTag**](InlineScriptApi.md#getInlineScriptTag) | **GET** /v1/inline_script_tags/{inlineScriptTagId}.json | インラインスクリプトタグの取得 |
| [**getInlineScriptTags**](InlineScriptApi.md#getInlineScriptTags) | **GET** /v1/inline_script_tags.json | インラインスクリプトタグの取得 |
| [**updateInlineScriptTag**](InlineScriptApi.md#updateInlineScriptTag) | **PUT** /v1/inline_script_tags/{inlineScriptTagId}.json | インラインスクリプトタグの更新 |


<a id="createInlineScriptTag"></a>
# **createInlineScriptTag**
> CreateInlineScriptTag201Response createInlineScriptTag(createInlineScriptTagRequest)

インラインスクリプトタグの登録



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InlineScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InlineScriptApi apiInstance = new InlineScriptApi(defaultClient);
    CreateInlineScriptTagRequest createInlineScriptTagRequest = new CreateInlineScriptTagRequest(); // CreateInlineScriptTagRequest | 作成するインラインスクリプトタグの情報
    try {
      CreateInlineScriptTag201Response result = apiInstance.createInlineScriptTag(createInlineScriptTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InlineScriptApi#createInlineScriptTag");
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
| **createInlineScriptTagRequest** | [**CreateInlineScriptTagRequest**](CreateInlineScriptTagRequest.md)| 作成するインラインスクリプトタグの情報 | [optional] |

### Return type

[**CreateInlineScriptTag201Response**](CreateInlineScriptTag201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="deleteInlineScriptTag"></a>
# **deleteInlineScriptTag**
> deleteInlineScriptTag(inlineScriptTagId)

インラインスクリプトタグの削除



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InlineScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InlineScriptApi apiInstance = new InlineScriptApi(defaultClient);
    Integer inlineScriptTagId = 56; // Integer | インラインスクリプトタグID
    try {
      apiInstance.deleteInlineScriptTag(inlineScriptTagId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InlineScriptApi#deleteInlineScriptTag");
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
| **inlineScriptTagId** | **Integer**| インラインスクリプトタグID | |

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

<a id="getInlineScriptTag"></a>
# **getInlineScriptTag**
> CreateInlineScriptTag201Response getInlineScriptTag(inlineScriptTagId)

インラインスクリプトタグの取得



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InlineScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InlineScriptApi apiInstance = new InlineScriptApi(defaultClient);
    Integer inlineScriptTagId = 56; // Integer | インラインスクリプトタグID
    try {
      CreateInlineScriptTag201Response result = apiInstance.getInlineScriptTag(inlineScriptTagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InlineScriptApi#getInlineScriptTag");
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
| **inlineScriptTagId** | **Integer**| インラインスクリプトタグID | |

### Return type

[**CreateInlineScriptTag201Response**](CreateInlineScriptTag201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getInlineScriptTags"></a>
# **getInlineScriptTags**
> GetInlineScriptTags200Response getInlineScriptTags()

インラインスクリプトタグの取得



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InlineScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InlineScriptApi apiInstance = new InlineScriptApi(defaultClient);
    try {
      GetInlineScriptTags200Response result = apiInstance.getInlineScriptTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InlineScriptApi#getInlineScriptTags");
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

[**GetInlineScriptTags200Response**](GetInlineScriptTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateInlineScriptTag"></a>
# **updateInlineScriptTag**
> CreateInlineScriptTag201Response updateInlineScriptTag(inlineScriptTagId, createInlineScriptTagRequest)

インラインスクリプトタグの更新



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InlineScriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InlineScriptApi apiInstance = new InlineScriptApi(defaultClient);
    Integer inlineScriptTagId = 56; // Integer | インラインスクリプトタグID
    CreateInlineScriptTagRequest createInlineScriptTagRequest = new CreateInlineScriptTagRequest(); // CreateInlineScriptTagRequest | 更新するスクリプトタグの情報
    try {
      CreateInlineScriptTag201Response result = apiInstance.updateInlineScriptTag(inlineScriptTagId, createInlineScriptTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InlineScriptApi#updateInlineScriptTag");
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
| **inlineScriptTagId** | **Integer**| インラインスクリプトタグID | |
| **createInlineScriptTagRequest** | [**CreateInlineScriptTagRequest**](CreateInlineScriptTagRequest.md)| 更新するスクリプトタグの情報 | [optional] |

### Return type

[**CreateInlineScriptTag201Response**](CreateInlineScriptTag201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

