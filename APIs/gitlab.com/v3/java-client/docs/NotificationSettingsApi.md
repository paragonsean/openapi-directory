# NotificationSettingsApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getV3NotificationSettings**](NotificationSettingsApi.md#getV3NotificationSettings) | **GET** /v3/notification_settings | Get global notification level settings and email, defaults to Participate |
| [**putV3NotificationSettings**](NotificationSettingsApi.md#putV3NotificationSettings) | **PUT** /v3/notification_settings | Update global notification level settings and email, defaults to Participate |


<a id="getV3NotificationSettings"></a>
# **getV3NotificationSettings**
> GlobalNotificationSetting getV3NotificationSettings()

Get global notification level settings and email, defaults to Participate

This feature was introduced in GitLab 8.12

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationSettingsApi;

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

    NotificationSettingsApi apiInstance = new NotificationSettingsApi(defaultClient);
    try {
      GlobalNotificationSetting result = apiInstance.getV3NotificationSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationSettingsApi#getV3NotificationSettings");
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

[**GlobalNotificationSetting**](GlobalNotificationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get global notification level settings and email, defaults to Participate |  -  |

<a id="putV3NotificationSettings"></a>
# **putV3NotificationSettings**
> GlobalNotificationSetting putV3NotificationSettings(putV3NotificationSettingsRequest)

Update global notification level settings and email, defaults to Participate

This feature was introduced in GitLab 8.12

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationSettingsApi;

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

    NotificationSettingsApi apiInstance = new NotificationSettingsApi(defaultClient);
    PutV3NotificationSettingsRequest putV3NotificationSettingsRequest = new PutV3NotificationSettingsRequest(); // PutV3NotificationSettingsRequest | 
    try {
      GlobalNotificationSetting result = apiInstance.putV3NotificationSettings(putV3NotificationSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationSettingsApi#putV3NotificationSettings");
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
| **putV3NotificationSettingsRequest** | [**PutV3NotificationSettingsRequest**](PutV3NotificationSettingsRequest.md)|  | [optional] |

### Return type

[**GlobalNotificationSetting**](GlobalNotificationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update global notification level settings and email, defaults to Participate |  -  |

