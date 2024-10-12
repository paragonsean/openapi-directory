# DepositMethodsApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**depositMethodsGet**](DepositMethodsApi.md#depositMethodsGet) | **GET** /deposit-methods | List of deposit methods |
| [**depositMethodsIdGet**](DepositMethodsApi.md#depositMethodsIdGet) | **GET** /deposit-methods/{id} | Deposit method by ID |


<a id="depositMethodsGet"></a>
# **depositMethodsGet**
> DepositMethodsResponse depositMethodsGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterProcessorName, filterCategory, sort)

List of deposit methods

Returns list of deposit methods. Each object contains information about deposit method such as name and category, also related link to deposit method issuer (which processing it). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DepositMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    DepositMethodsApi apiInstance = new DepositMethodsApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSearch = "filterSearch_example"; // String | Full text search with id, name, code, category.
    String filterName = "filterName_example"; // String | Filtering by name.
    String filterCode = "filterCode_example"; // String | Filtering by code.
    String filterProcessorName = "filterProcessorName_example"; // String | Filtering by processor_name.
    Set<String> filterCategory = Arrays.asList(); // Set<String> | Filtering by category.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category | 
    try {
      DepositMethodsResponse result = apiInstance.depositMethodsGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterProcessorName, filterCategory, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DepositMethodsApi#depositMethodsGet");
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

[**DepositMethodsResponse**](DepositMethodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of deposit methods. |  -  |

<a id="depositMethodsIdGet"></a>
# **depositMethodsIdGet**
> DepositMethodResponse depositMethodsIdGet(id)

Deposit method by ID

Returns deposit method with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DepositMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    DepositMethodsApi apiInstance = new DepositMethodsApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      DepositMethodResponse result = apiInstance.depositMethodsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DepositMethodsApi#depositMethodsIdGet");
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

[**DepositMethodResponse**](DepositMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deposit method information. |  -  |
| **404** | deposit method ID is not valid. |  -  |

