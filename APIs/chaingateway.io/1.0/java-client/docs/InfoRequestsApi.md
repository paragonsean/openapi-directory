# InfoRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBlock**](InfoRequestsApi.md#getBlock) | **POST** /getBlock | getBlock |
| [**getEthereumBalance**](InfoRequestsApi.md#getEthereumBalance) | **POST** /getEthereumBalance | getEthereumBalance |
| [**getExchangeRate**](InfoRequestsApi.md#getExchangeRate) | **POST** /getExchangeRate | getExchangeRate |
| [**getGasPrice**](InfoRequestsApi.md#getGasPrice) | **POST** /getGasPrice | getGasPrice |
| [**getLastBlockNumber**](InfoRequestsApi.md#getLastBlockNumber) | **POST** /getLastBlockNumber | getLastBlockNumber |
| [**getToken**](InfoRequestsApi.md#getToken) | **POST** /getToken | getToken |
| [**getTokenBalance**](InfoRequestsApi.md#getTokenBalance) | **POST** /getTokenBalance | getTokenBalance |
| [**getTransactions**](InfoRequestsApi.md#getTransactions) | **POST** /getTransactions | getTransactions |


<a id="getBlock"></a>
# **getBlock**
> GetBlock getBlock(authorization, getBlockRequest)

getBlock

Returns information of an ethereum block with or without transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    GetBlockRequest getBlockRequest = new GetBlockRequest(); // GetBlockRequest | 
    try {
      GetBlock result = apiInstance.getBlock(authorization, getBlockRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getBlock");
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
| **getBlockRequest** | [**GetBlockRequest**](GetBlockRequest.md)|  | |

### Return type

[**GetBlock**](GetBlock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getEthereumBalance"></a>
# **getEthereumBalance**
> GetEthereumBalance getEthereumBalance(authorization, getEthereumBalanceRequest)

getEthereumBalance

Returns the ethereum balance of a given address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    GetEthereumBalanceRequest getEthereumBalanceRequest = new GetEthereumBalanceRequest(); // GetEthereumBalanceRequest | 
    try {
      GetEthereumBalance result = apiInstance.getEthereumBalance(authorization, getEthereumBalanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getEthereumBalance");
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
| **getEthereumBalanceRequest** | [**GetEthereumBalanceRequest**](GetEthereumBalanceRequest.md)|  | |

### Return type

[**GetEthereumBalance**](GetEthereumBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getExchangeRate"></a>
# **getExchangeRate**
> GetExchangeRate getExchangeRate(authorization, getExchangeRateRequest)

getExchangeRate

Returns the current Ethereum price in Euro or US Dollar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    GetExchangeRateRequest getExchangeRateRequest = new GetExchangeRateRequest(); // GetExchangeRateRequest | 
    try {
      GetExchangeRate result = apiInstance.getExchangeRate(authorization, getExchangeRateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getExchangeRate");
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
| **getExchangeRateRequest** | [**GetExchangeRateRequest**](GetExchangeRateRequest.md)|  | |

### Return type

[**GetExchangeRate**](GetExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getGasPrice"></a>
# **getGasPrice**
> GetGasPrice getGasPrice(contentType, authorization)

getGasPrice

Returns the current gas price in GWEI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String contentType = "application/json"; // String | 
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    try {
      GetGasPrice result = apiInstance.getGasPrice(contentType, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getGasPrice");
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
| **contentType** | **String**|  | |
| **authorization** | **String**| API Key | |

### Return type

[**GetGasPrice**](GetGasPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getLastBlockNumber"></a>
# **getLastBlockNumber**
> GetLastBlockNumber getLastBlockNumber(contentType, authorization)

getLastBlockNumber

Returns the block number of the last mined ethereum block.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String contentType = "application/json"; // String | 
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    try {
      GetLastBlockNumber result = apiInstance.getLastBlockNumber(contentType, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getLastBlockNumber");
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
| **contentType** | **String**|  | |
| **authorization** | **String**| API Key | |

### Return type

[**GetLastBlockNumber**](GetLastBlockNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getToken"></a>
# **getToken**
> GetToken getToken(authorization, getTokenRequest)

getToken

Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    GetTokenRequest getTokenRequest = new GetTokenRequest(); // GetTokenRequest | 
    try {
      GetToken result = apiInstance.getToken(authorization, getTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getToken");
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
| **getTokenRequest** | [**GetTokenRequest**](GetTokenRequest.md)|  | |

### Return type

[**GetToken**](GetToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getTokenBalance"></a>
# **getTokenBalance**
> GetTokenBalance getTokenBalance(authorization, getTokenBalanceRequest)

getTokenBalance

Returns the token balance of a given address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    GetTokenBalanceRequest getTokenBalanceRequest = new GetTokenBalanceRequest(); // GetTokenBalanceRequest | 
    try {
      GetTokenBalance result = apiInstance.getTokenBalance(authorization, getTokenBalanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getTokenBalance");
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
| **getTokenBalanceRequest** | [**GetTokenBalanceRequest**](GetTokenBalanceRequest.md)|  | |

### Return type

[**GetTokenBalance**](GetTokenBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getTransactions"></a>
# **getTransactions**
> GetTransactions getTransactions(authorization, getTransactionsRequest)

getTransactions

Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    InfoRequestsApi apiInstance = new InfoRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    GetTransactionsRequest getTransactionsRequest = new GetTransactionsRequest(); // GetTransactionsRequest | 
    try {
      GetTransactions result = apiInstance.getTransactions(authorization, getTransactionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoRequestsApi#getTransactions");
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
| **getTransactionsRequest** | [**GetTransactionsRequest**](GetTransactionsRequest.md)|  | |

### Return type

[**GetTransactions**](GetTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

