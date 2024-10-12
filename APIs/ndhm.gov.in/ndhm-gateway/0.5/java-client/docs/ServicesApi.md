# ServicesApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05HiServicesServiceIdGet**](ServicesApi.md#v05HiServicesServiceIdGet) | **GET** /v0.5/hi-services/{service-id} | Get bridge service details/profile by the serviceId provided. |


<a id="v05HiServicesServiceIdGet"></a>
# **v05HiServicesServiceIdGet**
> ServiceProfileResponse v05HiServicesServiceIdGet(authorization, serviceId)

Get bridge service details/profile by the serviceId provided.

This API is meant for displaying the bridge service details by the serviceId provided . 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String serviceId = "serviceId_example"; // String | 
    try {
      ServiceProfileResponse result = apiInstance.v05HiServicesServiceIdGet(authorization, serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#v05HiServicesServiceIdGet");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **serviceId** | **String**|  | |

### Return type

[**ServiceProfileResponse**](ServiceProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | service details fetched successfully |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **404** | Service doesn&#39;t exist. |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

