# NotificationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inventoryNotification**](NotificationApi.md#inventoryNotification) | **POST** /notificator/{sellerId}/changenotification/{skuId}/inventory | Notify marketplace of inventory update |
| [**priceNotification**](NotificationApi.md#priceNotification) | **POST** /notificator/{sellerId}/changenotification/{skuId}/price | Notify marketplace of price update |


<a id="inventoryNotification"></a>
# **inventoryNotification**
> inventoryNotification(accountName, environment, accept, contentType, sellerId, skuId)

Notify marketplace of inventory update

This endpoint is used by *sellers* to notify marketplaces that the inventory level has changed for one of their SKUs.   There is no request body in this call, indicating the new inventory level, for instance. It only notifies a specific marketplace (&#x60;accountName&#x60;) that a seller (&#x60;sellerId&#x60;) has changed the inventory level of an SKU (&#x60;skuId&#x60;).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated inventory  information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationApi;

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

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    String skuId = "1234"; // String | A string that identifies the SKU in the seller, that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications.
    try {
      apiInstance.inventoryNotification(accountName, environment, accept, contentType, sellerId, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#inventoryNotification");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to seller123] |
| **skuId** | **String**| A string that identifies the SKU in the seller, that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications. | [default to 1234] |

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
| **202** | Accepted |  -  |

<a id="priceNotification"></a>
# **priceNotification**
> priceNotification(accountName, contentType, environment, accept, sellerId, skuId)

Notify marketplace of price update

This endpoint is used by *sellers* to notify marketplaces that the price has changed for one of their SKUs.   There is no request body in this call, indicating the new price value, for instance. It only notifies a specific marketplace (&#x60;accountName&#x60;) that a seller (&#x60;sellerId&#x60;) has changed the price of an SKU (&#x60;skuId&#x60;).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated price information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationApi;

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

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    String skuId = "1234"; // String | A string that identifies the seller's SKU that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications.
    try {
      apiInstance.priceNotification(accountName, contentType, environment, accept, sellerId, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#priceNotification");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account. | [default to apiexamples] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to seller123] |
| **skuId** | **String**| A string that identifies the seller&#39;s SKU that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications. | [default to 1234] |

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
| **202** | Accepted |  -  |

