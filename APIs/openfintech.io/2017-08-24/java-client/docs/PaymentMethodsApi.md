# PaymentMethodsApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentMethodsGet**](PaymentMethodsApi.md#paymentMethodsGet) | **GET** /payment-methods | List of payment methods |
| [**paymentMethodsIdGet**](PaymentMethodsApi.md#paymentMethodsIdGet) | **GET** /payment-methods/{id} | Payment method by ID |


<a id="paymentMethodsGet"></a>
# **paymentMethodsGet**
> PaymentMethodsResponse paymentMethodsGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterProcessorName, filterCategory, sort)

List of payment methods

Returns list of payment methods. Each object contains information about payment method such as name and category, also related link to payment method issuer (which processing it). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    PaymentMethodsApi apiInstance = new PaymentMethodsApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSearch = "filterSearch_example"; // String | Full text search with id, name, code, category.
    String filterName = "filterName_example"; // String | Filtering by name.
    String filterCode = "filterCode_example"; // String | Filtering by code.
    String filterProcessorName = "filterProcessorName_example"; // String | Filtering by processor_name.
    Set<String> filterCategory = Arrays.asList(); // Set<String> | Filtering by category.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category | 
    try {
      PaymentMethodsResponse result = apiInstance.paymentMethodsGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterProcessorName, filterCategory, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsApi#paymentMethodsGet");
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
| **pageNumber** | **Integer**| Current page number. | [optional] |
| **pageSize** | **Integer**| Page size.&lt;br&gt;*Default value: 100*  | [optional] |
| **filterSearch** | **String**| Full text search with id, name, code, category. | [optional] |
| **filterName** | **String**| Filtering by name. | [optional] |
| **filterCode** | **String**| Filtering by code. | [optional] |
| **filterProcessorName** | **String**| Filtering by processor_name. | [optional] |
| **filterCategory** | [**Set&lt;String&gt;**](String.md)| Filtering by category. | [optional] [enum: card, alternative, wallet, credit_cards, debit_cards, prepaid_cards, check, invoice, bank_transaction, direct_debits, mobile_carrier_billing, cash_on_delivery] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category |  | [optional] [enum: name, -name, code, -code, processor_name, -processor_name, category, -category] |

### Return type

[**PaymentMethodsResponse**](PaymentMethodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of payment methods. |  -  |

<a id="paymentMethodsIdGet"></a>
# **paymentMethodsIdGet**
> PaymentMethodResponse paymentMethodsIdGet(id)

Payment method by ID

Returns payment method with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    PaymentMethodsApi apiInstance = new PaymentMethodsApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      PaymentMethodResponse result = apiInstance.paymentMethodsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsApi#paymentMethodsIdGet");
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
| **id** | **String**| Unique ID. | |

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment method information. |  -  |
| **404** | Payment method ID is not valid. |  -  |

