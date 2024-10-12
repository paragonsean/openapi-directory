# ValidateProbeApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**validateProbe**](ValidateProbeApi.md#validateProbe) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Cdn/validateProbe |  |


<a id="validateProbe"></a>
# **validateProbe**
> ValidateProbeOutput validateProbe(subscriptionId, apiVersion, validateProbeInput)



Check if the probe path is a valid path and the file can be accessed. Probe path is the path to a file hosted on the origin server to help accelerate the delivery of dynamic content via the CDN endpoint. This path is relative to the origin path specified in the endpoint configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidateProbeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ValidateProbeApi apiInstance = new ValidateProbeApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    ValidateProbeInput validateProbeInput = new ValidateProbeInput(); // ValidateProbeInput | Input to check.
    try {
      ValidateProbeOutput result = apiInstance.validateProbe(subscriptionId, apiVersion, validateProbeInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidateProbeApi#validateProbe");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **validateProbeInput** | [**ValidateProbeInput**](ValidateProbeInput.md)| Input to check. | |

### Return type

[**ValidateProbeOutput**](ValidateProbeOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

