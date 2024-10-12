# FraudManagementApi

All URIs are relative to *https://api.nexmo.com/verify*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkUnblock**](FraudManagementApi.md#networkUnblock) | **POST** /network-unblock | Request a network unblock |


<a id="networkUnblock"></a>
# **networkUnblock**
> NetworkUnblockResponseOk networkUnblock(networkUnblock)

Request a network unblock

Request to unblock a network that has been blocked due to potential fraud detection &lt;div class&#x3D;\&quot;Vlt-callout Vlt-callout--critical\&quot;&gt;   &lt;div class&#x3D;\&quot;Vlt-callout__content\&quot;&gt;     &lt;h4&gt;Network Unblock is switched off by default.&lt;/h4&gt;     Please contact Sales to enable the Network Unblock API for your account.   &lt;/div&gt; &lt;/div&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FraudManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/verify");

    FraudManagementApi apiInstance = new FraudManagementApi(defaultClient);
    NetworkUnblock networkUnblock = new NetworkUnblock(); // NetworkUnblock | 
    try {
      NetworkUnblockResponseOk result = apiInstance.networkUnblock(networkUnblock);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FraudManagementApi#networkUnblock");
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
| **networkUnblock** | [**NetworkUnblock**](NetworkUnblock.md)|  | |

### Return type

[**NetworkUnblockResponseOk**](NetworkUnblockResponseOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |
| **429** | Rate Limited |  -  |

