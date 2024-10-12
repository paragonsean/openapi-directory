# ReservedInstancesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationsDetailsList**](ReservedInstancesApi.md#reservationsDetailsList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationDetails |  |
| [**reservationsSummariesList**](ReservedInstancesApi.md#reservationsSummariesList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationSummaries |  |


<a id="reservationsDetailsList"></a>
# **reservationsDetailsList**
> ReservationDetailsListResult reservationsDetailsList(scope, $filter, apiVersion)



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
    String scope = "scope_example"; // String | The scope of the reservation details. The scope can be 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}' or 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}'
    String $filter = "$filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-30.
    try {
      ReservationDetailsListResult result = apiInstance.reservationsDetailsList(scope, $filter, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsDetailsList");
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
| **scope** | **String**| The scope of the reservation details. The scope can be &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}&#39; or &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}&#39; | |
| **$filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-30. | |

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

<a id="reservationsSummariesList"></a>
# **reservationsSummariesList**
> ReservationSummariesListResult reservationsSummariesList(scope, grain, apiVersion, $filter)



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
    String scope = "scope_example"; // String | The scope of the reservation summaries. The scope can be 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}' or 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}'
    String grain = "daily"; // String | Can be daily or monthly
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-30.
    String $filter = "$filter_example"; // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
    try {
      ReservationSummariesListResult result = apiInstance.reservationsSummariesList(scope, grain, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservedInstancesApi#reservationsSummariesList");
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
| **scope** | **String**| The scope of the reservation summaries. The scope can be &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}&#39; or &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}&#39; | |
| **grain** | **String**| Can be daily or monthly | [enum: daily, monthly] |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-30. | |
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

