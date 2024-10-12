# TestnetNtp1Api

All URIs are relative to *https://ntp1node.nebl.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testnetBroadcastTx**](TestnetNtp1Api.md#testnetBroadcastTx) | **POST** /testnet/ntp1/broadcast | Broadcasts a signed raw transaction to the network |
| [**testnetBurnToken**](TestnetNtp1Api.md#testnetBurnToken) | **POST** /testnet/ntp1/burntoken | Builds a transaction that burns an NTP1 Token |
| [**testnetGetAddressInfo**](TestnetNtp1Api.md#testnetGetAddressInfo) | **GET** /testnet/ntp1/addressinfo/{address} | Information On a Neblio Address |
| [**testnetGetTokenHolders**](TestnetNtp1Api.md#testnetGetTokenHolders) | **GET** /testnet/ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token |
| [**testnetGetTokenId**](TestnetNtp1Api.md#testnetGetTokenId) | **GET** /testnet/ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token |
| [**testnetGetTokenMetadata**](TestnetNtp1Api.md#testnetGetTokenMetadata) | **GET** /testnet/ntp1/tokenmetadata/{tokenid} | Get Metadata of Token |
| [**testnetGetTokenMetadataOfUtxo**](TestnetNtp1Api.md#testnetGetTokenMetadataOfUtxo) | **GET** /testnet/ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token |
| [**testnetGetTransactionInfo**](TestnetNtp1Api.md#testnetGetTransactionInfo) | **GET** /testnet/ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction |
| [**testnetIssueToken**](TestnetNtp1Api.md#testnetIssueToken) | **POST** /testnet/ntp1/issue | Builds a transaction that issues a new NTP1 Token |
| [**testnetSendToken**](TestnetNtp1Api.md#testnetSendToken) | **POST** /testnet/ntp1/sendtoken | Builds a transaction that sends an NTP1 Token |


<a id="testnetBroadcastTx"></a>
# **testnetBroadcastTx**
> BroadcastTxResponse testnetBroadcastTx(broadcastTxRequest)

Broadcasts a signed raw transaction to the network

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    BroadcastTxRequest broadcastTxRequest = new BroadcastTxRequest(); // BroadcastTxRequest | Object representing a transaction to broadcast
    try {
      BroadcastTxResponse result = apiInstance.testnetBroadcastTx(broadcastTxRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetBroadcastTx");
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
| **broadcastTxRequest** | [**BroadcastTxRequest**](BroadcastTxRequest.md)| Object representing a transaction to broadcast | |

### Return type

[**BroadcastTxResponse**](BroadcastTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object containing the TXID if the broadcast was successful |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetBurnToken"></a>
# **testnetBurnToken**
> BurnTokenResponse testnetBurnToken(burnTokenRequest)

Builds a transaction that burns an NTP1 Token

Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    BurnTokenRequest burnTokenRequest = new BurnTokenRequest(); // BurnTokenRequest | Object representing the token to be burned
    try {
      BurnTokenResponse result = apiInstance.testnetBurnToken(burnTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetBurnToken");
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
| **burnTokenRequest** | [**BurnTokenRequest**](BurnTokenRequest.md)| Object representing the token to be burned | |

### Return type

[**BurnTokenResponse**](BurnTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object representing the tx to burn the token |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetGetAddressInfo"></a>
# **testnetGetAddressInfo**
> GetAddressInfoResponse testnetGetAddressInfo(address)

Information On a Neblio Address

Returns both NEBL and NTP1 token UTXOs held at the given address. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    String address = "address_example"; // String | Neblio Address to get information on.
    try {
      GetAddressInfoResponse result = apiInstance.testnetGetAddressInfo(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetGetAddressInfo");
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
| **address** | **String**| Neblio Address to get information on. | |

### Return type

[**GetAddressInfoResponse**](GetAddressInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object with an array of UTXOs for this address |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetGetTokenHolders"></a>
# **testnetGetTokenHolders**
> GetTokenHoldersResponse testnetGetTokenHolders(tokenid)

Get Addresses Holding a Token

Returns the the the addresses holding a token and how many tokens are held 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    String tokenid = "tokenid_example"; // String | TokenId to request metadata for
    try {
      GetTokenHoldersResponse result = apiInstance.testnetGetTokenHolders(tokenid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetGetTokenHolders");
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
| **tokenid** | **String**| TokenId to request metadata for | |

### Return type

[**GetTokenHoldersResponse**](GetTokenHoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object containing all of the addresses holding a token |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetGetTokenId"></a>
# **testnetGetTokenId**
> GetTokenIdResponse testnetGetTokenId(tokensymbol)

Returns the tokenId representing a token

Translates a token symbol to a tokenId if a token exists with that symbol on the network 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    String tokensymbol = "tokensymbol_example"; // String | Token symbol
    try {
      GetTokenIdResponse result = apiInstance.testnetGetTokenId(tokensymbol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetGetTokenId");
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
| **tokensymbol** | **String**| Token symbol | |

### Return type

[**GetTokenIdResponse**](GetTokenIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing the token symbol and ID, if token symbol does not exist on network, empty object is returned. |  -  |

<a id="testnetGetTokenMetadata"></a>
# **testnetGetTokenMetadata**
> GetTokenMetadataResponse testnetGetTokenMetadata(tokenid, verbosity)

Get Metadata of Token

Returns the metadata associated with a token. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    String tokenid = "tokenid_example"; // String | TokenId to request metadata for
    BigDecimal verbosity = new BigDecimal(78); // BigDecimal | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
    try {
      GetTokenMetadataResponse result = apiInstance.testnetGetTokenMetadata(tokenid, verbosity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetGetTokenMetadata");
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
| **tokenid** | **String**| TokenId to request metadata for | |
| **verbosity** | **BigDecimal**| 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses | [optional] |

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object containing the metadata of a token |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetGetTokenMetadataOfUtxo"></a>
# **testnetGetTokenMetadataOfUtxo**
> GetTokenMetadataResponse testnetGetTokenMetadataOfUtxo(tokenid, utxo, verbosity)

Get UTXO Metadata of Token

Returns the metadata associated with a token for that specific utxo instead of the issuance transaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    String tokenid = "tokenid_example"; // String | TokenId to request metadata for
    String utxo = "utxo_example"; // String | Specific UTXO to request metadata for
    BigDecimal verbosity = new BigDecimal(78); // BigDecimal | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
    try {
      GetTokenMetadataResponse result = apiInstance.testnetGetTokenMetadataOfUtxo(tokenid, utxo, verbosity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetGetTokenMetadataOfUtxo");
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
| **tokenid** | **String**| TokenId to request metadata for | |
| **utxo** | **String**| Specific UTXO to request metadata for | |
| **verbosity** | **BigDecimal**| 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses | [optional] |

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object containing the metadata of a token for a UTXO |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetGetTransactionInfo"></a>
# **testnetGetTransactionInfo**
> GetTransactionInfoResponse testnetGetTransactionInfo(txid)

Information On an NTP1 Transaction

Returns detailed information regarding an NTP1 transaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    String txid = "txid_example"; // String | Neblio txid to get information on.
    try {
      GetTransactionInfoResponse result = apiInstance.testnetGetTransactionInfo(txid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetGetTransactionInfo");
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
| **txid** | **String**| Neblio txid to get information on. | |

### Return type

[**GetTransactionInfoResponse**](GetTransactionInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object represending this transaction |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetIssueToken"></a>
# **testnetIssueToken**
> IssueTokenResponse testnetIssueToken(issueTokenRequest)

Builds a transaction that issues a new NTP1 Token

Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    IssueTokenRequest issueTokenRequest = new IssueTokenRequest(); // IssueTokenRequest | Object representing the token to be created
    try {
      IssueTokenResponse result = apiInstance.testnetIssueToken(issueTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetIssueToken");
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
| **issueTokenRequest** | [**IssueTokenRequest**](IssueTokenRequest.md)| Object representing the token to be created | |

### Return type

[**IssueTokenResponse**](IssueTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object representing the token created |  -  |
| **0** | Unexpected error |  -  |

<a id="testnetSendToken"></a>
# **testnetSendToken**
> SendTokenResponse testnetSendToken(sendTokenRequest)

Builds a transaction that sends an NTP1 Token

Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetNtp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetNtp1Api apiInstance = new TestnetNtp1Api(defaultClient);
    SendTokenRequest sendTokenRequest = new SendTokenRequest(); // SendTokenRequest | Object representing the token to be sent
    try {
      SendTokenResponse result = apiInstance.testnetSendToken(sendTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetNtp1Api#testnetSendToken");
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
| **sendTokenRequest** | [**SendTokenRequest**](SendTokenRequest.md)| Object representing the token to be sent | |

### Return type

[**SendTokenResponse**](SendTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object representing the tx to send the token |  -  |
| **0** | Unexpected error |  -  |

