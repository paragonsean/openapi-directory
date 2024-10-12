# ReservationsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acknowledgmentReservation**](ReservationsApi.md#acknowledgmentReservation) | **POST** /api/logistics/pvt/inventory/reservations/{reservationId}/acknowledge | Acknowledgment reservation |
| [**cancelReservation**](ReservationsApi.md#cancelReservation) | **POST** /api/logistics/pvt/inventory/reservations/{reservationId}/cancel | Cancel reservation |
| [**confirmReservation**](ReservationsApi.md#confirmReservation) | **POST** /api/logistics/pvt/inventory/reservations/{reservationId}/confirm | Confirm reservation |
| [**createReservation**](ReservationsApi.md#createReservation) | **POST** /api/logistics/pvt/inventory/reservations | Create reservation |
| [**reservationById**](ReservationsApi.md#reservationById) | **GET** /api/logistics/pvt/inventory/reservations/{reservationId} | List reservation by ID |
| [**reservationbyWarehouseandSku**](ReservationsApi.md#reservationbyWarehouseandSku) | **GET** /api/logistics/pvt/inventory/reservations/{warehouseId}/{skuId} | List reservation by warehouse and SKU |


<a id="acknowledgmentReservation"></a>
# **acknowledgmentReservation**
> acknowledgmentReservation(contentType, accept, reservationId)

Acknowledgment reservation

Acknowledges reservations made by reservation ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

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

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String reservationId = "reservationId_example"; // String | 
    try {
      apiInstance.acknowledgmentReservation(contentType, accept, reservationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#acknowledgmentReservation");
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
| **reservationId** | **String**|  | |

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

<a id="cancelReservation"></a>
# **cancelReservation**
> cancelReservation(contentType, accept, reservationId)

Cancel reservation

Cancels reservation by reservation ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

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

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String reservationId = "reservationId_example"; // String | 
    try {
      apiInstance.cancelReservation(contentType, accept, reservationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#cancelReservation");
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
| **reservationId** | **String**|  | |

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

<a id="confirmReservation"></a>
# **confirmReservation**
> confirmReservation(contentType, accept, reservationId)

Confirm reservation

Confirms reservation by reservation ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

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

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String reservationId = "reservationId_example"; // String | 
    try {
      apiInstance.confirmReservation(contentType, accept, reservationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#confirmReservation");
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
| **reservationId** | **String**|  | |

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

<a id="createReservation"></a>
# **createReservation**
> CreateReservation200Response createReservation(accept, contentType, createReservationRequest1)

Create reservation

Creates [reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

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

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent.
    CreateReservationRequest1 createReservationRequest1 = new CreateReservationRequest1(); // CreateReservationRequest1 | 
    try {
      CreateReservation200Response result = apiInstance.createReservation(accept, contentType, createReservationRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#createReservation");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json; charset&#x3D;utf-8] |
| **createReservationRequest1** | [**CreateReservationRequest1**](CreateReservationRequest1.md)|  | |

### Return type

[**CreateReservation200Response**](CreateReservation200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CDNIgnore -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Powered-by-VTEX-Janus-Router -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * x-vtex-operation-id -  <br>  |

<a id="reservationById"></a>
# **reservationById**
> ReservationById200Response reservationById(contentType, accept, reservationId)

List reservation by ID

Lists reservation&#39;s information by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

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

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String reservationId = "reservationId_example"; // String | 
    try {
      ReservationById200Response result = apiInstance.reservationById(contentType, accept, reservationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#reservationById");
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
| **reservationId** | **String**|  | |

### Return type

[**ReservationById200Response**](ReservationById200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CDNIgnore -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Powered-by-VTEX-Janus-Router -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * x-vtex-operation-id -  <br>  |

<a id="reservationbyWarehouseandSku"></a>
# **reservationbyWarehouseandSku**
> reservationbyWarehouseandSku(contentType, accept, warehouseId, skuId)

List reservation by warehouse and SKU

Lists reservations in your store, by searching through warehouse and SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

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

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String warehouseId = "warehouseId_example"; // String | 
    String skuId = "skuId_example"; // String | 
    try {
      apiInstance.reservationbyWarehouseandSku(contentType, accept, warehouseId, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#reservationbyWarehouseandSku");
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
| **warehouseId** | **String**|  | |
| **skuId** | **String**|  | |

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

