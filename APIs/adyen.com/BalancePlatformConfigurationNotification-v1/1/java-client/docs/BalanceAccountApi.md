# BalanceAccountApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalancePlatformBalanceAccountCreated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountCreated) | **POST** /balancePlatform.balanceAccount.created | Balance account created |
| [**postBalancePlatformBalanceAccountSweepCreated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountSweepCreated) | **POST** /balancePlatform.balanceAccountSweep.created | Sweep created |
| [**postBalancePlatformBalanceAccountSweepDeleted**](BalanceAccountApi.md#postBalancePlatformBalanceAccountSweepDeleted) | **POST** /balancePlatform.balanceAccountSweep.deleted | Sweep deleted |
| [**postBalancePlatformBalanceAccountSweepUpdated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountSweepUpdated) | **POST** /balancePlatform.balanceAccountSweep.updated | Sweep updated |
| [**postBalancePlatformBalanceAccountUpdated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountUpdated) | **POST** /balancePlatform.balanceAccount.updated | Balance account updated |


<a id="postBalancePlatformBalanceAccountCreated"></a>
# **postBalancePlatformBalanceAccountCreated**
> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountCreated(balanceAccountNotificationRequest)

Balance account created

Adyen sends this webhook when you successfully [create a balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    BalanceAccountApi apiInstance = new BalanceAccountApi(defaultClient);
    BalanceAccountNotificationRequest balanceAccountNotificationRequest = new BalanceAccountNotificationRequest(); // BalanceAccountNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformBalanceAccountCreated(balanceAccountNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceAccountApi#postBalancePlatformBalanceAccountCreated");
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
| **balanceAccountNotificationRequest** | [**BalanceAccountNotificationRequest**](BalanceAccountNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postBalancePlatformBalanceAccountSweepCreated"></a>
# **postBalancePlatformBalanceAccountSweepCreated**
> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountSweepCreated(sweepConfigurationNotificationRequest)

Sweep created

Adyen sends this webhook when you successfully [create a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/_balanceAccountId_/sweeps).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    BalanceAccountApi apiInstance = new BalanceAccountApi(defaultClient);
    SweepConfigurationNotificationRequest sweepConfigurationNotificationRequest = new SweepConfigurationNotificationRequest(); // SweepConfigurationNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformBalanceAccountSweepCreated(sweepConfigurationNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceAccountApi#postBalancePlatformBalanceAccountSweepCreated");
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
| **sweepConfigurationNotificationRequest** | [**SweepConfigurationNotificationRequest**](SweepConfigurationNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postBalancePlatformBalanceAccountSweepDeleted"></a>
# **postBalancePlatformBalanceAccountSweepDeleted**
> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountSweepDeleted(sweepConfigurationNotificationRequest)

Sweep deleted

Adyen sends this webhook when you successfully [delete a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/_balanceAccountId_/sweeps/_sweepId_).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    BalanceAccountApi apiInstance = new BalanceAccountApi(defaultClient);
    SweepConfigurationNotificationRequest sweepConfigurationNotificationRequest = new SweepConfigurationNotificationRequest(); // SweepConfigurationNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformBalanceAccountSweepDeleted(sweepConfigurationNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceAccountApi#postBalancePlatformBalanceAccountSweepDeleted");
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
| **sweepConfigurationNotificationRequest** | [**SweepConfigurationNotificationRequest**](SweepConfigurationNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postBalancePlatformBalanceAccountSweepUpdated"></a>
# **postBalancePlatformBalanceAccountSweepUpdated**
> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountSweepUpdated(sweepConfigurationNotificationRequest)

Sweep updated

Adyen sends this webhook when you successfully [update a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/_balanceAccountId_/sweeps/_sweepId_).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    BalanceAccountApi apiInstance = new BalanceAccountApi(defaultClient);
    SweepConfigurationNotificationRequest sweepConfigurationNotificationRequest = new SweepConfigurationNotificationRequest(); // SweepConfigurationNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformBalanceAccountSweepUpdated(sweepConfigurationNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceAccountApi#postBalancePlatformBalanceAccountSweepUpdated");
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
| **sweepConfigurationNotificationRequest** | [**SweepConfigurationNotificationRequest**](SweepConfigurationNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postBalancePlatformBalanceAccountUpdated"></a>
# **postBalancePlatformBalanceAccountUpdated**
> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountUpdated(balanceAccountNotificationRequest)

Balance account updated

Adyen sends this webhook when you successfully [update a balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/_id_).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    BalanceAccountApi apiInstance = new BalanceAccountApi(defaultClient);
    BalanceAccountNotificationRequest balanceAccountNotificationRequest = new BalanceAccountNotificationRequest(); // BalanceAccountNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformBalanceAccountUpdated(balanceAccountNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceAccountApi#postBalancePlatformBalanceAccountUpdated");
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
| **balanceAccountNotificationRequest** | [**BalanceAccountNotificationRequest**](BalanceAccountNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

