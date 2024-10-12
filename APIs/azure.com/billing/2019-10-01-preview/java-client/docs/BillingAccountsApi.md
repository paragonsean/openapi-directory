# BillingAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingAccountsGet**](BillingAccountsApi.md#billingAccountsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName} |  |
| [**billingAccountsList**](BillingAccountsApi.md#billingAccountsList) | **GET** /providers/Microsoft.Billing/billingAccounts |  |
| [**billingAccountsListInvoiceSectionsByCreateSubscriptionPermission**](BillingAccountsApi.md#billingAccountsListInvoiceSectionsByCreateSubscriptionPermission) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/listInvoiceSectionsWithCreateSubscriptionPermission |  |
| [**billingAccountsUpdate**](BillingAccountsApi.md#billingAccountsUpdate) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountName} |  |


<a id="billingAccountsGet"></a>
# **billingAccountsGet**
> BillingAccount billingAccountsGet(apiVersion, billingAccountName, $expand)



Get the billing account by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the address, invoiceSections and billingProfiles.
    try {
      BillingAccount result = apiInstance.billingAccountsGet(apiVersion, billingAccountName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#billingAccountsGet");
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
| **$expand** | **String**| May be used to expand the address, invoiceSections and billingProfiles. | [optional] |

### Return type

[**BillingAccount**](BillingAccount.md)

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

<a id="billingAccountsList"></a>
# **billingAccountsList**
> BillingAccountListResult billingAccountsList(apiVersion, $expand)



Lists all billing accounts for a user which he has access to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String $expand = "$expand_example"; // String | May be used to expand the address, invoiceSections and billingProfiles.
    try {
      BillingAccountListResult result = apiInstance.billingAccountsList(apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#billingAccountsList");
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
| **$expand** | **String**| May be used to expand the address, invoiceSections and billingProfiles. | [optional] |

### Return type

[**BillingAccountListResult**](BillingAccountListResult.md)

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

<a id="billingAccountsListInvoiceSectionsByCreateSubscriptionPermission"></a>
# **billingAccountsListInvoiceSectionsByCreateSubscriptionPermission**
> InvoiceSectionListWithCreateSubPermissionResult billingAccountsListInvoiceSectionsByCreateSubscriptionPermission(apiVersion, billingAccountName)



Lists all invoice sections with create subscription permission for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    try {
      InvoiceSectionListWithCreateSubPermissionResult result = apiInstance.billingAccountsListInvoiceSectionsByCreateSubscriptionPermission(apiVersion, billingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#billingAccountsListInvoiceSectionsByCreateSubscriptionPermission");
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

[**InvoiceSectionListWithCreateSubPermissionResult**](InvoiceSectionListWithCreateSubPermissionResult.md)

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

<a id="billingAccountsUpdate"></a>
# **billingAccountsUpdate**
> BillingAccount billingAccountsUpdate(apiVersion, billingAccountName, parameters)



The operation to update a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    BillingAccountUpdateRequest parameters = new BillingAccountUpdateRequest(); // BillingAccountUpdateRequest | Request parameters supplied to the update billing account operation.
    try {
      BillingAccount result = apiInstance.billingAccountsUpdate(apiVersion, billingAccountName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#billingAccountsUpdate");
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
| **parameters** | [**BillingAccountUpdateRequest**](BillingAccountUpdateRequest.md)| Request parameters supplied to the update billing account operation. | |

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. Billing account update is in progress. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

