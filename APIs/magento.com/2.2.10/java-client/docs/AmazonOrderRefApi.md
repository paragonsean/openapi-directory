# AmazonOrderRefApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete**](AmazonOrderRefApi.md#amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete) | **DELETE** /V1/amazon/order-ref | amazon/order-ref |


<a id="amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete"></a>
# **amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete**
> ErrorResponse amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete()

amazon/order-ref



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AmazonOrderRefApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AmazonOrderRefApi apiInstance = new AmazonOrderRefApi(defaultClient);
    try {
      ErrorResponse result = apiInstance.amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmazonOrderRefApi#amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete");
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

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

