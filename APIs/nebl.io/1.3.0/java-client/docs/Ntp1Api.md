# Ntp1Api

All URIs are relative to *https://ntp1node.nebl.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**broadcastTx**](Ntp1Api.md#broadcastTx) | **POST** /ntp1/broadcast | Broadcasts a signed raw transaction to the network |
| [**burnToken**](Ntp1Api.md#burnToken) | **POST** /ntp1/burntoken | Builds a transaction that burns an NTP1 Token |
| [**getAddressInfo**](Ntp1Api.md#getAddressInfo) | **GET** /ntp1/addressinfo/{address} | Information On a Neblio Address |
| [**getTokenHolders**](Ntp1Api.md#getTokenHolders) | **GET** /ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token |
| [**getTokenId**](Ntp1Api.md#getTokenId) | **GET** /ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token |
| [**getTokenMetadata**](Ntp1Api.md#getTokenMetadata) | **GET** /ntp1/tokenmetadata/{tokenid} | Get Metadata of Token |
| [**getTokenMetadataOfUtxo**](Ntp1Api.md#getTokenMetadataOfUtxo) | **GET** /ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token |
| [**getTransactionInfo**](Ntp1Api.md#getTransactionInfo) | **GET** /ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction |
| [**issueToken**](Ntp1Api.md#issueToken) | **POST** /ntp1/issue | Builds a transaction that issues a new NTP1 Token |
| [**sendToken**](Ntp1Api.md#sendToken) | **POST** /ntp1/sendtoken | Builds a transaction that sends an NTP1 Token |


<a id="broadcastTx"></a>
# **broadcastTx**
> BroadcastTxResponse broadcastTx(broadcastTxRequest)

Broadcasts a signed raw transaction to the network

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    BroadcastTxRequest broadcastTxRequest = new BroadcastTxRequest(); // BroadcastTxRequest | Object representing a transaction to broadcast
    try {
      BroadcastTxResponse result = apiInstance.broadcastTx(broadcastTxRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#broadcastTx");
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

<a id="burnToken"></a>
# **burnToken**
> BurnTokenResponse burnToken(burnTokenRequest)

Builds a transaction that burns an NTP1 Token

Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    BurnTokenRequest burnTokenRequest = new BurnTokenRequest(); // BurnTokenRequest | Object representing the token to be burned
    try {
      BurnTokenResponse result = apiInstance.burnToken(burnTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#burnToken");
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

<a id="getAddressInfo"></a>
# **getAddressInfo**
> GetAddressInfoResponse getAddressInfo(address)

Information On a Neblio Address

Returns both NEBL and NTP1 token UTXOs held at the given address. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    String address = "address_example"; // String | Neblio Address to get information on.
    try {
      GetAddressInfoResponse result = apiInstance.getAddressInfo(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#getAddressInfo");
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

<a id="getTokenHolders"></a>
# **getTokenHolders**
> GetTokenHoldersResponse getTokenHolders(tokenid)

Get Addresses Holding a Token

Returns the the the addresses holding a token and how many tokens are held 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    String tokenid = "tokenid_example"; // String | TokenId to request metadata for
    try {
      GetTokenHoldersResponse result = apiInstance.getTokenHolders(tokenid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#getTokenHolders");
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

<a id="getTokenId"></a>
# **getTokenId**
> GetTokenIdResponse getTokenId(tokensymbol)

Returns the tokenId representing a token

Translates a token symbol to a tokenId if a token exists with that symbol on the network 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    String tokensymbol = "tokensymbol_example"; // String | Token symbol
    try {
      GetTokenIdResponse result = apiInstance.getTokenId(tokensymbol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#getTokenId");
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

<a id="getTokenMetadata"></a>
# **getTokenMetadata**
> GetTokenMetadataResponse getTokenMetadata(tokenid, verbosity)

Get Metadata of Token

Returns the metadata associated with a token. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    String tokenid = "tokenid_example"; // String | TokenId to request metadata for
    BigDecimal verbosity = new BigDecimal(78); // BigDecimal | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
    try {
      GetTokenMetadataResponse result = apiInstance.getTokenMetadata(tokenid, verbosity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#getTokenMetadata");
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

<a id="getTokenMetadataOfUtxo"></a>
# **getTokenMetadataOfUtxo**
> GetTokenMetadataResponse getTokenMetadataOfUtxo(tokenid, utxo, verbosity)

Get UTXO Metadata of Token

Returns the metadata associated with a token for that specific utxo instead of the issuance transaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    String tokenid = "tokenid_example"; // String | TokenId to request metadata for
    String utxo = "utxo_example"; // String | Specific UTXO to request metadata for
    BigDecimal verbosity = new BigDecimal(78); // BigDecimal | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
    try {
      GetTokenMetadataResponse result = apiInstance.getTokenMetadataOfUtxo(tokenid, utxo, verbosity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#getTokenMetadataOfUtxo");
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

<a id="getTransactionInfo"></a>
# **getTransactionInfo**
> GetTransactionInfoResponse getTransactionInfo(txid)

Information On an NTP1 Transaction

Returns detailed information regarding an NTP1 transaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    String txid = "txid_example"; // String | Neblio txid to get information on.
    try {
      GetTransactionInfoResponse result = apiInstance.getTransactionInfo(txid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#getTransactionInfo");
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

<a id="issueToken"></a>
# **issueToken**
> IssueTokenResponse issueToken(issueTokenRequest)

Builds a transaction that issues a new NTP1 Token

Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    IssueTokenRequest issueTokenRequest = new IssueTokenRequest(); // IssueTokenRequest | Object representing the token to be created
    try {
      IssueTokenResponse result = apiInstance.issueToken(issueTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#issueToken");
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

<a id="sendToken"></a>
# **sendToken**
> SendTokenResponse sendToken(sendTokenRequest)

Builds a transaction that sends an NTP1 Token

Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Ntp1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    Ntp1Api apiInstance = new Ntp1Api(defaultClient);
    SendTokenRequest sendTokenRequest = new SendTokenRequest(); // SendTokenRequest | Object representing the token to be sent
    try {
      SendTokenResponse result = apiInstance.sendToken(sendTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Ntp1Api#sendToken");
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

