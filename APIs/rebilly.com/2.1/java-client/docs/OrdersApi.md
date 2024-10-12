# OrdersApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSubscriptionCancellation**](OrdersApi.md#deleteSubscriptionCancellation) | **DELETE** /subscription-cancellations/{id} | Delete a cancellation |
| [**deleteSubscriptionTimeline**](OrdersApi.md#deleteSubscriptionTimeline) | **DELETE** /subscriptions/{id}/timeline/{messageId} | Delete an Order Timeline message |
| [**getSubscription**](OrdersApi.md#getSubscription) | **GET** /subscriptions/{id} | Retrieve an order |
| [**getSubscriptionCancellation**](OrdersApi.md#getSubscriptionCancellation) | **GET** /subscription-cancellations/{id} | Retrieve an order сancellation |
| [**getSubscriptionCancellationCollection**](OrdersApi.md#getSubscriptionCancellationCollection) | **GET** /subscription-cancellations | Retrieve a list of cancellations |
| [**getSubscriptionCollection**](OrdersApi.md#getSubscriptionCollection) | **GET** /subscriptions | Retrieve a list of orders |
| [**getSubscriptionReactivation**](OrdersApi.md#getSubscriptionReactivation) | **GET** /subscription-reactivations/{id} | Retrieve an order reactivation |
| [**getSubscriptionReactivationCollection**](OrdersApi.md#getSubscriptionReactivationCollection) | **GET** /subscription-reactivations | Retrieve a list of reactivations |
| [**getSubscriptionTimeline**](OrdersApi.md#getSubscriptionTimeline) | **GET** /subscriptions/{id}/timeline/{messageId} | Retrieve an Order Timeline message |
| [**getSubscriptionTimelineCollection**](OrdersApi.md#getSubscriptionTimelineCollection) | **GET** /subscriptions/{id}/timeline | Retrieve a list of order timeline messages |
| [**getSubscriptionUpcomingInvoiceCollection**](OrdersApi.md#getSubscriptionUpcomingInvoiceCollection) | **GET** /subscriptions/{id}/upcoming-invoices | Retrieve subscription order&#39;s upcoming invoice |
| [**postSubscription**](OrdersApi.md#postSubscription) | **POST** /subscriptions | Create an order |
| [**postSubscriptionCancellation**](OrdersApi.md#postSubscriptionCancellation) | **POST** /subscription-cancellations | Cancel an order |
| [**postSubscriptionInterimInvoice**](OrdersApi.md#postSubscriptionInterimInvoice) | **POST** /subscriptions/{id}/interim-invoice | Issue an interim invoice for a subscription order |
| [**postSubscriptionItemsChange**](OrdersApi.md#postSubscriptionItemsChange) | **POST** /subscriptions/{id}/change-items | Change an order&#39;s items |
| [**postSubscriptionReactivation**](OrdersApi.md#postSubscriptionReactivation) | **POST** /subscription-reactivations | Reactivate an order |
| [**postSubscriptionTimeline**](OrdersApi.md#postSubscriptionTimeline) | **POST** /subscriptions/{id}/timeline | Create an order Timeline comment |
| [**postUpcomingInvoiceIssuance**](OrdersApi.md#postUpcomingInvoiceIssuance) | **POST** /subscriptions/{id}/upcoming-invoices/{invoiceId}/issue | Issue an upcoming invoice for early pay |
| [**putSubscription**](OrdersApi.md#putSubscription) | **PUT** /subscriptions/{id} | Upsert an order with predefined ID |
| [**putSubscriptionCancellation**](OrdersApi.md#putSubscriptionCancellation) | **PUT** /subscription-cancellations/{id} | Cancel an order |


<a id="deleteSubscriptionCancellation"></a>
# **deleteSubscriptionCancellation**
> deleteSubscriptionCancellation(id, organizationId)

Delete a cancellation

Delete an order&#39;s cancellation. Only draft can be deleted.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      apiInstance.deleteSubscriptionCancellation(id, organizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#deleteSubscriptionCancellation");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

null (empty response body)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Cancellaton was deleted. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **409** | Conflict. |  -  |

<a id="deleteSubscriptionTimeline"></a>
# **deleteSubscriptionTimeline**
> deleteSubscriptionTimeline(id, messageId, organizationId)

Delete an Order Timeline message

Delete an Order Timeline message with predefined identifier string. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String messageId = "messageId_example"; // String | The Order Timeline message ID.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      apiInstance.deleteSubscriptionTimeline(id, messageId, organizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#deleteSubscriptionTimeline");
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
| **id** | **String**| The resource identifier string. | |
| **messageId** | **String**| The Order Timeline message ID. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

null (empty response body)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Order Timeline message was deleted. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **409** | Conflict. |  -  |

<a id="getSubscription"></a>
# **getSubscription**
> Subscription getSubscription(id, organizationId, expand)

Retrieve an order

Retrieve an order with specified identifier string. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      Subscription result = apiInstance.getSubscription(id, organizationId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscription");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getSubscriptionCancellation"></a>
# **getSubscriptionCancellation**
> SubscriptionCancellation getSubscriptionCancellation(id, organizationId)

Retrieve an order сancellation

Retrieve an order сancellation with specified identifier string.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      SubscriptionCancellation result = apiInstance.getSubscriptionCancellation(id, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionCancellation");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**SubscriptionCancellation**](SubscriptionCancellation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancellation was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getSubscriptionCancellationCollection"></a>
# **getSubscriptionCancellationCollection**
> List&lt;SubscriptionCancellation&gt; getSubscriptionCancellationCollection(organizationId, limit, offset, filter, sort)

Retrieve a list of cancellations

Retrieve a list of cancellations for all subscriptions.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    try {
      List<SubscriptionCancellation> result = apiInstance.getSubscriptionCancellationCollection(organizationId, limit, offset, filter, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionCancellationCollection");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |

### Return type

[**List&lt;SubscriptionCancellation&gt;**](SubscriptionCancellation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of cancellations was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="getSubscriptionCollection"></a>
# **getSubscriptionCollection**
> List&lt;Subscription&gt; getSubscriptionCollection(organizationId, filter, sort, limit, offset, q, expand)

Retrieve a list of orders

Retrieve a list of orders. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String q = "q_example"; // String | The partial search of the text fields.
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      List<Subscription> result = apiInstance.getSubscriptionCollection(organizationId, filter, sort, limit, offset, q, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionCollection");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **q** | **String**| The partial search of the text fields. | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of subscriptions was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="getSubscriptionReactivation"></a>
# **getSubscriptionReactivation**
> SubscriptionReactivation getSubscriptionReactivation(id, organizationId)

Retrieve an order reactivation

Retrieve an order reactivation with specified identifier string.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      SubscriptionReactivation result = apiInstance.getSubscriptionReactivation(id, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionReactivation");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**SubscriptionReactivation**](SubscriptionReactivation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reactivation was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getSubscriptionReactivationCollection"></a>
# **getSubscriptionReactivationCollection**
> List&lt;SubscriptionReactivation&gt; getSubscriptionReactivationCollection(organizationId, limit, offset, filter, sort)

Retrieve a list of reactivations

Retrieve a list of reactivations for all subscriptions.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    try {
      List<SubscriptionReactivation> result = apiInstance.getSubscriptionReactivationCollection(organizationId, limit, offset, filter, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionReactivationCollection");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |

### Return type

[**List&lt;SubscriptionReactivation&gt;**](SubscriptionReactivation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of reactivations was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="getSubscriptionTimeline"></a>
# **getSubscriptionTimeline**
> OrderTimeline getSubscriptionTimeline(id, messageId, organizationId)

Retrieve an Order Timeline message

Retrieve a order message with specified identifier string. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String messageId = "messageId_example"; // String | The Order Timeline message ID.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      OrderTimeline result = apiInstance.getSubscriptionTimeline(id, messageId, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionTimeline");
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
| **id** | **String**| The resource identifier string. | |
| **messageId** | **String**| The Order Timeline message ID. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**OrderTimeline**](OrderTimeline.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order message was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getSubscriptionTimelineCollection"></a>
# **getSubscriptionTimelineCollection**
> List&lt;OrderTimeline&gt; getSubscriptionTimelineCollection(id, organizationId, limit, offset, filter, sort, q)

Retrieve a list of order timeline messages

Retrieve a list of order timeline messages. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    String q = "q_example"; // String | The partial search of the text fields.
    try {
      List<OrderTimeline> result = apiInstance.getSubscriptionTimelineCollection(id, organizationId, limit, offset, filter, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionTimelineCollection");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |
| **q** | **String**| The partial search of the text fields. | [optional] |

### Return type

[**List&lt;OrderTimeline&gt;**](OrderTimeline.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of order timeline messages was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |

<a id="getSubscriptionUpcomingInvoiceCollection"></a>
# **getSubscriptionUpcomingInvoiceCollection**
> List&lt;Invoice&gt; getSubscriptionUpcomingInvoiceCollection(id, organizationId, expand)

Retrieve subscription order&#39;s upcoming invoice

Retrieve an upcoming invoice from the specified subscription order. The endpoint is temporary before upcoming invoices get a complete integration. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      List<Invoice> result = apiInstance.getSubscriptionUpcomingInvoiceCollection(id, organizationId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getSubscriptionUpcomingInvoiceCollection");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**List&lt;Invoice&gt;**](Invoice.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upcoming invoices are retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="postSubscription"></a>
# **postSubscription**
> Subscription postSubscription(subscription, organizationId, expand)

Create an order

Create an order. Consider using the upsert. operation to accomplish this task. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Subscription subscription = new Subscription(); // Subscription | Order resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      Subscription result = apiInstance.postSubscription(subscription, organizationId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postSubscription");
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
| **subscription** | [**Subscription**](Subscription.md)| Order resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Order was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postSubscriptionCancellation"></a>
# **postSubscriptionCancellation**
> SubscriptionCancellation postSubscriptionCancellation(subscriptionCancellation, organizationId)

Cancel an order

Cancel an order or preview the cancellation parameters before that.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    SubscriptionCancellation subscriptionCancellation = new SubscriptionCancellation(); // SubscriptionCancellation | Cancellation resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      SubscriptionCancellation result = apiInstance.postSubscriptionCancellation(subscriptionCancellation, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postSubscriptionCancellation");
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
| **subscriptionCancellation** | [**SubscriptionCancellation**](SubscriptionCancellation.md)| Cancellation resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**SubscriptionCancellation**](SubscriptionCancellation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cancellation was created, the order is or will be deactivated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postSubscriptionInterimInvoice"></a>
# **postSubscriptionInterimInvoice**
> Invoice postSubscriptionInterimInvoice(id, subscriptionInvoice, organizationId)

Issue an interim invoice for a subscription order

Issue an interim invoice for a subscription, typically used in conjunction. with plan changes and pro rata adjustments. This process creates an invoice, adds the subscription&#39;s line items to the invoice, and issues the invoice, and applies payment to it if a transaction id is supplied. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    SubscriptionInvoice subscriptionInvoice = new SubscriptionInvoice(); // SubscriptionInvoice | Issue an interim invoice.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Invoice result = apiInstance.postSubscriptionInterimInvoice(id, subscriptionInvoice, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postSubscriptionInterimInvoice");
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
| **id** | **String**| The resource identifier string. | |
| **subscriptionInvoice** | [**SubscriptionInvoice**](SubscriptionInvoice.md)| Issue an interim invoice. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invoice was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postSubscriptionItemsChange"></a>
# **postSubscriptionItemsChange**
> Subscription postSubscriptionItemsChange(id, subscriptionChange, organizationId)

Change an order&#39;s items

Change an order&#39;s items or quantities and designate when and if there should be pro-rata credits given. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    SubscriptionChange subscriptionChange = new SubscriptionChange(); // SubscriptionChange | Change items request.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Subscription result = apiInstance.postSubscriptionItemsChange(id, subscriptionChange, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postSubscriptionItemsChange");
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
| **id** | **String**| The resource identifier string. | |
| **subscriptionChange** | [**SubscriptionChange**](SubscriptionChange.md)| Change items request. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Order was changed. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postSubscriptionReactivation"></a>
# **postSubscriptionReactivation**
> SubscriptionReactivation postSubscriptionReactivation(subscriptionReactivation, organizationId)

Reactivate an order

Reactivate a subscription.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    SubscriptionReactivation subscriptionReactivation = new SubscriptionReactivation(); // SubscriptionReactivation | Reactivation resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      SubscriptionReactivation result = apiInstance.postSubscriptionReactivation(subscriptionReactivation, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postSubscriptionReactivation");
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
| **subscriptionReactivation** | [**SubscriptionReactivation**](SubscriptionReactivation.md)| Reactivation resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**SubscriptionReactivation**](SubscriptionReactivation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reactivation was created, the order is active and won&#39;t be. deactivated. If there was a cancellation with status \&quot;confirmed\&quot;, it is revoked.  |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postSubscriptionTimeline"></a>
# **postSubscriptionTimeline**
> OrderTimeline postSubscriptionTimeline(id, orderTimeline, organizationId)

Create an order Timeline comment

Create an order Timeline comment. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    OrderTimeline orderTimeline = new OrderTimeline(); // OrderTimeline | Order Timeline resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      OrderTimeline result = apiInstance.postSubscriptionTimeline(id, orderTimeline, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postSubscriptionTimeline");
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
| **id** | **String**| The resource identifier string. | |
| **orderTimeline** | [**OrderTimeline**](OrderTimeline.md)| Order Timeline resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**OrderTimeline**](OrderTimeline.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Order Timeline comment was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postUpcomingInvoiceIssuance"></a>
# **postUpcomingInvoiceIssuance**
> Invoice postUpcomingInvoiceIssuance(id, invoiceId, invoiceIssue, organizationId)

Issue an upcoming invoice for early pay

Issue an upcoming invoice with specified identifier string for early pay. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String invoiceId = "invoiceId_example"; // String | The Upcoming Invoice ID.
    InvoiceIssue invoiceIssue = new InvoiceIssue(); // InvoiceIssue | InvoiceIssue resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Invoice result = apiInstance.postUpcomingInvoiceIssuance(id, invoiceId, invoiceIssue, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postUpcomingInvoiceIssuance");
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
| **id** | **String**| The resource identifier string. | |
| **invoiceId** | **String**| The Upcoming Invoice ID. | |
| **invoiceIssue** | [**InvoiceIssue**](InvoiceIssue.md)| InvoiceIssue resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Upcoming Invoice was issued successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **409** | Conflict. |  -  |

<a id="putSubscription"></a>
# **putSubscription**
> Subscription putSubscription(id, subscription, organizationId, expand)

Upsert an order with predefined ID

Create or update an order with predefined identifier string. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    Subscription subscription = new Subscription(); // Subscription | Order resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      Subscription result = apiInstance.putSubscription(id, subscription, organizationId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#putSubscription");
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
| **id** | **String**| The resource identifier string. | |
| **subscription** | [**Subscription**](Subscription.md)| Order resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order was updated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **201** | Order was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="putSubscriptionCancellation"></a>
# **putSubscriptionCancellation**
> SubscriptionCancellation putSubscriptionCancellation(id, subscriptionCancellation, organizationId)

Cancel an order

Cancel a subscription.

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    SubscriptionCancellation subscriptionCancellation = new SubscriptionCancellation(); // SubscriptionCancellation | Cancellation resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      SubscriptionCancellation result = apiInstance.putSubscriptionCancellation(id, subscriptionCancellation, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#putSubscriptionCancellation");
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
| **id** | **String**| The resource identifier string. | |
| **subscriptionCancellation** | [**SubscriptionCancellation**](SubscriptionCancellation.md)| Cancellation resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**SubscriptionCancellation**](SubscriptionCancellation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancellation was updated, the order is or will be deactivated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **201** | Cancellation was created, the order is or will be deactivated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

