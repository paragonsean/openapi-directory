# TestnetInsightApi

All URIs are relative to *https://ntp1node.nebl.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testnetGetAddress**](TestnetInsightApi.md#testnetGetAddress) | **GET** /testnet/ins/addr/{address} | Returns address object |
| [**testnetGetAddressBalance**](TestnetInsightApi.md#testnetGetAddressBalance) | **GET** /testnet/ins/addr/{address}/balance | Returns address balance in sats |
| [**testnetGetAddressTotalReceived**](TestnetInsightApi.md#testnetGetAddressTotalReceived) | **GET** /testnet/ins/addr/{address}/totalReceived | Returns total received by address in sats |
| [**testnetGetAddressTotalSent**](TestnetInsightApi.md#testnetGetAddressTotalSent) | **GET** /testnet/ins/addr/{address}/totalSent | Returns total sent by address in sats |
| [**testnetGetAddressUnconfirmedBalance**](TestnetInsightApi.md#testnetGetAddressUnconfirmedBalance) | **GET** /testnet/ins/addr/{address}/unconfirmedBalance | Returns address unconfirmed balance in sats |
| [**testnetGetAddressUtxos**](TestnetInsightApi.md#testnetGetAddressUtxos) | **GET** /testnet/ins/addr/{address}/utxo | Returns all UTXOs at a given address |
| [**testnetGetBlock**](TestnetInsightApi.md#testnetGetBlock) | **GET** /testnet/ins/block/{blockhash} | Returns information regarding a Neblio block |
| [**testnetGetBlockIndex**](TestnetInsightApi.md#testnetGetBlockIndex) | **GET** /testnet/ins/block-index/{blockindex} | Returns block hash of block |
| [**testnetGetRawTx**](TestnetInsightApi.md#testnetGetRawTx) | **GET** /testnet/ins/rawtx/{txid} | Returns raw transaction hex |
| [**testnetGetStatus**](TestnetInsightApi.md#testnetGetStatus) | **GET** /testnet/ins/status | Utility API for calling several blockchain node functions |
| [**testnetGetSync**](TestnetInsightApi.md#testnetGetSync) | **GET** /testnet/ins/sync | Get node sync status |
| [**testnetGetTx**](TestnetInsightApi.md#testnetGetTx) | **GET** /testnet/ins/tx/{txid} | Returns transaction object |
| [**testnetGetTxs**](TestnetInsightApi.md#testnetGetTxs) | **GET** /testnet/ins/txs | Get transactions by block or address |
| [**testnetSendTx**](TestnetInsightApi.md#testnetSendTx) | **POST** /testnet/ins/tx/send | Broadcasts a signed raw transaction to the network (not NTP1 specific) |


<a id="testnetGetAddress"></a>
# **testnetGetAddress**
> GetAddressResponse testnetGetAddress(address)

Returns address object

Returns NEBL address object containing information on a specific address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      GetAddressResponse result = apiInstance.testnetGetAddress(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetAddress");
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
| **address** | **String**| Address | |

### Return type

[**GetAddressResponse**](GetAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing address info |  -  |

<a id="testnetGetAddressBalance"></a>
# **testnetGetAddressBalance**
> BigDecimal testnetGetAddressBalance(address)

Returns address balance in sats

Returns NEBL address balance in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.testnetGetAddressBalance(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetAddressBalance");
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
| **address** | **String**| Address | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address balance |  -  |

<a id="testnetGetAddressTotalReceived"></a>
# **testnetGetAddressTotalReceived**
> BigDecimal testnetGetAddressTotalReceived(address)

Returns total received by address in sats

Returns total NEBL received by address in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.testnetGetAddressTotalReceived(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetAddressTotalReceived");
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
| **address** | **String**| Address | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Total received by address |  -  |

<a id="testnetGetAddressTotalSent"></a>
# **testnetGetAddressTotalSent**
> BigDecimal testnetGetAddressTotalSent(address)

Returns total sent by address in sats

Returns total NEBL sent by address in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.testnetGetAddressTotalSent(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetAddressTotalSent");
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
| **address** | **String**| Address | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Total sent by address |  -  |

<a id="testnetGetAddressUnconfirmedBalance"></a>
# **testnetGetAddressUnconfirmedBalance**
> BigDecimal testnetGetAddressUnconfirmedBalance(address)

Returns address unconfirmed balance in sats

Returns NEBL address unconfirmed balance in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.testnetGetAddressUnconfirmedBalance(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetAddressUnconfirmedBalance");
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
| **address** | **String**| Address | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address unconfirmed balance |  -  |

<a id="testnetGetAddressUtxos"></a>
# **testnetGetAddressUtxos**
> List&lt;GetAddressUtxosResponseInner&gt; testnetGetAddressUtxos(address)

Returns all UTXOs at a given address

Returns information on each Unspent Transaction Output contained at an address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      List<GetAddressUtxosResponseInner> result = apiInstance.testnetGetAddressUtxos(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetAddressUtxos");
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
| **address** | **String**| Address | |

### Return type

[**List&lt;GetAddressUtxosResponseInner&gt;**](GetAddressUtxosResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UTXOs at an address |  -  |

<a id="testnetGetBlock"></a>
# **testnetGetBlock**
> GetBlockResponse testnetGetBlock(blockhash)

Returns information regarding a Neblio block

Returns blockchain data for a given block based upon the block hash

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String blockhash = "blockhash_example"; // String | Block Hash
    try {
      GetBlockResponse result = apiInstance.testnetGetBlock(blockhash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetBlock");
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
| **blockhash** | **String**| Block Hash | |

### Return type

[**GetBlockResponse**](GetBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing all information on a blockchain block |  -  |

<a id="testnetGetBlockIndex"></a>
# **testnetGetBlockIndex**
> GetBlockIndexResponse testnetGetBlockIndex(blockindex)

Returns block hash of block

Returns the block hash of a block at a given block index

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    BigDecimal blockindex = new BigDecimal(78); // BigDecimal | Block Index
    try {
      GetBlockIndexResponse result = apiInstance.testnetGetBlockIndex(blockindex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetBlockIndex");
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
| **blockindex** | **BigDecimal**| Block Index | |

### Return type

[**GetBlockIndexResponse**](GetBlockIndexResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing block hash |  -  |

<a id="testnetGetRawTx"></a>
# **testnetGetRawTx**
> GetRawTxResponse testnetGetRawTx(txid)

Returns raw transaction hex

Returns raw transaction hex representing a NEBL transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String txid = "txid_example"; // String | Transaction ID
    try {
      GetRawTxResponse result = apiInstance.testnetGetRawTx(txid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetRawTx");
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
| **txid** | **String**| Transaction ID | |

### Return type

[**GetRawTxResponse**](GetRawTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing raw hex of transaction |  -  |

<a id="testnetGetStatus"></a>
# **testnetGetStatus**
> Object testnetGetStatus(q)

Utility API for calling several blockchain node functions

Utility API for calling several blockchain node functions - getInfo, getDifficulty, getBestBlockHash, getLastBlockHash

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String q = "q_example"; // String | Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash
    try {
      Object result = apiInstance.testnetGetStatus(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetStatus");
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
| **q** | **String**| Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Function Response |  -  |

<a id="testnetGetSync"></a>
# **testnetGetSync**
> GetSyncResponse testnetGetSync()

Get node sync status

Returns information on the node&#39;s sync progress

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    try {
      GetSyncResponse result = apiInstance.testnetGetSync();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetSync");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSyncResponse**](GetSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sync Info |  -  |

<a id="testnetGetTx"></a>
# **testnetGetTx**
> GetTxResponse testnetGetTx(txid)

Returns transaction object

Returns NEBL transaction object representing a NEBL transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String txid = "txid_example"; // String | Transaction ID
    try {
      GetTxResponse result = apiInstance.testnetGetTx(txid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetTx");
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
| **txid** | **String**| Transaction ID | |

### Return type

[**GetTxResponse**](GetTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing transaction info |  -  |

<a id="testnetGetTxs"></a>
# **testnetGetTxs**
> GetTxsResponse testnetGetTxs(address, block, pageNum)

Get transactions by block or address

Returns all transactions by block or address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    String address = "address_example"; // String | Address
    String block = "block_example"; // String | Block Hash
    BigDecimal pageNum = new BigDecimal(78); // BigDecimal | Page number to display
    try {
      GetTxsResponse result = apiInstance.testnetGetTxs(address, block, pageNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetGetTxs");
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
| **address** | **String**| Address | [optional] |
| **block** | **String**| Block Hash | [optional] |
| **pageNum** | **BigDecimal**| Page number to display | [optional] |

### Return type

[**GetTxsResponse**](GetTxsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of transactions |  -  |

<a id="testnetSendTx"></a>
# **testnetSendTx**
> BroadcastTxResponse testnetSendTx(sendTxRequest)

Broadcasts a signed raw transaction to the network (not NTP1 specific)

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetInsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetInsightApi apiInstance = new TestnetInsightApi(defaultClient);
    SendTxRequest sendTxRequest = new SendTxRequest(); // SendTxRequest | Object representing a transaction to broadcast
    try {
      BroadcastTxResponse result = apiInstance.testnetSendTx(sendTxRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetInsightApi#testnetSendTx");
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
| **sendTxRequest** | [**SendTxRequest**](SendTxRequest.md)| Object representing a transaction to broadcast | |

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

