# OrdersApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orders**](OrdersApi.md#orders) | **GET** /orders/orders/{orderID}/{name} | Orders |


<a id="orders"></a>
# **orders**
> String orders(orderID, accept, name)

Orders

Retrieve order by ID and optionally name. This service is only accessible for LH privileged partners

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
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderID = "orderID_example"; // String | Unique order identifier
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String name = "name_example"; // String | Surname of traveller
    try {
      String result = apiInstance.orders(orderID, accept, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orders");
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
| **orderID** | **String**| Unique order identifier | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **name** | **String**| Surname of traveller | |

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

