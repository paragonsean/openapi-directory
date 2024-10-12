# SettingsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMarketingV3MarketingEventsAppIdSettingsGetAll**](SettingsApi.md#getMarketingV3MarketingEventsAppIdSettingsGetAll) | **GET** /marketing/v3/marketing-events/{appId}/settings | Retrieve the application settings |
| [**postMarketingV3MarketingEventsAppIdSettingsCreate**](SettingsApi.md#postMarketingV3MarketingEventsAppIdSettingsCreate) | **POST** /marketing/v3/marketing-events/{appId}/settings | Update the application settings |


<a id="getMarketingV3MarketingEventsAppIdSettingsGetAll"></a>
# **getMarketingV3MarketingEventsAppIdSettingsGetAll**
> EventDetailSettings getMarketingV3MarketingEventsAppIdSettingsGetAll(appId)

Retrieve the application settings

Retrieve the current settings for the application.

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
    Integer appId = 56; // Integer | The id of the application to retrieve the settings for.
    try {
      EventDetailSettings result = apiInstance.getMarketingV3MarketingEventsAppIdSettingsGetAll(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getMarketingV3MarketingEventsAppIdSettingsGetAll");
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
| **appId** | **Integer**| The id of the application to retrieve the settings for. | |

### Return type

[**EventDetailSettings**](EventDetailSettings.md)

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

<a id="postMarketingV3MarketingEventsAppIdSettingsCreate"></a>
# **postMarketingV3MarketingEventsAppIdSettingsCreate**
> EventDetailSettings postMarketingV3MarketingEventsAppIdSettingsCreate(appId, eventDetailSettingsUrl)

Update the application settings

Create or update the current settings for the application.

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
    Integer appId = 56; // Integer | The id of the application to update the settings for.
    EventDetailSettingsUrl eventDetailSettingsUrl = new EventDetailSettingsUrl(); // EventDetailSettingsUrl | The new application settings
    try {
      EventDetailSettings result = apiInstance.postMarketingV3MarketingEventsAppIdSettingsCreate(appId, eventDetailSettingsUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#postMarketingV3MarketingEventsAppIdSettingsCreate");
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
| **appId** | **Integer**| The id of the application to update the settings for. | |
| **eventDetailSettingsUrl** | [**EventDetailSettingsUrl**](EventDetailSettingsUrl.md)| The new application settings | |

### Return type

[**EventDetailSettings**](EventDetailSettings.md)

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

