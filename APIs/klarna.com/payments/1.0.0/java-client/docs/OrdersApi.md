# OrdersApi

All URIs are relative to *https://api.klarna.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelAuthorization**](OrdersApi.md#cancelAuthorization) | **DELETE** /payments/v1/authorizations/{authorizationToken} | Cancel an existing authorization |
| [**createOrder**](OrdersApi.md#createOrder) | **POST** /payments/v1/authorizations/{authorizationToken}/order | Create a new order |
| [**purchaseToken**](OrdersApi.md#purchaseToken) | **POST** /payments/v1/authorizations/{authorizationToken}/customer-token | Generate a consumer token |


<a id="cancelAuthorization"></a>
# **cancelAuthorization**
> cancelAuthorization(authorizationToken)

Cancel an existing authorization

Use this API call to cancel/release an authorization. If the &#x60;authorization_token&#x60; received during a Klarna Payments won’t be used to place an order immediately you could release the authorization. Read more on **[Cancel an existing authorization](https://docs.klarna.com/klarna-payments/other-actions/cancel-an-authorization/)**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.klarna.com");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorizationToken = "authorizationToken_example"; // String | 
    try {
      apiInstance.cancelAuthorization(authorizationToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#cancelAuthorization");
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
| **authorizationToken** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The authorization was cancelled successfully. |  -  |
| **403** | You were not authorized to execute this operation. |  -  |
| **404** | The authorization does not exist. |  -  |

<a id="createOrder"></a>
# **createOrder**
> Order createOrder(authorizationToken, createOrderRequest)

Create a new order

Use this API call to create a new order. Placing an order towards Klarna means that the Klarna Payments session will be closed and that an order will be created in Klarna&#39;s system.&lt;br/&gt;When you have received the &#x60;authorization_token&#x60; for a successful authorization you can place the order. Among the other order details in this request, you include a URL to the confirmation page for the customer.&lt;br/&gt;When the Order has been successfully placed at Klarna, you need to handle it either through the Merchant Portal or using [Klarna’s Order Management API](#order-management-api). Read more on **[Create a new order](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-3-create-an-order/)**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.klarna.com");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorizationToken = "authorizationToken_example"; // String | 
    CreateOrderRequest createOrderRequest = new CreateOrderRequest(); // CreateOrderRequest | 
    try {
      Order result = apiInstance.createOrder(authorizationToken, createOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#createOrder");
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
| **authorizationToken** | **String**|  | |
| **createOrderRequest** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | [optional] |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order was successfully created. |  -  |
| **400** | We were unable to create an order with the provided data. Some field constraint was violated. |  -  |
| **403** | You were not authorized to execute this operation. |  -  |
| **404** | The authorization does not exist. |  -  |
| **409** | The data in the request does not match the session for the authorization. |  -  |

<a id="purchaseToken"></a>
# **purchaseToken**
> CustomerTokenCreationResponse purchaseToken(authorizationToken, customerTokenCreationRequest)

Generate a consumer token

Use this API call to create a Klarna Customer Token.&lt;br/&gt;After having obtained an &#x60;authorization_token&#x60; for a successful authorization, this can be used to create a purchase token instead of placing the order. Creating a Klarna Customer Token results in Klarna storing customer and payment method details. Read more on **[Generate a consumer token](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-token/)**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.klarna.com");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorizationToken = "authorizationToken_example"; // String | 
    CustomerTokenCreationRequest customerTokenCreationRequest = new CustomerTokenCreationRequest(); // CustomerTokenCreationRequest | 
    try {
      CustomerTokenCreationResponse result = apiInstance.purchaseToken(authorizationToken, customerTokenCreationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#purchaseToken");
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
| **authorizationToken** | **String**|  | |
| **customerTokenCreationRequest** | [**CustomerTokenCreationRequest**](CustomerTokenCreationRequest.md)|  | [optional] |

### Return type

[**CustomerTokenCreationResponse**](CustomerTokenCreationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token was successfully created. |  -  |
| **400** | We were unable to create a customer token with the provided data. Some field constraint was violated. |  -  |
| **403** | You were not authorized to execute this operation. |  -  |
| **404** | The authorization does not exist. |  -  |
| **409** | The data in the request does not match the session for the authorization. |  -  |

