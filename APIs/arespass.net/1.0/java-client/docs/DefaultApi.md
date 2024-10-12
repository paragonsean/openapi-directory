# DefaultApi

All URIs are relative to *http://arespass.net/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aboutGet**](DefaultApi.md#aboutGet) | **GET** /about | Metadata about this API&amp;#58; version number, release date and available languages.  Metadata requests are NOT billed.  |
| [**ecGet**](DefaultApi.md#ecGet) | **GET** /ec | The entropy calculator - alias ec -, analyzes a password and calculates its entropy.  Entropy calculator requests are billed.  |


<a id="aboutGet"></a>
# **aboutGet**
> About aboutGet(outputFormat)

Metadata about this API&amp;#58; version number, release date and available languages.  Metadata requests are NOT billed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://arespass.net/v1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String outputFormat = "outputFormat_example"; // String | **The format of the returned metadata.**  Allowed values are *json*, *xml* and *yaml*.  The default value is *xml*. 
    try {
      About result = apiInstance.aboutGet(outputFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#aboutGet");
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
| **outputFormat** | **String**| **The format of the returned metadata.**  Allowed values are *json*, *xml* and *yaml*.  The default value is *xml*.  | [optional] |

### Return type

[**About**](About.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | **The metadata about this API&amp;#58; version number, release date and available languages.**  |  -  |
| **400** | **At least one error was found in the request parameters.**  |  -  |
| **405** | **HTTP method POST is not allowed.**  |  -  |
| **500** | **Unexpected server error.**                  |  -  |

<a id="ecGet"></a>
# **ecGet**
> Ec ecGet(password, outputFormat, penalty, reqId)

The entropy calculator - alias ec -, analyzes a password and calculates its entropy.  Entropy calculator requests are billed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://arespass.net/v1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String password = "password_example"; // String | **The password to be analyzed.**  Minimum length is 4 characters; maximum length is 128 characters.  Beware that certain characters like '&#35;', '&#61;' or '&#63;' must be properly encoded.  For more information about this issue, please refer to RFC 3986 (\"*Uniform Resource Identifier (URI): Generic Syntax*\"), sections 2.1, 2.2 and 2.4. 
    String outputFormat = "outputFormat_example"; // String | **The format of the returned analysis.**  Allowed values are *json*, *xml* and *yaml*.  The default value is *xml*. 
    BigDecimal penalty = new BigDecimal(78); // BigDecimal | **The penalty applied to each character that is part of a word, number sequence, alphabet sequence, etc.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  The character used as decimal separator is always '&#46;'. Hence, a parameter value like *0,33* would be illegal.  The default value is *0.25*. 
    String reqId = "reqId_example"; // String | **An identifier for this request.**  The request identifier is a string that must match the regular expression *_/(?i)^[a-z0-9]{8,16}$/_*.  This identifier is echoed in the returned response. Its value has no effect on the password analysis.  If this parameter is unset, a randomly generated identifier will be automatically assigned to this request. 
    try {
      Ec result = apiInstance.ecGet(password, outputFormat, penalty, reqId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ecGet");
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
| **password** | **String**| **The password to be analyzed.**  Minimum length is 4 characters; maximum length is 128 characters.  Beware that certain characters like &#39;&amp;#35;&#39;, &#39;&amp;#61;&#39; or &#39;&amp;#63;&#39; must be properly encoded.  For more information about this issue, please refer to RFC 3986 (\&quot;*Uniform Resource Identifier (URI): Generic Syntax*\&quot;), sections 2.1, 2.2 and 2.4.  | |
| **outputFormat** | **String**| **The format of the returned analysis.**  Allowed values are *json*, *xml* and *yaml*.  The default value is *xml*.  | [optional] |
| **penalty** | **BigDecimal**| **The penalty applied to each character that is part of a word, number sequence, alphabet sequence, etc.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  The character used as decimal separator is always &#39;&amp;#46;&#39;. Hence, a parameter value like *0,33* would be illegal.  The default value is *0.25*.  | [optional] |
| **reqId** | **String**| **An identifier for this request.**  The request identifier is a string that must match the regular expression *_/(?i)^[a-z0-9]{8,16}$/_*.  This identifier is echoed in the returned response. Its value has no effect on the password analysis.  If this parameter is unset, a randomly generated identifier will be automatically assigned to this request.  | [optional] |

### Return type

[**Ec**](Ec.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The password analysis, including the calculated entropy. |  -  |
| **400** | **At least one error was found in the request parameters.**  |  -  |
| **405** | **HTTP method POST is not allowed.**  |  -  |
| **500** | **Unexpected server error.**  |  -  |

