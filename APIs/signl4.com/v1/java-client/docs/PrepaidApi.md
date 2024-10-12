# PrepaidApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**prepaidBalanceGet**](PrepaidApi.md#prepaidBalanceGet) | **GET** /prepaid/balance | Get your subscription&#39;s current prepaid balance. |
| [**prepaidSettingsGet**](PrepaidApi.md#prepaidSettingsGet) | **GET** /prepaid/settings | Get your subscription&#39;s current prepaid settings. |
| [**prepaidSettingsPut**](PrepaidApi.md#prepaidSettingsPut) | **PUT** /prepaid/settings | Update your subscription&#39;s current prepaid settings. |
| [**prepaidTransactionsGet**](PrepaidApi.md#prepaidTransactionsGet) | **GET** /prepaid/transactions | Get your subscription&#39;s prepaid transactions. |
| [**subscriptionsSubscriptionIdPrepaidBalanceGet**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidBalanceGet) | **GET** /subscriptions/{subscriptionId}/prepaidBalance | Get a subscription&#39;s current prepaid balance. |
| [**subscriptionsSubscriptionIdPrepaidSettingsGet**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidSettingsGet) | **GET** /subscriptions/{subscriptionId}/prepaidSettings | Get a subscription&#39;s current prepaid settings. |
| [**subscriptionsSubscriptionIdPrepaidSettingsPut**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidSettingsPut) | **PUT** /subscriptions/{subscriptionId}/prepaidSettings | Update a subscription&#39;s current prepaid settings. |
| [**subscriptionsSubscriptionIdPrepaidTransactionsGet**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidTransactionsGet) | **GET** /subscriptions/{subscriptionId}/prepaidTransactions | Get a subscription&#39;s prepaid transactions. |


<a id="prepaidBalanceGet"></a>
# **prepaidBalanceGet**
> PrepaidBalanceInfo prepaidBalanceGet()

Get your subscription&#39;s current prepaid balance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    try {
      PrepaidBalanceInfo result = apiInstance.prepaidBalanceGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#prepaidBalanceGet");
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

[**PrepaidBalanceInfo**](PrepaidBalanceInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="prepaidSettingsGet"></a>
# **prepaidSettingsGet**
> PrepaidSettingsInfo prepaidSettingsGet()

Get your subscription&#39;s current prepaid settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    try {
      PrepaidSettingsInfo result = apiInstance.prepaidSettingsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#prepaidSettingsGet");
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

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="prepaidSettingsPut"></a>
# **prepaidSettingsPut**
> PrepaidSettingsInfo prepaidSettingsPut(prepaidSettingsInfo)

Update your subscription&#39;s current prepaid settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    PrepaidSettingsInfo prepaidSettingsInfo = new PrepaidSettingsInfo(); // PrepaidSettingsInfo | Settings object containing the new values.
    try {
      PrepaidSettingsInfo result = apiInstance.prepaidSettingsPut(prepaidSettingsInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#prepaidSettingsPut");
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
| **prepaidSettingsInfo** | [**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)| Settings object containing the new values. | [optional] |

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="prepaidTransactionsGet"></a>
# **prepaidTransactionsGet**
> List&lt;PrepaidTransactionInfo&gt; prepaidTransactionsGet()

Get your subscription&#39;s prepaid transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    try {
      List<PrepaidTransactionInfo> result = apiInstance.prepaidTransactionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#prepaidTransactionsGet");
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

[**List&lt;PrepaidTransactionInfo&gt;**](PrepaidTransactionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="subscriptionsSubscriptionIdPrepaidBalanceGet"></a>
# **subscriptionsSubscriptionIdPrepaidBalanceGet**
> PrepaidBalanceInfo subscriptionsSubscriptionIdPrepaidBalanceGet(subscriptionId)

Get a subscription&#39;s current prepaid balance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | 
    try {
      PrepaidBalanceInfo result = apiInstance.subscriptionsSubscriptionIdPrepaidBalanceGet(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#subscriptionsSubscriptionIdPrepaidBalanceGet");
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
| **subscriptionId** | **String**|  | |

### Return type

[**PrepaidBalanceInfo**](PrepaidBalanceInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="subscriptionsSubscriptionIdPrepaidSettingsGet"></a>
# **subscriptionsSubscriptionIdPrepaidSettingsGet**
> PrepaidSettingsInfo subscriptionsSubscriptionIdPrepaidSettingsGet(subscriptionId)

Get a subscription&#39;s current prepaid settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | 
    try {
      PrepaidSettingsInfo result = apiInstance.subscriptionsSubscriptionIdPrepaidSettingsGet(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#subscriptionsSubscriptionIdPrepaidSettingsGet");
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
| **subscriptionId** | **String**|  | |

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="subscriptionsSubscriptionIdPrepaidSettingsPut"></a>
# **subscriptionsSubscriptionIdPrepaidSettingsPut**
> PrepaidSettingsInfo subscriptionsSubscriptionIdPrepaidSettingsPut(subscriptionId, prepaidSettingsInfo)

Update a subscription&#39;s current prepaid settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | ID of the subscription
    PrepaidSettingsInfo prepaidSettingsInfo = new PrepaidSettingsInfo(); // PrepaidSettingsInfo | Settings object containing the new values.
    try {
      PrepaidSettingsInfo result = apiInstance.subscriptionsSubscriptionIdPrepaidSettingsPut(subscriptionId, prepaidSettingsInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#subscriptionsSubscriptionIdPrepaidSettingsPut");
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
| **subscriptionId** | **String**| ID of the subscription | |
| **prepaidSettingsInfo** | [**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)| Settings object containing the new values. | [optional] |

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="subscriptionsSubscriptionIdPrepaidTransactionsGet"></a>
# **subscriptionsSubscriptionIdPrepaidTransactionsGet**
> List&lt;PrepaidTransactionInfo&gt; subscriptionsSubscriptionIdPrepaidTransactionsGet(subscriptionId)

Get a subscription&#39;s prepaid transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepaidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PrepaidApi apiInstance = new PrepaidApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | ID of the subscription to get transactions for
    try {
      List<PrepaidTransactionInfo> result = apiInstance.subscriptionsSubscriptionIdPrepaidTransactionsGet(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepaidApi#subscriptionsSubscriptionIdPrepaidTransactionsGet");
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
| **subscriptionId** | **String**| ID of the subscription to get transactions for | |

### Return type

[**List&lt;PrepaidTransactionInfo&gt;**](PrepaidTransactionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

