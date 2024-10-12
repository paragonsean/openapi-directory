# ApiApi

All URIs are relative to *https://vatapi.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiUsage**](ApiApi.md#apiUsage) | **GET** /usage-check | Check api requests remaining on current subscription plan |
| [**convertPrice**](ApiApi.md#convertPrice) | **GET** /vat-price | Convert a price to or from VAT price. |
| [**countryCodeCheck**](ApiApi.md#countryCodeCheck) | **GET** /country-code-check | Retrieve a countries VAT rates by its 2 digit country code |
| [**createInvoice**](ApiApi.md#createInvoice) | **POST** /invoice | Create a VAT invoice |
| [**currencyConversion**](ApiApi.md#currencyConversion) | **GET** /currency-conversion | Convert a currency |
| [**getInvoice**](ApiApi.md#getInvoice) | **GET** /invoice/{id} | Retrieve an invoice |
| [**invoiceDelete**](ApiApi.md#invoiceDelete) | **DELETE** /invoice/{id} | Delete an invoice |
| [**invoiceUpdate**](ApiApi.md#invoiceUpdate) | **PUT** /invoice/{id} | Update an existing invoice |
| [**ipCheck**](ApiApi.md#ipCheck) | **GET** /ip-check | Retrieve a countries VAT rates from an IP address |
| [**vatNumberValidate**](ApiApi.md#vatNumberValidate) | **GET** /vat-number-check | Validate a VAT number |
| [**vatRates**](ApiApi.md#vatRates) | **GET** /vat-rates | Retrieve all current EU VAT rates |


<a id="apiUsage"></a>
# **apiUsage**
> ApiUsage apiUsage(responseType)

Check api requests remaining on current subscription plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      ApiUsage result = apiInstance.apiUsage(responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#apiUsage");
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
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**ApiUsage**](ApiUsage.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="convertPrice"></a>
# **convertPrice**
> ConvertPrice convertPrice(code, price, responseType, countryRate, type)

Convert a price to or from VAT price.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String code = "code_example"; // String | The 2 digit country code
    Integer price = 56; // Integer | The price you want converting
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    String countryRate = "countryRate_example"; // String | The VAT rate to get the price for. Default: standard
    String type = "type_example"; // String | Optional, if the price is including VAT set the type to 'incl'. Otherwise the default is assumed as excluding VAT already, 'excl'
    try {
      ConvertPrice result = apiInstance.convertPrice(code, price, responseType, countryRate, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#convertPrice");
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
| **code** | **String**| The 2 digit country code | |
| **price** | **Integer**| The price you want converting | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |
| **countryRate** | **String**| The VAT rate to get the price for. Default: standard | [optional] |
| **type** | **String**| Optional, if the price is including VAT set the type to &#39;incl&#39;. Otherwise the default is assumed as excluding VAT already, &#39;excl&#39; | [optional] |

### Return type

[**ConvertPrice**](ConvertPrice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="countryCodeCheck"></a>
# **countryCodeCheck**
> CountryCodeCheck countryCodeCheck(code, responseType)

Retrieve a countries VAT rates by its 2 digit country code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String code = "code_example"; // String | The 2 digit country code
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      CountryCodeCheck result = apiInstance.countryCodeCheck(code, responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#countryCodeCheck");
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
| **code** | **String**| The 2 digit country code | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**CountryCodeCheck**](CountryCodeCheck.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="createInvoice"></a>
# **createInvoice**
> CreateInvoice createInvoice(body, responseType)

Create a VAT invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    InvoiceData body = new InvoiceData(); // InvoiceData | Enter invoice data as JSON
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      CreateInvoice result = apiInstance.createInvoice(body, responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#createInvoice");
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
| **body** | [**InvoiceData**](InvoiceData.md)| Enter invoice data as JSON | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**CreateInvoice**](CreateInvoice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="currencyConversion"></a>
# **currencyConversion**
> CurrencyConversion currencyConversion(currencyFrom, currencyTo, responseType, amount)

Convert a currency

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String currencyFrom = "currencyFrom_example"; // String | The currency code you are converting from
    String currencyTo = "currencyTo_example"; // String | The currency code you are converting to
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    Integer amount = 56; // Integer | Optional, an amount you are wanting to convert. Leave blank to just get the current rate
    try {
      CurrencyConversion result = apiInstance.currencyConversion(currencyFrom, currencyTo, responseType, amount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#currencyConversion");
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
| **currencyFrom** | **String**| The currency code you are converting from | |
| **currencyTo** | **String**| The currency code you are converting to | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |
| **amount** | **Integer**| Optional, an amount you are wanting to convert. Leave blank to just get the current rate | [optional] |

### Return type

[**CurrencyConversion**](CurrencyConversion.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getInvoice"></a>
# **getInvoice**
> RetrieveInvoice getInvoice(id, responseType)

Retrieve an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    Integer id = 56; // Integer | Enter the invoice id
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      RetrieveInvoice result = apiInstance.getInvoice(id, responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#getInvoice");
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
| **id** | **Integer**| Enter the invoice id | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**RetrieveInvoice**](RetrieveInvoice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="invoiceDelete"></a>
# **invoiceDelete**
> invoiceDelete(id, responseType)

Delete an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    Integer id = 56; // Integer | Enter an invoice id
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      apiInstance.invoiceDelete(id, responseType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#invoiceDelete");
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
| **id** | **Integer**| Enter an invoice id | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="invoiceUpdate"></a>
# **invoiceUpdate**
> UpdateInvoice invoiceUpdate(id, body, responseType)

Update an existing invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    Integer id = 56; // Integer | Enter an invoice id
    UpdateInvoiceArray body = new UpdateInvoiceArray(); // UpdateInvoiceArray | Enter invoice data as JSON
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      UpdateInvoice result = apiInstance.invoiceUpdate(id, body, responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#invoiceUpdate");
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
| **id** | **Integer**| Enter an invoice id | |
| **body** | [**UpdateInvoiceArray**](UpdateInvoiceArray.md)| Enter invoice data as JSON | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**UpdateInvoice**](UpdateInvoice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="ipCheck"></a>
# **ipCheck**
> IPCheck ipCheck(address, responseType)

Retrieve a countries VAT rates from an IP address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String address = "address_example"; // String | The IP address to search against
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      IPCheck result = apiInstance.ipCheck(address, responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#ipCheck");
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
| **address** | **String**| The IP address to search against | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**IPCheck**](IPCheck.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="vatNumberValidate"></a>
# **vatNumberValidate**
> vatNumberValidate(vatid, responseType)

Validate a VAT number

&lt;p&gt;We highly recommend if you are able, to check a VAT number on your end first to save wasted API lookups. It maybe that your customer has simply entered the wrong format. &lt;a href&#x3D;&#39;http://www.braemoor.co.uk/software/vat.shtml&#39; target&#x3D;&#39;_blank&#39;&gt;Heres a client side way to check the format using Javascript&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String vatid = "vatid_example"; // String | The VAT number to validate
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      apiInstance.vatNumberValidate(vatid, responseType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#vatNumberValidate");
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
| **vatid** | **String**| The VAT number to validate | |
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="vatRates"></a>
# **vatRates**
> VatRates vatRates(responseType)

Retrieve all current EU VAT rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vatapi.com/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String responseType = "responseType_example"; // String | The default response type is application/json if you would like to receive an XML response then set this to XML
    try {
      VatRates result = apiInstance.vatRates(responseType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#vatRates");
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
| **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] |

### Return type

[**VatRates**](VatRates.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

