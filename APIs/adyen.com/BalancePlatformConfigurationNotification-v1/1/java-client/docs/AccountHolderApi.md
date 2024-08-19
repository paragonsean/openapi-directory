# AccountHolderApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalancePlatformAccountHolderCreated**](AccountHolderApi.md#postBalancePlatformAccountHolderCreated) | **POST** /balancePlatform.accountHolder.created | Account holder created |
| [**postBalancePlatformAccountHolderUpdated**](AccountHolderApi.md#postBalancePlatformAccountHolderUpdated) | **POST** /balancePlatform.accountHolder.updated | Account holder updated |


<a id="postBalancePlatformAccountHolderCreated"></a>
# **postBalancePlatformAccountHolderCreated**
> BalancePlatformNotificationResponse postBalancePlatformAccountHolderCreated(accountHolderNotificationRequest)

Account holder created

Adyen sends this webhook when you successfully [create an account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHolderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHolderApi apiInstance = new AccountHolderApi(defaultClient);
    AccountHolderNotificationRequest accountHolderNotificationRequest = new AccountHolderNotificationRequest(); // AccountHolderNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformAccountHolderCreated(accountHolderNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHolderApi#postBalancePlatformAccountHolderCreated");
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
| **accountHolderNotificationRequest** | [**AccountHolderNotificationRequest**](AccountHolderNotificationRequest.md)|  | [optional] |

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

<a id="postBalancePlatformAccountHolderUpdated"></a>
# **postBalancePlatformAccountHolderUpdated**
> BalancePlatformNotificationResponse postBalancePlatformAccountHolderUpdated(accountHolderNotificationRequest)

Account holder updated

Adyen sends this webhook when you successfully [update an account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/accountHolders/_id_).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHolderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHolderApi apiInstance = new AccountHolderApi(defaultClient);
    AccountHolderNotificationRequest accountHolderNotificationRequest = new AccountHolderNotificationRequest(); // AccountHolderNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformAccountHolderUpdated(accountHolderNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHolderApi#postBalancePlatformAccountHolderUpdated");
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
| **accountHolderNotificationRequest** | [**AccountHolderNotificationRequest**](AccountHolderNotificationRequest.md)|  | [optional] |

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

