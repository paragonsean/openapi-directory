# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callList**](V1Api.md#callList) | **GET** /v1/subscriptions | Retrieve a list of Subscriptions for the specified Shopper |
| [**cancel**](V1Api.md#cancel) | **DELETE** /v1/subscriptions/{subscriptionId} | Cancel the specified Subscription |
| [**get**](V1Api.md#get) | **GET** /v1/subscriptions/{subscriptionId} | Retrieve details for the specified Subscription |
| [**productGroups**](V1Api.md#productGroups) | **GET** /v1/subscriptions/productGroups | Retrieve a list of ProductGroups for the specified Shopper |
| [**update**](V1Api.md#update) | **PATCH** /v1/subscriptions/{subscriptionId} | Update details for the specified Subscription |


<a id="callList"></a>
# **callList**
> SubscriptionList callList(xShopperId, xMarketId, productGroupKeys, includes, offset, limit, sort)

Retrieve a list of Subscriptions for the specified Shopper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String xShopperId = "xShopperId_example"; // String | Shopper ID to return subscriptions for when not using JWT
    String xMarketId = "en-US"; // String | The market that the response should be formatted for
    List<String> productGroupKeys = Arrays.asList(); // List<String> | Only return Subscriptions with the specified product groups
    List<String> includes = Arrays.asList(); // List<String> | Optional details to be included in the response
    Integer offset = 0; // Integer | Number of Subscriptions to skip before starting to return paged results (must be a multiple of the limit)
    Integer limit = 25; // Integer | Number of Subscriptions to retrieve in this page, starting after offset
    String sort = "expiresAt"; // String | Property name that will be used to sort results. \"-\" indicates descending
    try {
      SubscriptionList result = apiInstance.callList(xShopperId, xMarketId, productGroupKeys, includes, offset, limit, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#callList");
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
| **xShopperId** | **String**| Shopper ID to return subscriptions for when not using JWT | [optional] |
| **xMarketId** | **String**| The market that the response should be formatted for | [optional] [default to en-US] |
| **productGroupKeys** | [**List&lt;String&gt;**](String.md)| Only return Subscriptions with the specified product groups | [optional] |
| **includes** | [**List&lt;String&gt;**](String.md)| Optional details to be included in the response | [optional] [enum: addons, relations] |
| **offset** | **Integer**| Number of Subscriptions to skip before starting to return paged results (must be a multiple of the limit) | [optional] [default to 0] |
| **limit** | **Integer**| Number of Subscriptions to retrieve in this page, starting after offset | [optional] [default to 25] |
| **sort** | **String**| Property name that will be used to sort results. \&quot;-\&quot; indicates descending | [optional] [default to -expiresAt] [enum: expiresAt, -expiresAt] |

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | Invalid query parameter (custom message returned for each parameter) |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="cancel"></a>
# **cancel**
> cancel(subscriptionId, xShopperId)

Cancel the specified Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Subscription to cancel
    String xShopperId = "xShopperId_example"; // String | Shopper ID to cancel subscriptions for when not using JWT
    try {
      apiInstance.cancel(subscriptionId, xShopperId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cancel");
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
| **subscriptionId** | **String**| Unique identifier of the Subscription to cancel | |
| **xShopperId** | **String**| Shopper ID to cancel subscriptions for when not using JWT | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Failed to determine if the domain is protected (invalid domain ID)&lt;br&gt;Invalid Subscription Id&lt;br&gt;The Office 365 Subscription cannot be cancelled (shopper is migrating)&lt;br&gt;The Subscription cannot be cancelled&lt;br&gt;The Subscription cannot be cancelled (PFID is disabled for cancellation)&lt;br&gt;The Subscription cannot be cancelled (domain is protected)&lt;br&gt;The domain alert Subscription cannot be cancelled |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Failed to determine if the Office 365 account is migrating&lt;br&gt;Failed to determine if the domain alert is cancellable&lt;br&gt;Failed to determine if the domain is protected&lt;br&gt;Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="get"></a>
# **get**
> Subscription get(subscriptionId, xShopperId, xMarketId)

Retrieve details for the specified Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Subscription to retrieve
    String xShopperId = "xShopperId_example"; // String | Shopper ID to be operated on, if different from JWT
    String xMarketId = "en-US"; // String | Unique identifier of the Market in which the request is happening
    try {
      Subscription result = apiInstance.get(subscriptionId, xShopperId, xMarketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#get");
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
| **subscriptionId** | **String**| Unique identifier of the Subscription to retrieve | |
| **xShopperId** | **String**| Shopper ID to be operated on, if different from JWT | [optional] |
| **xMarketId** | **String**| Unique identifier of the Market in which the request is happening | [optional] [default to en-US] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Invalid Subscription Id |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="productGroups"></a>
# **productGroups**
> List&lt;ProductGroup&gt; productGroups(xShopperId, xMarketId)

Retrieve a list of ProductGroups for the specified Shopper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String xShopperId = "xShopperId_example"; // String | Shopper ID to return data for when not using JWT
    String xMarketId = "en-US"; // String | The market that the response should be formatted for
    try {
      List<ProductGroup> result = apiInstance.productGroups(xShopperId, xMarketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#productGroups");
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
| **xShopperId** | **String**| Shopper ID to return data for when not using JWT | [optional] |
| **xMarketId** | **String**| The market that the response should be formatted for | [optional] [default to en-US] |

### Return type

[**List&lt;ProductGroup&gt;**](ProductGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="update"></a>
# **update**
> update(subscriptionId, subscriptionUpdate)

Update details for the specified Subscription

Only Subscription properties that can be changed without immediate financial impact can be modified via PATCH, whereas some properties can be changed by purchasing a renewal&lt;br/&gt;&lt;strong&gt;This endpoint only supports JWT authentication&lt;/strong&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Subscription to update
    SubscriptionUpdate subscriptionUpdate = new SubscriptionUpdate(); // SubscriptionUpdate | Details of the Subscription to change
    try {
      apiInstance.update(subscriptionId, subscriptionUpdate);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#update");
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
| **subscriptionId** | **String**| Unique identifier of the Subscription to update | |
| **subscriptionUpdate** | [**SubscriptionUpdate**](SubscriptionUpdate.md)| Details of the Subscription to change | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access &lt;br&gt; This method only supports JWT authentication |  -  |
| **404** | Subscription not found &lt;br&gt; Payment profile not found |  -  |
| **500** | Internal server error |  -  |

