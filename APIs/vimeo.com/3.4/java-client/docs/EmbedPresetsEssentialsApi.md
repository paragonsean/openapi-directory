# EmbedPresetsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**editEmbedPreset**](EmbedPresetsEssentialsApi.md#editEmbedPreset) | **PATCH** /users/{user_id}/presets/{preset_id} | Edit an embed preset |
| [**editEmbedPresetAlt1**](EmbedPresetsEssentialsApi.md#editEmbedPresetAlt1) | **PATCH** /me/presets/{preset_id} | Edit an embed preset |
| [**getEmbedPreset**](EmbedPresetsEssentialsApi.md#getEmbedPreset) | **GET** /users/{user_id}/presets/{preset_id} | Get a specific embed preset |
| [**getEmbedPresetAlt1**](EmbedPresetsEssentialsApi.md#getEmbedPresetAlt1) | **GET** /me/presets/{preset_id} | Get a specific embed preset |
| [**getEmbedPresets**](EmbedPresetsEssentialsApi.md#getEmbedPresets) | **GET** /users/{user_id}/presets | Get all the embed presets that a user has created |
| [**getEmbedPresetsAlt1**](EmbedPresetsEssentialsApi.md#getEmbedPresetsAlt1) | **GET** /me/presets | Get all the embed presets that a user has created |


<a id="editEmbedPreset"></a>
# **editEmbedPreset**
> Presets editEmbedPreset(presetId, userId, editEmbedPresetAlt1Request)

Edit an embed preset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmbedPresetsEssentialsApi apiInstance = new EmbedPresetsEssentialsApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    EditEmbedPresetAlt1Request editEmbedPresetAlt1Request = new EditEmbedPresetAlt1Request(); // EditEmbedPresetAlt1Request | 
    try {
      Presets result = apiInstance.editEmbedPreset(presetId, userId, editEmbedPresetAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsEssentialsApi#editEmbedPreset");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **editEmbedPresetAlt1Request** | [**EditEmbedPresetAlt1Request**](EditEmbedPresetAlt1Request.md)|  | [optional] |

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.preset+json
 - **Accept**: application/vnd.vimeo.preset+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The embed preset was edited. |  -  |
| **400** | The outro type is invalid. |  -  |
| **404** | * The preset doesn&#39;t exist. * The authenticated user doesn&#39;t own the preset. |  -  |

<a id="editEmbedPresetAlt1"></a>
# **editEmbedPresetAlt1**
> Presets editEmbedPresetAlt1(presetId, editEmbedPresetAlt1Request)

Edit an embed preset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmbedPresetsEssentialsApi apiInstance = new EmbedPresetsEssentialsApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    EditEmbedPresetAlt1Request editEmbedPresetAlt1Request = new EditEmbedPresetAlt1Request(); // EditEmbedPresetAlt1Request | 
    try {
      Presets result = apiInstance.editEmbedPresetAlt1(presetId, editEmbedPresetAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsEssentialsApi#editEmbedPresetAlt1");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
| **editEmbedPresetAlt1Request** | [**EditEmbedPresetAlt1Request**](EditEmbedPresetAlt1Request.md)|  | [optional] |

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.preset+json
 - **Accept**: application/vnd.vimeo.preset+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The embed preset was edited. |  -  |
| **400** | The outro type is invalid. |  -  |
| **404** | * The preset doesn&#39;t exist. * The authenticated user doesn&#39;t own the preset. |  -  |

<a id="getEmbedPreset"></a>
# **getEmbedPreset**
> Presets getEmbedPreset(presetId, userId)

Get a specific embed preset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmbedPresetsEssentialsApi apiInstance = new EmbedPresetsEssentialsApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Presets result = apiInstance.getEmbedPreset(presetId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsEssentialsApi#getEmbedPreset");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.preset+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The embed preset was returned. |  -  |

<a id="getEmbedPresetAlt1"></a>
# **getEmbedPresetAlt1**
> Presets getEmbedPresetAlt1(presetId)

Get a specific embed preset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmbedPresetsEssentialsApi apiInstance = new EmbedPresetsEssentialsApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    try {
      Presets result = apiInstance.getEmbedPresetAlt1(presetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsEssentialsApi#getEmbedPresetAlt1");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.preset+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The embed preset was returned. |  -  |

<a id="getEmbedPresets"></a>
# **getEmbedPresets**
> List&lt;Presets&gt; getEmbedPresets(userId, page, perPage)

Get all the embed presets that a user has created

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmbedPresetsEssentialsApi apiInstance = new EmbedPresetsEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Presets> result = apiInstance.getEmbedPresets(userId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsEssentialsApi#getEmbedPresets");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Presets&gt;**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.preset+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The embed presets were returned. |  -  |

<a id="getEmbedPresetsAlt1"></a>
# **getEmbedPresetsAlt1**
> List&lt;Presets&gt; getEmbedPresetsAlt1(page, perPage)

Get all the embed presets that a user has created

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmbedPresetsEssentialsApi apiInstance = new EmbedPresetsEssentialsApi(defaultClient);
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Presets> result = apiInstance.getEmbedPresetsAlt1(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsEssentialsApi#getEmbedPresetsAlt1");
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
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Presets&gt;**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.preset+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The embed presets were returned. |  -  |

