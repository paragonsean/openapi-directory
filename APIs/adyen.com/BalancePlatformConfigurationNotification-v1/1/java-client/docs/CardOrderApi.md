# CardOrderApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalancePlatformCardorderCreated**](CardOrderApi.md#postBalancePlatformCardorderCreated) | **POST** /balancePlatform.cardorder.created | Card order created |
| [**postBalancePlatformCardorderUpdated**](CardOrderApi.md#postBalancePlatformCardorderUpdated) | **POST** /balancePlatform.cardorder.updated | Card order updated |


<a id="postBalancePlatformCardorderCreated"></a>
# **postBalancePlatformCardorderCreated**
> BalancePlatformNotificationResponse postBalancePlatformCardorderCreated(cardOrderNotificationRequest)

Card order created

Adyen sends this webhook to indicate a successful creation of a card order after you create a [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments) of &#x60;type&#x60; **card** and &#x60;formFactor&#x60; **physical**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    CardOrderApi apiInstance = new CardOrderApi(defaultClient);
    CardOrderNotificationRequest cardOrderNotificationRequest = new CardOrderNotificationRequest(); // CardOrderNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformCardorderCreated(cardOrderNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardOrderApi#postBalancePlatformCardorderCreated");
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
| **cardOrderNotificationRequest** | [**CardOrderNotificationRequest**](CardOrderNotificationRequest.md)|  | [optional] |

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

<a id="postBalancePlatformCardorderUpdated"></a>
# **postBalancePlatformCardorderUpdated**
> BalancePlatformNotificationResponse postBalancePlatformCardorderUpdated(cardOrderNotificationRequest)

Card order updated

Adyen sends this webhook when there is an update in card order status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    CardOrderApi apiInstance = new CardOrderApi(defaultClient);
    CardOrderNotificationRequest cardOrderNotificationRequest = new CardOrderNotificationRequest(); // CardOrderNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformCardorderUpdated(cardOrderNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardOrderApi#postBalancePlatformCardorderUpdated");
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
| **cardOrderNotificationRequest** | [**CardOrderNotificationRequest**](CardOrderNotificationRequest.md)|  | [optional] |

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

