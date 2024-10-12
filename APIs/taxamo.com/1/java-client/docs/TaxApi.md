# TaxApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calculateSimpleTax**](TaxApi.md#calculateSimpleTax) | **GET** /api/v1/tax/calculate | Simple tax |
| [**calculateTax**](TaxApi.md#calculateTax) | **POST** /api/v1/tax/calculate | Calculate tax |
| [**calculateTaxLocation**](TaxApi.md#calculateTaxLocation) | **GET** /api/v1/tax/location/calculate | Calculate location |
| [**validateTaxNumber**](TaxApi.md#validateTaxNumber) | **GET** /api/v1/tax/vat_numbers/{tax_number}/validate | Validate VAT number |


<a id="calculateSimpleTax"></a>
# **calculateSimpleTax**
> CalculateSimpleTaxOut calculateSimpleTax(currencyCode, productType, invoiceAddressCity, buyerCreditCardPrefix, invoiceAddressRegion, unitPrice, quantity, buyerTaxNumber, forceCountryCode, orderDate, amount, billingCountryCode, invoiceAddressPostalCode, totalAmount, taxDeducted)

Simple tax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String currencyCode = "currencyCode_example"; // String | Currency code for transaction - e.g. EUR.
    String productType = "productType_example"; // String | Product type, according to dictionary /dictionaries/product_types. 
    String invoiceAddressCity = "invoiceAddressCity_example"; // String | Invoice address/postal_code
    String buyerCreditCardPrefix = "buyerCreditCardPrefix_example"; // String | First 6 digits of buyer's credit card prefix.
    String invoiceAddressRegion = "invoiceAddressRegion_example"; // String | Invoice address/region
    BigDecimal unitPrice = new BigDecimal(78); // BigDecimal | Unit price.
    BigDecimal quantity = new BigDecimal(78); // BigDecimal | Quantity Defaults to 1.
    String buyerTaxNumber = "buyerTaxNumber_example"; // String |  Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
    String forceCountryCode = "forceCountryCode_example"; // String | Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.
    String orderDate = "orderDate_example"; // String | Order date in yyyy-MM-dd format, in merchant's timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used.
    BigDecimal amount = new BigDecimal(78); // BigDecimal | Amount. Required if total amount or both unit price and quantity are not provided.
    String billingCountryCode = "billingCountryCode_example"; // String | Billing two letter ISO country code.
    String invoiceAddressPostalCode = "invoiceAddressPostalCode_example"; // String | Invoice address/postal_code
    BigDecimal totalAmount = new BigDecimal(78); // BigDecimal | Total amount. Required if amount or both unit price and quantity are not provided.
    Boolean taxDeducted = true; // Boolean | If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
    try {
      CalculateSimpleTaxOut result = apiInstance.calculateSimpleTax(currencyCode, productType, invoiceAddressCity, buyerCreditCardPrefix, invoiceAddressRegion, unitPrice, quantity, buyerTaxNumber, forceCountryCode, orderDate, amount, billingCountryCode, invoiceAddressPostalCode, totalAmount, taxDeducted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#calculateSimpleTax");
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
| **currencyCode** | **String**| Currency code for transaction - e.g. EUR. | |
| **productType** | **String**| Product type, according to dictionary /dictionaries/product_types.  | [optional] |
| **invoiceAddressCity** | **String**| Invoice address/postal_code | [optional] |
| **buyerCreditCardPrefix** | **String**| First 6 digits of buyer&#39;s credit card prefix. | [optional] |
| **invoiceAddressRegion** | **String**| Invoice address/region | [optional] |
| **unitPrice** | **BigDecimal**| Unit price. | [optional] |
| **quantity** | **BigDecimal**| Quantity Defaults to 1. | [optional] |
| **buyerTaxNumber** | **String**|  Buyer&#39;s tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly. | [optional] |
| **forceCountryCode** | **String**| Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation. | [optional] |
| **orderDate** | **String**| Order date in yyyy-MM-dd format, in merchant&#39;s timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used. | [optional] |
| **amount** | **BigDecimal**| Amount. Required if total amount or both unit price and quantity are not provided. | [optional] |
| **billingCountryCode** | **String**| Billing two letter ISO country code. | [optional] |
| **invoiceAddressPostalCode** | **String**| Invoice address/postal_code | [optional] |
| **totalAmount** | **BigDecimal**| Total amount. Required if amount or both unit price and quantity are not provided. | [optional] |
| **taxDeducted** | **Boolean**| If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example. | [optional] |

### Return type

[**CalculateSimpleTaxOut**](CalculateSimpleTaxOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="calculateTax"></a>
# **calculateTax**
> CalculateTaxOut calculateTax(input)

Calculate tax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TaxApi apiInstance = new TaxApi(defaultClient);
    CalculateTaxIn input = new CalculateTaxIn(); // CalculateTaxIn | Input
    try {
      CalculateTaxOut result = apiInstance.calculateTax(input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#calculateTax");
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
| **input** | [**CalculateTaxIn**](CalculateTaxIn.md)| Input | |

### Return type

[**CalculateTaxOut**](CalculateTaxOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="calculateTaxLocation"></a>
# **calculateTaxLocation**
> CalculateTaxLocationOut calculateTaxLocation(billingCountryCode, buyerCreditCardPrefix)

Calculate location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String billingCountryCode = "billingCountryCode_example"; // String | Billing two letter ISO country code.
    String buyerCreditCardPrefix = "buyerCreditCardPrefix_example"; // String | First 6 digits of buyer's credit card prefix.
    try {
      CalculateTaxLocationOut result = apiInstance.calculateTaxLocation(billingCountryCode, buyerCreditCardPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#calculateTaxLocation");
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
| **billingCountryCode** | **String**| Billing two letter ISO country code. | [optional] |
| **buyerCreditCardPrefix** | **String**| First 6 digits of buyer&#39;s credit card prefix. | [optional] |

### Return type

[**CalculateTaxLocationOut**](CalculateTaxLocationOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="validateTaxNumber"></a>
# **validateTaxNumber**
> ValidateTaxNumberOut validateTaxNumber(taxNumber, countryCode)

Validate VAT number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String taxNumber = "taxNumber_example"; // String | Tax number
    String countryCode = "countryCode_example"; // String | Two-letter ISO country code.
    try {
      ValidateTaxNumberOut result = apiInstance.validateTaxNumber(taxNumber, countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#validateTaxNumber");
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
| **taxNumber** | **String**| Tax number | |
| **countryCode** | **String**| Two-letter ISO country code. | [optional] |

### Return type

[**ValidateTaxNumberOut**](ValidateTaxNumberOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

