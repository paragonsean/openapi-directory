# MerchantTransferFundingAndPaymentApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMerchantTransfer**](MerchantTransferFundingAndPaymentApi.md#createMerchantTransfer) | **POST** /send/#env/v1/partners/{partnerId}/merchant/transfer | Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction. |


<a id="createMerchantTransfer"></a>
# **createMerchantTransfer**
> MerchantTransfer14Wrapper createMerchantTransfer(partnerId, merchantTransfer)

Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.

Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantTransferFundingAndPaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantTransferFundingAndPaymentApi apiInstance = new MerchantTransferFundingAndPaymentApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32
    MerchantTransfer1Wrapper merchantTransfer = new MerchantTransfer1Wrapper(); // MerchantTransfer1Wrapper | Contains the details of the request message.
    try {
      MerchantTransfer14Wrapper result = apiInstance.createMerchantTransfer(partnerId, merchantTransfer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantTransferFundingAndPaymentApi#createMerchantTransfer");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32 | |
| **merchantTransfer** | [**MerchantTransfer1Wrapper**](MerchantTransfer1Wrapper.md)| Contains the details of the request message. | |

### Return type

[**MerchantTransfer14Wrapper**](MerchantTransfer14Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a merchant transfer. |  -  |

