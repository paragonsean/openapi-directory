# StorageSyncServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageSyncServicesCheckNameAvailability**](StorageSyncServiceApi.md#storageSyncServicesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.StorageSync/locations/{locationName}/checkNameAvailability |  |


<a id="storageSyncServicesCheckNameAvailability"></a>
# **storageSyncServicesCheckNameAvailability**
> CheckNameAvailabilityResult storageSyncServicesCheckNameAvailability(locationName, apiVersion, subscriptionId, parameters)



Check the give namespace name availability.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServiceApi apiInstance = new StorageSyncServiceApi(defaultClient);
    String locationName = "locationName_example"; // String | The desired region for the name check.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    CheckNameAvailabilityParameters parameters = new CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Parameters to check availability of the given namespace name
    try {
      CheckNameAvailabilityResult result = apiInstance.storageSyncServicesCheckNameAvailability(locationName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServiceApi#storageSyncServicesCheckNameAvailability");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Parameters to check availability of the given namespace name | |

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
| **200** | check availability returned successfully. |  -  |

