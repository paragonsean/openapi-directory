# CharityPremiumApi

All URIs are relative to *http://data.orghunter.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CharitypremiumPost**](CharityPremiumApi.md#v1CharitypremiumPost) | **POST** /v1/charitypremium | Get details! |


<a id="v1CharitypremiumPost"></a>
# **v1CharitypremiumPost**
> v1CharitypremiumPost(ein)

Get details!

&lt;p&gt;This operation detail data.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharityPremiumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data.orghunter.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CharityPremiumApi apiInstance = new CharityPremiumApi(defaultClient);
    String ein = "ein_example"; // String | ein (Employer Identification Number)
    try {
      apiInstance.v1CharitypremiumPost(ein);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharityPremiumApi#v1CharitypremiumPost");
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
| **ein** | **String**| ein (Employer Identification Number) | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

