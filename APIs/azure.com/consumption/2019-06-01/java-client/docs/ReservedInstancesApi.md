# ReservedInstancesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationTransactionsListByBillingAccountId**](ReservedInstancesApi.md#reservationTransactionsListByBillingAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/reservationTransactions |  |
| [**reservationsDetailsListByBillingAccountId**](ReservedInstancesApi.md#reservationsDetailsListByBillingAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/reservationDetails |  |
| [**reservationsDetailsListByReservationOrder**](ReservedInstancesApi.md#reservationsDetailsListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationDetails |  |
| [**reservationsDetailsListByReservationOrderAndReservation**](ReservedInstancesApi.md#reservationsDetailsListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationDetails |  |
| [**reservationsSummariesListByBillingAccountId**](ReservedInstancesApi.md#reservationsSummariesListByBillingAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/reservationSummaries |  |
| [**reservationsSummariesListByReservationOrder**](ReservedInstancesApi.md#reservationsSummariesListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationSummaries |  |
| [**reservationsSummariesListByReservationOrderAndReservation**](ReservedInstancesApi.md#reservationsSummariesListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationSummaries |  |


<a id="reservationTransactionsListByBillingAccountId"></a>
# **reservationTransactionsListByBillingAccountId**
> ReservationTransactionsListResult reservationTransactionsListByBillingAccountId(apiVersion, billingAccountId, $filter)



List of transactions for reserved instances on billing account scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | Filter reservation transactions by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    try {
      ReservationTransactionsListResult result = apiInstance.reservationTransactionsListByBillingAccountId(apiVersion, billingAccountId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationTransactionsListByBillingAccountId");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **$filter** | **String**| Filter reservation transactions by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | [optional] |

### Return type

[**ReservationTransactionsListResult**](ReservationTransactionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reservationsDetailsListByBillingAccountId"></a>
# **reservationsDetailsListByBillingAccountId**
> ReservationDetailsListResult reservationsDetailsListByBillingAccountId(billingAccountId, $filter, apiVersion)



Lists the reservations details for provided date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsListByBillingAccountId(billingAccountId, $filter, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsDetailsListByBillingAccountId");
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
| **billingAccountId** | **String**| BillingAccount ID | |
| **$filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reservationsDetailsListByReservationOrder"></a>
# **reservationsDetailsListByReservationOrder**
> ReservationDetailsListResult reservationsDetailsListByReservationOrder(reservationOrderId, $filter, apiVersion)



Lists the reservations details for provided date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsListByReservationOrder(reservationOrderId, $filter, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsDetailsListByReservationOrder");
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
| **$filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reservationsDetailsListByReservationOrderAndReservation"></a>
# **reservationsDetailsListByReservationOrderAndReservation**
> ReservationDetailsListResult reservationsDetailsListByReservationOrderAndReservation(reservationOrderId, reservationId, $filter, apiVersion)



Lists the reservations details for provided date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String reservationId = "reservationId_example"; // String | Id of the reservation
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsListByReservationOrderAndReservation(reservationOrderId, reservationId, $filter, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsDetailsListByReservationOrderAndReservation");
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
| **reservationId** | **String**| Id of the reservation | |
| **$filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reservationsSummariesListByBillingAccountId"></a>
# **reservationsSummariesListByBillingAccountId**
> ReservationSummariesListResult reservationsSummariesListByBillingAccountId(billingAccountId, grain, apiVersion, $filter)



Lists the reservations summaries for daily or monthly grain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesListByBillingAccountId(billingAccountId, grain, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsSummariesListByBillingAccountId");
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
| **billingAccountId** | **String**| BillingAccount ID | |
| **grain** | **String**| Can be daily or monthly | [enum: daily, monthly] |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |
| **$filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] |

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reservationsSummariesListByReservationOrder"></a>
# **reservationsSummariesListByReservationOrder**
> ReservationSummariesListResult reservationsSummariesListByReservationOrder(reservationOrderId, grain, apiVersion, $filter)



Lists the reservations summaries for daily or monthly grain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesListByReservationOrder(reservationOrderId, grain, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsSummariesListByReservationOrder");
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
| **grain** | **String**| Can be daily or monthly | [enum: daily, monthly] |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |
| **$filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] |

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reservationsSummariesListByReservationOrderAndReservation"></a>
# **reservationsSummariesListByReservationOrderAndReservation**
> ReservationSummariesListResult reservationsSummariesListByReservationOrderAndReservation(reservationOrderId, reservationId, grain, apiVersion, $filter)



Lists the reservations summaries for daily or monthly grain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservedInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservedInstancesApi apiInstance = new ReservedInstancesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String reservationId = "reservationId_example"; // String | Id of the reservation
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-06-01.
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesListByReservationOrderAndReservation(reservationOrderId, reservationId, grain, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsSummariesListByReservationOrderAndReservation");
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
| **reservationId** | **String**| Id of the reservation | |
| **grain** | **String**| Can be daily or monthly | [enum: daily, monthly] |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-06-01. | |
| **$filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] |

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

