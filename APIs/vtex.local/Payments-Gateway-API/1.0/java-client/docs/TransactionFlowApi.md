# TransactionFlowApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelthetransaction**](TransactionFlowApi.md#cancelthetransaction) | **POST** /api/pvt/transactions/{transactionId}/cancellation-request | Cancel the transaction |
| [**refundthetransaction**](TransactionFlowApi.md#refundthetransaction) | **POST** /api/pvt/transactions/{transactionId}/refunding-request | Refund the transaction |
| [**settlethetransaction**](TransactionFlowApi.md#settlethetransaction) | **POST** /api/pvt/transactions/{transactionId}/settlement-request | Settle the transaction |


<a id="cancelthetransaction"></a>
# **cancelthetransaction**
> cancelthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, cancelthetransactionRequest)

Cancel the transaction

Cancel&#39;s transaction that was previously approved, but not settled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionFlowApi apiInstance = new TransactionFlowApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    CancelthetransactionRequest cancelthetransactionRequest = new CancelthetransactionRequest(); // CancelthetransactionRequest | 
    try {
      apiInstance.cancelthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, cancelthetransactionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionFlowApi#cancelthetransaction");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |
| **cancelthetransactionRequest** | [**CancelthetransactionRequest**](CancelthetransactionRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="refundthetransaction"></a>
# **refundthetransaction**
> refundthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, refundthetransactionRequest)

Refund the transaction

Refunds transaction&#39;s value that was previously settled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionFlowApi apiInstance = new TransactionFlowApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    RefundthetransactionRequest refundthetransactionRequest = new RefundthetransactionRequest(); // RefundthetransactionRequest | 
    try {
      apiInstance.refundthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, refundthetransactionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionFlowApi#refundthetransaction");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |
| **refundthetransactionRequest** | [**RefundthetransactionRequest**](RefundthetransactionRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="settlethetransaction"></a>
# **settlethetransaction**
> SettleResponse settlethetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, settlethetransactionRequest)

Settle the transaction

Settles transaction&#39;s value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionFlowApi apiInstance = new TransactionFlowApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    SettlethetransactionRequest settlethetransactionRequest = new SettlethetransactionRequest(); // SettlethetransactionRequest | 
    try {
      SettleResponse result = apiInstance.settlethetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, settlethetransactionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionFlowApi#settlethetransaction");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |
| **settlethetransactionRequest** | [**SettlethetransactionRequest**](SettlethetransactionRequest.md)|  | |

### Return type

[**SettleResponse**](SettleResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * cache-control -  <br>  * connection -  <br>  * content-length -  <br>  * content-type -  <br>  * date -  <br>  * expires -  <br>  * pragma -  <br>  * server -  <br>  * x-aspnet-version -  <br>  * x-powered-by -  <br>  * x-vtex-operation-id -  <br>  |

