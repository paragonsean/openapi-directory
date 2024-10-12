# DefaultApi

All URIs are relative to *https://api.ean-search.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**barcodeImage**](DefaultApi.md#barcodeImage) | **GET** /barcode-image | Generate a PNG barcode image |
| [**barcodeLookup**](DefaultApi.md#barcodeLookup) | **GET** /barcode-lookup | Look up an EAN |
| [**barcodePrefixSearch**](DefaultApi.md#barcodePrefixSearch) | **GET** /barcode-prefix-search | Query the database for all barcodes with the same beginning |
| [**categorySearch**](DefaultApi.md#categorySearch) | **GET** /category-search | Search for products form a certain category |
| [**issuingCountry**](DefaultApi.md#issuingCountry) | **GET** /issuing-country | Search for a issuing country of a barcode |
| [**productSearch**](DefaultApi.md#productSearch) | **GET** /product-search | Search by product name |
| [**verifyChecksum**](DefaultApi.md#verifyChecksum) | **GET** /verify-checksum | Verify the checksum of an EAN code |


<a id="barcodeImage"></a>
# **barcodeImage**
> List&lt;Barcode&gt; barcodeImage(op, ean, width, height, format)

Generate a PNG barcode image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "barcode-image"; // String | API operation
    Integer ean = 56; // Integer | EAN code to search for
    Integer width = 102; // Integer | 
    Integer height = 50; // Integer | 
    String format = "json"; // String | output format
    try {
      List<Barcode> result = apiInstance.barcodeImage(op, ean, width, height, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#barcodeImage");
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
| **op** | **String**| API operation | [enum: barcode-image] |
| **ean** | **Integer**| EAN code to search for | |
| **width** | **Integer**|  | [optional] [default to 102] |
| **height** | **Integer**|  | [optional] [default to 50] |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;Barcode&gt;**](Barcode.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

<a id="barcodeLookup"></a>
# **barcodeLookup**
> List&lt;Product&gt; barcodeLookup(op, ean, language, format)

Look up an EAN

Search by EAN code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "barcode-lookup"; // String | API operation
    Integer ean = 56; // Integer | EAN code to search for
    Integer language = 1; // Integer | preferred language for the product name
    String format = "json"; // String | output format
    try {
      List<Product> result = apiInstance.barcodeLookup(op, ean, language, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#barcodeLookup");
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
| **op** | **String**| API operation | [enum: barcode-lookup] |
| **ean** | **Integer**| EAN code to search for | |
| **language** | **Integer**| preferred language for the product name | [optional] [default to 1] |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

<a id="barcodePrefixSearch"></a>
# **barcodePrefixSearch**
> List&lt;Product&gt; barcodePrefixSearch(op, prefix, language, page, format)

Query the database for all barcodes with the same beginning

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "barcode-prefix-search"; // String | API operation
    String prefix = "prefix_example"; // String | barcode prefix to search for, at least 4 digits
    Integer language = 1; // Integer | preferred language for the product name
    Integer page = 0; // Integer | result page
    String format = "json"; // String | output format
    try {
      List<Product> result = apiInstance.barcodePrefixSearch(op, prefix, language, page, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#barcodePrefixSearch");
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
| **op** | **String**| API operation | [enum: barcode-prefix-search] |
| **prefix** | **String**| barcode prefix to search for, at least 4 digits | |
| **language** | **Integer**| preferred language for the product name | [optional] [default to 1] |
| **page** | **Integer**| result page | [optional] [default to 0] |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

<a id="categorySearch"></a>
# **categorySearch**
> List&lt;Product&gt; categorySearch(op, category, name, language, page, format)

Search for products form a certain category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "category-search"; // String | API operation
    Integer category = 56; // Integer | category number
    String name = "name_example"; // String | name or keyords to search for
    Integer language = 99; // Integer | preferred language for the product name (default any language)
    Integer page = 0; // Integer | result page
    String format = "json"; // String | output format
    try {
      List<Product> result = apiInstance.categorySearch(op, category, name, language, page, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#categorySearch");
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
| **op** | **String**| API operation | [enum: category-search] |
| **category** | **Integer**| category number | |
| **name** | **String**| name or keyords to search for | [optional] |
| **language** | **Integer**| preferred language for the product name (default any language) | [optional] [default to 99] |
| **page** | **Integer**| result page | [optional] [default to 0] |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

<a id="issuingCountry"></a>
# **issuingCountry**
> List&lt;IssuingCountry&gt; issuingCountry(op, ean, format)

Search for a issuing country of a barcode

Search for a issuing country of a barcode. In contrast to barcode-lookup, this will always give a result, even if we don&#39;t know the product name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "issuing-country"; // String | API operation
    Integer ean = 56; // Integer | EAN code to search for
    String format = "json"; // String | output format
    try {
      List<IssuingCountry> result = apiInstance.issuingCountry(op, ean, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#issuingCountry");
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
| **op** | **String**| API operation | [enum: issuing-country] |
| **ean** | **Integer**| EAN code to search for | |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;IssuingCountry&gt;**](IssuingCountry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

<a id="productSearch"></a>
# **productSearch**
> List&lt;Product&gt; productSearch(op, name, language, page, format)

Search by product name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "product-search"; // String | API operation
    String name = "name_example"; // String | name or keyords to search for
    Integer language = 99; // Integer | preferred language for the product name (default any language)
    Integer page = 0; // Integer | result page
    String format = "json"; // String | output format
    try {
      List<Product> result = apiInstance.productSearch(op, name, language, page, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#productSearch");
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
| **op** | **String**| API operation | [enum: product-search] |
| **name** | **String**| name or keyords to search for | |
| **language** | **Integer**| preferred language for the product name (default any language) | [optional] [default to 99] |
| **page** | **Integer**| result page | [optional] [default to 0] |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

<a id="verifyChecksum"></a>
# **verifyChecksum**
> List&lt;VerifyChecksum&gt; verifyChecksum(op, ean, format)

Verify the checksum of an EAN code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ean-search.org");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "verify-checksum"; // String | API operation
    Integer ean = 56; // Integer | EAN code to search for
    String format = "json"; // String | output format
    try {
      List<VerifyChecksum> result = apiInstance.verifyChecksum(op, ean, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#verifyChecksum");
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
| **op** | **String**| API operation | [enum: verify-checksum] |
| **ean** | **Integer**| EAN code to search for | |
| **format** | **String**| output format | [optional] [enum: json, xml] |

### Return type

[**List&lt;VerifyChecksum&gt;**](VerifyChecksum.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid operation requested |  -  |
| **401** | Invalid access token |  -  |
| **402** | Request limit reached |  -  |
| **405** | Must use HTTP GET to access the API |  -  |
| **429** | Too many requests (eg. rate limit exeeded) |  -  |

