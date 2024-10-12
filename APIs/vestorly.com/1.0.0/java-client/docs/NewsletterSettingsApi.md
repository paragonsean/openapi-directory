# NewsletterSettingsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findNewsletterSettings**](NewsletterSettingsApi.md#findNewsletterSettings) | **GET** /newsletter_settings |  |
| [**findNewsletterSettingsByID**](NewsletterSettingsApi.md#findNewsletterSettingsByID) | **GET** /newsletter_settings/{id} |  |
| [**updateNewsletterSettingsByID**](NewsletterSettingsApi.md#updateNewsletterSettingsByID) | **PUT** /newsletter_settings/{id} |  |


<a id="findNewsletterSettings"></a>
# **findNewsletterSettings**
> NewsletterSettings findNewsletterSettings(vestorlyAuth, accessToken)



Returns all newsletter settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewsletterSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    NewsletterSettingsApi apiInstance = new NewsletterSettingsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      NewsletterSettings result = apiInstance.findNewsletterSettings(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewsletterSettingsApi#findNewsletterSettings");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**NewsletterSettings**](NewsletterSettings.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | newsletter settings response |  -  |

<a id="findNewsletterSettingsByID"></a>
# **findNewsletterSettingsByID**
> Newslettersettingresponse findNewsletterSettingsByID(id, vestorlyAuth, accessToken)



Returns a single newsletter settings if the user has access

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewsletterSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    NewsletterSettingsApi apiInstance = new NewsletterSettingsApi(defaultClient);
    String id = "id_example"; // String | Mongo ID of newsletter settings to fetch
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Newslettersettingresponse result = apiInstance.findNewsletterSettingsByID(id, vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewsletterSettingsApi#findNewsletterSettingsByID");
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
| **id** | **String**| Mongo ID of newsletter settings to fetch | |
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Newslettersettingresponse**](Newslettersettingresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | newsletting setting response |  -  |

<a id="updateNewsletterSettingsByID"></a>
# **updateNewsletterSettingsByID**
> Newslettersettingresponse updateNewsletterSettingsByID(id, vestorlyAuth, newsletterSetting, accessToken)



Update a single newsletter setting by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewsletterSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    NewsletterSettingsApi apiInstance = new NewsletterSettingsApi(defaultClient);
    String id = "id_example"; // String | Mongo ID of newsletter settings to update
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    NewsletterSettingsInput newsletterSetting = new NewsletterSettingsInput(); // NewsletterSettingsInput | newsletter settings
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Newslettersettingresponse result = apiInstance.updateNewsletterSettingsByID(id, vestorlyAuth, newsletterSetting, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewsletterSettingsApi#updateNewsletterSettingsByID");
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
| **id** | **String**| Mongo ID of newsletter settings to update | |
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **newsletterSetting** | [**NewsletterSettingsInput**](NewsletterSettingsInput.md)| newsletter settings | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Newslettersettingresponse**](Newslettersettingresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | newsletter settings response |  -  |

