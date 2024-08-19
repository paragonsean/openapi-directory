# LookupsApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**restLookupsCwaParametersGet**](LookupsApi.md#restLookupsCwaParametersGet) | **GET** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service |
| [**restLookupsCwaParametersPost**](LookupsApi.md#restLookupsCwaParametersPost) | **POST** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service |


<a id="restLookupsCwaParametersGet"></a>
# **restLookupsCwaParametersGet**
> RestLookupsCwaParametersGet200Response restLookupsCwaParametersGet(output, paramCallback, searchTerm, searchCode)

ECHO CWA Parameter Lookup Service

Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    LookupsApi apiInstance = new LookupsApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String searchTerm = "searchTerm_example"; // String | Enter a partial or complete search phrase or word.
    String searchCode = "searchCode_example"; // String | Enter a partial or complete code value.
    try {
      RestLookupsCwaParametersGet200Response result = apiInstance.restLookupsCwaParametersGet(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsCwaParametersGet");
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
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] |
| **searchCode** | **String**| Enter a partial or complete code value. | [optional] |

### Return type

[**RestLookupsCwaParametersGet200Response**](RestLookupsCwaParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of parameter codes and descriptions that contain the search_term or search_code entered. If search term or search code not provided, returns all values. ValueCode is the 5-digit parameter code. ValueDescription is the parameter description. |  -  |

<a id="restLookupsCwaParametersPost"></a>
# **restLookupsCwaParametersPost**
> RestLookupsCwaParametersGet200Response restLookupsCwaParametersPost(output, paramCallback, searchTerm, searchCode)

ECHO CWA Parameter Lookup Service

Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    LookupsApi apiInstance = new LookupsApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String searchTerm = "searchTerm_example"; // String | Enter a partial or complete search phrase or word.
    String searchCode = "searchCode_example"; // String | Enter a partial or complete code value.
    try {
      RestLookupsCwaParametersGet200Response result = apiInstance.restLookupsCwaParametersPost(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsCwaParametersPost");
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
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] |
| **searchCode** | **String**| Enter a partial or complete code value. | [optional] |

### Return type

[**RestLookupsCwaParametersGet200Response**](RestLookupsCwaParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of parameter codes and descriptions that contain the search_term or search_code entered. If search term or search code not provided, returns all values. ValueCode is the 5-digit parameter code. ValueDescription is the parameter description. |  -  |

