# ProductsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsGet**](ProductsApi.md#productsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName} |  |
| [**productsGetByCustomer**](ProductsApi.md#productsGetByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/products/{productName} |  |
| [**productsListByBillingAccount**](ProductsApi.md#productsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products |  |
| [**productsListByCustomer**](ProductsApi.md#productsListByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/products |  |
| [**productsListByInvoiceSection**](ProductsApi.md#productsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products |  |
| [**productsTransfer**](ProductsApi.md#productsTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName}/transfer |  |
| [**productsUpdateAutoRenewByInvoiceSection**](ProductsApi.md#productsUpdateAutoRenewByInvoiceSection) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName}/updateAutoRenew |  |


<a id="productsGet"></a>
# **productsGet**
> Product productsGet(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion)



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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      Product result = apiInstance.productsGet(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion);
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**Product**](Product.md)

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

<a id="productsGetByCustomer"></a>
# **productsGetByCustomer**
> Product productsGetByCustomer(billingAccountName, customerName, productName, apiVersion)



Get a customer&#39;s product by name.

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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String customerName = "customerName_example"; // String | Customer name.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    try {
      Product result = apiInstance.productsGetByCustomer(billingAccountName, customerName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsGetByCustomer");
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
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |

### Return type

[**Product**](Product.md)

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

<a id="productsListByBillingAccount"></a>
# **productsListByBillingAccount**
> ProductsListResult productsListByBillingAccount(billingAccountName, apiVersion, $filter)



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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String $filter = "$filter_example"; // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      ProductsListResult result = apiInstance.productsListByBillingAccount(billingAccountName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsListByBillingAccount");
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

<a id="productsListByCustomer"></a>
# **productsListByCustomer**
> ProductsListResult productsListByCustomer(billingAccountName, customerName, apiVersion, $filter)



Lists products by customer id.

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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String customerName = "customerName_example"; // String | Customer name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String $filter = "$filter_example"; // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      ProductsListResult result = apiInstance.productsListByCustomer(billingAccountName, customerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsListByCustomer");
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

<a id="productsListByInvoiceSection"></a>
# **productsListByInvoiceSection**
> ProductsListResult productsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, $filter)



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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String $filter = "$filter_example"; // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
    try {
      ProductsListResult result = apiInstance.productsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsListByInvoiceSection");
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
> Product productsTransfer(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, parameters)



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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    TransferProductRequestProperties parameters = new TransferProductRequestProperties(); // TransferProductRequestProperties | Parameters supplied to the Transfer Product operation.
    try {
      Product result = apiInstance.productsTransfer(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, parameters);
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **parameters** | [**TransferProductRequestProperties**](TransferProductRequestProperties.md)| Parameters supplied to the Transfer Product operation. | |

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted |  * Retry-After - Recommends the retryable time after receiving this. <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsUpdateAutoRenewByInvoiceSection"></a>
# **productsUpdateAutoRenewByInvoiceSection**
> UpdateAutoRenewOperation productsUpdateAutoRenewByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, body)



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
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    UpdateAutoRenewRequest body = new UpdateAutoRenewRequest(); // UpdateAutoRenewRequest | Update auto renew request parameters.
    try {
      UpdateAutoRenewOperation result = apiInstance.productsUpdateAutoRenewByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsUpdateAutoRenewByInvoiceSection");
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
| **productName** | **String**| Invoice Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **body** | [**UpdateAutoRenewRequest**](UpdateAutoRenewRequest.md)| Update auto renew request parameters. | |

### Return type

[**UpdateAutoRenewOperation**](UpdateAutoRenewOperation.md)

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

