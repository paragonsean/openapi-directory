# PaymentsApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listPaymentMethods**](PaymentsApi.md#listPaymentMethods) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods | List payment methods |
| [**listPayments**](PaymentsApi.md#listPayments) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-payments | List payments |


<a id="listPaymentMethods"></a>
# **listPaymentMethods**
> PaymentMethods listPaymentMethods(page, pageSize, query, orderBy)

List payment methods

Retrieve a list of payment methods, such as card, cash or other online payment methods, as held in the linked commerce platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Integer page = 1; // Integer | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    Integer pageSize = 100; // Integer | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    String query = "query_example"; // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    String orderBy = "-modifiedDate"; // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    try {
      PaymentMethods result = apiInstance.listPaymentMethods(page, pageSize, query, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#listPaymentMethods");
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
| **page** | **Integer**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1] |
| **pageSize** | **Integer**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100] |
| **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] |
| **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] |

### Return type

[**PaymentMethods**](PaymentMethods.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listPayments"></a>
# **listPayments**
> Payments listPayments(page, pageSize, query, orderBy)

List payments

List commerce payments for the given company &amp; data connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Integer page = 1; // Integer | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    Integer pageSize = 100; // Integer | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    String query = "query_example"; // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    String orderBy = "-modifiedDate"; // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    try {
      Payments result = apiInstance.listPayments(page, pageSize, query, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#listPayments");
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
| **page** | **Integer**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1] |
| **pageSize** | **Integer**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100] |
| **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] |
| **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] |

### Return type

[**Payments**](Payments.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

