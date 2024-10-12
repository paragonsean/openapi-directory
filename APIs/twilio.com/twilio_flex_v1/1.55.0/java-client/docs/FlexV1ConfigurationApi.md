# FlexV1ConfigurationApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchConfiguration**](FlexV1ConfigurationApi.md#fetchConfiguration) | **GET** /v1/Configuration |  |


<a id="fetchConfiguration"></a>
# **fetchConfiguration**
> FlexV1Configuration fetchConfiguration(uiVersion)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1ConfigurationApi apiInstance = new FlexV1ConfigurationApi(defaultClient);
    String uiVersion = "uiVersion_example"; // String | The Pinned UI version of the Configuration resource to fetch.
    try {
      FlexV1Configuration result = apiInstance.fetchConfiguration(uiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1ConfigurationApi#fetchConfiguration");
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
| **uiVersion** | **String**| The Pinned UI version of the Configuration resource to fetch. | [optional] |

### Return type

[**FlexV1Configuration**](FlexV1Configuration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

