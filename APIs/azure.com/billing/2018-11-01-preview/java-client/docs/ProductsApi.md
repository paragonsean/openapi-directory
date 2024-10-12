# ProductsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsGet**](ProductsApi.md#productsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName} |  |
| [**productsListByBillingAccountName**](ProductsApi.md#productsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products |  |
| [**productsListByInvoiceSectionName**](ProductsApi.md#productsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products |  |
| [**productsTransfer**](ProductsApi.md#productsTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName}/transfer |  |
| [**productsUpdateAutoRenewByBillingAccountName**](ProductsApi.md#productsUpdateAutoRenewByBillingAccountName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products/{productName}/updateAutoRenew |  |
| [**productsUpdateAutoRenewByInvoiceSectionName**](ProductsApi.md#productsUpdateAutoRenewByInvoiceSectionName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName}/updateAutoRenew |  |


<a id="productsGet"></a>
# **productsGet**
> ProductSummary productsGet(billingAccountName, invoiceSectionName, productName, apiVersion)



Get a single product by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    try {
      ProductSummary result = apiInstance.productsGet(billingAccountName, invoiceSectionName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsGet");
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
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |

### Return type

[**ProductSummary**](ProductSummary.md)

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

<a id="productsListByBillingAccountName"></a>
# **productsListByBillingAccountName**
> ProductsListResult productsListByBillingAccountName(billingAccountName, apiVersion, $filter)



Lists products by billing account name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String $filter = "$filter_example"; // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      ProductsListResult result = apiInstance.productsListByBillingAccountName(billingAccountName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsListByBillingAccountName");
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
| **$filter** | **String**| May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**ProductsListResult**](ProductsListResult.md)

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

<a id="productsListByInvoiceSectionName"></a>
# **productsListByInvoiceSectionName**
> ProductsListResult productsListByInvoiceSectionName(billingAccountName, invoiceSectionName, apiVersion, $filter)



Lists products by invoice section name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String $filter = "$filter_example"; // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      ProductsListResult result = apiInstance.productsListByInvoiceSectionName(billingAccountName, invoiceSectionName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsListByInvoiceSectionName");
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
| **$filter** | **String**| May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] |

### Return type

[**ProductsListResult**](ProductsListResult.md)

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

<a id="productsTransfer"></a>
# **productsTransfer**
> ProductSummary productsTransfer(billingAccountName, invoiceSectionName, productName, apiVersion, parameters)



The operation to transfer a Product to another invoice section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    TransferProductRequestProperties parameters = new TransferProductRequestProperties(); // TransferProductRequestProperties | Parameters supplied to the Transfer Product operation.
    try {
      ProductSummary result = apiInstance.productsTransfer(billingAccountName, invoiceSectionName, productName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsTransfer");
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
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **parameters** | [**TransferProductRequestProperties**](TransferProductRequestProperties.md)| Parameters supplied to the Transfer Product operation. | |

### Return type

[**ProductSummary**](ProductSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted |  * Retry-After - Recommends the retryable time after receiving this. <br>  * Azure-AsyncOperation - URI to poll for the operation status <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsUpdateAutoRenewByBillingAccountName"></a>
# **productsUpdateAutoRenewByBillingAccountName**
> UpdateAutoRenewOperationSummary productsUpdateAutoRenewByBillingAccountName(billingAccountName, productName, apiVersion, body)



Cancel auto renew for product by product id and billing account name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    UpdateAutoRenewRequest body = new UpdateAutoRenewRequest(); // UpdateAutoRenewRequest | Update auto renew request parameters.
    try {
      UpdateAutoRenewOperationSummary result = apiInstance.productsUpdateAutoRenewByBillingAccountName(billingAccountName, productName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsUpdateAutoRenewByBillingAccountName");
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
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **body** | [**UpdateAutoRenewRequest**](UpdateAutoRenewRequest.md)| Update auto renew request parameters. | |

### Return type

[**UpdateAutoRenewOperationSummary**](UpdateAutoRenewOperationSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsUpdateAutoRenewByInvoiceSectionName"></a>
# **productsUpdateAutoRenewByInvoiceSectionName**
> UpdateAutoRenewOperationSummary productsUpdateAutoRenewByInvoiceSectionName(billingAccountName, invoiceSectionName, productName, apiVersion, body)



Cancel auto renew for product by product id and invoice section name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    UpdateAutoRenewRequest body = new UpdateAutoRenewRequest(); // UpdateAutoRenewRequest | Update auto renew request parameters.
    try {
      UpdateAutoRenewOperationSummary result = apiInstance.productsUpdateAutoRenewByInvoiceSectionName(billingAccountName, invoiceSectionName, productName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsUpdateAutoRenewByInvoiceSectionName");
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
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **body** | [**UpdateAutoRenewRequest**](UpdateAutoRenewRequest.md)| Update auto renew request parameters. | |

### Return type

[**UpdateAutoRenewOperationSummary**](UpdateAutoRenewOperationSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

