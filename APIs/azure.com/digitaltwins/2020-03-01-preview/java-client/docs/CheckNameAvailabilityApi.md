# CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**digitalTwinsCheckNameAvailability**](CheckNameAvailabilityApi.md#digitalTwinsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DigitalTwins/locations/{location}/checkNameAvailability |  |


<a id="digitalTwinsCheckNameAvailability"></a>
# **digitalTwinsCheckNameAvailability**
> CheckNameResult digitalTwinsCheckNameAvailability(apiVersion, subscriptionId, location, digitalTwinsInstanceCheckName)



Check if a DigitalTwinsInstance name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckNameAvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckNameAvailabilityApi apiInstance = new CheckNameAvailabilityApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String location = "location_example"; // String | Location of DigitalTwinsInstance.
    CheckNameRequest digitalTwinsInstanceCheckName = new CheckNameRequest(); // CheckNameRequest | Set the name parameter in the DigitalTwinsInstanceCheckName structure to the name of the DigitalTwinsInstance to check.
    try {
      CheckNameResult result = apiInstance.digitalTwinsCheckNameAvailability(apiVersion, subscriptionId, location, digitalTwinsInstanceCheckName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckNameAvailabilityApi#digitalTwinsCheckNameAvailability");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **location** | **String**| Location of DigitalTwinsInstance. | |
| **digitalTwinsInstanceCheckName** | [**CheckNameRequest**](CheckNameRequest.md)| Set the name parameter in the DigitalTwinsInstanceCheckName structure to the name of the DigitalTwinsInstance to check. | |

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the DigitalTwins service name is available. If the name is not available, the body contains the reason. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

