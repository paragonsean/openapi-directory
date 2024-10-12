# NetworksApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRadioNetworks**](NetworksApi.md#getRadioNetworks) | **GET** /radio/networks.json | Networks |


<a id="getRadioNetworks"></a>
# **getRadioNetworks**
> NetworksResponse getRadioNetworks(xAPIKey, preset, international)

Networks

All iPlayer Radio networks - contains business logic for masterbrand and service relationships 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Boolean preset = true; // Boolean | Returns all networks needed for iPlayer Radio responsive web navigation
    Boolean international = true; // Boolean | Returns all networks available internationally
    try {
      NetworksResponse result = apiInstance.getRadioNetworks(xAPIKey, preset, international);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getRadioNetworks");
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
| **xAPIKey** | **String**| API_KEY | |
| **preset** | **Boolean**| Returns all networks needed for iPlayer Radio responsive web navigation | [optional] |
| **international** | **Boolean**| Returns all networks available internationally | [optional] |

### Return type

[**NetworksResponse**](NetworksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

