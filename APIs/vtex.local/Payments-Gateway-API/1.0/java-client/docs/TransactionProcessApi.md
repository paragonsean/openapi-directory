# TransactionProcessApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**call1createanewtransaction**](TransactionProcessApi.md#call1createanewtransaction) | **POST** /api/pvt/transactions | 1. Starts a new transaction |
| [**call2sendPaymentsPublic**](TransactionProcessApi.md#call2sendPaymentsPublic) | **POST** /api/pub/transactions/{transactionId}/payments | 2.1 Send Payments Information Public |
| [**call2sendPaymentsWithSavedCreditCard**](TransactionProcessApi.md#call2sendPaymentsWithSavedCreditCard) | **POST** /api/pvt/transactions/{transactionId}/payments | 2.2 Send Payments With Saved Credit Card |
| [**call3sendAdditionalData**](TransactionProcessApi.md#call3sendAdditionalData) | **POST** /api/pvt/transactions/{transactionId}/additional-data | 3. Send Additional Data |
| [**call4doauthorization**](TransactionProcessApi.md#call4doauthorization) | **POST** /api/pvt/transactions/{transactionId}/authorization-request | Do authorization |
| [**paymentDetails**](TransactionProcessApi.md#paymentDetails) | **GET** /api/pvt/transactions/{transactionId}/payments/{paymentId} | Payment Details |
| [**transactionDetails**](TransactionProcessApi.md#transactionDetails) | **GET** /api/pvt/transactions/{transactionId} | Transaction Details |
| [**transactionSettlementDetails**](TransactionProcessApi.md#transactionSettlementDetails) | **GET** /api/pvt/transactions/{transactionId}/settlements | Transaction Settlement  Details |


<a id="call1createanewtransaction"></a>
# **call1createanewtransaction**
> StartTransactionResponse call1createanewtransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, model1CreateanewtransactionRequest)

1. Starts a new transaction

This request is the first step to create a new transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    Model1CreateanewtransactionRequest model1CreateanewtransactionRequest = new Model1CreateanewtransactionRequest(); // Model1CreateanewtransactionRequest | 
    try {
      StartTransactionResponse result = apiInstance.call1createanewtransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, model1CreateanewtransactionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#call1createanewtransaction");
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
| **model1CreateanewtransactionRequest** | [**Model1CreateanewtransactionRequest**](Model1CreateanewtransactionRequest.md)|  | |

### Return type

[**StartTransactionResponse**](StartTransactionResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Access-Control-Allow-Credentials -  <br>  * Access-Control-Allow-Origin -  <br>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * x-vtex-operation-id -  <br>  |

<a id="call2sendPaymentsPublic"></a>
# **call2sendPaymentsPublic**
> call2sendPaymentsPublic(orderId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsPublicRequest)

2.1 Send Payments Information Public

The second step to create a new transaction. Here, you have the option to send the data in three diferent ways: doing a private request, a public request or a private request that uses a saved Credit Card. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String orderId = "{{orderId}}"; // String | 
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    List<Model2SendPaymentsPublicRequest> model2SendPaymentsPublicRequest = Arrays.asList(); // List<Model2SendPaymentsPublicRequest> | 
    try {
      apiInstance.call2sendPaymentsPublic(orderId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsPublicRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#call2sendPaymentsPublic");
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
| **orderId** | **String**|  | |
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |
| **model2SendPaymentsPublicRequest** | [**List&lt;Model2SendPaymentsPublicRequest&gt;**](Model2SendPaymentsPublicRequest.md)|  | |

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

<a id="call2sendPaymentsWithSavedCreditCard"></a>
# **call2sendPaymentsWithSavedCreditCard**
> call2sendPaymentsWithSavedCreditCard(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsWithSavedCreditCardRequest)

2.2 Send Payments With Saved Credit Card

The second step to create a new transaction. Here, you have the option to send the data in three diferent ways: doing a private request, a public request or a private request that uses a saved Credit Card.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    List<Model2SendPaymentsWithSavedCreditCardRequest> model2SendPaymentsWithSavedCreditCardRequest = Arrays.asList(); // List<Model2SendPaymentsWithSavedCreditCardRequest> | 
    try {
      apiInstance.call2sendPaymentsWithSavedCreditCard(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsWithSavedCreditCardRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#call2sendPaymentsWithSavedCreditCard");
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
| **model2SendPaymentsWithSavedCreditCardRequest** | [**List&lt;Model2SendPaymentsWithSavedCreditCardRequest&gt;**](Model2SendPaymentsWithSavedCreditCardRequest.md)|  | |

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

<a id="call3sendAdditionalData"></a>
# **call3sendAdditionalData**
> call3sendAdditionalData(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, requestBody)

3. Send Additional Data

The third step to create a new transaction. It will send the additional related data to the transaction, like billig and shipping adress.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | Transaction identification.
    List<List<Object>> requestBody = new List(); // List<List<Object>> | 
    try {
      apiInstance.call3sendAdditionalData(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#call3sendAdditionalData");
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
| **transactionId** | **String**| Transaction identification. | |
| **requestBody** | [**List&lt;List&lt;Object&gt;&gt;**](List.md)|  | |

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
| **200** | OK |  -  |

<a id="call4doauthorization"></a>
# **call4doauthorization**
> call4doauthorization(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model4DoauthorizationRequest)

Do authorization

The fouth and last step to create a new transaction. It will authorized the new transction creation acorrdint to the data previously informed in the latests requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    Model4DoauthorizationRequest model4DoauthorizationRequest = new Model4DoauthorizationRequest(); // Model4DoauthorizationRequest | 
    try {
      apiInstance.call4doauthorization(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model4DoauthorizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#call4doauthorization");
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
| **model4DoauthorizationRequest** | [**Model4DoauthorizationRequest**](Model4DoauthorizationRequest.md)|  | |

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

<a id="paymentDetails"></a>
# **paymentDetails**
> PaymentDetailsResponse paymentDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId, paymentId)

Payment Details

Returns associated information details for the specified payment id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    String paymentId = "paymentId_example"; // String | 
    try {
      PaymentDetailsResponse result = apiInstance.paymentDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId, paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#paymentDetails");
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
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |
| **paymentId** | **String**|  | |

### Return type

[**PaymentDetailsResponse**](PaymentDetailsResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * x-vtex-operation-id -  <br>  |

<a id="transactionDetails"></a>
# **transactionDetails**
> TransactionDetailsResponse transactionDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId)

Transaction Details

Returns associated data for the specified transaction id, like value and status, for exemple.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    try {
      TransactionDetailsResponse result = apiInstance.transactionDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#transactionDetails");
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
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |

### Return type

[**TransactionDetailsResponse**](TransactionDetailsResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * x-vtex-operation-id -  <br>  |

<a id="transactionSettlementDetails"></a>
# **transactionSettlementDetails**
> TransactionSettlementDetails transactionSettlementDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId)

Transaction Settlement  Details

Returns associated settlements data for the specified transaction id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionProcessApi;

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

    TransactionProcessApi apiInstance = new TransactionProcessApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String transactionId = "transactionId_example"; // String | 
    try {
      TransactionSettlementDetails result = apiInstance.transactionSettlementDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionProcessApi#transactionSettlementDetails");
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
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **transactionId** | **String**|  | |

### Return type

[**TransactionSettlementDetails**](TransactionSettlementDetails.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * cache-control -  <br>  * connection -  <br>  * content-length -  <br>  * content-type -  <br>  * date -  <br>  * expires -  <br>  * pragma -  <br>  * server -  <br>  * x-aspnet-version -  <br>  * x-powered-by -  <br>  * x-vtex-operation-id -  <br>  |

