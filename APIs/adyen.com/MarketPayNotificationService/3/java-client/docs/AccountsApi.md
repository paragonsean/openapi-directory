# AccountsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postACCOUNTCLOSED**](AccountsApi.md#postACCOUNTCLOSED) | **POST** /ACCOUNT_CLOSED | Account closed |
| [**postACCOUNTCREATED**](AccountsApi.md#postACCOUNTCREATED) | **POST** /ACCOUNT_CREATED | Account created |
| [**postACCOUNTUPDATED**](AccountsApi.md#postACCOUNTUPDATED) | **POST** /ACCOUNT_UPDATED | Account updated |


<a id="postACCOUNTCLOSED"></a>
# **postACCOUNTCLOSED**
> NotificationResponse postACCOUNTCLOSED(accountCloseNotification)

Account closed

Adyen sends this webhook when [an account is closed](https://docs.adyen.com/api-explorer/#/Account/latest/post/closeAccount).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    AccountCloseNotification accountCloseNotification = new AccountCloseNotification(); // AccountCloseNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTCLOSED(accountCloseNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#postACCOUNTCLOSED");
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
| **accountCloseNotification** | [**AccountCloseNotification**](AccountCloseNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTCREATED"></a>
# **postACCOUNTCREATED**
> NotificationResponse postACCOUNTCREATED(accountCreateNotification)

Account created

Adyen sends this webhook when [an account is created](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccount).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    AccountCreateNotification accountCreateNotification = new AccountCreateNotification(); // AccountCreateNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTCREATED(accountCreateNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#postACCOUNTCREATED");
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
| **accountCreateNotification** | [**AccountCreateNotification**](AccountCreateNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTUPDATED"></a>
# **postACCOUNTUPDATED**
> NotificationResponse postACCOUNTUPDATED(accountUpdateNotification)

Account updated

Adyen sends this webhook when [an account is updated](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccount).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    AccountUpdateNotification accountUpdateNotification = new AccountUpdateNotification(); // AccountUpdateNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTUPDATED(accountUpdateNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#postACCOUNTUPDATED");
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
| **accountUpdateNotification** | [**AccountUpdateNotification**](AccountUpdateNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

