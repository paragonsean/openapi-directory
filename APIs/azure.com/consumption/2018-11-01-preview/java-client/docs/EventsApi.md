# EventsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsByBillingProfileList**](EventsApi.md#eventsByBillingProfileList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/events |  |


<a id="eventsByBillingProfileList"></a>
# **eventsByBillingProfileList**
> Events eventsByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate)



Lists the events by billingAccountId and billingProfileId for given start and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String billingProfileId = "billingProfileId_example"; // String | Billing Profile Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    try {
      Events result = apiInstance.eventsByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsByBillingProfileList");
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
| **billingProfileId** | **String**| Billing Profile Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |

### Return type

[**Events**](Events.md)

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

