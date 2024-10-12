# PlayDtmfApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startDTMF**](PlayDtmfApi.md#startDTMF) | **PUT** /{uuid}/dtmf | Play DTMF tones into a call |


<a id="startDTMF"></a>
# **startDTMF**
> DTMFResponse startDTMF(uuid, dtMFRequest)

Play DTMF tones into a call

Play DTMF tones into a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayDtmfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayDtmfApi apiInstance = new PlayDtmfApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
    DTMFRequest dtMFRequest = new DTMFRequest(); // DTMFRequest | action to perform
    try {
      DTMFResponse result = apiInstance.startDTMF(uuid, dtMFRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayDtmfApi#startDTMF");
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
| **uuid** | **String**| UUID of the Call Leg | |
| **dtMFRequest** | [**DTMFRequest**](DTMFRequest.md)| action to perform | |

### Return type

[**DTMFResponse**](DTMFResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

