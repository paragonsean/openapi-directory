# TransactionRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clearAddress**](TransactionRequestsApi.md#clearAddress) | **POST** /clearAddress | clearAddress |
| [**sendEthereum**](TransactionRequestsApi.md#sendEthereum) | **POST** /sendEthereum | sendEthereum |
| [**sendToken**](TransactionRequestsApi.md#sendToken) | **POST** /sendToken | sendToken |


<a id="clearAddress"></a>
# **clearAddress**
> ClearAddress clearAddress(authorization, clearAddressRequest)

clearAddress

Sends all available ethereum funds of an address to a specified receiver address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    TransactionRequestsApi apiInstance = new TransactionRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    ClearAddressRequest clearAddressRequest = new ClearAddressRequest(); // ClearAddressRequest | 
    try {
      ClearAddress result = apiInstance.clearAddress(authorization, clearAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionRequestsApi#clearAddress");
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
| **authorization** | **String**| API Key | |
| **clearAddressRequest** | [**ClearAddressRequest**](ClearAddressRequest.md)|  | |

### Return type

[**ClearAddress**](ClearAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="sendEthereum"></a>
# **sendEthereum**
> SendEthereum sendEthereum(authorization, sendEthereumRequest)

sendEthereum

Sends ethereum from an address controlled by the account to a specified receiver address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    TransactionRequestsApi apiInstance = new TransactionRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    SendEthereumRequest sendEthereumRequest = new SendEthereumRequest(); // SendEthereumRequest | 
    try {
      SendEthereum result = apiInstance.sendEthereum(authorization, sendEthereumRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionRequestsApi#sendEthereum");
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
| **authorization** | **String**| API Key | |
| **sendEthereumRequest** | [**SendEthereumRequest**](SendEthereumRequest.md)|  | |

### Return type

[**SendEthereum**](SendEthereum.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="sendToken"></a>
# **sendToken**
> SendToken sendToken(authorization, sendTokenRequest)

sendToken

Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    TransactionRequestsApi apiInstance = new TransactionRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    SendTokenRequest sendTokenRequest = new SendTokenRequest(); // SendTokenRequest | 
    try {
      SendToken result = apiInstance.sendToken(authorization, sendTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionRequestsApi#sendToken");
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
| **authorization** | **String**| API Key | |
| **sendTokenRequest** | [**SendTokenRequest**](SendTokenRequest.md)|  | |

### Return type

[**SendToken**](SendToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

