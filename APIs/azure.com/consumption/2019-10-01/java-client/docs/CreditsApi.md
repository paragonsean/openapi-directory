# CreditsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**creditsGet**](CreditsApi.md#creditsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/credits/balanceSummary |  |


<a id="creditsGet"></a>
# **creditsGet**
> CreditSummary creditsGet(billingAccountId, billingProfileId, apiVersion)



The credit summary by billingAccountId and billingProfileId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CreditsApi apiInstance = new CreditsApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String billingProfileId = "billingProfileId_example"; // String | Azure Billing Profile ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
    try {
      CreditSummary result = apiInstance.creditsGet(billingAccountId, billingProfileId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditsApi#creditsGet");
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
| **billingProfileId** | **String**| Azure Billing Profile ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | |

### Return type

[**CreditSummary**](CreditSummary.md)

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

