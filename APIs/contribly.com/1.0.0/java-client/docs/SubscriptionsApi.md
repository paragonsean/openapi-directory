# SubscriptionsApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionTypesGet**](SubscriptionsApi.md#subscriptionTypesGet) | **GET** /subscription-types | Subscription types |
| [**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions | List subscriptions for the authorised user. |
| [**subscriptionsIdDelete**](SubscriptionsApi.md#subscriptionsIdDelete) | **DELETE** /subscriptions/{id} | Delete a subscription. |


<a id="subscriptionTypesGet"></a>
# **subscriptionTypesGet**
> List&lt;SubscriptionType&gt; subscriptionTypesGet()

Subscription types

List available subscription types

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
    defaultClient.setBasePath("https://api.contribly.com/1");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    try {
      List<SubscriptionType> result = apiInstance.subscriptionTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionTypesGet");
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

[**List&lt;SubscriptionType&gt;**](SubscriptionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of subscription event types |  -  |

<a id="subscriptionsGet"></a>
# **subscriptionsGet**
> List&lt;Subscription&gt; subscriptionsGet(subscriptionSubmission)

List subscriptions for the authorised user.

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
    defaultClient.setBasePath("https://api.contribly.com/1");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    SubscriptionSubmission subscriptionSubmission = new SubscriptionSubmission(); // SubscriptionSubmission | Subscription to be created
    try {
      List<Subscription> result = apiInstance.subscriptionsGet(subscriptionSubmission);
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
| **subscriptionSubmission** | [**SubscriptionSubmission**](SubscriptionSubmission.md)| Subscription to be created | |

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
| **200** | A list of notification subscriptions |  * X-total-count - Total number of matching users <br>  |

<a id="subscriptionsIdDelete"></a>
# **subscriptionsIdDelete**
> subscriptionsIdDelete(id)

Delete a subscription.

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
    defaultClient.setBasePath("https://api.contribly.com/1");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String id = "id_example"; // String | Id of the subscription to delete
    try {
      apiInstance.subscriptionsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionsIdDelete");
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
| **id** | **String**| Id of the subscription to delete | |

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
| **200** | The subscription has been successfully deleted. |  -  |

