# DefinitionApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCommunicationPreferencesV3DefinitionsGetPage**](DefinitionApi.md#getCommunicationPreferencesV3DefinitionsGetPage) | **GET** /communication-preferences/v3/definitions | Get subscription definitions |


<a id="getCommunicationPreferencesV3DefinitionsGetPage"></a>
# **getCommunicationPreferencesV3DefinitionsGetPage**
> SubscriptionDefinitionsResponse getCommunicationPreferencesV3DefinitionsGetPage()

Get subscription definitions

Get a list of all subscription definitions for the portal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    DefinitionApi apiInstance = new DefinitionApi(defaultClient);
    try {
      SubscriptionDefinitionsResponse result = apiInstance.getCommunicationPreferencesV3DefinitionsGetPage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinitionApi#getCommunicationPreferencesV3DefinitionsGetPage");
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

[**SubscriptionDefinitionsResponse**](SubscriptionDefinitionsResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

