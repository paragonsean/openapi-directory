# UserOrdersApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userorderdetails**](UserOrdersApi.md#userorderdetails) | **GET** /api/oms/user/orders/{orderId} | Retrieve user order details |
| [**userorderslist**](UserOrdersApi.md#userorderslist) | **GET** /api/oms/user/orders | Retrieve user&#39;s orders |


<a id="userorderdetails"></a>
# **userorderdetails**
> Userorderdetails userorderdetails(clientEmail, contentType, accept, orderId)

Retrieve user order details

Lists all details from a user&#39;s order, through client&#39;s perspective.     &gt; Note that these requests are meant to be made by **Call center operator** profiles. Otherwise, they will return only orders from the same email making the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    UserOrdersApi apiInstance = new UserOrdersApi(defaultClient);
    String clientEmail = "customer@mail.com"; // String | Customer email.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String orderId = "1172452900788-01"; // String | Order ID is a unique code that identifies an order.
    try {
      Userorderdetails result = apiInstance.userorderdetails(clientEmail, contentType, accept, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserOrdersApi#userorderdetails");
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
| **clientEmail** | **String**| Customer email. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **orderId** | **String**| Order ID is a unique code that identifies an order. | |

### Return type

[**Userorderdetails**](Userorderdetails.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="userorderslist"></a>
# **userorderslist**
> Userorderslist userorderslist(clientEmail, page, perPage, contentType, accept)

Retrieve user&#39;s orders

Lists all orders from a given client, filtering by their email.     &gt; Note that these requests are meant to be made by **Call center operator** profiles. Otherwise, they will return only orders from the same email making the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    UserOrdersApi apiInstance = new UserOrdersApi(defaultClient);
    String clientEmail = "customer@mail.com"; // String | Customer email.
    String page = "15"; // String | Page number for result pagination.
    String perPage = "15"; // String | Page quantity for result pagination.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      Userorderslist result = apiInstance.userorderslist(clientEmail, page, perPage, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserOrdersApi#userorderslist");
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
| **clientEmail** | **String**| Customer email. | |
| **page** | **String**| Page number for result pagination. | |
| **perPage** | **String**| Page quantity for result pagination. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**Userorderslist**](Userorderslist.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

