# GeocodingApi

All URIs are relative to *http://free.gisgraphy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geocode**](GeocodingApi.md#geocode) | **GET** /geocoding/geocode | Geocode an address |


<a id="geocode"></a>
# **geocode**
> AddressResultsDto geocode(address, country, postal, format, from, to, paramCallback, indent)

Geocode an address

The Gisgraphy geocoding service allows you to transform postal addresses or other descriptions (a street, a city, a postal code, a country, or a combination) of a location into a (latitude, longitude) coordinate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://free.gisgraphy.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GeocodingApi apiInstance = new GeocodingApi(defaultClient);
    String address = "address_example"; // String | A postal address, structured or not, a street, a city, a postal code, a country, or a combination.
    String country = "country_example"; // String | The country where the place/address is. It is used to determine the postal address format and to improve performance. It will probably be optional in next version to ease the usability. The value must be the ISO 3166 Alpha 2 code of the country.
    String postal = "postal_example"; // String | Whether the given address is a postal address. default to false. In other words, if the address follow the specification or if it is a well-formed address as it was written on an envelope. This parameter will enable the parsing of the address by the address parser before geocoding, this way, the relevance will be better because because if parsing is successful, we will know the meaning of each word. Note that you can also specify each field if you already know them.
    String format = "XML"; // String | The output format.
    Integer from = 1; // Integer | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
    Integer to = 10; // Integer | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
    String paramCallback = "paramCallback_example"; // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    Boolean indent = false; // Boolean | indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    try {
      AddressResultsDto result = apiInstance.geocode(address, country, postal, format, from, to, paramCallback, indent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeocodingApi#geocode");
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
| **address** | **String**| A postal address, structured or not, a street, a city, a postal code, a country, or a combination. | |
| **country** | **String**| The country where the place/address is. It is used to determine the postal address format and to improve performance. It will probably be optional in next version to ease the usability. The value must be the ISO 3166 Alpha 2 code of the country. | [optional] |
| **postal** | **String**| Whether the given address is a postal address. default to false. In other words, if the address follow the specification or if it is a well-formed address as it was written on an envelope. This parameter will enable the parsing of the address by the address parser before geocoding, this way, the relevance will be better because because if parsing is successful, we will know the meaning of each word. Note that you can also specify each field if you already know them. | [optional] |
| **format** | **String**| The output format. | [optional] [default to XML] [enum: XML, JSON, PHP, RUBY, PYTHON, YAML] |
| **from** | **Integer**| The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1 | [optional] [default to 1] |
| **to** | **Integer**| The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed) | [optional] [default to 10] |
| **paramCallback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] |
| **indent** | **Boolean**| indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |

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

