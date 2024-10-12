# AspspsApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsAspspsPost**](AspspsApi.md#paymentsAspspsPost) | **POST** /payments/aspsps | Get list of ASPSPs |


<a id="paymentsAspspsPost"></a>
# **paymentsAspspsPost**
> PostAspspsOKBody paymentsAspspsPost(body)

Get list of ASPSPs

Get the list of all active ASPSPs supported by the Open Banking Connect platform at this time with possibility to filter by id, name or country. This list is updated regularly as new ASPSPs are connected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AspspsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    AspspsApi apiInstance = new AspspsApi(defaultClient);
    PostAspspsParamsBody body = new PostAspspsParamsBody(); // PostAspspsParamsBody | Request Body
    try {
      PostAspspsOKBody result = apiInstance.paymentsAspspsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AspspsApi#paymentsAspspsPost");
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
| **body** | [**PostAspspsParamsBody**](PostAspspsParamsBody.md)| Request Body | |

### Return type

[**PostAspspsOKBody**](PostAspspsOKBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Error |  -  |
| **504** | Server while acting as a gateway or proxy, cannot get a response in time. |  -  |

