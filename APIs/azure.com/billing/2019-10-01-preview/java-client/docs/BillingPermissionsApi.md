# BillingPermissionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingPermissionsListByBillingAccount**](BillingPermissionsApi.md#billingPermissionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingPermissions |  |
| [**billingPermissionsListByBillingProfile**](BillingPermissionsApi.md#billingPermissionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingPermissions |  |
| [**billingPermissionsListByCustomer**](BillingPermissionsApi.md#billingPermissionsListByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingPermissions |  |
| [**billingPermissionsListByInvoiceSections**](BillingPermissionsApi.md#billingPermissionsListByInvoiceSections) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingPermissions |  |


<a id="billingPermissionsListByBillingAccount"></a>
# **billingPermissionsListByBillingAccount**
> BillingPermissionsListResult billingPermissionsListByBillingAccount(apiVersion, billingAccountName)



Lists all billing permissions for the caller under a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingPermissionsApi apiInstance = new BillingPermissionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    try {
      BillingPermissionsListResult result = apiInstance.billingPermissionsListByBillingAccount(apiVersion, billingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingPermissionsApi#billingPermissionsListByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

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

<a id="billingPermissionsListByBillingProfile"></a>
# **billingPermissionsListByBillingProfile**
> BillingPermissionsListResult billingPermissionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



Lists all billing permissions the caller has for a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingPermissionsApi apiInstance = new BillingPermissionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      BillingPermissionsListResult result = apiInstance.billingPermissionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingPermissionsApi#billingPermissionsListByBillingProfile");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

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

<a id="billingPermissionsListByCustomer"></a>
# **billingPermissionsListByCustomer**
> BillingPermissionsListResult billingPermissionsListByCustomer(apiVersion, billingAccountName, customerName)



Lists all billing permissions the caller has for a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingPermissionsApi apiInstance = new BillingPermissionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String customerName = "customerName_example"; // String | Customer name.
    try {
      BillingPermissionsListResult result = apiInstance.billingPermissionsListByCustomer(apiVersion, billingAccountName, customerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingPermissionsApi#billingPermissionsListByCustomer");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **customerName** | **String**| Customer name. | |

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

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

<a id="billingPermissionsListByInvoiceSections"></a>
# **billingPermissionsListByInvoiceSections**
> BillingPermissionsListResult billingPermissionsListByInvoiceSections(apiVersion, billingAccountName, billingProfileName, invoiceSectionName)



Lists all billing permissions for the caller under invoice section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingPermissionsApi apiInstance = new BillingPermissionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      BillingPermissionsListResult result = apiInstance.billingPermissionsListByInvoiceSections(apiVersion, billingAccountName, billingProfileName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingPermissionsApi#billingPermissionsListByInvoiceSections");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

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

