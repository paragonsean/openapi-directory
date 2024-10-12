# PaymentProvidersApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentProvidersGet**](PaymentProvidersApi.md#paymentProvidersGet) | **GET** /payment-providers | List of payment providers |
| [**paymentProvidersIdGet**](PaymentProvidersApi.md#paymentProvidersIdGet) | **GET** /payment-providers/{id} | Payment provider by ID |


<a id="paymentProvidersGet"></a>
# **paymentProvidersGet**
> PaymentProvidersResponse paymentProvidersGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterTypes, filterSalesChannels, filterFeatures, sort)

List of payment providers

A payment service provider (PSP) offers shops online services for accepting electronic payments by a variety of payment methods.&lt;br&gt; Endpoint returns list of PSPs. Each object contains: name, type, supported features and sales channels, also related link to available payment methods and main organization. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    PaymentProvidersApi apiInstance = new PaymentProvidersApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSearch = "filterSearch_example"; // String | Full text search with id, code, name.
    String filterName = "filterName_example"; // String | Filtering by name.
    String filterCode = "filterCode_example"; // String | Filtering by code.
    Set<String> filterTypes = Arrays.asList(); // Set<String> | Filtering by types.
    Set<String> filterSalesChannels = Arrays.asList(); // Set<String> | Filtering by sales channels.
    Set<String> filterFeatures = Arrays.asList(); // Set<String> | Filtering by features.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | 
    try {
      PaymentProvidersResponse result = apiInstance.paymentProvidersGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterTypes, filterSalesChannels, filterFeatures, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentProvidersApi#paymentProvidersGet");
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
| **filterSearch** | **String**| Full text search with id, code, name. | [optional] |
| **filterName** | **String**| Filtering by name. | [optional] |
| **filterCode** | **String**| Filtering by code. | [optional] |
| **filterTypes** | [**Set&lt;String&gt;**](String.md)| Filtering by types. | [optional] [enum: distributor, aggregator, collector, acquirer] |
| **filterSalesChannels** | [**Set&lt;String&gt;**](String.md)| Filtering by sales channels. | [optional] [enum: e_commerce, in_app, m_commerce, moto, m_pos, pos] |
| **filterFeatures** | [**Set&lt;String&gt;**](String.md)| Filtering by features. | [optional] [enum: e_commerce, installments, partial_captures, mastercard_secure, american_express_safe_key, a_b_testing, payment_transfer, hosted_payment_page, edcc, multi_lingual, fraud_scrubbing, multi_currency, pay_out_of_winnings, refunds, verified_by_visa, tokenization, recurring_payments, avs, pre_authorisation, chargeback_management, discover_protectbuy, level_iii_data, j_secure_by_jcb] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code |  | [optional] [enum: name, -name, code, -code] |

### Return type

[**PaymentProvidersResponse**](PaymentProvidersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Payment providers. |  -  |

<a id="paymentProvidersIdGet"></a>
# **paymentProvidersIdGet**
> PaymentProviderResponse paymentProvidersIdGet(id)

Payment provider by ID

Returns payment provider with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    PaymentProvidersApi apiInstance = new PaymentProvidersApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      PaymentProviderResponse result = apiInstance.paymentProvidersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentProvidersApi#paymentProvidersIdGet");
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

[**PaymentProviderResponse**](PaymentProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment provider. |  -  |
| **404** | Payment provider ID is not valid. |  -  |

