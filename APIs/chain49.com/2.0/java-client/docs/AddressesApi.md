# AddressesApi

All URIs are relative to *https://api.chain49.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAddressV2**](AddressesApi.md#getAddressV2) | **GET** /{blockchain}/v2/address/{address} | Get address V2 |
| [**getBalanceHistoryV2**](AddressesApi.md#getBalanceHistoryV2) | **GET** /{blockchain}/v2/balancehistory/{addressOrXpub} | Get Balance History V2 |
| [**getUTXOV2**](AddressesApi.md#getUTXOV2) | **GET** /{blockchain}/v2/utxo/{addressOrXpub} | Get UTXO V2 |
| [**getXpubV2**](AddressesApi.md#getXpubV2) | **GET** /{blockchain}/v2/xpub/{xpub} | Get xpub V2 |


<a id="getAddressV2"></a>
# **getAddressV2**
> Object getAddressV2(blockchain, address, page, pageSize, fromBlock, toBlock, details, contract, secondary)

Get address V2

Returns balances and transactions of an address. The returned transactions are sorted by block height, newest blocks first.  The **details** query parameter can specify the level of details returned by the request (default: \&quot;txids\&quot;). Possible values are:  **basic**: return only xpub balances, without any derived addresses and transactions  **tokens**: basic + tokens (addresses) derived from the xpub, subject to tokens parameter  **tokenBalances**: basic + tokens (addresses) derived from the xpub with balances, subject to tokens parameter  **txids**: tokenBalances + list of txids, subject to from, to filter and paging  **txs**: tokenBalances + list of transaction with details, subject to from, to filter and paging 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String address = "321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL"; // String | Wallet address
    Integer page = 1; // Integer | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    Integer pageSize = 1000; // Integer | number of transactions returned by call (default and maximum 1000)
    Integer fromBlock = 10; // Integer | filter of the returned transactions from block height to block height (default no filter)
    Integer toBlock = 100; // Integer | filter of the returned transactions from block height to block height (default no filter)
    String details = "basic"; // String | specifies level of details returned by request
    String contract = "0xdAC17F958D2ee523a2206206994597C13D831ec7"; // String | return only transactions which affect specified contract (applicable only to coins which support contracts)
    String secondary = "usd"; // String | specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
    try {
      Object result = apiInstance.getAddressV2(blockchain, address, page, pageSize, fromBlock, toBlock, details, contract, secondary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getAddressV2");
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
| **blockchain** | **String**| Blockchain name | |
| **address** | **String**| Wallet address | |
| **page** | **Integer**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] |
| **pageSize** | **Integer**| number of transactions returned by call (default and maximum 1000) | [optional] |
| **fromBlock** | **Integer**| filter of the returned transactions from block height to block height (default no filter) | [optional] |
| **toBlock** | **Integer**| filter of the returned transactions from block height to block height (default no filter) | [optional] |
| **details** | **String**| specifies level of details returned by request | [optional] [default to txids] [enum: basic, tokens, tokenBalances, txids, txslight, txs] |
| **contract** | **String**| return only transactions which affect specified contract (applicable only to coins which support contracts) | [optional] |
| **secondary** | **String**| specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values | [optional] |

### Return type

**Object**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getBalanceHistoryV2"></a>
# **getBalanceHistoryV2**
> List&lt;GetBalanceHistoryV2200ResponseInner&gt; getBalanceHistoryV2(blockchain, addressOrXpub, fromDate, toDate, fiatcurrency, groupBy)

Get Balance History V2

Returns a balance history for the specified XPUB or address  The value of sentToSelf is the amount sent from the same address to the same address or within addresses of xpub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String addressOrXpub = "321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL"; // String | Address or XPUB
    String fromDate = "1578391200"; // String | specifies a start date as a Unix timestamp
    String toDate = "1599053802"; // String | specifies an end date as a Unix timestamp
    String fiatcurrency = "usd"; // String | if specified, the response will contain secondary (fiat) rate at the time of transaction. If not, all available currencies will be returned
    BigDecimal groupBy = new BigDecimal("3600"); // BigDecimal | an interval in seconds, to group results by. Default is 3600 seconds
    try {
      List<GetBalanceHistoryV2200ResponseInner> result = apiInstance.getBalanceHistoryV2(blockchain, addressOrXpub, fromDate, toDate, fiatcurrency, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getBalanceHistoryV2");
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
| **blockchain** | **String**| Blockchain name | |
| **addressOrXpub** | **String**| Address or XPUB | |
| **fromDate** | **String**| specifies a start date as a Unix timestamp | [optional] |
| **toDate** | **String**| specifies an end date as a Unix timestamp | [optional] |
| **fiatcurrency** | **String**| if specified, the response will contain secondary (fiat) rate at the time of transaction. If not, all available currencies will be returned | [optional] |
| **groupBy** | **BigDecimal**| an interval in seconds, to group results by. Default is 3600 seconds | [optional] [default to 3600] |

### Return type

[**List&lt;GetBalanceHistoryV2200ResponseInner&gt;**](GetBalanceHistoryV2200ResponseInner.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUTXOV2"></a>
# **getUTXOV2**
> List&lt;Object&gt; getUTXOV2(blockchain, addressOrXpub, confirmed)

Get UTXO V2

Returns array of unspent transaction outputs of address or xpub, applicable only for Bitcoin-type coins. By default, the list contains both confirmed and unconfirmed transactions. The query parameter confirmed&#x3D;true disables return of unconfirmed transactions. The returned utxos are sorted by block height, newest blocks first. For xpubs or output descriptors, the response also contains address and derivation path of the utxo.    Unconfirmed utxos do not have field height, the field confirmations has value 0 and may contain field lockTime, if not zero.  Coinbase utxos have field coinbase set to true, however due to performance reasons only up to minimum coinbase confirmations limit (100). After this limit, utxos are not detected as coinbase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String addressOrXpub = "321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL"; // String | Address or XPUB
    Boolean confirmed = true; // Boolean | confirmed=true disables return of unconfirmed transactions
    try {
      List<Object> result = apiInstance.getUTXOV2(blockchain, addressOrXpub, confirmed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getUTXOV2");
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
| **blockchain** | **String**| Blockchain name | |
| **addressOrXpub** | **String**| Address or XPUB | |
| **confirmed** | **Boolean**| confirmed&#x3D;true disables return of unconfirmed transactions | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getXpubV2"></a>
# **getXpubV2**
> GetXpubV2200Response getXpubV2(blockchain, xpub, page, pageSize, fromBlock, toBlock, details, tokens, secondary)

Get xpub V2

Returns balances and transactions of an xpub or output descriptor, applicable only for Bitcoin-type coins.  Blockbook supports BIP44, BIP49, BIP84 and BIP86 (Taproot) derivation schemes, using either xpubs or output descriptors (see https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md)  Note: usedTokens always returns total number of used addresses of xpub.  Detailed documentation found here: https://github.com/trezor/blockbook/blob/master/docs/api.md#get-xpub

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String xpub = "tpubDC88gkaZi5HvJGxGDNLADkvtdpni3mLmx6vr2KnXmWMG8zfkBRggsxHVBkUpgcwPe2KKpkyvTJCdXHb1UHEWE64vczyyPQfHr1skBcsRedN"; // String | xpub or output descriptor, applicable only for Bitcoin-type coins
    Integer page = 1; // Integer | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    Integer pageSize = 1000; // Integer | number of transactions returned by call (default and maximum 1000)
    Integer fromBlock = 10; // Integer | filter of the returned transactions from block height to block height (default no filter)
    Integer toBlock = 100; // Integer | filter of the returned transactions from block height to block height (default no filter)
    String details = "basic"; // String | specifies level of details returned by request
    String tokens = "nonzero"; // String | specifies what tokens (xpub addresses) are returned by the request (default nonzero)
    String secondary = "usd"; // String | specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
    try {
      GetXpubV2200Response result = apiInstance.getXpubV2(blockchain, xpub, page, pageSize, fromBlock, toBlock, details, tokens, secondary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getXpubV2");
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
| **blockchain** | **String**| Blockchain name | |
| **xpub** | **String**| xpub or output descriptor, applicable only for Bitcoin-type coins | |
| **page** | **Integer**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] |
| **pageSize** | **Integer**| number of transactions returned by call (default and maximum 1000) | [optional] |
| **fromBlock** | **Integer**| filter of the returned transactions from block height to block height (default no filter) | [optional] |
| **toBlock** | **Integer**| filter of the returned transactions from block height to block height (default no filter) | [optional] |
| **details** | **String**| specifies level of details returned by request | [optional] [default to txids] [enum: basic, tokens, tokenBalances, txids, txslight, txs] |
| **tokens** | **String**| specifies what tokens (xpub addresses) are returned by the request (default nonzero) | [optional] [default to nonzero] [enum: nonzero, used, derived] |
| **secondary** | **String**| specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values | [optional] |

### Return type

[**GetXpubV2200Response**](GetXpubV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

