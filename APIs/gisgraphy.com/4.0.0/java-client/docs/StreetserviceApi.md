# StreetserviceApi

All URIs are relative to *http://free.gisgraphy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streetsearch**](StreetserviceApi.md#streetsearch) | **GET** /street/find | Geocode an address |


<a id="streetsearch"></a>
# **streetsearch**
> StreetSearchResultsDto streetsearch(lat, lng, radius, oneway, distance, streettype, format, from, to, paramCallback, indent)

Geocode an address

The street service allows you to search for street by GPS position. You can : Specify GPS position, Give the beginning or a part of the name of the street (useful for autocompletion), Limit search to a specific type (e.g : Pedestrian, highway, residential, ... 25 types available), Limit search to a specified radius, Limit search to one way streets,

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreetserviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://free.gisgraphy.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    StreetserviceApi apiInstance = new StreetserviceApi(defaultClient);
    Double lat = 3.4D; // Double | The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
    Double lng = 3.4D; // Double | TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
    Double radius = 10000.0D; // Double | distance from the location point in meters we'd like to search around. The value is a number > 0 if it is not specify or incorrect.
    Boolean oneway = false; // Boolean | whether the street should be a oneWay street (optional) : limit the search to the street that are one way street. If you use a checkbox in a form to indent the results, the value will be 'on' or 'off', so to simplify the use : the value for the web service can be 'true' or 'on'
    Boolean distance = true; // Boolean | Whether (or not) we want the distance field to be output. This option is useful to improve the performance if we don't care about the distance (e.g : we search for name). Of course, the results won't be sorted by distance. If you use a checkbox in a form to indent the results, the value will be 'on' or 'off', so to simplify the use : the value for the web service can be 'true' or 'on'
    String streettype = "streettype_example"; // String | filter search with a stret type
    String format = "XML"; // String | The output format.
    Integer from = 1; // Integer | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
    Integer to = 10; // Integer | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
    String paramCallback = "paramCallback_example"; // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    Boolean indent = false; // Boolean | indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    try {
      StreetSearchResultsDto result = apiInstance.streetsearch(lat, lng, radius, oneway, distance, streettype, format, from, to, paramCallback, indent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreetserviceApi#streetsearch");
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
| **radius** | **Double**| distance from the location point in meters we&#39;d like to search around. The value is a number &gt; 0 if it is not specify or incorrect. | [optional] [default to 10000.0] |
| **oneway** | **Boolean**| whether the street should be a oneWay street (optional) : limit the search to the street that are one way street. If you use a checkbox in a form to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so to simplify the use : the value for the web service can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |
| **distance** | **Boolean**| Whether (or not) we want the distance field to be output. This option is useful to improve the performance if we don&#39;t care about the distance (e.g : we search for name). Of course, the results won&#39;t be sorted by distance. If you use a checkbox in a form to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so to simplify the use : the value for the web service can be &#39;true&#39; or &#39;on&#39; | [optional] [default to true] |
| **streettype** | **String**| filter search with a stret type | [optional] |
| **format** | **String**| The output format. | [optional] [default to XML] [enum: XML, JSON, PHP, RUBY, PYTHON, YAML] |
| **from** | **Integer**| The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1 | [optional] [default to 1] |
| **to** | **Integer**| The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed) | [optional] [default to 10] |
| **paramCallback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] |
| **indent** | **Boolean**| indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |

### Return type

[**StreetSearchResultsDto**](StreetSearchResultsDto.md)

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

