# AddressparserStandardizerApi

All URIs are relative to *http://free.gisgraphy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addressparsing**](AddressparserStandardizerApi.md#addressparsing) | **GET** /addressparser/parse | split a raw address into several parts |


<a id="addressparsing"></a>
# **addressparsing**
> AddressResultsDto addressparsing(address, country, format, paramCallback, indent, standardize, geocode)

split a raw address into several parts

The address parser and address standardizer, are part of the Gisgraphy project (free open source worldwide geocoder). Address parsing is the process of dividing a single address string into its individual component parts. Please visit [http://www.address-parser.net](http://www.address-parser.net) for more details 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressparserStandardizerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://free.gisgraphy.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AddressparserStandardizerApi apiInstance = new AddressparserStandardizerApi(defaultClient);
    String address = "address_example"; // String | A postal address.
    String country = "country_example"; // String | The ISO 3166 Alpha 2 code of the country.
    String format = "XML"; // String | The output format.
    String paramCallback = "paramCallback_example"; // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    Boolean indent = false; // Boolean | indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    Boolean standardize = false; // Boolean | Whether the address should be standardized after parsing, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    Boolean geocode = false; // Boolean | UNUSED YET. Whether the address should be geocoded after parsing, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    try {
      AddressResultsDto result = apiInstance.addressparsing(address, country, format, paramCallback, indent, standardize, geocode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressparserStandardizerApi#addressparsing");
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
| **address** | **String**| A postal address. | |
| **country** | **String**| The ISO 3166 Alpha 2 code of the country. | [optional] |
| **format** | **String**| The output format. | [optional] [default to XML] [enum: XML, JSON, PHP, RUBY, PYTHON, YAML] |
| **paramCallback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] |
| **indent** | **Boolean**| indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |
| **standardize** | **Boolean**| Whether the address should be standardized after parsing, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |
| **geocode** | **Boolean**| UNUSED YET. Whether the address should be geocoded after parsing, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |

### Return type

[**AddressResultsDto**](AddressResultsDto.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessfully processed |  -  |
| **401** | Need auth. The API key parameter is missing or wrong, or doesn&#39;t correspond to any subscriptions |  -  |
| **403** | Unhauthorize (auth will change nothing).Your IP is not allowed. |  -  |
| **412** | Missing parameter. Some parameters required for the webservices ar missing, please consult documentation |  -  |
| **429** | Too many requests. You exceed the authorized rate |  -  |
| **500** | Internal error |  -  |

