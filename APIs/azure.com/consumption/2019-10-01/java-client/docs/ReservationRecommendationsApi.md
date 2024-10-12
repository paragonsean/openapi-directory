# ReservationRecommendationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationRecommendationsList**](ReservationRecommendationsApi.md#reservationRecommendationsList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationRecommendations |  |


<a id="reservationRecommendationsList"></a>
# **reservationRecommendationsList**
> ReservationRecommendationsListResult reservationRecommendationsList(apiVersion, scope, $filter)



List of recommendations for purchasing reserved instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationRecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReservationRecommendationsApi apiInstance = new ReservationRecommendationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    String scope = "scope_example"; // String | The scope associated with reservation recommendations operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope
    String $filter = "$filter_example"; // String | May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod.
    try {
      ReservationRecommendationsListResult result = apiInstance.reservationRecommendationsList(apiVersion, scope, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationRecommendationsApi#reservationRecommendationsList");
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
| **scope** | **String**| The scope associated with reservation recommendations operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope, and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope | |
| **$filter** | **String**| May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod. | [optional] |

### Return type

[**ReservationRecommendationsListResult**](ReservationRecommendationsListResult.md)

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

