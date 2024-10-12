# CustomersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customersGet**](CustomersApi.md#customersGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName} |  |
| [**customersListByBillingAccountName**](CustomersApi.md#customersListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers |  |


<a id="customersGet"></a>
# **customersGet**
> Customer customersGet(apiVersion, billingAccountName, customerName, $expand)



Get the customer by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String customerName = "customerName_example"; // String | Customer Id.
    String $expand = "$expand_example"; // String | May be used to expand enabledAzureSkus, resellers.
    try {
      Customer result = apiInstance.customersGet(apiVersion, billingAccountName, customerName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **customerName** | **String**| Customer Id. | |
| **$expand** | **String**| May be used to expand enabledAzureSkus, resellers. | [optional] |

### Return type

[**Customer**](Customer.md)

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

<a id="customersListByBillingAccountName"></a>
# **customersListByBillingAccountName**
> CustomerListResult customersListByBillingAccountName(apiVersion, billingAccountName, $filter, $skiptoken)



Lists all customers which the current user can work with on-behalf of a partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String $filter = "$filter_example"; // String | May be used to filter using hasPermission('{permissionId}') to only return customers for which the caller has the specified permission.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      CustomerListResult result = apiInstance.customersListByBillingAccountName(apiVersion, billingAccountName, $filter, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersListByBillingAccountName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **$filter** | **String**| May be used to filter using hasPermission(&#39;{permissionId}&#39;) to only return customers for which the caller has the specified permission. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**CustomerListResult**](CustomerListResult.md)

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

