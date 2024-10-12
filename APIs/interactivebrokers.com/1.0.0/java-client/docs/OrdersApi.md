# OrdersApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountOrdersCustomerOrderIdDelete**](OrdersApi.md#accountsAccountOrdersCustomerOrderIdDelete) | **DELETE** /accounts/{account}/orders/{CustomerOrderId} | Cancel Order |
| [**accountsAccountOrdersCustomerOrderIdGet**](OrdersApi.md#accountsAccountOrdersCustomerOrderIdGet) | **GET** /accounts/{account}/orders/{CustomerOrderId} | Return specific order info |
| [**accountsAccountOrdersCustomerOrderIdPut**](OrdersApi.md#accountsAccountOrdersCustomerOrderIdPut) | **PUT** /accounts/{account}/orders/{CustomerOrderId} | Modify Order |
| [**accountsAccountOrdersGet**](OrdersApi.md#accountsAccountOrdersGet) | **GET** /accounts/{account}/orders | Open Orders |
| [**accountsAccountOrdersPost**](OrdersApi.md#accountsAccountOrdersPost) | **POST** /accounts/{account}/orders | Place Order |


<a id="accountsAccountOrdersCustomerOrderIdDelete"></a>
# **accountsAccountOrdersCustomerOrderIdDelete**
> List&lt;AccountsAccountOrdersCustomerOrderIdPut200ResponseInner&gt; accountsAccountOrdersCustomerOrderIdDelete(account, customerOrderId)

Cancel Order

Cancels the order with the referenced Customer Order ID for the account passed in the URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String account = "account_example"; // String | Account Number
    String customerOrderId = "customerOrderId_example"; // String | Customer Order ID
    try {
      List<AccountsAccountOrdersCustomerOrderIdPut200ResponseInner> result = apiInstance.accountsAccountOrdersCustomerOrderIdDelete(account, customerOrderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#accountsAccountOrdersCustomerOrderIdDelete");
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
| **account** | **String**| Account Number | |
| **customerOrderId** | **String**| Customer Order ID | |

### Return type

[**List&lt;AccountsAccountOrdersCustomerOrderIdPut200ResponseInner&gt;**](AccountsAccountOrdersCustomerOrderIdPut200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns result of cancellation attempt |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="accountsAccountOrdersCustomerOrderIdGet"></a>
# **accountsAccountOrdersCustomerOrderIdGet**
> List&lt;OrderState&gt; accountsAccountOrdersCustomerOrderIdGet(account, customerOrderId)

Return specific order info

Returns the order with the referenced Customer Order ID for the account passed in the URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String account = "account_example"; // String | Account Number
    String customerOrderId = "customerOrderId_example"; // String | Customer Order ID
    try {
      List<OrderState> result = apiInstance.accountsAccountOrdersCustomerOrderIdGet(account, customerOrderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#accountsAccountOrdersCustomerOrderIdGet");
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
| **account** | **String**| Account Number | |
| **customerOrderId** | **String**| Customer Order ID | |

### Return type

[**List&lt;OrderState&gt;**](OrderState.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns order status information |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="accountsAccountOrdersCustomerOrderIdPut"></a>
# **accountsAccountOrdersCustomerOrderIdPut**
> List&lt;AccountsAccountOrdersCustomerOrderIdPut200ResponseInner&gt; accountsAccountOrdersCustomerOrderIdPut(account, customerOrderId, accountsAccountOrdersCustomerOrderIdPutRequest)

Modify Order

Allows the caller to modify the order with the referenced Customer Order ID specified in the URL. A separate Customer Order ID must be provided in the request body for the modification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String account = "account_example"; // String | Account Number
    String customerOrderId = "customerOrderId_example"; // String | Customer Order ID
    AccountsAccountOrdersCustomerOrderIdPutRequest accountsAccountOrdersCustomerOrderIdPutRequest = new AccountsAccountOrdersCustomerOrderIdPutRequest(); // AccountsAccountOrdersCustomerOrderIdPutRequest | Order Parameters
    try {
      List<AccountsAccountOrdersCustomerOrderIdPut200ResponseInner> result = apiInstance.accountsAccountOrdersCustomerOrderIdPut(account, customerOrderId, accountsAccountOrdersCustomerOrderIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#accountsAccountOrdersCustomerOrderIdPut");
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
| **account** | **String**| Account Number | |
| **customerOrderId** | **String**| Customer Order ID | |
| **accountsAccountOrdersCustomerOrderIdPutRequest** | [**AccountsAccountOrdersCustomerOrderIdPutRequest**](AccountsAccountOrdersCustomerOrderIdPutRequest.md)| Order Parameters | |

### Return type

[**List&lt;AccountsAccountOrdersCustomerOrderIdPut200ResponseInner&gt;**](AccountsAccountOrdersCustomerOrderIdPut200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of order modification attempt |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="accountsAccountOrdersGet"></a>
# **accountsAccountOrdersGet**
> List&lt;OrderState&gt; accountsAccountOrdersGet(account)

Open Orders

Returns a list of orders for the account passed in the URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String account = "account_example"; // String | Account Number
    try {
      List<OrderState> result = apiInstance.accountsAccountOrdersGet(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#accountsAccountOrdersGet");
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
| **account** | **String**| Account Number | |

### Return type

[**List&lt;OrderState&gt;**](OrderState.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of orders for the indicated account |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="accountsAccountOrdersPost"></a>
# **accountsAccountOrdersPost**
> List&lt;OrderState&gt; accountsAccountOrdersPost(account, accountsAccountOrdersPostRequest)

Place Order

Places order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String account = "account_example"; // String | Account Number
    AccountsAccountOrdersPostRequest accountsAccountOrdersPostRequest = new AccountsAccountOrdersPostRequest(); // AccountsAccountOrdersPostRequest | Order Parameters
    try {
      List<OrderState> result = apiInstance.accountsAccountOrdersPost(account, accountsAccountOrdersPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#accountsAccountOrdersPost");
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
| **account** | **String**| Account Number | |
| **accountsAccountOrdersPostRequest** | [**AccountsAccountOrdersPostRequest**](AccountsAccountOrdersPostRequest.md)| Order Parameters | |

### Return type

[**List&lt;OrderState&gt;**](OrderState.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns order status information |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

