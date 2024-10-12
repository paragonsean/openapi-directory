# ReservationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationGet**](ReservationApi.md#reservationGet) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId} | Get &#x60;Reservation&#x60; details. |
| [**reservationList**](ReservationApi.md#reservationList) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations | Get &#x60;Reservation&#x60;s in a given reservation Order |
| [**reservationListRevisions**](ReservationApi.md#reservationListRevisions) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}/revisions | Get &#x60;Reservation&#x60; revisions. |
| [**reservationOrderGet**](ReservationApi.md#reservationOrderGet) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId} | Get a specific &#x60;ReservationOrder&#x60;. |
| [**reservationOrderList**](ReservationApi.md#reservationOrderList) | **GET** /providers/Microsoft.Capacity/reservationOrders | Get all &#x60;ReservationOrder&#x60;s. |
| [**reservationUpdate**](ReservationApi.md#reservationUpdate) | **PATCH** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId} | Updates a &#x60;Reservation&#x60;. |


<a id="reservationGet"></a>
# **reservationGet**
> ReservationResponse reservationGet(reservationId, reservationOrderId, apiVersion, expand)

Get &#x60;Reservation&#x60; details.

Get specific &#x60;Reservation&#x60; details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationApi apiInstance = new ReservationApi(defaultClient);
    String reservationId = "reservationId_example"; // String | Id of the Reservation Item
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    String expand = "expand_example"; // String | Supported value of this query is renewProperties
    try {
      ReservationResponse result = apiInstance.reservationGet(reservationId, reservationOrderId, apiVersion, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationApi#reservationGet");
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
| **reservationId** | **String**| Id of the Reservation Item | |
| **reservationOrderId** | **String**| Order Id of the reservation | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **expand** | **String**| Supported value of this query is renewProperties | [optional] |

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get &#x60;Reservation&#x60; details. |  -  |
| **0** | Unexpected error |  -  |

<a id="reservationList"></a>
# **reservationList**
> ReservationList reservationList(reservationOrderId, apiVersion)

Get &#x60;Reservation&#x60;s in a given reservation Order

List &#x60;Reservation&#x60;s within a single &#x60;ReservationOrder&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationApi apiInstance = new ReservationApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    try {
      ReservationList result = apiInstance.reservationList(reservationOrderId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationApi#reservationList");
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
| **reservationOrderId** | **String**| Order Id of the reservation | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |

### Return type

[**ReservationList**](ReservationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List &#x60;Reservation&#x60;s within a single &#x60;ReservationOrder&#x60;. |  -  |
| **0** | Unexpected error |  -  |

<a id="reservationListRevisions"></a>
# **reservationListRevisions**
> ReservationList reservationListRevisions(reservationId, reservationOrderId, apiVersion)

Get &#x60;Reservation&#x60; revisions.

List of all the revisions for the &#x60;Reservation&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationApi apiInstance = new ReservationApi(defaultClient);
    String reservationId = "reservationId_example"; // String | Id of the Reservation Item
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    try {
      ReservationList result = apiInstance.reservationListRevisions(reservationId, reservationOrderId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationApi#reservationListRevisions");
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
| **reservationId** | **String**| Id of the Reservation Item | |
| **reservationOrderId** | **String**| Order Id of the reservation | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |

### Return type

[**ReservationList**](ReservationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all the revisions for the &#x60;Reservation&#x60;. |  -  |
| **0** | Unexpected error |  -  |

<a id="reservationOrderGet"></a>
# **reservationOrderGet**
> ReservationOrderResponse reservationOrderGet(reservationOrderId, apiVersion, $expand)

Get a specific &#x60;ReservationOrder&#x60;.

Get the details of the &#x60;ReservationOrder&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationApi apiInstance = new ReservationApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    String $expand = "$expand_example"; // String | May be used to expand the planInformation.
    try {
      ReservationOrderResponse result = apiInstance.reservationOrderGet(reservationOrderId, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationApi#reservationOrderGet");
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
| **reservationOrderId** | **String**| Order Id of the reservation | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **$expand** | **String**| May be used to expand the planInformation. | [optional] |

### Return type

[**ReservationOrderResponse**](ReservationOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the details of the &#x60;ReservationOrder&#x60;. |  -  |
| **0** | Unexpected error |  -  |

<a id="reservationOrderList"></a>
# **reservationOrderList**
> ReservationOrderList reservationOrderList(apiVersion)

Get all &#x60;ReservationOrder&#x60;s.

List of all the &#x60;ReservationOrder&#x60;s that the user has access to in the current tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationApi apiInstance = new ReservationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    try {
      ReservationOrderList result = apiInstance.reservationOrderList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationApi#reservationOrderList");
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
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |

### Return type

[**ReservationOrderList**](ReservationOrderList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of &#x60;ReservationOrder&#x60;s |  -  |
| **0** | Unexpected error |  -  |

<a id="reservationUpdate"></a>
# **reservationUpdate**
> ReservationResponse reservationUpdate(reservationOrderId, reservationId, apiVersion, parameters)

Updates a &#x60;Reservation&#x60;.

Updates the applied scopes of the &#x60;Reservation&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationApi apiInstance = new ReservationApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String reservationId = "reservationId_example"; // String | Id of the Reservation Item
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    Patch parameters = new Patch(); // Patch | Information needed to patch a reservation item
    try {
      ReservationResponse result = apiInstance.reservationUpdate(reservationOrderId, reservationId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationApi#reservationUpdate");
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
| **reservationOrderId** | **String**| Order Id of the reservation | |
| **reservationId** | **String**| Id of the Reservation Item | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **parameters** | [**Patch**](Patch.md)| Information needed to patch a reservation item | |

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated &#x60;Reservation&#x60;. |  -  |
| **202** | The request is accepted and is being processed |  -  |
| **0** | Unexpected error |  -  |

