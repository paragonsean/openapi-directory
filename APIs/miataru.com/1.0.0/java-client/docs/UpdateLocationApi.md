# UpdateLocationApi

All URIs are relative to *http://service.miataru.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateLocation**](UpdateLocationApi.md#updateLocation) | **POST** /UpdateLocation |  |


<a id="updateLocation"></a>
# **updateLocation**
> ACK updateLocation(body)



This method is used to update the location of a device. The device does not need to be known already to the Miataru server but it rather creates a unique identifier for itself in the client application. This unique identifier, or device ID is then used to address this particular device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateLocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.miataru.com/v1");

    UpdateLocationApi apiInstance = new UpdateLocationApi(defaultClient);
    MiataruUpdateLocationRequest body = new MiataruUpdateLocationRequest(); // MiataruUpdateLocationRequest | the body of this UpdateLocation POST request contains the JSON formatted parameters.
    try {
      ACK result = apiInstance.updateLocation(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateLocationApi#updateLocation");
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
| **body** | [**MiataruUpdateLocationRequest**](MiataruUpdateLocationRequest.md)| the body of this UpdateLocation POST request contains the JSON formatted parameters. | |

### Return type

[**ACK**](ACK.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful request |  -  |

