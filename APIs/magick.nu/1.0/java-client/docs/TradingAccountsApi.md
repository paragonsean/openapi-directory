# TradingAccountsApi

All URIs are relative to *http://devui.magick.nu/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postTradingAccounts**](TradingAccountsApi.md#postTradingAccounts) | **POST** /tradingAccounts | Add a Trading Account |
| [**putTradingAccountsPasswordUsernameBrokerserverMt4username**](TradingAccountsApi.md#putTradingAccountsPasswordUsernameBrokerserverMt4username) | **PUT** /tradingAccounts/password/{username}/{brokerserver}/{mt4username} | Update MT4 Account Password |


<a id="postTradingAccounts"></a>
# **postTradingAccounts**
> postTradingAccounts(body)

Add a Trading Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    TradingAccountsApi apiInstance = new TradingAccountsApi(defaultClient);
    TradingAccount body = new TradingAccount(); // TradingAccount | 
    try {
      apiInstance.postTradingAccounts(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradingAccountsApi#postTradingAccounts");
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
| **body** | [**TradingAccount**](TradingAccount.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="putTradingAccountsPasswordUsernameBrokerserverMt4username"></a>
# **putTradingAccountsPasswordUsernameBrokerserverMt4username**
> putTradingAccountsPasswordUsernameBrokerserverMt4username(username, brokerserver, mt4username, body)

Update MT4 Account Password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    TradingAccountsApi apiInstance = new TradingAccountsApi(defaultClient);
    String username = "username_example"; // String | 
    String brokerserver = "brokerserver_example"; // String | 
    String mt4username = "mt4username_example"; // String | 
    PasswordDTO body = new PasswordDTO(); // PasswordDTO | 
    try {
      apiInstance.putTradingAccountsPasswordUsernameBrokerserverMt4username(username, brokerserver, mt4username, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradingAccountsApi#putTradingAccountsPasswordUsernameBrokerserverMt4username");
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
| **username** | **String**|  | |
| **brokerserver** | **String**|  | |
| **mt4username** | **String**|  | |
| **body** | [**PasswordDTO**](PasswordDTO.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

