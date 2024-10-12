# InsightApi

All URIs are relative to *https://ntp1node.nebl.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAddress**](InsightApi.md#getAddress) | **GET** /ins/addr/{address} | Returns address object |
| [**getAddressBalance**](InsightApi.md#getAddressBalance) | **GET** /ins/addr/{address}/balance | Returns address balance in sats |
| [**getAddressTotalReceived**](InsightApi.md#getAddressTotalReceived) | **GET** /ins/addr/{address}/totalReceived | Returns total received by address in sats |
| [**getAddressTotalSent**](InsightApi.md#getAddressTotalSent) | **GET** /ins/addr/{address}/totalSent | Returns total sent by address in sats |
| [**getAddressUnconfirmedBalance**](InsightApi.md#getAddressUnconfirmedBalance) | **GET** /ins/addr/{address}/unconfirmedBalance | Returns address unconfirmed balance in sats |
| [**getAddressUtxos**](InsightApi.md#getAddressUtxos) | **GET** /ins/addr/{address}/utxo | Returns all UTXOs at a given address |
| [**getBlock**](InsightApi.md#getBlock) | **GET** /ins/block/{blockhash} | Returns information regarding a Neblio block |
| [**getBlockIndex**](InsightApi.md#getBlockIndex) | **GET** /ins/block-index/{blockindex} | Returns block hash of block |
| [**getRawTx**](InsightApi.md#getRawTx) | **GET** /ins/rawtx/{txid} | Returns raw transaction hex |
| [**getStatus**](InsightApi.md#getStatus) | **GET** /ins/status | Utility API for calling several blockchain node functions |
| [**getSync**](InsightApi.md#getSync) | **GET** /ins/sync | Get node sync status |
| [**getTx**](InsightApi.md#getTx) | **GET** /ins/tx/{txid} | Returns transaction object |
| [**getTxs**](InsightApi.md#getTxs) | **GET** /ins/txs | Get transactions by block or address |
| [**sendTx**](InsightApi.md#sendTx) | **POST** /ins/tx/send | Broadcasts a signed raw transaction to the network (not NTP1 specific) |


<a id="getAddress"></a>
# **getAddress**
> GetAddressResponse getAddress(address)

Returns address object

Returns NEBL address object containing information on a specific address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      GetAddressResponse result = apiInstance.getAddress(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getAddress");
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

<a id="getAddressBalance"></a>
# **getAddressBalance**
> BigDecimal getAddressBalance(address)

Returns address balance in sats

Returns NEBL address balance in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.getAddressBalance(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getAddressBalance");
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

<a id="getAddressTotalReceived"></a>
# **getAddressTotalReceived**
> BigDecimal getAddressTotalReceived(address)

Returns total received by address in sats

Returns total NEBL received by address in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.getAddressTotalReceived(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getAddressTotalReceived");
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

<a id="getAddressTotalSent"></a>
# **getAddressTotalSent**
> BigDecimal getAddressTotalSent(address)

Returns total sent by address in sats

Returns total NEBL sent by address in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.getAddressTotalSent(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getAddressTotalSent");
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

<a id="getAddressUnconfirmedBalance"></a>
# **getAddressUnconfirmedBalance**
> BigDecimal getAddressUnconfirmedBalance(address)

Returns address unconfirmed balance in sats

Returns NEBL address unconfirmed balance in satoshis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      BigDecimal result = apiInstance.getAddressUnconfirmedBalance(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getAddressUnconfirmedBalance");
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

<a id="getAddressUtxos"></a>
# **getAddressUtxos**
> List&lt;GetAddressUtxosResponseInner&gt; getAddressUtxos(address)

Returns all UTXOs at a given address

Returns information on each Unspent Transaction Output contained at an address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    try {
      List<GetAddressUtxosResponseInner> result = apiInstance.getAddressUtxos(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getAddressUtxos");
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

<a id="getBlock"></a>
# **getBlock**
> GetBlockResponse getBlock(blockhash)

Returns information regarding a Neblio block

Returns blockchain data for a given block based upon the block hash

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String blockhash = "blockhash_example"; // String | Block Hash
    try {
      GetBlockResponse result = apiInstance.getBlock(blockhash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getBlock");
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

<a id="getBlockIndex"></a>
# **getBlockIndex**
> GetBlockIndexResponse getBlockIndex(blockindex)

Returns block hash of block

Returns the block hash of a block at a given block index

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    BigDecimal blockindex = new BigDecimal(78); // BigDecimal | Block Index
    try {
      GetBlockIndexResponse result = apiInstance.getBlockIndex(blockindex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getBlockIndex");
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

<a id="getRawTx"></a>
# **getRawTx**
> GetRawTxResponse getRawTx(txid)

Returns raw transaction hex

Returns raw transaction hex representing a NEBL transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String txid = "txid_example"; // String | Transaction ID
    try {
      GetRawTxResponse result = apiInstance.getRawTx(txid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getRawTx");
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

<a id="getStatus"></a>
# **getStatus**
> Object getStatus(q)

Utility API for calling several blockchain node functions

Utility API for calling several blockchain node functions - getInfo, getDifficulty, getBestBlockHash, getLastBlockHash

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String q = "q_example"; // String | Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash
    try {
      Object result = apiInstance.getStatus(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getStatus");
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

<a id="getSync"></a>
# **getSync**
> GetSyncResponse getSync()

Get node sync status

Returns information on the node&#39;s sync progress

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    try {
      GetSyncResponse result = apiInstance.getSync();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getSync");
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

<a id="getTx"></a>
# **getTx**
> GetTxResponse getTx(txid)

Returns transaction object

Returns NEBL transaction object representing a NEBL transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String txid = "txid_example"; // String | Transaction ID
    try {
      GetTxResponse result = apiInstance.getTx(txid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getTx");
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

<a id="getTxs"></a>
# **getTxs**
> GetTxsResponse getTxs(address, block, pageNum)

Get transactions by block or address

Returns all transactions by block or address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String address = "address_example"; // String | Address
    String block = "block_example"; // String | Block Hash
    BigDecimal pageNum = new BigDecimal(78); // BigDecimal | Page number to display
    try {
      GetTxsResponse result = apiInstance.getTxs(address, block, pageNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getTxs");
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

<a id="sendTx"></a>
# **sendTx**
> BroadcastTxResponse sendTx(sendTxRequest)

Broadcasts a signed raw transaction to the network (not NTP1 specific)

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    InsightApi apiInstance = new InsightApi(defaultClient);
    SendTxRequest sendTxRequest = new SendTxRequest(); // SendTxRequest | Object representing a transaction to broadcast
    try {
      BroadcastTxResponse result = apiInstance.sendTx(sendTxRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#sendTx");
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

