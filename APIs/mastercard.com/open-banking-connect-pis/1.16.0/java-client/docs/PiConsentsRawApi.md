# PiConsentsRawApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsConsentsRawPost**](PiConsentsRawApi.md#paymentsConsentsRawPost) | **POST** /payments/consents/raw | Extracts the original raw consent given by the aspsp |


<a id="paymentsConsentsRawPost"></a>
# **paymentsConsentsRawPost**
> PostPaymentsConsentsRawOKBody paymentsConsentsRawPost(body)

Extracts the original raw consent given by the aspsp

Extracts the original raw consent given by the aspsp

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiConsentsRawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    PiConsentsRawApi apiInstance = new PiConsentsRawApi(defaultClient);
    PostPaymentsConsentsRawParamsBody body = new PostPaymentsConsentsRawParamsBody(); // PostPaymentsConsentsRawParamsBody | Request Body
    try {
      PostPaymentsConsentsRawOKBody result = apiInstance.paymentsConsentsRawPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiConsentsRawApi#paymentsConsentsRawPost");
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
| **body** | [**PostPaymentsConsentsRawParamsBody**](PostPaymentsConsentsRawParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsConsentsRawOKBody**](PostPaymentsConsentsRawOKBody.md)

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

