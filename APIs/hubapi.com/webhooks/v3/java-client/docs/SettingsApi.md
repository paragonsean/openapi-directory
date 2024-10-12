# SettingsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteWebhooksV3AppIdSettingsClear**](SettingsApi.md#deleteWebhooksV3AppIdSettingsClear) | **DELETE** /webhooks/v3/{appId}/settings |  |
| [**getWebhooksV3AppIdSettingsGetAll**](SettingsApi.md#getWebhooksV3AppIdSettingsGetAll) | **GET** /webhooks/v3/{appId}/settings |  |
| [**putWebhooksV3AppIdSettingsConfigure**](SettingsApi.md#putWebhooksV3AppIdSettingsConfigure) | **PUT** /webhooks/v3/{appId}/settings |  |


<a id="deleteWebhooksV3AppIdSettingsClear"></a>
# **deleteWebhooksV3AppIdSettingsClear**
> deleteWebhooksV3AppIdSettingsClear(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    Integer appId = 56; // Integer | 
    try {
      apiInstance.deleteWebhooksV3AppIdSettingsClear(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#deleteWebhooksV3AppIdSettingsClear");
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
| **appId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getWebhooksV3AppIdSettingsGetAll"></a>
# **getWebhooksV3AppIdSettingsGetAll**
> SettingsResponse getWebhooksV3AppIdSettingsGetAll(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    Integer appId = 56; // Integer | 
    try {
      SettingsResponse result = apiInstance.getWebhooksV3AppIdSettingsGetAll(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getWebhooksV3AppIdSettingsGetAll");
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
| **appId** | **Integer**|  | |

### Return type

[**SettingsResponse**](SettingsResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="putWebhooksV3AppIdSettingsConfigure"></a>
# **putWebhooksV3AppIdSettingsConfigure**
> SettingsResponse putWebhooksV3AppIdSettingsConfigure(appId, settingsChangeRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    Integer appId = 56; // Integer | 
    SettingsChangeRequest settingsChangeRequest = new SettingsChangeRequest(); // SettingsChangeRequest | 
    try {
      SettingsResponse result = apiInstance.putWebhooksV3AppIdSettingsConfigure(appId, settingsChangeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#putWebhooksV3AppIdSettingsConfigure");
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
| **appId** | **Integer**|  | |
| **settingsChangeRequest** | [**SettingsChangeRequest**](SettingsChangeRequest.md)|  | |

### Return type

[**SettingsResponse**](SettingsResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

