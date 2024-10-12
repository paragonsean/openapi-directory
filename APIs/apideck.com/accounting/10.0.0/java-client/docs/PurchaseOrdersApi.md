# PurchaseOrdersApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**purchaseOrdersAdd**](PurchaseOrdersApi.md#purchaseOrdersAdd) | **POST** /accounting/purchase-orders | Create Purchase Order |
| [**purchaseOrdersAll**](PurchaseOrdersApi.md#purchaseOrdersAll) | **GET** /accounting/purchase-orders | List Purchase Orders |
| [**purchaseOrdersDelete**](PurchaseOrdersApi.md#purchaseOrdersDelete) | **DELETE** /accounting/purchase-orders/{id} | Delete Purchase Order |
| [**purchaseOrdersOne**](PurchaseOrdersApi.md#purchaseOrdersOne) | **GET** /accounting/purchase-orders/{id} | Get Purchase Order |
| [**purchaseOrdersUpdate**](PurchaseOrdersApi.md#purchaseOrdersUpdate) | **PATCH** /accounting/purchase-orders/{id} | Update Purchase Order |


<a id="purchaseOrdersAdd"></a>
# **purchaseOrdersAdd**
> CreatePurchaseOrderResponse purchaseOrdersAdd(xApideckConsumerId, xApideckAppId, purchaseOrder, raw, xApideckServiceId)

Create Purchase Order

Create Purchase Order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PurchaseOrdersApi apiInstance = new PurchaseOrdersApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    PurchaseOrder purchaseOrder = new PurchaseOrder(); // PurchaseOrder | 
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    try {
      CreatePurchaseOrderResponse result = apiInstance.purchaseOrdersAdd(xApideckConsumerId, xApideckAppId, purchaseOrder, raw, xApideckServiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseOrdersApi#purchaseOrdersAdd");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **purchaseOrder** | [**PurchaseOrder**](PurchaseOrder.md)|  | |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |

### Return type

[**CreatePurchaseOrderResponse**](CreatePurchaseOrderResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | PurchaseOrders |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="purchaseOrdersAll"></a>
# **purchaseOrdersAll**
> GetPurchaseOrdersResponse purchaseOrdersAll(xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, cursor, passThrough, limit)

List Purchase Orders

List Purchase Orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PurchaseOrdersApi apiInstance = new PurchaseOrdersApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    PassThroughQuery passThrough = null; // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
    Integer limit = 20; // Integer | Number of results to return. Minimum 1, Maximum 200, Default 20
    try {
      GetPurchaseOrdersResponse result = apiInstance.purchaseOrdersAll(xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, cursor, passThrough, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseOrdersApi#purchaseOrdersAll");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] |
| **limit** | **Integer**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20] |

### Return type

[**GetPurchaseOrdersResponse**](GetPurchaseOrdersResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PurchaseOrders |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="purchaseOrdersDelete"></a>
# **purchaseOrdersDelete**
> DeletePurchaseOrderResponse purchaseOrdersDelete(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw)

Delete Purchase Order

Delete Purchase Order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PurchaseOrdersApi apiInstance = new PurchaseOrdersApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      DeletePurchaseOrderResponse result = apiInstance.purchaseOrdersDelete(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseOrdersApi#purchaseOrdersDelete");
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
| **id** | **String**| ID of the record you are acting upon. | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**DeletePurchaseOrderResponse**](DeletePurchaseOrderResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PurchaseOrders |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="purchaseOrdersOne"></a>
# **purchaseOrdersOne**
> GetPurchaseOrderResponse purchaseOrdersOne(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw)

Get Purchase Order

Get Purchase Order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PurchaseOrdersApi apiInstance = new PurchaseOrdersApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      GetPurchaseOrderResponse result = apiInstance.purchaseOrdersOne(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseOrdersApi#purchaseOrdersOne");
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
| **id** | **String**| ID of the record you are acting upon. | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**GetPurchaseOrderResponse**](GetPurchaseOrderResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PurchaseOrders |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="purchaseOrdersUpdate"></a>
# **purchaseOrdersUpdate**
> UpdatePurchaseOrderResponse purchaseOrdersUpdate(id, xApideckConsumerId, xApideckAppId, purchaseOrder, xApideckServiceId, raw)

Update Purchase Order

Update Purchase Order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PurchaseOrdersApi apiInstance = new PurchaseOrdersApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    PurchaseOrder purchaseOrder = new PurchaseOrder(); // PurchaseOrder | 
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      UpdatePurchaseOrderResponse result = apiInstance.purchaseOrdersUpdate(id, xApideckConsumerId, xApideckAppId, purchaseOrder, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseOrdersApi#purchaseOrdersUpdate");
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
| **id** | **String**| ID of the record you are acting upon. | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **purchaseOrder** | [**PurchaseOrder**](PurchaseOrder.md)|  | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**UpdatePurchaseOrderResponse**](UpdatePurchaseOrderResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PurchaseOrders |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

