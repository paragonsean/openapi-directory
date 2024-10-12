# SplashLoginAttemptsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSplashLoginAttempts**](SplashLoginAttemptsApi.md#getNetworkSplashLoginAttempts) | **GET** /networks/{networkId}/splashLoginAttempts | List the splash login attempts for a network |


<a id="getNetworkSplashLoginAttempts"></a>
# **getNetworkSplashLoginAttempts**
> List&lt;Object&gt; getNetworkSplashLoginAttempts(networkId, ssidNumber, loginIdentifier, timespan)

List the splash login attempts for a network

List the splash login attempts for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplashLoginAttemptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashLoginAttemptsApi apiInstance = new SplashLoginAttemptsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer ssidNumber = 0; // Integer | Only return the login attempts for the specified SSID
    String loginIdentifier = "loginIdentifier_example"; // String | The username, email, or phone number used during login
    Integer timespan = 56; // Integer | The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months
    try {
      List<Object> result = apiInstance.getNetworkSplashLoginAttempts(networkId, ssidNumber, loginIdentifier, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashLoginAttemptsApi#getNetworkSplashLoginAttempts");
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
| **networkId** | **String**|  | |
| **ssidNumber** | **Integer**| Only return the login attempts for the specified SSID | [optional] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] |
| **loginIdentifier** | **String**| The username, email, or phone number used during login | [optional] |
| **timespan** | **Integer**| The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

