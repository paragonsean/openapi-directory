# BillingSubscriptionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingSubscriptionsGet**](BillingSubscriptionsApi.md#billingSubscriptionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName} |  |
| [**billingSubscriptionsGetByCustomer**](BillingSubscriptionsApi.md#billingSubscriptionsGetByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingSubscriptions/{billingSubscriptionName} |  |
| [**billingSubscriptionsListByBillingAccount**](BillingSubscriptionsApi.md#billingSubscriptionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions |  |
| [**billingSubscriptionsListByBillingProfile**](BillingSubscriptionsApi.md#billingSubscriptionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingSubscriptions |  |
| [**billingSubscriptionsListByCustomer**](BillingSubscriptionsApi.md#billingSubscriptionsListByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingSubscriptions |  |
| [**billingSubscriptionsListByInvoiceSection**](BillingSubscriptionsApi.md#billingSubscriptionsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingSubscriptions |  |


<a id="billingSubscriptionsGet"></a>
# **billingSubscriptionsGet**
> BillingSubscription billingSubscriptionsGet(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, apiVersion)



Get a single billing subscription by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingSubscriptionsApi apiInstance = new BillingSubscriptionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      BillingSubscription result = apiInstance.billingSubscriptionsGet(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubscriptionsApi#billingSubscriptionsGet");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **billingSubscriptionName** | **String**| Billing Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**BillingSubscription**](BillingSubscription.md)

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

<a id="billingSubscriptionsGetByCustomer"></a>
# **billingSubscriptionsGetByCustomer**
> BillingSubscription billingSubscriptionsGetByCustomer(billingAccountName, customerName, billingSubscriptionName, apiVersion)



Get a single billing subscription by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingSubscriptionsApi apiInstance = new BillingSubscriptionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String customerName = "customerName_example"; // String | Customer name.
    String billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      BillingSubscription result = apiInstance.billingSubscriptionsGetByCustomer(billingAccountName, customerName, billingSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubscriptionsApi#billingSubscriptionsGetByCustomer");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **customerName** | **String**| Customer name. | |
| **billingSubscriptionName** | **String**| Billing Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**BillingSubscription**](BillingSubscription.md)

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

<a id="billingSubscriptionsListByBillingAccount"></a>
# **billingSubscriptionsListByBillingAccount**
> BillingSubscriptionsListResult billingSubscriptionsListByBillingAccount(billingAccountName, apiVersion)



Lists billing subscriptions by billing account name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingSubscriptionsApi apiInstance = new BillingSubscriptionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      BillingSubscriptionsListResult result = apiInstance.billingSubscriptionsListByBillingAccount(billingAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubscriptionsApi#billingSubscriptionsListByBillingAccount");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

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

<a id="billingSubscriptionsListByBillingProfile"></a>
# **billingSubscriptionsListByBillingProfile**
> BillingSubscriptionsListResult billingSubscriptionsListByBillingProfile(billingAccountName, billingProfileName, apiVersion)



Lists billing subscriptions by billing profile name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingSubscriptionsApi apiInstance = new BillingSubscriptionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      BillingSubscriptionsListResult result = apiInstance.billingSubscriptionsListByBillingProfile(billingAccountName, billingProfileName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubscriptionsApi#billingSubscriptionsListByBillingProfile");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

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

<a id="billingSubscriptionsListByCustomer"></a>
# **billingSubscriptionsListByCustomer**
> BillingSubscriptionsListResult billingSubscriptionsListByCustomer(billingAccountName, customerName, apiVersion)



Lists billing subscription by customer id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingSubscriptionsApi apiInstance = new BillingSubscriptionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String customerName = "customerName_example"; // String | Customer name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      BillingSubscriptionsListResult result = apiInstance.billingSubscriptionsListByCustomer(billingAccountName, customerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubscriptionsApi#billingSubscriptionsListByCustomer");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **customerName** | **String**| Customer name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

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

<a id="billingSubscriptionsListByInvoiceSection"></a>
# **billingSubscriptionsListByInvoiceSection**
> BillingSubscriptionsListResult billingSubscriptionsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion)



Lists billing subscription by invoice section name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingSubscriptionsApi apiInstance = new BillingSubscriptionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      BillingSubscriptionsListResult result = apiInstance.billingSubscriptionsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubscriptionsApi#billingSubscriptionsListByInvoiceSection");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

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

