# MarketplacesOrdersGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMarketplaceAccountsSynchronization**](MarketplacesOrdersGlobalApi.md#getMarketplaceAccountsSynchronization) | **GET** /v2/user/marketplaces/orders/status | [DEPRECATED] Get current synchronization status between your marketplaces and BeezUP accounts |
| [**getOrderIndex**](MarketplacesOrdersGlobalApi.md#getOrderIndex) | **GET** /v2/user/marketplaces/orders/ | [DEPRECATED] Get all actions you can do on the order API |
| [**harvestAll**](MarketplacesOrdersGlobalApi.md#harvestAll) | **POST** /v2/user/marketplaces/orders/harvest | [DEPRECATED] Send harvest request to all your marketplaces |


<a id="getMarketplaceAccountsSynchronization"></a>
# **getMarketplaceAccountsSynchronization**
> AccountSynchronizationList getMarketplaceAccountsSynchronization(storeId, ifNoneMatch)

[DEPRECATED] Get current synchronization status between your marketplaces and BeezUP accounts

Use /orders/v3

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersGlobalApi apiInstance = new MarketplacesOrdersGlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The StoreId to filter by
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      AccountSynchronizationList result = apiInstance.getMarketplaceAccountsSynchronization(storeId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersGlobalApi#getMarketplaceAccountsSynchronization");
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
| **storeId** | **String**| The StoreId to filter by | [optional] |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**AccountSynchronizationList**](AccountSynchronizationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched current synchronization status |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Requested Store could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderIndex"></a>
# **getOrderIndex**
> OrderIndex getOrderIndex(ifNoneMatch)

[DEPRECATED] Get all actions you can do on the order API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersGlobalApi apiInstance = new MarketplacesOrdersGlobalApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      OrderIndex result = apiInstance.getOrderIndex(ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersGlobalApi#getOrderIndex");
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
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**OrderIndex**](OrderIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order index |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="harvestAll"></a>
# **harvestAll**
> harvestAll(storeId)

[DEPRECATED] Send harvest request to all your marketplaces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersGlobalApi apiInstance = new MarketplacesOrdersGlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The StoreId to filter by
    try {
      apiInstance.harvestAll(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersGlobalApi#harvestAll");
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
| **storeId** | **String**| The StoreId to filter by | [optional] |

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
| **202** | Successfully sent harvest request to all marketplaces |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **404** | Requested Store could not be found |  -  |
| **409** | Failed to send harvest request because allowed rate limits have been exceeded |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **0** | Occurs when something goes wrong |  -  |

