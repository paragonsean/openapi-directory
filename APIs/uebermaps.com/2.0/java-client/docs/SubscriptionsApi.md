# SubscriptionsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsIdSubscriptionsDelete**](SubscriptionsApi.md#mapsIdSubscriptionsDelete) | **DELETE** /maps/{id}/subscriptions | Unsubscribe from map |
| [**mapsIdSubscriptionsGet**](SubscriptionsApi.md#mapsIdSubscriptionsGet) | **GET** /maps/{id}/subscriptions | List subscriptions for a given map |
| [**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions | List subscriptions. Pass no parameters to get own subscriptions |
| [**subscriptionsPost**](SubscriptionsApi.md#subscriptionsPost) | **POST** /subscriptions | Create map subscription |


<a id="mapsIdSubscriptionsDelete"></a>
# **mapsIdSubscriptionsDelete**
> Subscription mapsIdSubscriptionsDelete(id)

Unsubscribe from map

Unsubscribe from map.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer id = 56; // Integer | map id
    try {
      Subscription result = apiInstance.mapsIdSubscriptionsDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#mapsIdSubscriptionsDelete");
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
| **id** | **Integer**| map id | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted subscription. |  -  |

<a id="mapsIdSubscriptionsGet"></a>
# **mapsIdSubscriptionsGet**
> List&lt;Subscription&gt; mapsIdSubscriptionsGet(id)

List subscriptions for a given map

List subscriptions for a given map.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer id = 56; // Integer | Id of map
    try {
      List<Subscription> result = apiInstance.mapsIdSubscriptionsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#mapsIdSubscriptionsGet");
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
| **id** | **Integer**| Id of map | |

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
| **200** | Contains list of subscriptions. |  -  |

<a id="subscriptionsGet"></a>
# **subscriptionsGet**
> List&lt;Subscription&gt; subscriptionsGet(userId, mapId)

List subscriptions. Pass no parameters to get own subscriptions

List subscriptions.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer userId = 56; // Integer | Id of user
    Integer mapId = 56; // Integer | Id of map
    try {
      List<Subscription> result = apiInstance.subscriptionsGet(userId, mapId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionsGet");
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
| **userId** | **Integer**| Id of user | [optional] |
| **mapId** | **Integer**| Id of map | [optional] |

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
| **200** | Contains list of subscriptions. |  -  |

<a id="subscriptionsPost"></a>
# **subscriptionsPost**
> Subscription subscriptionsPost(mapId)

Create map subscription

Create map subscription.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    BigDecimal mapId = new BigDecimal(78); // BigDecimal | map id
    try {
      Subscription result = apiInstance.subscriptionsPost(mapId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionsPost");
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
| **mapId** | **BigDecimal**| map id | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains subscription data. |  -  |

