# ReservationDetailsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationsDetailsList**](ReservationDetailsApi.md#reservationsDetailsList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationDetails |  |
| [**reservationsDetailsListByReservationOrder**](ReservationDetailsApi.md#reservationsDetailsListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationDetails |  |
| [**reservationsDetailsListByReservationOrderAndReservation**](ReservationDetailsApi.md#reservationsDetailsListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationDetails |  |


<a id="reservationsDetailsList"></a>
# **reservationsDetailsList**
> ReservationDetailsListResult reservationsDetailsList(scope, apiVersion, startDate, endDate, $filter)



Lists the reservations details for the defined scope and provided date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationDetailsApi apiInstance = new ReservationDetailsApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with reservations details operations. This includes '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope (legacy), and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope (modern). 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsList(scope, apiVersion, startDate, endDate, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationDetailsApi#reservationsDetailsList");
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
| **scope** | **String**| The scope associated with reservations details operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope (legacy), and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope (modern).  | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |
| **startDate** | **String**| Start date | [optional] |
| **endDate** | **String**| End date | [optional] |
| **$filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | [optional] |

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
import org.openapitools.client.api.ReservationDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationDetailsApi apiInstance = new ReservationDetailsApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsListByReservationOrder(reservationOrderId, $filter, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationDetailsApi#reservationsDetailsListByReservationOrder");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |

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
import org.openapitools.client.api.ReservationDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationDetailsApi apiInstance = new ReservationDetailsApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String reservationId = "reservationId_example"; // String | Id of the reservation
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsListByReservationOrderAndReservation(reservationOrderId, reservationId, $filter, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationDetailsApi#reservationsDetailsListByReservationOrderAndReservation");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |

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

