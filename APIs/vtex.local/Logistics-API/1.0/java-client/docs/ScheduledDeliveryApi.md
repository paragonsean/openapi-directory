# ScheduledDeliveryApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addBlockedDeliveryWindows**](ScheduledDeliveryApi.md#addBlockedDeliveryWindows) | **POST** /api/logistics/pvt/configuration/carriers/{carrierId}/adddayofweekblocked | Add blocked delivery windows |
| [**apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet**](ScheduledDeliveryApi.md#apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet) | **GET** /api/logistics-capacity/resources/carrier@{capacityType}@{shippingPolicyId}/time-frames | Search capacity reservations in time range |
| [**apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet**](ScheduledDeliveryApi.md#apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet) | **GET** /api/logistics-capacity/resources/carrier@{capacityType}@{shippingPolicyId}/time-frames/{windowDay}F{windowStartTime}T{windowEndTime} | Get capacity reservation usage by window |
| [**removeBlockedDeliveryWindows**](ScheduledDeliveryApi.md#removeBlockedDeliveryWindows) | **POST** /api/logistics/pvt/configuration/carriers/{carrierId}/removedayofweekblocked | Remove blocked delivery windows |
| [**retrieveBlockedDeliveryWindows**](ScheduledDeliveryApi.md#retrieveBlockedDeliveryWindows) | **GET** /api/logistics/pvt/configuration/carriers/{carrierId}/getdayofweekblocked | Retrieve blocked delivery windows |


<a id="addBlockedDeliveryWindows"></a>
# **addBlockedDeliveryWindows**
> addBlockedDeliveryWindows(contentType, accept, carrierId, body)

Add blocked delivery windows

Adds blocked delivery windows for your store&#39;s shipping policies.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledDeliveryApi;

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

    ScheduledDeliveryApi apiInstance = new ScheduledDeliveryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String carrierId = "carrierId_example"; // String | 
    String body = "2016-08-09T08:00:00"; // String | 
    try {
      apiInstance.addBlockedDeliveryWindows(contentType, accept, carrierId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledDeliveryApi#addBlockedDeliveryWindows");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **carrierId** | **String**|  | |
| **body** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet"></a>
# **apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet**
> apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet(contentType, accept, capacityType, shippingPolicyId, rangeStart, rangeEnd)

Search capacity reservations in time range

Get information on all capacity reservations made to scheduled delivery windows in a given time range.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.    &gt; Note that the combined string &#x60;carrier@{capacityType}@{shippingPolicyId}&#x60; can be referred to as a \&quot;resource\&quot; in the API&#39;s messages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledDeliveryApi;

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

    ScheduledDeliveryApi apiInstance = new ScheduledDeliveryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.availability.v1+json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String capacityType = "{{capacityType}}"; // String | How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (`\"orders_quantity\"`) or SKUs (`\"skus_quantity\"`).
    String shippingPolicyId = "{{shippingPolicyId}}"; // String | ID of shipping policy to search.
    String rangeStart = "yyyy-mm-dd"; // String | Starting date of time range
    String rangeEnd = "yyyy-mm-dd"; // String | End date of time range.
    try {
      apiInstance.apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet(contentType, accept, capacityType, shippingPolicyId, rangeStart, rangeEnd);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledDeliveryApi#apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **capacityType** | **String**| How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (&#x60;\&quot;orders_quantity\&quot;&#x60;) or SKUs (&#x60;\&quot;skus_quantity\&quot;&#x60;). | |
| **shippingPolicyId** | **String**| ID of shipping policy to search. | |
| **rangeStart** | **String**| Starting date of time range | |
| **rangeEnd** | **String**| End date of time range. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet"></a>
# **apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet**
> apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet(contentType, accept, capacityType, shippingPolicyId, windowDay, windowStartTime, windowEndTime)

Get capacity reservation usage by window

Retrieves capacity usage of a specific scheduled delivery reservation window.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.    &gt; Note that the combined string &#x60;carrier@{capacityType}@{shippingPolicyId}&#x60; can be referred to as a \&quot;resource\&quot; in the API&#39;s messages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledDeliveryApi;

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

    ScheduledDeliveryApi apiInstance = new ScheduledDeliveryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.availability.v1+json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String capacityType = "{{capacityType}}"; // String | How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (`\"orders_quantity\"`) or SKUs (`\"skus_quantity\"`).
    String shippingPolicyId = "{{shippingPolicyId}}"; // String | ID of shipping policy to search.
    String windowDay = "yyyy-mm-dd"; // String | Day of the specific scheduled delivery window to be consulted for reservations.
    String windowStartTime = "hhmm"; // String | Start time of specific scheduled delivery window to be consulted for reservations.
    String windowEndTime = "hhmm"; // String | End time of specific scheduled delivery window to be consulted for reservations.
    try {
      apiInstance.apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet(contentType, accept, capacityType, shippingPolicyId, windowDay, windowStartTime, windowEndTime);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledDeliveryApi#apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **capacityType** | **String**| How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (&#x60;\&quot;orders_quantity\&quot;&#x60;) or SKUs (&#x60;\&quot;skus_quantity\&quot;&#x60;). | |
| **shippingPolicyId** | **String**| ID of shipping policy to search. | |
| **windowDay** | **String**| Day of the specific scheduled delivery window to be consulted for reservations. | |
| **windowStartTime** | **String**| Start time of specific scheduled delivery window to be consulted for reservations. | |
| **windowEndTime** | **String**| End time of specific scheduled delivery window to be consulted for reservations. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeBlockedDeliveryWindows"></a>
# **removeBlockedDeliveryWindows**
> removeBlockedDeliveryWindows(contentType, accept, carrierId, body)

Remove blocked delivery windows

Removes the blocked delivery windows set to your store&#39;s shipping policies.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledDeliveryApi;

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

    ScheduledDeliveryApi apiInstance = new ScheduledDeliveryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String carrierId = "carrierId_example"; // String | 
    String body = "2016-08-09T08:00:00"; // String | 
    try {
      apiInstance.removeBlockedDeliveryWindows(contentType, accept, carrierId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledDeliveryApi#removeBlockedDeliveryWindows");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **carrierId** | **String**|  | |
| **body** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieveBlockedDeliveryWindows"></a>
# **retrieveBlockedDeliveryWindows**
> retrieveBlockedDeliveryWindows(contentType, accept, carrierId)

Retrieve blocked delivery windows

Lists all blocked delivery windows of your store&#39;s shipping policies, searching by carrier ID.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledDeliveryApi;

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

    ScheduledDeliveryApi apiInstance = new ScheduledDeliveryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String carrierId = "carrierId_example"; // String | 
    try {
      apiInstance.retrieveBlockedDeliveryWindows(contentType, accept, carrierId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledDeliveryApi#retrieveBlockedDeliveryWindows");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **carrierId** | **String**|  | |

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
| **200** | OK |  -  |

