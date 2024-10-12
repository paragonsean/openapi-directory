# NetworkFabricOperationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkFabricOperationsGet**](NetworkFabricOperationsApi.md#networkFabricOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/System.{location}/providers/{provider}/fabricLocations/{location}/networkOperationResults/{networkOperationResult} |  |


<a id="networkFabricOperationsGet"></a>
# **networkFabricOperationsGet**
> OperationStatus networkFabricOperationsGet(subscriptionId, location, provider, networkOperationResult, apiVersion)



Get the status of a network fabric operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFabricOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkFabricOperationsApi apiInstance = new NetworkFabricOperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String provider = "provider_example"; // String | Name of the provider.
    String networkOperationResult = "networkOperationResult_example"; // String | Id of a network fabric operation.
    String apiVersion = "2016-05-01"; // String | Client Api Version.
    try {
      OperationStatus result = apiInstance.networkFabricOperationsGet(subscriptionId, location, provider, networkOperationResult, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFabricOperationsApi#networkFabricOperationsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **provider** | **String**| Name of the provider. | |
| **networkOperationResult** | **String**| Id of a network fabric operation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-05-01] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | ACCEPTED |  -  |

