# PartnersApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**putOrdersIdShip**](PartnersApi.md#putOrdersIdShip) | **PUT** /orders/{id}/ship | Ship an Order |
| [**putOrdersIdStatus**](PartnersApi.md#putOrdersIdStatus) | **PUT** /orders/{id}/status | Update Order Status |


<a id="putOrdersIdShip"></a>
# **putOrdersIdShip**
> Object putOrdersIdShip(id, body)

Ship an Order

Note, this API is used to update orders and is reserved for our shipping partners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    Integer id = 56; // Integer | The FDC order Id
    OrderShipV2 body = new OrderShipV2(); // OrderShipV2 | Shipping Details
    try {
      Object result = apiInstance.putOrdersIdShip(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#putOrdersIdShip");
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
| **id** | **Integer**| The FDC order Id | |
| **body** | [**OrderShipV2**](OrderShipV2.md)| Shipping Details | |

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order Found |  -  |
| **404** | Order not found |  -  |

<a id="putOrdersIdStatus"></a>
# **putOrdersIdStatus**
> Object putOrdersIdStatus(id, body)

Update Order Status

Note, this API is used to update orders and is reserved for our shipping partners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    Integer id = 56; // Integer | The FDC order Id
    StatusTypeSimpleV2 body = new StatusTypeSimpleV2(); // StatusTypeSimpleV2 | New status event
    try {
      Object result = apiInstance.putOrdersIdStatus(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#putOrdersIdStatus");
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
| **id** | **Integer**| The FDC order Id | |
| **body** | [**StatusTypeSimpleV2**](StatusTypeSimpleV2.md)| New status event | |

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order Found |  -  |
| **404** | Order not found |  -  |

