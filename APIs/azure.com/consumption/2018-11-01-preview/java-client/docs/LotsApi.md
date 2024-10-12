# LotsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lotsByBillingProfileList**](LotsApi.md#lotsByBillingProfileList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/lots |  |


<a id="lotsByBillingProfileList"></a>
# **lotsByBillingProfileList**
> Lots lotsByBillingProfileList(billingAccountId, billingProfileId, apiVersion)



Lists the lots by billingAccountId and billingProfileId for given start and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LotsApi apiInstance = new LotsApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String billingProfileId = "billingProfileId_example"; // String | Billing Profile Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    try {
      Lots result = apiInstance.lotsByBillingProfileList(billingAccountId, billingProfileId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LotsApi#lotsByBillingProfileList");
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

### Return type

[**Lots**](Lots.md)

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

