# ReservationSummariesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationsSummariesList**](ReservationSummariesApi.md#reservationsSummariesList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationSummaries |  |
| [**reservationsSummariesListByReservationOrder**](ReservationSummariesApi.md#reservationsSummariesListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationSummaries |  |
| [**reservationsSummariesListByReservationOrderAndReservation**](ReservationSummariesApi.md#reservationsSummariesListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationSummaries |  |


<a id="reservationsSummariesList"></a>
# **reservationsSummariesList**
> ReservationSummariesListResult reservationsSummariesList(scope, grain, apiVersion, startDate, endDate, $filter)



Lists the reservations summaries for the defined scope daily or monthly grain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationSummariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationSummariesApi apiInstance = new ReservationSummariesApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with reservations summaries operations. This includes '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope (legacy), and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope (modern). 
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesList(scope, grain, apiVersion, startDate, endDate, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationSummariesApi#reservationsSummariesList");
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
| **scope** | **String**| The scope associated with reservations summaries operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope (legacy), and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope (modern).  | |
| **grain** | **String**| Can be daily or monthly | [enum: daily, monthly] |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |
| **startDate** | **String**| Start date | [optional] |
| **endDate** | **String**| End date | [optional] |
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
import org.openapitools.client.api.ReservationSummariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationSummariesApi apiInstance = new ReservationSummariesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesListByReservationOrder(reservationOrderId, grain, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationSummariesApi#reservationsSummariesListByReservationOrder");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |
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
import org.openapitools.client.api.ReservationSummariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationSummariesApi apiInstance = new ReservationSummariesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String reservationId = "reservationId_example"; // String | Id of the reservation
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesListByReservationOrderAndReservation(reservationOrderId, reservationId, grain, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationSummariesApi#reservationsSummariesListByReservationOrderAndReservation");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |
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

