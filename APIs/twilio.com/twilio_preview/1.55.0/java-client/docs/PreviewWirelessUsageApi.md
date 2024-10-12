# PreviewWirelessUsageApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchWirelessUsage**](PreviewWirelessUsageApi.md#fetchWirelessUsage) | **GET** /wireless/Sims/{SimSid}/Usage |  |


<a id="fetchWirelessUsage"></a>
# **fetchWirelessUsage**
> PreviewWirelessSimUsage fetchWirelessUsage(simSid, end, start)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessUsageApi apiInstance = new PreviewWirelessUsageApi(defaultClient);
    String simSid = "simSid_example"; // String | 
    String end = "end_example"; // String | 
    String start = "start_example"; // String | 
    try {
      PreviewWirelessSimUsage result = apiInstance.fetchWirelessUsage(simSid, end, start);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessUsageApi#fetchWirelessUsage");
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
| **simSid** | **String**|  | |
| **end** | **String**|  | [optional] |
| **start** | **String**|  | [optional] |

### Return type

[**PreviewWirelessSimUsage**](PreviewWirelessSimUsage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

