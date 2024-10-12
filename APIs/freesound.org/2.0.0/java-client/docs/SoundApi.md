# SoundApi

All URIs are relative to *http://www.freesound.org/apiv2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSoundById**](SoundApi.md#getSoundById) | **GET** /sounds/{soundId} | Details of a sound |


<a id="getSoundById"></a>
# **getSoundById**
> Sound getSoundById(soundId)

Details of a sound

This resource allows the retrieval of detailed information about a sound.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.freesound.org/apiv2");

    SoundApi apiInstance = new SoundApi(defaultClient);
    Long soundId = 56L; // Long | ID of the sound that needs to be fetched
    try {
      Sound result = apiInstance.getSoundById(soundId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundApi#getSoundById");
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
| **soundId** | **Long**| ID of the sound that needs to be fetched | |

### Return type

[**Sound**](Sound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | Order not found |  -  |

