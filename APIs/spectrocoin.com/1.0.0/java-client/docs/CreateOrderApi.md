# CreateOrderApi

All URIs are relative to *https://spectrocoin.com/api/merchant/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrder**](CreateOrderApi.md#createOrder) | **POST** /api/createOrder | Create merchant order |


<a id="createOrder"></a>
# **createOrder**
> OrderInformationClass createOrder(apiId, merchantId, payCurrency, receiveCurrency, sign, callbackUrl, culture, description, failureUrl, orderId, payAmount, payerEmail, payerName, payerSurname, receiveAmount, successUrl)

Create merchant order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreateOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spectrocoin.com/api/merchant/1");

    CreateOrderApi apiInstance = new CreateOrderApi(defaultClient);
    Long apiId = 56L; // Long | API ID of specific API you have configured on your merchant account
    Long merchantId = 56L; // Long | Merchant ID assigned to your account
    String payCurrency = "payCurrency_example"; // String | Currency of pay amount
    String receiveCurrency = "receiveCurrency_example"; // String | Currency of receive amount
    String sign = "sign_example"; // String | Signature required for signing create order request
    String callbackUrl = "callbackUrl_example"; // String | Url of merchant endpoint callback about order status to be returned
    String culture = "en"; // String | Merchant customer culture payment window to be presented
    String description = "description_example"; // String | Order description. Will be presented for merchant customer at payment window
    String failureUrl = "failureUrl_example"; // String | Url of merchant page customer should be redirected after unsuccessful payment
    String orderId = "orderId_example"; // String | Custom order ID. Must be unique per API. If not provided it will be generated.
    BigDecimal payAmount = new BigDecimal(78); // BigDecimal | Pay amount in pay currency of value which should be paid by merchant customer. If not provided receive amount will be used to calculate pay amount
    String payerEmail = "payerEmail_example"; // String | Specified payer email.
    String payerName = "payerName_example"; // String | Specified payer name.
    String payerSurname = "payerSurname_example"; // String | Specified payer surname.
    BigDecimal receiveAmount = new BigDecimal(78); // BigDecimal | Receive amount in receive currency of value that merchant will be funded after merchant customers payment approval. If not provided pay amount will be used to calculate receive amount
    String successUrl = "successUrl_example"; // String | Url of merchant page customer should be redirected after successful payment
    try {
      OrderInformationClass result = apiInstance.createOrder(apiId, merchantId, payCurrency, receiveCurrency, sign, callbackUrl, culture, description, failureUrl, orderId, payAmount, payerEmail, payerName, payerSurname, receiveAmount, successUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreateOrderApi#createOrder");
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
| **apiId** | **Long**| API ID of specific API you have configured on your merchant account | |
| **merchantId** | **Long**| Merchant ID assigned to your account | |
| **payCurrency** | **String**| Currency of pay amount | |
| **receiveCurrency** | **String**| Currency of receive amount | |
| **sign** | **String**| Signature required for signing create order request | |
| **callbackUrl** | **String**| Url of merchant endpoint callback about order status to be returned | [optional] |
| **culture** | **String**| Merchant customer culture payment window to be presented | [optional] [enum: en, lt, ru, de] |
| **description** | **String**| Order description. Will be presented for merchant customer at payment window | [optional] |
| **failureUrl** | **String**| Url of merchant page customer should be redirected after unsuccessful payment | [optional] |
| **orderId** | **String**| Custom order ID. Must be unique per API. If not provided it will be generated. | [optional] |
| **payAmount** | **BigDecimal**| Pay amount in pay currency of value which should be paid by merchant customer. If not provided receive amount will be used to calculate pay amount | [optional] |
| **payerEmail** | **String**| Specified payer email. | [optional] |
| **payerName** | **String**| Specified payer name. | [optional] |
| **payerSurname** | **String**| Specified payer surname. | [optional] |
| **receiveAmount** | **BigDecimal**| Receive amount in receive currency of value that merchant will be funded after merchant customers payment approval. If not provided pay amount will be used to calculate receive amount | [optional] |
| **successUrl** | **String**| Url of merchant page customer should be redirected after successful payment | [optional] |

### Return type

[**OrderInformationClass**](OrderInformationClass.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

