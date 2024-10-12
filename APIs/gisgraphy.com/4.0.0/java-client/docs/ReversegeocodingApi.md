# ReversegeocodingApi

All URIs are relative to *http://free.gisgraphy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reversegeocode**](ReversegeocodingApi.md#reversegeocode) | **GET** /reversegeocoding/reversegeocode | Reverse geocode an address |


<a id="reversegeocode"></a>
# **reversegeocode**
> AddressResultsDto reversegeocode(lat, lng, format, from, to, paramCallback, indent)

Reverse geocode an address

The Reverse geocoding service allows to search for an address for a given GPS position.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversegeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://free.gisgraphy.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ReversegeocodingApi apiInstance = new ReversegeocodingApi(defaultClient);
    Double lat = 3.4D; // Double | The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
    Double lng = 3.4D; // Double | TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
    String format = "XML"; // String | The output format.
    Integer from = 1; // Integer | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
    Integer to = 10; // Integer | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
    String paramCallback = "paramCallback_example"; // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    Boolean indent = false; // Boolean | indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    try {
      AddressResultsDto result = apiInstance.reversegeocode(lat, lng, format, from, to, paramCallback, indent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversegeocodingApi#reversegeocode");
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
| **lat** | **Double**| The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates | |
| **lng** | **Double**| TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates. | |
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
 - **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessfully processed |  -  |
| **401** | Need auth. The API key parameter is missing or wrong, or doesn&#39;t correspond to any subscriptions |  -  |
| **403** | Unhauthorize (auth will change nothing).Your IP is not allowed. |  -  |
| **412** | Missing parameter. Some parameters required for the webservices ar missing, please consult documentation |  -  |
| **429** | Too many requests. You exceed the authorized rate |  -  |
| **500** | Internal error |  -  |

