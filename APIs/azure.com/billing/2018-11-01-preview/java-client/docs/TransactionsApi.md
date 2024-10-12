# TransactionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transactionsListByBillingAccountName**](TransactionsApi.md#transactionsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/transactions |  |
| [**transactionsListByBillingProfileName**](TransactionsApi.md#transactionsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/transactions |  |
| [**transactionsListByCustomerName**](TransactionsApi.md#transactionsListByCustomerName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/transactions |  |
| [**transactionsListByInvoiceSectionName**](TransactionsApi.md#transactionsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/transactions |  |


<a id="transactionsListByBillingAccountName"></a>
# **transactionsListByBillingAccountName**
> TransactionsListResult transactionsListByBillingAccountName(billingAccountName, apiVersion, startDate, endDate, $filter)



Lists the transactions by billing account name for given start and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $filter = "$filter_example"; // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      TransactionsListResult result = apiInstance.transactionsListByBillingAccountName(billingAccountName, apiVersion, startDate, endDate, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsListByBillingAccountName");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |
| **$filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**TransactionsListResult**](TransactionsListResult.md)

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

<a id="transactionsListByBillingProfileName"></a>
# **transactionsListByBillingProfileName**
> TransactionsListResult transactionsListByBillingProfileName(billingAccountName, billingProfileName, apiVersion, startDate, endDate, $filter)



Lists the transactions by billing profile name for given start date and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $filter = "$filter_example"; // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      TransactionsListResult result = apiInstance.transactionsListByBillingProfileName(billingAccountName, billingProfileName, apiVersion, startDate, endDate, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsListByBillingProfileName");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |
| **$filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**TransactionsListResult**](TransactionsListResult.md)

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

<a id="transactionsListByCustomerName"></a>
# **transactionsListByCustomerName**
> TransactionsListResult transactionsListByCustomerName(billingAccountName, customerName, apiVersion, startDate, endDate, $filter)



Lists the transactions by invoice section name for given start date and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String customerName = "customerName_example"; // String | Customer Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $filter = "$filter_example"; // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      TransactionsListResult result = apiInstance.transactionsListByCustomerName(billingAccountName, customerName, apiVersion, startDate, endDate, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsListByCustomerName");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **customerName** | **String**| Customer Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |
| **$filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**TransactionsListResult**](TransactionsListResult.md)

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

<a id="transactionsListByInvoiceSectionName"></a>
# **transactionsListByInvoiceSectionName**
> TransactionsListResult transactionsListByInvoiceSectionName(billingAccountName, invoiceSectionName, apiVersion, startDate, endDate, $filter)



Lists the transactions by invoice section name for given start date and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $filter = "$filter_example"; // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      TransactionsListResult result = apiInstance.transactionsListByInvoiceSectionName(billingAccountName, invoiceSectionName, apiVersion, startDate, endDate, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsListByInvoiceSectionName");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |
| **$filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**TransactionsListResult**](TransactionsListResult.md)

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

