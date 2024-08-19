# MerchantRefundApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMerchantRefund**](MerchantRefundApi.md#createMerchantRefund) | **POST** /send/#env/v1/partners/{partnerId}/merchant/transfers/refund | Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account. |


<a id="createMerchantRefund"></a>
# **createMerchantRefund**
> MerchantTransfer104Wrapper createMerchantRefund(partnerId, merchantRefundTransfer)

Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.

Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantRefundApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantRefundApi apiInstance = new MerchantRefundApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    MerchantRefundTransfer93Wrapper merchantRefundTransfer = new MerchantRefundTransfer93Wrapper(); // MerchantRefundTransfer93Wrapper | Contains the details of the request message.
    try {
      MerchantTransfer104Wrapper result = apiInstance.createMerchantRefund(partnerId, merchantRefundTransfer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantRefundApi#createMerchantRefund");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | |
| **merchantRefundTransfer** | [**MerchantRefundTransfer93Wrapper**](MerchantRefundTransfer93Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**MerchantTransfer104Wrapper**](MerchantTransfer104Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a merchant transfer. |  -  |

