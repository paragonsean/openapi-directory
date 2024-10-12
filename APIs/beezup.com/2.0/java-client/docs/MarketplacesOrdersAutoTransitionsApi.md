# MarketplacesOrdersAutoTransitionsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureAutomaticTransitions**](MarketplacesOrdersAutoTransitionsApi.md#configureAutomaticTransitions) | **POST** /v2/user/marketplaces/orders/automaticTransitions | Configure new or existing automatic Order status transition |
| [**getAutomaticTransitions**](MarketplacesOrdersAutoTransitionsApi.md#getAutomaticTransitions) | **GET** /v2/user/marketplaces/orders/automaticTransitions | Get list of configured automatic Order status transitions |


<a id="configureAutomaticTransitions"></a>
# **configureAutomaticTransitions**
> configureAutomaticTransitions(configureAutomaticTransitionRequest)

Configure new or existing automatic Order status transition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersAutoTransitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersAutoTransitionsApi apiInstance = new MarketplacesOrdersAutoTransitionsApi(defaultClient);
    ConfigureAutomaticTransitionRequest configureAutomaticTransitionRequest = new ConfigureAutomaticTransitionRequest(); // ConfigureAutomaticTransitionRequest | 
    try {
      apiInstance.configureAutomaticTransitions(configureAutomaticTransitionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersAutoTransitionsApi#configureAutomaticTransitions");
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
| **configureAutomaticTransitionRequest** | [**ConfigureAutomaticTransitionRequest**](ConfigureAutomaticTransitionRequest.md)|  | |

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
| **204** | Successfully confirugred new or existing automatic Order status transition |  -  |
| **400** | Requested automatic Order status transition could not be configured |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getAutomaticTransitions"></a>
# **getAutomaticTransitions**
> AutomaticTransitionInfoList getAutomaticTransitions(storeId, ifNoneMatch)

Get list of configured automatic Order status transitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersAutoTransitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersAutoTransitionsApi apiInstance = new MarketplacesOrdersAutoTransitionsApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The StoreId to filter by
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      AutomaticTransitionInfoList result = apiInstance.getAutomaticTransitions(storeId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersAutoTransitionsApi#getAutomaticTransitions");
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

[**AutomaticTransitionInfoList**](AutomaticTransitionInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched list of configured automatic Order status transitions |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Requested Store could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

