# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationCheckNameAvailability**](DefaultApi.md#locationCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/checkNameAvailability |  |


<a id="locationCheckNameAvailability"></a>
# **locationCheckNameAvailability**
> CheckNameAvailabilityResult locationCheckNameAvailability(locationName, apiVersion, subscriptionId, parameters)



Checks whether the Batch account name is available in the specified region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String locationName = "locationName_example"; // String | The desired region for the name check.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    CheckNameAvailabilityParameters parameters = new CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Properties needed to check the availability of a name.
    try {
      CheckNameAvailabilityResult result = apiInstance.locationCheckNameAvailability(locationName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#locationCheckNameAvailability");
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
| **locationName** | **String**| The desired region for the name check. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Properties needed to check the availability of a name. | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Returns details about whether a Batch account name is available. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

