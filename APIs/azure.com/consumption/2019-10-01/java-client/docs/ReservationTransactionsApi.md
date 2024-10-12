# ReservationTransactionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationTransactionsList**](ReservationTransactionsApi.md#reservationTransactionsList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/reservationTransactions |  |


<a id="reservationTransactionsList"></a>
# **reservationTransactionsList**
> ReservationTransactionsListResult reservationTransactionsList(apiVersion, billingAccountId, $filter)



List of transactions for reserved instances on billing account scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationTransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationTransactionsApi apiInstance = new ReservationTransactionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | Filter reservation transactions by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
    try {
      ReservationTransactionsListResult result = apiInstance.reservationTransactionsList(apiVersion, billingAccountId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationTransactionsApi#reservationTransactionsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |
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

