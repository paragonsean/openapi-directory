# CloudApiApi

All URIs are relative to *https://api.tradematic.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudAccountsAccountidCloseallPost**](CloudApiApi.md#cloudAccountsAccountidCloseallPost) | **POST** /cloud/accounts/{accountid}/closeall | Close all positions by account |
| [**cloudAccountsAccountidGet**](CloudApiApi.md#cloudAccountsAccountidGet) | **GET** /cloud/accounts/{accountid} | Get trading account by ID |
| [**cloudAccountsAccountidOrdersGet**](CloudApiApi.md#cloudAccountsAccountidOrdersGet) | **GET** /cloud/accounts/{accountid}/orders | Get orders list by account |
| [**cloudAccountsAccountidOrdersOrderidDelete**](CloudApiApi.md#cloudAccountsAccountidOrdersOrderidDelete) | **DELETE** /cloud/accounts/{accountid}/orders/{orderid} | Cancel an order by ID |
| [**cloudAccountsAccountidOrdersPost**](CloudApiApi.md#cloudAccountsAccountidOrdersPost) | **POST** /cloud/accounts/{accountid}/orders | Place a new order |
| [**cloudAccountsAccountidSnapshotsGet**](CloudApiApi.md#cloudAccountsAccountidSnapshotsGet) | **GET** /cloud/accounts/{accountid}/snapshots | Get account equity and cash snapshots |
| [**cloudAccountsAccountidSyncPost**](CloudApiApi.md#cloudAccountsAccountidSyncPost) | **POST** /cloud/accounts/{accountid}/sync | Syhchronize an account with account active strategies |
| [**cloudAccountsAccountidTradesGet**](CloudApiApi.md#cloudAccountsAccountidTradesGet) | **GET** /cloud/accounts/{accountid}/trades | Get trades list by account |
| [**cloudAccountsGet**](CloudApiApi.md#cloudAccountsGet) | **GET** /cloud/accounts | Get trading accounts list |
| [**cloudCommandsCommandidGet**](CloudApiApi.md#cloudCommandsCommandidGet) | **GET** /cloud/commands/{commandid} | Get command by ID |
| [**cloudCommandsGet**](CloudApiApi.md#cloudCommandsGet) | **GET** /cloud/commands | Get commands list |
| [**cloudConnectionsConnectionidDelete**](CloudApiApi.md#cloudConnectionsConnectionidDelete) | **DELETE** /cloud/connections/{connectionid} | Delete connection by ID |
| [**cloudConnectionsConnectionidGet**](CloudApiApi.md#cloudConnectionsConnectionidGet) | **GET** /cloud/connections/{connectionid} | Get connection by ID |
| [**cloudConnectionsConnectionidPut**](CloudApiApi.md#cloudConnectionsConnectionidPut) | **PUT** /cloud/connections/{connectionid} | Update existing connection |
| [**cloudConnectionsGet**](CloudApiApi.md#cloudConnectionsGet) | **GET** /cloud/connections | Get connections list |
| [**cloudConnectionsPost**](CloudApiApi.md#cloudConnectionsPost) | **POST** /cloud/connections | Create a new connection |
| [**cloudConnectorsConnectoridGet**](CloudApiApi.md#cloudConnectorsConnectoridGet) | **GET** /cloud/connectors/{connectorid} | Get connector by ID |
| [**cloudConnectorsGet**](CloudApiApi.md#cloudConnectorsGet) | **GET** /cloud/connectors | Get available connectors list |
| [**cloudSessionsGet**](CloudApiApi.md#cloudSessionsGet) | **GET** /cloud/sessions | Get sessions list |
| [**cloudSessionsSessionidGet**](CloudApiApi.md#cloudSessionsSessionidGet) | **GET** /cloud/sessions/{sessionid} | Get session by ID |
| [**cloudStrategiesGet**](CloudApiApi.md#cloudStrategiesGet) | **GET** /cloud/strategies | Get list of active (executing) strategies |
| [**cloudStrategiesStartPost**](CloudApiApi.md#cloudStrategiesStartPost) | **POST** /cloud/strategies/start | Start a strategy execution for account |
| [**cloudStrategiesStrategyidGet**](CloudApiApi.md#cloudStrategiesStrategyidGet) | **GET** /cloud/strategies/{strategyid} | Get active (executing) strategy by ID |
| [**cloudStrategiesStrategyidStopPost**](CloudApiApi.md#cloudStrategiesStrategyidStopPost) | **POST** /cloud/strategies/{strategyid}/stop | Stop a strategy execution by ID |


<a id="cloudAccountsAccountidCloseallPost"></a>
# **cloudAccountsAccountidCloseallPost**
> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidCloseallPost(accountid)

Close all positions by account

Close all positions by account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    try {
      CloudAccountsAccountidCloseallPost202Response result = apiInstance.cloudAccountsAccountidCloseallPost(accountid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidCloseallPost");
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
| **accountid** | **Long**|  | |

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidGet"></a>
# **cloudAccountsAccountidGet**
> Account cloudAccountsAccountidGet(accountid)

Get trading account by ID

Get trading account by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    try {
      Account result = apiInstance.cloudAccountsAccountidGet(accountid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidGet");
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
| **accountid** | **Long**|  | |

### Return type

[**Account**](Account.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidOrdersGet"></a>
# **cloudAccountsAccountidOrdersGet**
> List&lt;Order&gt; cloudAccountsAccountidOrdersGet(accountid)

Get orders list by account

Get orders list by account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    try {
      List<Order> result = apiInstance.cloudAccountsAccountidOrdersGet(accountid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidOrdersGet");
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
| **accountid** | **Long**|  | |

### Return type

[**List&lt;Order&gt;**](Order.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidOrdersOrderidDelete"></a>
# **cloudAccountsAccountidOrdersOrderidDelete**
> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidOrdersOrderidDelete(accountid, orderid)

Cancel an order by ID

Cancel an order by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    Long orderid = 56L; // Long | 
    try {
      CloudAccountsAccountidCloseallPost202Response result = apiInstance.cloudAccountsAccountidOrdersOrderidDelete(accountid, orderid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidOrdersOrderidDelete");
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
| **accountid** | **Long**|  | |
| **orderid** | **Long**|  | |

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidOrdersPost"></a>
# **cloudAccountsAccountidOrdersPost**
> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidOrdersPost(accountid, body)

Place a new order

Place a new order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    CloudAccountsAccountidOrdersPostRequest body = new CloudAccountsAccountidOrdersPostRequest(); // CloudAccountsAccountidOrdersPostRequest | 
    try {
      CloudAccountsAccountidCloseallPost202Response result = apiInstance.cloudAccountsAccountidOrdersPost(accountid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidOrdersPost");
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
| **accountid** | **Long**|  | |
| **body** | [**CloudAccountsAccountidOrdersPostRequest**](CloudAccountsAccountidOrdersPostRequest.md)|  | |

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidSnapshotsGet"></a>
# **cloudAccountsAccountidSnapshotsGet**
> List&lt;Snapshot&gt; cloudAccountsAccountidSnapshotsGet(accountid)

Get account equity and cash snapshots

Get account equity and cash snapshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    try {
      List<Snapshot> result = apiInstance.cloudAccountsAccountidSnapshotsGet(accountid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidSnapshotsGet");
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
| **accountid** | **Long**|  | |

### Return type

[**List&lt;Snapshot&gt;**](Snapshot.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidSyncPost"></a>
# **cloudAccountsAccountidSyncPost**
> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidSyncPost(accountid)

Syhchronize an account with account active strategies

Syhchronize an account with account active strategies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    try {
      CloudAccountsAccountidCloseallPost202Response result = apiInstance.cloudAccountsAccountidSyncPost(accountid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidSyncPost");
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
| **accountid** | **Long**|  | |

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsAccountidTradesGet"></a>
# **cloudAccountsAccountidTradesGet**
> List&lt;Trade&gt; cloudAccountsAccountidTradesGet(accountid)

Get trades list by account

Get trades list by account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long accountid = 56L; // Long | 
    try {
      List<Trade> result = apiInstance.cloudAccountsAccountidTradesGet(accountid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsAccountidTradesGet");
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
| **accountid** | **Long**|  | |

### Return type

[**List&lt;Trade&gt;**](Trade.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudAccountsGet"></a>
# **cloudAccountsGet**
> List&lt;Account&gt; cloudAccountsGet()

Get trading accounts list

Get trading accounts list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    try {
      List<Account> result = apiInstance.cloudAccountsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudAccountsGet");
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

[**List&lt;Account&gt;**](Account.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudCommandsCommandidGet"></a>
# **cloudCommandsCommandidGet**
> Command cloudCommandsCommandidGet(commandid)

Get command by ID

Get command by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long commandid = 56L; // Long | 
    try {
      Command result = apiInstance.cloudCommandsCommandidGet(commandid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudCommandsCommandidGet");
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
| **commandid** | **Long**|  | |

### Return type

[**Command**](Command.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudCommandsGet"></a>
# **cloudCommandsGet**
> List&lt;Command&gt; cloudCommandsGet()

Get commands list

Get commands list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    try {
      List<Command> result = apiInstance.cloudCommandsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudCommandsGet");
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

[**List&lt;Command&gt;**](Command.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectionsConnectionidDelete"></a>
# **cloudConnectionsConnectionidDelete**
> CloudConnectionsPost200Response cloudConnectionsConnectionidDelete(connectionid)

Delete connection by ID

Delete connection by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long connectionid = 56L; // Long | 
    try {
      CloudConnectionsPost200Response result = apiInstance.cloudConnectionsConnectionidDelete(connectionid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectionsConnectionidDelete");
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
| **connectionid** | **Long**|  | |

### Return type

[**CloudConnectionsPost200Response**](CloudConnectionsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectionsConnectionidGet"></a>
# **cloudConnectionsConnectionidGet**
> Connection cloudConnectionsConnectionidGet(connectionid)

Get connection by ID

Get connection by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long connectionid = 56L; // Long | 
    try {
      Connection result = apiInstance.cloudConnectionsConnectionidGet(connectionid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectionsConnectionidGet");
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
| **connectionid** | **Long**|  | |

### Return type

[**Connection**](Connection.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectionsConnectionidPut"></a>
# **cloudConnectionsConnectionidPut**
> CloudConnectionsPost200Response cloudConnectionsConnectionidPut(connectionid, body)

Update existing connection

Update existing connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long connectionid = 56L; // Long | 
    CloudConnectionsPostRequest body = new CloudConnectionsPostRequest(); // CloudConnectionsPostRequest | 
    try {
      CloudConnectionsPost200Response result = apiInstance.cloudConnectionsConnectionidPut(connectionid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectionsConnectionidPut");
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
| **connectionid** | **Long**|  | |
| **body** | [**CloudConnectionsPostRequest**](CloudConnectionsPostRequest.md)|  | |

### Return type

[**CloudConnectionsPost200Response**](CloudConnectionsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectionsGet"></a>
# **cloudConnectionsGet**
> List&lt;Connection&gt; cloudConnectionsGet()

Get connections list

Get connections list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    try {
      List<Connection> result = apiInstance.cloudConnectionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectionsGet");
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

[**List&lt;Connection&gt;**](Connection.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectionsPost"></a>
# **cloudConnectionsPost**
> CloudConnectionsPost200Response cloudConnectionsPost(body)

Create a new connection

Create a new connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    CloudConnectionsPostRequest body = new CloudConnectionsPostRequest(); // CloudConnectionsPostRequest | 
    try {
      CloudConnectionsPost200Response result = apiInstance.cloudConnectionsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectionsPost");
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
| **body** | [**CloudConnectionsPostRequest**](CloudConnectionsPostRequest.md)|  | |

### Return type

[**CloudConnectionsPost200Response**](CloudConnectionsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectorsConnectoridGet"></a>
# **cloudConnectorsConnectoridGet**
> Connector cloudConnectorsConnectoridGet(connectorid)

Get connector by ID

Get connector by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long connectorid = 56L; // Long | 
    try {
      Connector result = apiInstance.cloudConnectorsConnectoridGet(connectorid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectorsConnectoridGet");
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
| **connectorid** | **Long**|  | |

### Return type

[**Connector**](Connector.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudConnectorsGet"></a>
# **cloudConnectorsGet**
> List&lt;Connector&gt; cloudConnectorsGet()

Get available connectors list

Get available connectors list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    try {
      List<Connector> result = apiInstance.cloudConnectorsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudConnectorsGet");
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

[**List&lt;Connector&gt;**](Connector.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudSessionsGet"></a>
# **cloudSessionsGet**
> List&lt;Session&gt; cloudSessionsGet()

Get sessions list

Get sessions list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    try {
      List<Session> result = apiInstance.cloudSessionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudSessionsGet");
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

[**List&lt;Session&gt;**](Session.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudSessionsSessionidGet"></a>
# **cloudSessionsSessionidGet**
> Session cloudSessionsSessionidGet(sessionid)

Get session by ID

Get session by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long sessionid = 56L; // Long | 
    try {
      Session result = apiInstance.cloudSessionsSessionidGet(sessionid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudSessionsSessionidGet");
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
| **sessionid** | **Long**|  | |

### Return type

[**Session**](Session.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudStrategiesGet"></a>
# **cloudStrategiesGet**
> List&lt;CloudStrategy&gt; cloudStrategiesGet()

Get list of active (executing) strategies

Get list of active (executing) strategies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    try {
      List<CloudStrategy> result = apiInstance.cloudStrategiesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudStrategiesGet");
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

[**List&lt;CloudStrategy&gt;**](CloudStrategy.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudStrategiesStartPost"></a>
# **cloudStrategiesStartPost**
> CloudAccountsAccountidCloseallPost202Response cloudStrategiesStartPost(body)

Start a strategy execution for account

Start a strategy execution for account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    CloudStrategiesStartPostRequest body = new CloudStrategiesStartPostRequest(); // CloudStrategiesStartPostRequest | 
    try {
      CloudAccountsAccountidCloseallPost202Response result = apiInstance.cloudStrategiesStartPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudStrategiesStartPost");
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
| **body** | [**CloudStrategiesStartPostRequest**](CloudStrategiesStartPostRequest.md)|  | |

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudStrategiesStrategyidGet"></a>
# **cloudStrategiesStrategyidGet**
> List&lt;CloudStrategy&gt; cloudStrategiesStrategyidGet(strategyid)

Get active (executing) strategy by ID

Get active (executing) strategy by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    try {
      List<CloudStrategy> result = apiInstance.cloudStrategiesStrategyidGet(strategyid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudStrategiesStrategyidGet");
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
| **strategyid** | **Long**|  | |

### Return type

[**List&lt;CloudStrategy&gt;**](CloudStrategy.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="cloudStrategiesStrategyidStopPost"></a>
# **cloudStrategiesStrategyidStopPost**
> CloudAccountsAccountidCloseallPost202Response cloudStrategiesStrategyidStopPost(strategyid)

Stop a strategy execution by ID

Stop a strategy execution by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    CloudApiApi apiInstance = new CloudApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    try {
      CloudAccountsAccountidCloseallPost202Response result = apiInstance.cloudStrategiesStrategyidStopPost(strategyid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudApiApi#cloudStrategiesStrategyidStopPost");
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
| **strategyid** | **Long**|  | |

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

