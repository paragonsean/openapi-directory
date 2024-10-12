# CharityFinancialApi

All URIs are relative to *http://data.orghunter.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CharityfinancialPost**](CharityFinancialApi.md#v1CharityfinancialPost) | **POST** /v1/charityfinancial | Get details! |


<a id="v1CharityfinancialPost"></a>
# **v1CharityfinancialPost**
> v1CharityfinancialPost(ein)

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
import org.openapitools.client.api.CharityFinancialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data.orghunter.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CharityFinancialApi apiInstance = new CharityFinancialApi(defaultClient);
    String ein = "ein_example"; // String | ein (Employer Identification Number)
    try {
      apiInstance.v1CharityfinancialPost(ein);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharityFinancialApi#v1CharityfinancialPost");
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

