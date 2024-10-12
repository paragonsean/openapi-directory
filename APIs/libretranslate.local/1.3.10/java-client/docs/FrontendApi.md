# FrontendApi

All URIs are relative to *http://libretranslate.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**frontendSettingsGet**](FrontendApi.md#frontendSettingsGet) | **GET** /frontend/settings | Retrieve frontend specific settings |


<a id="frontendSettingsGet"></a>
# **frontendSettingsGet**
> FrontendSettings frontendSettingsGet()

Retrieve frontend specific settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://libretranslate.local");

    FrontendApi apiInstance = new FrontendApi(defaultClient);
    try {
      FrontendSettings result = apiInstance.frontendSettingsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontendApi#frontendSettingsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FrontendSettings**](FrontendSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | frontend settings |  -  |

