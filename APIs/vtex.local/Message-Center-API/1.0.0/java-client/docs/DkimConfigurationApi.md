# DkimConfigurationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDKIM**](DkimConfigurationApi.md#createDKIM) | **POST** /api/mail-service/pvt/providers/{EmailProvider}/dkim | Generate DKIM keys |


<a id="createDKIM"></a>
# **createDKIM**
> Model200OK createDKIM(emailProvider)

Generate DKIM keys

Create DKIM keys for sender that was setup in VTEX mail servers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DkimConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DkimConfigurationApi apiInstance = new DkimConfigurationApi(defaultClient);
    String emailProvider = "help@valdie.co"; // String | E-mail address for sender that was setup in VTEX mail servers
    try {
      Model200OK result = apiInstance.createDKIM(emailProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DkimConfigurationApi#createDKIM");
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
| **emailProvider** | **String**| E-mail address for sender that was setup in VTEX mail servers | [default to help@valdie.co] |

### Return type

[**Model200OK**](Model200OK.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

