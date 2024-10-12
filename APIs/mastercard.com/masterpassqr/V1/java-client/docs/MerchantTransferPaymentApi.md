# MerchantTransferPaymentApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMerchantPayment**](MerchantTransferPaymentApi.md#createMerchantPayment) | **POST** /send/#env/v1/partners/{partnerId}/merchant/transfers/payment | Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account. |


<a id="createMerchantPayment"></a>
# **createMerchantPayment**
> MerchantTransfer40Wrapper createMerchantPayment(partnerId, merchantPaymentTransfer)

Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.

Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantTransferPaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantTransferPaymentApi apiInstance = new MerchantTransferPaymentApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    MerchantPaymentTransfer29Wrapper merchantPaymentTransfer = new MerchantPaymentTransfer29Wrapper(); // MerchantPaymentTransfer29Wrapper | Contains the details of the request message.
    try {
      MerchantTransfer40Wrapper result = apiInstance.createMerchantPayment(partnerId, merchantPaymentTransfer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantTransferPaymentApi#createMerchantPayment");
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
| **merchantPaymentTransfer** | [**MerchantPaymentTransfer29Wrapper**](MerchantPaymentTransfer29Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**MerchantTransfer40Wrapper**](MerchantTransfer40Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a merchant transfer. |  -  |

