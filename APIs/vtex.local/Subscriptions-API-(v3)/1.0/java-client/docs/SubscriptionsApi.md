# SubscriptionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRnsPubSubscriptionsGet**](SubscriptionsApi.md#apiRnsPubSubscriptionsGet) | **GET** /api/rns/pub/subscriptions | List subscriptions |
| [**apiRnsPubSubscriptionsIdGet**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdGet) | **GET** /api/rns/pub/subscriptions/{id} | Get subscription details |
| [**apiRnsPubSubscriptionsIdItemsItemIdDelete**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdItemsItemIdDelete) | **DELETE** /api/rns/pub/subscriptions/{id}/items/{itemId} | Remove items from a subscription. |
| [**apiRnsPubSubscriptionsIdItemsItemIdPatch**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdItemsItemIdPatch) | **PATCH** /api/rns/pub/subscriptions/{id}/items/{itemId} | Edit items on a subscription. |
| [**apiRnsPubSubscriptionsIdItemsPost**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdItemsPost) | **POST** /api/rns/pub/subscriptions/{id}/items | Add item to subscription |
| [**apiRnsPubSubscriptionsIdPatch**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdPatch) | **PATCH** /api/rns/pub/subscriptions/{id} | Update subscription |
| [**apiRnsPubSubscriptionsIdSimulatePost**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdSimulatePost) | **POST** /api/rns/pub/subscriptions/{id}/simulate | Calculate the current prices for a specific subscription |
| [**apiRnsPubSubscriptionsPost**](SubscriptionsApi.md#apiRnsPubSubscriptionsPost) | **POST** /api/rns/pub/subscriptions | Create subscription |
| [**apiRnsPubSubscriptionsSimulatePost**](SubscriptionsApi.md#apiRnsPubSubscriptionsSimulatePost) | **POST** /api/rns/pub/subscriptions/simulate | Calculate the current prices for the provided subscription template |
| [**apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet**](SubscriptionsApi.md#apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet) | **GET** /api/rns/pub/subscriptions/{subscriptionId}/conversation-message | Get conversation messages |


<a id="apiRnsPubSubscriptionsGet"></a>
# **apiRnsPubSubscriptionsGet**
> List&lt;SubscriptionGroupResponse&gt; apiRnsPubSubscriptionsGet(contentType, accept, customerEmail, status, addressId, paymentId, planId, nextPurchaseDate, originalOrderId, page, size)

List subscriptions

List subscriptions filtering by some arguments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String customerEmail = "customerEmail_example"; // String | Customer that owns the subscription. Defaults to the current logged user.
    String status = "status_example"; // String | Current subscription status
    String addressId = "addressId_example"; // String | Id from the address used as shipping address
    String paymentId = "paymentId_example"; // String | Id from the payment used as payment method
    String planId = "planId_example"; // String | Id from the plan that the subscription belongs to
    String nextPurchaseDate = "nextPurchaseDate_example"; // String | Date for the next cycle
    String originalOrderId = "originalOrderId_example"; // String | Id from the order that generated the subscription
    Integer page = 1; // Integer | Page used for pagination
    Integer size = 15; // Integer | Page size used for pagination
    try {
      List<SubscriptionGroupResponse> result = apiInstance.apiRnsPubSubscriptionsGet(contentType, accept, customerEmail, status, addressId, paymentId, planId, nextPurchaseDate, originalOrderId, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsGet");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **customerEmail** | **String**| Customer that owns the subscription. Defaults to the current logged user. | [optional] |
| **status** | **String**| Current subscription status | [optional] |
| **addressId** | **String**| Id from the address used as shipping address | [optional] |
| **paymentId** | **String**| Id from the payment used as payment method | [optional] |
| **planId** | **String**| Id from the plan that the subscription belongs to | [optional] |
| **nextPurchaseDate** | **String**| Date for the next cycle | [optional] |
| **originalOrderId** | **String**| Id from the order that generated the subscription | [optional] |
| **page** | **Integer**| Page used for pagination | [optional] [default to 1] |
| **size** | **Integer**| Page size used for pagination | [optional] [default to 15] |

### Return type

[**List&lt;SubscriptionGroupResponse&gt;**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested subscriptions |  -  |

<a id="apiRnsPubSubscriptionsIdGet"></a>
# **apiRnsPubSubscriptionsIdGet**
> SubscriptionGroupResponse apiRnsPubSubscriptionsIdGet(id, contentType, accept)

Get subscription details

Retrieve a specific subscription by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "id_example"; // String | ID from the target subscription.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      SubscriptionGroupResponse result = apiInstance.apiRnsPubSubscriptionsIdGet(id, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsIdGet");
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
| **id** | **String**| ID from the target subscription. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested subscription |  -  |

<a id="apiRnsPubSubscriptionsIdItemsItemIdDelete"></a>
# **apiRnsPubSubscriptionsIdItemsItemIdDelete**
> apiRnsPubSubscriptionsIdItemsItemIdDelete(id, itemId, contentType, accept)

Remove items from a subscription.

Removes a specific item from a given subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "id_example"; // String | Id from the target subscription
    String itemId = "itemId_example"; // String | Id from the subscription item that will be removed
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.apiRnsPubSubscriptionsIdItemsItemIdDelete(id, itemId, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsIdItemsItemIdDelete");
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
| **id** | **String**| Id from the target subscription | |
| **itemId** | **String**| Id from the subscription item that will be removed | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiRnsPubSubscriptionsIdItemsItemIdPatch"></a>
# **apiRnsPubSubscriptionsIdItemsItemIdPatch**
> SubscriptionGroupResponse apiRnsPubSubscriptionsIdItemsItemIdPatch(id, itemId, contentType, accept, updateItemInput)

Edit items on a subscription.

Edit a given item on a specific subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "id_example"; // String | Id from the target subscription
    String itemId = "itemId_example"; // String | Id from the target item
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    UpdateItemInput updateItemInput = new UpdateItemInput(); // UpdateItemInput | 
    try {
      SubscriptionGroupResponse result = apiInstance.apiRnsPubSubscriptionsIdItemsItemIdPatch(id, itemId, contentType, accept, updateItemInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsIdItemsItemIdPatch");
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
| **id** | **String**| Id from the target subscription | |
| **itemId** | **String**| Id from the target item | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **updateItemInput** | [**UpdateItemInput**](UpdateItemInput.md)|  | [optional] |

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription updated |  -  |

<a id="apiRnsPubSubscriptionsIdItemsPost"></a>
# **apiRnsPubSubscriptionsIdItemsPost**
> SubscriptionGroupResponse apiRnsPubSubscriptionsIdItemsPost(id, contentType, accept, subscriptionThinItemRequest)

Add item to subscription

Add a new item to a given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "id_example"; // String | ID from the target subscription
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    SubscriptionThinItemRequest subscriptionThinItemRequest = new SubscriptionThinItemRequest(); // SubscriptionThinItemRequest | 
    try {
      SubscriptionGroupResponse result = apiInstance.apiRnsPubSubscriptionsIdItemsPost(id, contentType, accept, subscriptionThinItemRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsIdItemsPost");
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
| **id** | **String**| ID from the target subscription | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **subscriptionThinItemRequest** | [**SubscriptionThinItemRequest**](SubscriptionThinItemRequest.md)|  | [optional] |

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription successfully updated |  -  |

<a id="apiRnsPubSubscriptionsIdPatch"></a>
# **apiRnsPubSubscriptionsIdPatch**
> SubscriptionGroupResponse apiRnsPubSubscriptionsIdPatch(id, contentType, accept, subscriptionUpdateRequestV3)

Update subscription

Update a specific subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "4002961"; // String | ID from the given subscription.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    SubscriptionUpdateRequestV3 subscriptionUpdateRequestV3 = new SubscriptionUpdateRequestV3(); // SubscriptionUpdateRequestV3 | 
    try {
      SubscriptionGroupResponse result = apiInstance.apiRnsPubSubscriptionsIdPatch(id, contentType, accept, subscriptionUpdateRequestV3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsIdPatch");
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
| **id** | **String**| ID from the given subscription. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **subscriptionUpdateRequestV3** | [**SubscriptionUpdateRequestV3**](SubscriptionUpdateRequestV3.md)|  | [optional] |

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription successfully updated |  -  |

<a id="apiRnsPubSubscriptionsIdSimulatePost"></a>
# **apiRnsPubSubscriptionsIdSimulatePost**
> SimulateResponseVO apiRnsPubSubscriptionsIdSimulatePost(id, contentType, accept)

Calculate the current prices for a specific subscription

Simulates an order made by the specific subscription on checkout and retrieves the current price for items and shipping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "id_example"; // String | Id from the target subscription
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      SimulateResponseVO result = apiInstance.apiRnsPubSubscriptionsIdSimulatePost(id, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsIdSimulatePost");
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
| **id** | **String**| Id from the target subscription | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**SimulateResponseVO**](SimulateResponseVO.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Simulation result |  -  |

<a id="apiRnsPubSubscriptionsPost"></a>
# **apiRnsPubSubscriptionsPost**
> SubscriptionGroupResponse apiRnsPubSubscriptionsPost(contentType, accept, subscriptionGroupRequest)

Create subscription

Create a new subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    SubscriptionGroupRequest subscriptionGroupRequest = new SubscriptionGroupRequest(); // SubscriptionGroupRequest | 
    try {
      SubscriptionGroupResponse result = apiInstance.apiRnsPubSubscriptionsPost(contentType, accept, subscriptionGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsPost");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **subscriptionGroupRequest** | [**SubscriptionGroupRequest**](SubscriptionGroupRequest.md)|  | [optional] |

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscription created |  -  |

<a id="apiRnsPubSubscriptionsSimulatePost"></a>
# **apiRnsPubSubscriptionsSimulatePost**
> SimulateResponseVO apiRnsPubSubscriptionsSimulatePost(contentType, accept, subscriptionGroupRequest)

Calculate the current prices for the provided subscription template

Simulates an order made by subscriptions on checkout and retrieves the current price for items and shipping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    SubscriptionGroupRequest subscriptionGroupRequest = new SubscriptionGroupRequest(); // SubscriptionGroupRequest | 
    try {
      SimulateResponseVO result = apiInstance.apiRnsPubSubscriptionsSimulatePost(contentType, accept, subscriptionGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsSimulatePost");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **subscriptionGroupRequest** | [**SubscriptionGroupRequest**](SubscriptionGroupRequest.md)|  | [optional] |

### Return type

[**SimulateResponseVO**](SimulateResponseVO.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Simulation result |  -  |

<a id="apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet"></a>
# **apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet**
> List&lt;ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner&gt; apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet(subscriptionId, contentType, accept)

Get conversation messages

Retrieve all conversation messages sent to a customer regarding a given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

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

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String subscriptionId = "123456789abc"; // String | ID of the subscription.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      List<ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner> result = apiInstance.apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet(subscriptionId, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet");
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
| **subscriptionId** | **String**| ID of the subscription. | [default to 123456789abc] |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**List&lt;ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner&gt;**](ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

