# CustomGatewayProcessPaymentsAndRefundsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customGatewayPaymentOwnershipIdPost**](CustomGatewayProcessPaymentsAndRefundsApi.md#customGatewayPaymentOwnershipIdPost) | **POST** /custom-gateway/payment/{ownershipId} | Adds a payment for an app on behalf of a user |
| [**customGatewayRefundOwnershipIdPost**](CustomGatewayProcessPaymentsAndRefundsApi.md#customGatewayRefundOwnershipIdPost) | **POST** /custom-gateway/refund/{ownershipId} | Fully or partially refund payment for an app on behalf of a user |


<a id="customGatewayPaymentOwnershipIdPost"></a>
# **customGatewayPaymentOwnershipIdPost**
> Transaction customGatewayPaymentOwnershipIdPost(ownershipId, amount, date, feeAmount, marketplaceAmount, developerAmount, customData)

Adds a payment for an app on behalf of a user

- Results are returned for the market provided within the basic authentication credentials  - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomGatewayProcessPaymentsAndRefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CustomGatewayProcessPaymentsAndRefundsApi apiInstance = new CustomGatewayProcessPaymentsAndRefundsApi(defaultClient);
    String ownershipId = "ownershipId_example"; // String | The id of the ownership record involved in this transaction
    Integer amount = 56; // Integer | The total amount paid in cents
    Long date = 56L; // Long | The date (in milliseconds) of when this payment was made
    Integer feeAmount = 56; // Integer | The fee (in cents) paid to a payment processors or third parties to process this payment. Default is 0.
    Integer marketplaceAmount = 56; // Integer | The amount (in cents) paid to the marketplace owner as a commission for the purchase of this app. Defaults based on the commission amount configured for this marketplace.
    Integer developerAmount = 56; // Integer | The amount (in cents) paid to the owner of the app. Defaults based on the commission amount configured for this marketplace.
    String customData = "customData_example"; // String | A custom JSON object to attach to this transaction
    try {
      Transaction result = apiInstance.customGatewayPaymentOwnershipIdPost(ownershipId, amount, date, feeAmount, marketplaceAmount, developerAmount, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomGatewayProcessPaymentsAndRefundsApi#customGatewayPaymentOwnershipIdPost");
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
| **ownershipId** | **String**| The id of the ownership record involved in this transaction | |
| **amount** | **Integer**| The total amount paid in cents | |
| **date** | **Long**| The date (in milliseconds) of when this payment was made | [optional] |
| **feeAmount** | **Integer**| The fee (in cents) paid to a payment processors or third parties to process this payment. Default is 0. | [optional] |
| **marketplaceAmount** | **Integer**| The amount (in cents) paid to the marketplace owner as a commission for the purchase of this app. Defaults based on the commission amount configured for this marketplace. | [optional] |
| **developerAmount** | **Integer**| The amount (in cents) paid to the owner of the app. Defaults based on the commission amount configured for this marketplace. | [optional] |
| **customData** | **String**| A custom JSON object to attach to this transaction | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **412** | Precondition Failed - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint |  -  |
| **0** | OK |  -  |

<a id="customGatewayRefundOwnershipIdPost"></a>
# **customGatewayRefundOwnershipIdPost**
> Transaction customGatewayRefundOwnershipIdPost(ownershipId, amount, date, feeAmount, marketplaceAmount, developerAmount, customData)

Fully or partially refund payment for an app on behalf of a user

- Results are returned for the market provided within the basic authentication credentials - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomGatewayProcessPaymentsAndRefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CustomGatewayProcessPaymentsAndRefundsApi apiInstance = new CustomGatewayProcessPaymentsAndRefundsApi(defaultClient);
    String ownershipId = "ownershipId_example"; // String | The id of the ownership record involved in this transaction
    Integer amount = 56; // Integer | The total amount refunded in cents
    Long date = 56L; // Long | The date (in milliseconds) of when this refund was made
    Integer feeAmount = 56; // Integer | The fee (in cents) recovered from a payment processor or third party to process this payment. The default value is 0
    Integer marketplaceAmount = 56; // Integer | The amount (in cents) recovered from the marketplace owner as a commission refund for the purchase of this app
    Integer developerAmount = 56; // Integer | The amount (in cents) recovered from the owner of the app
    String customData = "customData_example"; // String | A custom JSON object to attach to this transaction
    try {
      Transaction result = apiInstance.customGatewayRefundOwnershipIdPost(ownershipId, amount, date, feeAmount, marketplaceAmount, developerAmount, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomGatewayProcessPaymentsAndRefundsApi#customGatewayRefundOwnershipIdPost");
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
| **ownershipId** | **String**| The id of the ownership record involved in this transaction | |
| **amount** | **Integer**| The total amount refunded in cents | |
| **date** | **Long**| The date (in milliseconds) of when this refund was made | [optional] |
| **feeAmount** | **Integer**| The fee (in cents) recovered from a payment processor or third party to process this payment. The default value is 0 | [optional] |
| **marketplaceAmount** | **Integer**| The amount (in cents) recovered from the marketplace owner as a commission refund for the purchase of this app | [optional] |
| **developerAmount** | **Integer**| The amount (in cents) recovered from the owner of the app | [optional] |
| **customData** | **String**| A custom JSON object to attach to this transaction | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **412** | Precondition Failed - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint |  -  |
| **0** | OK |  -  |

