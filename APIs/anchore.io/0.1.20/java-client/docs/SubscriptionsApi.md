# SubscriptionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSubscription**](SubscriptionsApi.md#addSubscription) | **POST** /subscriptions | Add a subscription of a specific type |
| [**deleteSubscription**](SubscriptionsApi.md#deleteSubscription) | **DELETE** /subscriptions/{subscriptionId} | Delete subscriptions of a specific type |
| [**getSubscription**](SubscriptionsApi.md#getSubscription) | **GET** /subscriptions/{subscriptionId} | Get a specific subscription set |
| [**listSubscriptions**](SubscriptionsApi.md#listSubscriptions) | **GET** /subscriptions | List all subscriptions |
| [**updateSubscription**](SubscriptionsApi.md#updateSubscription) | **PUT** /subscriptions/{subscriptionId} | Update an existing and specific subscription |


<a id="addSubscription"></a>
# **addSubscription**
> List&lt;Subscription&gt; addSubscription(subscriptionRequest, xAnchoreAccount)

Add a subscription of a specific type

Create a new subscription to watch a tag and get notifications of changes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    SubscriptionRequest subscriptionRequest = new SubscriptionRequest(); // SubscriptionRequest | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Subscription> result = apiInstance.addSubscription(subscriptionRequest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#addSubscription");
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
| **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription add success |  -  |

<a id="deleteSubscription"></a>
# **deleteSubscription**
> deleteSubscription(subscriptionId, xAnchoreAccount)

Delete subscriptions of a specific type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      apiInstance.deleteSubscription(subscriptionId, xAnchoreAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#deleteSubscription");
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
| **subscriptionId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

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
| **200** | Delete success |  -  |
| **500** | Internal Error |  -  |

<a id="getSubscription"></a>
# **getSubscription**
> List&lt;Subscription&gt; getSubscription(subscriptionId, xAnchoreAccount)

Get a specific subscription set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Subscription> result = apiInstance.getSubscription(subscriptionId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#getSubscription");
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
| **subscriptionId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Filtered subscription list by type |  -  |
| **500** | Internal Error |  -  |

<a id="listSubscriptions"></a>
# **listSubscriptions**
> List&lt;Subscription&gt; listSubscriptions(subscriptionKey, subscriptionType, xAnchoreAccount)

List all subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String subscriptionKey = "subscriptionKey_example"; // String | filter only subscriptions matching key
    String subscriptionType = "subscriptionType_example"; // String | filter only subscriptions matching type
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Subscription> result = apiInstance.listSubscriptions(subscriptionKey, subscriptionType, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#listSubscriptions");
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
| **subscriptionKey** | **String**| filter only subscriptions matching key | [optional] |
| **subscriptionType** | **String**| filter only subscriptions matching type | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription listing |  -  |
| **500** | Internal Error |  -  |

<a id="updateSubscription"></a>
# **updateSubscription**
> List&lt;Subscription&gt; updateSubscription(subscriptionId, subscriptionUpdate, xAnchoreAccount)

Update an existing and specific subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | 
    SubscriptionUpdate subscriptionUpdate = new SubscriptionUpdate(); // SubscriptionUpdate | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Subscription> result = apiInstance.updateSubscription(subscriptionId, subscriptionUpdate, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#updateSubscription");
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
| **subscriptionId** | **String**|  | |
| **subscriptionUpdate** | [**SubscriptionUpdate**](SubscriptionUpdate.md)|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription add success |  -  |

