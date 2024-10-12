# MarketplacesOrdersSubscriptionsSubscriptionsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#activateSubscription) | **POST** /v2/user/marketplaces/orders/subscriptions/{id}/activate | Activate a subscription to the orders |
| [**createSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#createSubscription) | **POST** /v2/user/marketplaces/orders/subscriptions/{id} | Creates a subscription to the orders |
| [**deactivateSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#deactivateSubscription) | **POST** /v2/user/marketplaces/orders/subscriptions/{id}/deactivate | Deactivate a subscription to the orders |
| [**deleteSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#deleteSubscription) | **DELETE** /v2/user/marketplaces/orders/subscriptions/{id} | Delete a subscription to the orders |
| [**getSubscription**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#getSubscription) | **GET** /v2/user/marketplaces/orders/subscriptions/{id} | Get a subscription to the orders |
| [**getSubscriptionList**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#getSubscriptionList) | **GET** /v2/user/marketplaces/orders/subscriptions/ | Get the subscription list |
| [**getSubscriptionPushReporting**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#getSubscriptionPushReporting) | **GET** /v2/user/marketplaces/orders/subscriptions/{id}/reporting | Get the push reporting related to this subscription |
| [**retryPushOrders**](MarketplacesOrdersSubscriptionsSubscriptionsApi.md#retryPushOrders) | **POST** /v2/user/marketplaces/orders/subscriptions/{id}/retry | Force retry push orders immediatly |


<a id="activateSubscription"></a>
# **activateSubscription**
> activateSubscription(id, activateSubscriptionRequest)

Activate a subscription to the orders

At this moment, BeezUP will ensure that your callback url is respecting this specification:  - https://api.beezup.com/swaggerhub/apis/BeezUP/public_marketplaces_orders_subscriptions_consumer-dev/1.0#/Subscriptions/Verification  After that we will send you the orders related to your subscription, respecting this specification:  - https://api.beezup.com/swaggerhub/apis/BeezUP/public_marketplaces_orders_subscriptions_consumer-dev/1.0#/Subscriptions/PushOrders 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    ActivateSubscriptionRequest activateSubscriptionRequest = new ActivateSubscriptionRequest(); // ActivateSubscriptionRequest | 
    try {
      apiInstance.activateSubscription(id, activateSubscriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#activateSubscription");
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
| **id** | **String**|  | |
| **activateSubscriptionRequest** | [**ActivateSubscriptionRequest**](ActivateSubscriptionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Subscription activation accepted |  -  |
| **400** | Activation subscription request is invalid |  -  |
| **404** | The subscription is not found |  -  |
| **503** | The target url is not available |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="createSubscription"></a>
# **createSubscription**
> createSubscription(id, createSubscriptionRequest)

Creates a subscription to the orders

Please take a look at this sequence diagram to understand the subscription process to follow [here](https://www.websequencediagrams.com/files/render?link&#x3D;SBYbeIc8NGshk6ooCbmjoBLIMl4fIGO1xjJbPBQAglBo0n6BwEReh7NXQiPSjOTX)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    CreateSubscriptionRequest createSubscriptionRequest = new CreateSubscriptionRequest(); // CreateSubscriptionRequest | 
    try {
      apiInstance.createSubscription(id, createSubscriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#createSubscription");
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
| **id** | **String**|  | |
| **createSubscriptionRequest** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Subscription creation accepted |  -  |
| **400** | Invalid subscription request. |  -  |
| **404** | The subscription is not found |  -  |
| **409** | The subscription id is already used. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="deactivateSubscription"></a>
# **deactivateSubscription**
> deactivateSubscription(id)

Deactivate a subscription to the orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deactivateSubscription(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#deactivateSubscription");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Subscription deactivation accepted |  -  |
| **404** | The subscription is not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="deleteSubscription"></a>
# **deleteSubscription**
> deleteSubscription(id)

Delete a subscription to the orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteSubscription(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#deleteSubscription");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Subscription deletion accepted |  -  |
| **404** | The subscription is not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getSubscription"></a>
# **getSubscription**
> SubscriptionIndex getSubscription(id)

Get a subscription to the orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      SubscriptionIndex result = apiInstance.getSubscription(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#getSubscription");
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
| **id** | **String**|  | |

### Return type

[**SubscriptionIndex**](SubscriptionIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription info |  -  |
| **404** | The subscription is not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getSubscriptionList"></a>
# **getSubscriptionList**
> List&lt;SubscriptionIndex&gt; getSubscriptionList()

Get the subscription list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    try {
      List<SubscriptionIndex> result = apiInstance.getSubscriptionList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#getSubscriptionList");
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

[**List&lt;SubscriptionIndex&gt;**](SubscriptionIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subscription list |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getSubscriptionPushReporting"></a>
# **getSubscriptionPushReporting**
> List&lt;SubscriptionPushReporting&gt; getSubscriptionPushReporting(id, pageNumber, pageSize)

Get the push reporting related to this subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    Integer pageNumber = 56; // Integer | 
    Integer pageSize = 56; // Integer | 
    try {
      List<SubscriptionPushReporting> result = apiInstance.getSubscriptionPushReporting(id, pageNumber, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#getSubscriptionPushReporting");
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
| **id** | **String**|  | |
| **pageNumber** | **Integer**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |

### Return type

[**List&lt;SubscriptionPushReporting&gt;**](SubscriptionPushReporting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription push reporting info |  * Link - Based on the RFC 5988 - Web Linking, the page navigation will be indicated here with the rel&#x3D;next, rel&#x3D;previous, rel&#x3D;first, rel&#x3D;last, the pageNumber and the pageSize will be indicated in the link param <br>  * X-Total-Count - The total item count related to this query <br>  |
| **404** | The subscription is not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="retryPushOrders"></a>
# **retryPushOrders**
> retryPushOrders(id)

Force retry push orders immediatly

In case your subscription consumption is unavailable and your subscription is still active you can ask to retry immediatly to push orders instead of waiting the next scheduled retry date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersSubscriptionsSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersSubscriptionsSubscriptionsApi apiInstance = new MarketplacesOrdersSubscriptionsSubscriptionsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.retryPushOrders(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersSubscriptionsSubscriptionsApi#retryPushOrders");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Retry push orders request accepted |  -  |
| **404** | The subscription is not found |  -  |
| **409** | The subscription is deactivated or your subscription consumption availability status is available. |  -  |
| **0** | Occurs when something goes wrong |  -  |

