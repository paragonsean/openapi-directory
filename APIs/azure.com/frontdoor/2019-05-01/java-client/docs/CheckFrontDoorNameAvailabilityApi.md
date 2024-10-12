# CheckFrontDoorNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkFrontDoorNameAvailability**](CheckFrontDoorNameAvailabilityApi.md#checkFrontDoorNameAvailability) | **POST** /providers/Microsoft.Network/checkFrontDoorNameAvailability |  |


<a id="checkFrontDoorNameAvailability"></a>
# **checkFrontDoorNameAvailability**
> CheckNameAvailabilityOutput checkFrontDoorNameAvailability(apiVersion, checkFrontDoorNameAvailabilityInput)



Check the availability of a Front Door resource name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckFrontDoorNameAvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckFrontDoorNameAvailabilityApi apiInstance = new CheckFrontDoorNameAvailabilityApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CheckNameAvailabilityInput checkFrontDoorNameAvailabilityInput = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
    try {
      CheckNameAvailabilityOutput result = apiInstance.checkFrontDoorNameAvailability(apiVersion, checkFrontDoorNameAvailabilityInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckFrontDoorNameAvailabilityApi#checkFrontDoorNameAvailability");
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

