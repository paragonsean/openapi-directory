# ServersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serversCheckNameAvailability**](ServersApi.md#serversCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/checkNameAvailability |  |


<a id="serversCheckNameAvailability"></a>
# **serversCheckNameAvailability**
> CheckNameAvailabilityResponse serversCheckNameAvailability(apiVersion, subscriptionId, parameters)



Determines whether a resource can be created with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    CheckNameAvailabilityRequest parameters = new CheckNameAvailabilityRequest(); // CheckNameAvailabilityRequest | The parameters to request for name availability.
    try {
      CheckNameAvailabilityResponse result = apiInstance.serversCheckNameAvailability(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversCheckNameAvailability");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **parameters** | [**CheckNameAvailabilityRequest**](CheckNameAvailabilityRequest.md)| The parameters to request for name availability. | |

### Return type

[**CheckNameAvailabilityResponse**](CheckNameAvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

