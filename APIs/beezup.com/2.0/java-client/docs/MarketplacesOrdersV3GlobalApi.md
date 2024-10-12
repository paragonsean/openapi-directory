# MarketplacesOrdersV3GlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMarketplaceAccountsSynchronizationV3**](MarketplacesOrdersV3GlobalApi.md#getMarketplaceAccountsSynchronizationV3) | **GET** /orders/v3/status |  |
| [**getOrderManagementReadyMarketplaceBusinessCode**](MarketplacesOrdersV3GlobalApi.md#getOrderManagementReadyMarketplaceBusinessCode) | **GET** /orders/v3/lov/orderManagementReadyMarketplaceBusinessCode |  |
| [**harvestAllV3**](MarketplacesOrdersV3GlobalApi.md#harvestAllV3) | **POST** /orders/v3/harvest | Send harvest request to all your marketplaces |


<a id="getMarketplaceAccountsSynchronizationV3"></a>
# **getMarketplaceAccountsSynchronizationV3**
> AccountSynchronizationList getMarketplaceAccountsSynchronizationV3(ifNoneMatch, storeIds)



Get current synchronization status between your marketplaces and BeezUP accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3GlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3GlobalApi apiInstance = new MarketplacesOrdersV3GlobalApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    List<String> storeIds = Arrays.asList(); // List<String> | StoredIds to filter
    try {
      AccountSynchronizationList result = apiInstance.getMarketplaceAccountsSynchronizationV3(ifNoneMatch, storeIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3GlobalApi#getMarketplaceAccountsSynchronizationV3");
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
| **storeIds** | [**List&lt;String&gt;**](String.md)| StoredIds to filter | [optional] |

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
| **200** | Successfully fetched the list of MarketplaceBusinessCode ready for Order Management |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **400** | Invalid store id |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderManagementReadyMarketplaceBusinessCode"></a>
# **getOrderManagementReadyMarketplaceBusinessCode**
> List&lt;ListOfValueItem&gt; getOrderManagementReadyMarketplaceBusinessCode(acceptLanguage, storeIds)



Get the list of MarketplaceBusinessCode ready for Order Management

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3GlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3GlobalApi apiInstance = new MarketplacesOrdersV3GlobalApi(defaultClient);
    List<String> acceptLanguage = Arrays.asList(); // List<String> | Indicates that the client accepts the following languages.
    List<String> storeIds = Arrays.asList(); // List<String> | StoredIds to filter
    try {
      List<ListOfValueItem> result = apiInstance.getOrderManagementReadyMarketplaceBusinessCode(acceptLanguage, storeIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3GlobalApi#getOrderManagementReadyMarketplaceBusinessCode");
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
| **acceptLanguage** | [**List&lt;String&gt;**](String.md)| Indicates that the client accepts the following languages. | [optional] |
| **storeIds** | [**List&lt;String&gt;**](String.md)| StoredIds to filter | [optional] |

### Return type

[**List&lt;ListOfValueItem&gt;**](ListOfValueItem.md)

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

<a id="harvestAllV3"></a>
# **harvestAllV3**
> harvestAllV3(storeId)

Send harvest request to all your marketplaces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3GlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3GlobalApi apiInstance = new MarketplacesOrdersV3GlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The StoreId to filter by
    try {
      apiInstance.harvestAllV3(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3GlobalApi#harvestAllV3");
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

