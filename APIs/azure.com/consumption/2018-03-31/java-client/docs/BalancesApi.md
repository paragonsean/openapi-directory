# BalancesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBalancesByBillingAccount**](BalancesApi.md#getBalancesByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/balances |  |
| [**getBalancesByBillingAccountByBillingPeriod**](BalancesApi.md#getBalancesByBillingAccountByBillingPeriod) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/balances |  |


<a id="getBalancesByBillingAccount"></a>
# **getBalancesByBillingAccount**
> Balance getBalancesByBillingAccount(apiVersion, billingAccountId)



Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BalancesApi apiInstance = new BalancesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    try {
      Balance result = apiInstance.getBalancesByBillingAccount(apiVersion, billingAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalancesApi#getBalancesByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **billingAccountId** | **String**| BillingAccount ID | |

### Return type

[**Balance**](Balance.md)

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

<a id="getBalancesByBillingAccountByBillingPeriod"></a>
# **getBalancesByBillingAccountByBillingPeriod**
> Balance getBalancesByBillingAccountByBillingPeriod(apiVersion, billingAccountId, billingPeriodName)



Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BalancesApi apiInstance = new BalancesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
    try {
      Balance result = apiInstance.getBalancesByBillingAccountByBillingPeriod(apiVersion, billingAccountId, billingPeriodName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalancesApi#getBalancesByBillingAccountByBillingPeriod");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **billingPeriodName** | **String**| Billing Period Name. | |

### Return type

[**Balance**](Balance.md)

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

