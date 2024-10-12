# PeeringLocationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peeringLocationsList**](PeeringLocationsApi.md#peeringLocationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringLocations |  |


<a id="peeringLocationsList"></a>
# **peeringLocationsList**
> PeeringLocationListResult peeringLocationsList(kind, subscriptionId, apiVersion, directPeeringType)



Lists all of the available peering locations for the specified kind of peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringLocationsApi apiInstance = new PeeringLocationsApi(defaultClient);
    String kind = "Direct"; // String | The kind of the peering.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String directPeeringType = "Edge"; // String | The type of direct peering.
    try {
      PeeringLocationListResult result = apiInstance.peeringLocationsList(kind, subscriptionId, apiVersion, directPeeringType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringLocationsApi#peeringLocationsList");
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
| **kind** | **String**| The kind of the peering. | [enum: Direct, Exchange] |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **directPeeringType** | **String**| The type of direct peering. | [optional] [enum: Edge, Transit, Cdn, Internal] |

### Return type

[**PeeringLocationListResult**](PeeringLocationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

