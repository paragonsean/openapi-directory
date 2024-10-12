# TransfersApi

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postTransfers**](TransfersApi.md#postTransfers) | **POST** /transfers | Transfer funds |
| [**postTransfersTransferIdReturns**](TransfersApi.md#postTransfersTransferIdReturns) | **POST** /transfers/{transferId}/returns | Return a transfer |


<a id="postTransfers"></a>
# **postTransfers**
> Transfer postTransfers(wwWAuthenticate, transferInfo)

Transfer funds

&gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Starts a request to transfer funds to [balance accounts](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts), [transfer instruments](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments), or third-party bank accounts. Adyen sends the outcome of the transfer request through webhooks.  To use this endpoint, you need an additional role for your API credential and transfers must be enabled for the source balance account. Your Adyen contact will set these up for you.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balanceplatform-api-test.adyen.com/btl/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: clientKey
    ApiKeyAuth clientKey = (ApiKeyAuth) defaultClient.getAuthentication("clientKey");
    clientKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientKey.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String wwWAuthenticate = "SCA realm=\"Transfer\" auth-param1=\"eyJjaGFsbGVuZ2UiOiJiVlV6ZW5wek0waFNl...\""; // String | Header for authenticating through SCA
    TransferInfo transferInfo = new TransferInfo(); // TransferInfo | 
    try {
      Transfer result = apiInstance.postTransfers(wwWAuthenticate, transferInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#postTransfers");
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
| **wwWAuthenticate** | **String**| Header for authenticating through SCA | [optional] |
| **transferInfo** | [**TransferInfo**](TransferInfo.md)|  | [optional] |

### Return type

[**Transfer**](Transfer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **401** | Unauthorized - authentication required. |  * auth-param1 -  <br>  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postTransfersTransferIdReturns"></a>
# **postTransfersTransferIdReturns**
> ReturnTransferResponse postTransfersTransferIdReturns(transferId, returnTransferRequest)

Return a transfer

Returns previously transferred funds without creating a new &#x60;transferId&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balanceplatform-api-test.adyen.com/btl/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: clientKey
    ApiKeyAuth clientKey = (ApiKeyAuth) defaultClient.getAuthentication("clientKey");
    clientKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientKey.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String transferId = "transferId_example"; // String | The unique identifier of the transfer to be returned.
    ReturnTransferRequest returnTransferRequest = new ReturnTransferRequest(); // ReturnTransferRequest | 
    try {
      ReturnTransferResponse result = apiInstance.postTransfersTransferIdReturns(transferId, returnTransferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#postTransfersTransferIdReturns");
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
| **transferId** | **String**| The unique identifier of the transfer to be returned. | |
| **returnTransferRequest** | [**ReturnTransferRequest**](ReturnTransferRequest.md)|  | [optional] |

### Return type

[**ReturnTransferResponse**](ReturnTransferResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

