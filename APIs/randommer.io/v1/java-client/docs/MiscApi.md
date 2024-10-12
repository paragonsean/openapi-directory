# MiscApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMiscCulturesGet**](MiscApi.md#apiMiscCulturesGet) | **GET** /api/Misc/Cultures |  |
| [**apiMiscRandomAddressGet**](MiscApi.md#apiMiscRandomAddressGet) | **GET** /api/Misc/Random-Address |  |


<a id="apiMiscCulturesGet"></a>
# **apiMiscCulturesGet**
> apiMiscCulturesGet(xApiKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MiscApi apiInstance = new MiscApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiMiscCulturesGet(xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscApi#apiMiscCulturesGet");
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
| **xApiKey** | **String**| Enter your key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiMiscRandomAddressGet"></a>
# **apiMiscRandomAddressGet**
> apiMiscRandomAddressGet(number, culture, xApiKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MiscApi apiInstance = new MiscApi(defaultClient);
    Integer number = 56; // Integer | 
    String culture = "en"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiMiscRandomAddressGet(number, culture, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscApi#apiMiscRandomAddressGet");
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
| **number** | **Integer**|  | |
| **culture** | **String**|  | [optional] [default to en] |
| **xApiKey** | **String**| Enter your key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

