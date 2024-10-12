# CurrenciesApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currenciesGet**](CurrenciesApi.md#currenciesGet) | **GET** /currencies | List of currencies |
| [**currenciesIdGet**](CurrenciesApi.md#currenciesIdGet) | **GET** /currencies/{id} | Currency by ID |


<a id="currenciesGet"></a>
# **currenciesGet**
> CurrenciesResponse currenciesGet(pageNumber, pageSize, filterSearch, filterCodeIsoAlpha3, filterCodeIsoNumeric3, filterCodeEstandardsAlpha, filterCurrencyType, filterCategory, sort)

List of currencies

Returns all available currencies. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSearch = "filterSearch_example"; // String | Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category.
    String filterCodeIsoAlpha3 = "filterCodeIsoAlpha3_example"; // String | Filtering by ISO code.
    Integer filterCodeIsoNumeric3 = 56; // Integer | Filtering by ISO number.
    String filterCodeEstandardsAlpha = "filterCodeEstandardsAlpha_example"; // String | Filtering by estandards code.
    Set<String> filterCurrencyType = Arrays.asList(); // Set<String> | Filtration by currency type.
    Set<String> filterCategory = Arrays.asList(); // Set<String> | Filtration by category.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha | 
    try {
      CurrenciesResponse result = apiInstance.currenciesGet(pageNumber, pageSize, filterSearch, filterCodeIsoAlpha3, filterCodeIsoNumeric3, filterCodeEstandardsAlpha, filterCurrencyType, filterCategory, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesGet");
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
| **filterSearch** | **String**| Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category. | [optional] |
| **filterCodeIsoAlpha3** | **String**| Filtering by ISO code. | [optional] |
| **filterCodeIsoNumeric3** | **Integer**| Filtering by ISO number. | [optional] |
| **filterCodeEstandardsAlpha** | **String**| Filtering by estandards code. | [optional] |
| **filterCurrencyType** | [**Set&lt;String&gt;**](String.md)| Filtration by currency type. | [optional] [enum: national, digital, virtual, metal, energy, crypto, code, technical] |
| **filterCategory** | [**Set&lt;String&gt;**](String.md)| Filtration by category. | [optional] [enum: electronic, online_bankings, money_transfers, crypto_exchangers, crypto_currencies, vouchers, cards, cash, games, psps, others] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  | [optional] [enum: name, -name, type, -type, category, -category, code, -code, code_iso_alpha3, -code_iso_alpha3, code_iso_numeric3, -code_iso_numeric3, code_estandards_alpha, -code_estandards_alpha] |

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of currencies. |  -  |

<a id="currenciesIdGet"></a>
# **currenciesIdGet**
> CurrencyResponse currenciesIdGet(id)

Currency by ID

Returns currency with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      CurrencyResponse result = apiInstance.currenciesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesIdGet");
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

[**CurrencyResponse**](CurrencyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Currency information. |  -  |
| **404** | Currency ID is not valid. |  -  |

