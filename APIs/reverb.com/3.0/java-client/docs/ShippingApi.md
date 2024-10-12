# ShippingApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shippingProvidersGet**](ShippingApi.md#shippingProvidersGet) | **GET** /shipping/providers | List of supported shipping providers |
| [**shippingRegionsGet**](ShippingApi.md#shippingRegionsGet) | **GET** /shipping/regions |  |


<a id="shippingProvidersGet"></a>
# **shippingProvidersGet**
> shippingProvidersGet()

List of supported shipping providers

List of supported shipping providers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShippingApi apiInstance = new ShippingApi(defaultClient);
    try {
      apiInstance.shippingProvidersGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingApi#shippingProvidersGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="shippingRegionsGet"></a>
# **shippingRegionsGet**
> shippingRegionsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ShippingApi apiInstance = new ShippingApi(defaultClient);
    try {
      apiInstance.shippingRegionsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingApi#shippingRegionsGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

