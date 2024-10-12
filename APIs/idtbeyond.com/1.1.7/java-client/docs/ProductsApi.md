# ProductsApi

All URIs are relative to *https://api.idtbeyond.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iatuProductsReportsAllCsvGet**](ProductsApi.md#iatuProductsReportsAllCsvGet) | **GET** /iatu/products/reports/all.csv | Get a list of products in CSV format |
| [**iatuProductsReportsAllGet**](ProductsApi.md#iatuProductsReportsAllGet) | **GET** /iatu/products/reports/all | Get a list of products in JSON format |
| [**iatuProductsReportsLocalValueGet**](ProductsApi.md#iatuProductsReportsLocalValueGet) | **GET** /iatu/products/reports/local-value | Get the estimated Local Value of a product |


<a id="iatuProductsReportsAllCsvGet"></a>
# **iatuProductsReportsAllCsvGet**
> iatuProductsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Get a list of products in CSV format

Returns a CSV of products, ranges, and their commissions percentages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    try {
      apiInstance.iatuProductsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#iatuProductsReportsAllCsvGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products CSV response |  -  |

<a id="iatuProductsReportsAllGet"></a>
# **iatuProductsReportsAllGet**
> iatuProductsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Get a list of products in JSON format

Returns a JSON list of products, ranges, and their commissions percentages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    try {
      apiInstance.iatuProductsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#iatuProductsReportsAllGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products JSON response |  -  |

<a id="iatuProductsReportsLocalValueGet"></a>
# **iatuProductsReportsLocalValueGet**
> iatuProductsReportsLocalValueGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, carrierCode, amount, currencyCode)

Get the estimated Local Value of a product

Returns a CSV of products, ranges, and their commissions percentages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String countryCode = "GT"; // String | 2-digit code of the country in ISO 3166 format. 'GT'
    String carrierCode = "Claro"; // String | Name of the mobile carrier. 'Claro'
    Integer amount = 500; // Integer | This is the amount, in cents, of the product you are purchasing. '500' = $5.00
    String currencyCode = "USD"; // String | The currency code (ISO 4217) on the product you are querying. 'USD'
    try {
      apiInstance.iatuProductsReportsLocalValueGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, carrierCode, amount, currencyCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#iatuProductsReportsLocalValueGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |
| **countryCode** | **String**| 2-digit code of the country in ISO 3166 format. &#39;GT&#39; | [default to GT] |
| **carrierCode** | **String**| Name of the mobile carrier. &#39;Claro&#39; | [default to Claro] |
| **amount** | **Integer**| This is the amount, in cents, of the product you are purchasing. &#39;500&#39; &#x3D; $5.00 | [default to 500] |
| **currencyCode** | **String**| The currency code (ISO 4217) on the product you are querying. &#39;USD&#39; | [default to USD] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Local value response |  -  |

