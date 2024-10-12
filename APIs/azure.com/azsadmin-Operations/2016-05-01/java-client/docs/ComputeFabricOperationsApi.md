# ComputeFabricOperationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeFabricOperationsGet**](ComputeFabricOperationsApi.md#computeFabricOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/System.{location}/providers/{provider}/fabricLocations/{location}/computeOperationResults/{computeOperationResult} |  |


<a id="computeFabricOperationsGet"></a>
# **computeFabricOperationsGet**
> OperationStatus computeFabricOperationsGet(subscriptionId, location, provider, computeOperationResult, apiVersion)



Get the status of a compute fabric operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeFabricOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeFabricOperationsApi apiInstance = new ComputeFabricOperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String provider = "provider_example"; // String | Name of the provider.
    String computeOperationResult = "computeOperationResult_example"; // String | Id of a compute fabric operation.
    String apiVersion = "2016-05-01"; // String | Client Api Version.
    try {
      OperationStatus result = apiInstance.computeFabricOperationsGet(subscriptionId, location, provider, computeOperationResult, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeFabricOperationsApi#computeFabricOperationsGet");
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
| **computeOperationResult** | **String**| Id of a compute fabric operation. | |
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

