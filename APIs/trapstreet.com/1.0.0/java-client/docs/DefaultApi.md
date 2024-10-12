# DefaultApi

All URIs are relative to *https://api.trapstreet.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addressGet**](DefaultApi.md#addressGet) | **GET** /{address} |  |


<a id="addressGet"></a>
# **addressGet**
> AddressGet200Response addressGet(address)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trapstreet.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String address = "address_example"; // String | 
    try {
      AddressGet200Response result = apiInstance.addressGet(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addressGet");
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
| **address** | **String**|  | |

### Return type

[**AddressGet200Response**](AddressGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

