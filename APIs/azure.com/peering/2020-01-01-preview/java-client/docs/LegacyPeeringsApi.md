# LegacyPeeringsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**legacyPeeringsList**](LegacyPeeringsApi.md#legacyPeeringsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/legacyPeerings |  |


<a id="legacyPeeringsList"></a>
# **legacyPeeringsList**
> PeeringListResult legacyPeeringsList(peeringLocation, kind, subscriptionId, apiVersion, asn)



Lists all of the legacy peerings under the given subscription matching the specified kind and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacyPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LegacyPeeringsApi apiInstance = new LegacyPeeringsApi(defaultClient);
    String peeringLocation = "peeringLocation_example"; // String | The location of the peering.
    String kind = "Direct"; // String | The kind of the peering.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    Integer asn = 56; // Integer | The ASN number associated with a legacy peering.
    try {
      PeeringListResult result = apiInstance.legacyPeeringsList(peeringLocation, kind, subscriptionId, apiVersion, asn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacyPeeringsApi#legacyPeeringsList");
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
| **peeringLocation** | **String**| The location of the peering. | |
| **kind** | **String**| The kind of the peering. | [enum: Direct, Exchange] |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **asn** | **Integer**| The ASN number associated with a legacy peering. | [optional] |

### Return type

[**PeeringListResult**](PeeringListResult.md)

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

