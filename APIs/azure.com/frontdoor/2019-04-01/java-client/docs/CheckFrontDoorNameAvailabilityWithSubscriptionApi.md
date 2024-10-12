# CheckFrontDoorNameAvailabilityWithSubscriptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkFrontDoorNameAvailabilityWithSubscription**](CheckFrontDoorNameAvailabilityWithSubscriptionApi.md#checkFrontDoorNameAvailabilityWithSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Network/checkFrontDoorNameAvailability |  |


<a id="checkFrontDoorNameAvailabilityWithSubscription"></a>
# **checkFrontDoorNameAvailabilityWithSubscription**
> CheckNameAvailabilityOutput checkFrontDoorNameAvailabilityWithSubscription(subscriptionId, apiVersion, checkFrontDoorNameAvailabilityInput)



Check the availability of a Front Door subdomain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckFrontDoorNameAvailabilityWithSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckFrontDoorNameAvailabilityWithSubscriptionApi apiInstance = new CheckFrontDoorNameAvailabilityWithSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CheckNameAvailabilityInput checkFrontDoorNameAvailabilityInput = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
    try {
      CheckNameAvailabilityOutput result = apiInstance.checkFrontDoorNameAvailabilityWithSubscription(subscriptionId, apiVersion, checkFrontDoorNameAvailabilityInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckFrontDoorNameAvailabilityWithSubscriptionApi#checkFrontDoorNameAvailabilityWithSubscription");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **checkFrontDoorNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | |

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

