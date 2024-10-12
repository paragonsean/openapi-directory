# VoiceV1SettingsApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDialingPermissionsSettings**](VoiceV1SettingsApi.md#fetchDialingPermissionsSettings) | **GET** /v1/Settings |  |
| [**updateDialingPermissionsSettings**](VoiceV1SettingsApi.md#updateDialingPermissionsSettings) | **POST** /v1/Settings |  |


<a id="fetchDialingPermissionsSettings"></a>
# **fetchDialingPermissionsSettings**
> VoiceV1DialingPermissionsDialingPermissionsSettings fetchDialingPermissionsSettings()



Retrieve voice dialing permissions inheritance for the sub-account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SettingsApi apiInstance = new VoiceV1SettingsApi(defaultClient);
    try {
      VoiceV1DialingPermissionsDialingPermissionsSettings result = apiInstance.fetchDialingPermissionsSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SettingsApi#fetchDialingPermissionsSettings");
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

[**VoiceV1DialingPermissionsDialingPermissionsSettings**](VoiceV1DialingPermissionsDialingPermissionsSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDialingPermissionsSettings"></a>
# **updateDialingPermissionsSettings**
> VoiceV1DialingPermissionsDialingPermissionsSettings updateDialingPermissionsSettings(dialingPermissionsInheritance)



Update voice dialing permissions inheritance for the sub-account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SettingsApi apiInstance = new VoiceV1SettingsApi(defaultClient);
    Boolean dialingPermissionsInheritance = true; // Boolean | `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.
    try {
      VoiceV1DialingPermissionsDialingPermissionsSettings result = apiInstance.updateDialingPermissionsSettings(dialingPermissionsInheritance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SettingsApi#updateDialingPermissionsSettings");
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
| **dialingPermissionsInheritance** | **Boolean**| &#x60;true&#x60; for the sub-account to inherit voice dialing permissions from the Master Project; otherwise &#x60;false&#x60;. | [optional] |

### Return type

[**VoiceV1DialingPermissionsDialingPermissionsSettings**](VoiceV1DialingPermissionsDialingPermissionsSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

