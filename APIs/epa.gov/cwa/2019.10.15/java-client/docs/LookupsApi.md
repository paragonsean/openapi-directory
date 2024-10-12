# LookupsApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**restLookupsBpTribesGet**](LookupsApi.md#restLookupsBpTribesGet) | **GET** /rest_lookups.bp_tribes | ECHO BP Tribes Lookup Service |
| [**restLookupsBpTribesPost**](LookupsApi.md#restLookupsBpTribesPost) | **POST** /rest_lookups.bp_tribes | ECHO BP Tribes Lookup Service |
| [**restLookupsCwaParametersGet**](LookupsApi.md#restLookupsCwaParametersGet) | **GET** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service |
| [**restLookupsCwaParametersPost**](LookupsApi.md#restLookupsCwaParametersPost) | **POST** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service |
| [**restLookupsCwaPollutantsGet**](LookupsApi.md#restLookupsCwaPollutantsGet) | **GET** /rest_lookups.cwa_pollutants | ECHO CWA Pollutants Lookup Service |
| [**restLookupsCwaPollutantsPost**](LookupsApi.md#restLookupsCwaPollutantsPost) | **POST** /rest_lookups.cwa_pollutants | ECHO CWA Pollutants Lookup Service |
| [**restLookupsFederalAgenciesGet**](LookupsApi.md#restLookupsFederalAgenciesGet) | **GET** /rest_lookups.federal_agencies | ECHO Federal Agency Lookup Service |
| [**restLookupsFederalAgenciesPost**](LookupsApi.md#restLookupsFederalAgenciesPost) | **POST** /rest_lookups.federal_agencies | ECHO Federal Agency Lookup Service |
| [**restLookupsIcisInspectionTypesGet**](LookupsApi.md#restLookupsIcisInspectionTypesGet) | **GET** /rest_lookups.icis_inspection_types | ECHO ICIS NPDES Inspection Types Lookup Service |
| [**restLookupsIcisInspectionTypesPost**](LookupsApi.md#restLookupsIcisInspectionTypesPost) | **POST** /rest_lookups.icis_inspection_types | ECHO ICIS NPDES Inspection Types Lookup Service |
| [**restLookupsIcisLawSectionsGet**](LookupsApi.md#restLookupsIcisLawSectionsGet) | **GET** /rest_lookups.icis_law_sections | ECHO ICIS NPDES Law Sections Lookup Service |
| [**restLookupsIcisLawSectionsPost**](LookupsApi.md#restLookupsIcisLawSectionsPost) | **POST** /rest_lookups.icis_law_sections | ECHO ICIS NPDES Law Sections Lookup Service |
| [**restLookupsNaicsCodesGet**](LookupsApi.md#restLookupsNaicsCodesGet) | **GET** /rest_lookups.naics_codes | ECHO NAICS Codes Lookup Service |
| [**restLookupsNaicsCodesPost**](LookupsApi.md#restLookupsNaicsCodesPost) | **POST** /rest_lookups.naics_codes | ECHO NAICS Codes Lookup Service |
| [**restLookupsNpdesParametersGet**](LookupsApi.md#restLookupsNpdesParametersGet) | **GET** /rest_lookups.npdes_parameters | ECHO NPDES Parameters Lookup Service |
| [**restLookupsNpdesParametersPost**](LookupsApi.md#restLookupsNpdesParametersPost) | **POST** /rest_lookups.npdes_parameters | ECHO NPDES Parameters Lookup Service |
| [**restLookupsWbdCodeLuGet**](LookupsApi.md#restLookupsWbdCodeLuGet) | **GET** /rest_lookups.wbd_code_lu | ECHO WBD Code Lookup Service |
| [**restLookupsWbdCodeLuPost**](LookupsApi.md#restLookupsWbdCodeLuPost) | **POST** /rest_lookups.wbd_code_lu | ECHO WBD Code Lookup Service |
| [**restLookupsWbdNameLuGet**](LookupsApi.md#restLookupsWbdNameLuGet) | **GET** /rest_lookups.wbd_name_lu | ECHO WBD Name Lookup Service |
| [**restLookupsWbdNameLuPost**](LookupsApi.md#restLookupsWbdNameLuPost) | **POST** /rest_lookups.wbd_name_lu | ECHO WBD Name Lookup Service |


<a id="restLookupsBpTribesGet"></a>
# **restLookupsBpTribesGet**
> RestLookupsBpTribesGet200Response restLookupsBpTribesGet(output, paramCallback, searchTerm, searchCode)

ECHO BP Tribes Lookup Service

Returns the EPA Standard Indian Tribes and Native Alaskan Villages tribal_id and tribe_name.

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
      RestLookupsBpTribesGet200Response result = apiInstance.restLookupsBpTribesGet(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsBpTribesGet");
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

[**RestLookupsBpTribesGet200Response**](RestLookupsBpTribesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of tribes containing the search term. If search term not provided, returns all values. |  -  |

<a id="restLookupsBpTribesPost"></a>
# **restLookupsBpTribesPost**
> RestLookupsBpTribesGet200Response restLookupsBpTribesPost(output, paramCallback, searchTerm, searchCode)

ECHO BP Tribes Lookup Service

Returns the EPA Standard Indian Tribes and Native Alaskan Villages tribal_id and tribe_name.

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
      RestLookupsBpTribesGet200Response result = apiInstance.restLookupsBpTribesPost(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsBpTribesPost");
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

[**RestLookupsBpTribesGet200Response**](RestLookupsBpTribesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of tribes containing the search term. If search term not provided, returns all values. |  -  |

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

<a id="restLookupsCwaPollutantsGet"></a>
# **restLookupsCwaPollutantsGet**
> RestLookupsCwaPollutantsGet200Response restLookupsCwaPollutantsGet(output, paramCallback, searchTerm, searchCode)

ECHO CWA Pollutants Lookup Service

Look up Clean Water Act pollutants by name

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
      RestLookupsCwaPollutantsGet200Response result = apiInstance.restLookupsCwaPollutantsGet(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsCwaPollutantsGet");
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

[**RestLookupsCwaPollutantsGet200Response**](RestLookupsCwaPollutantsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of water polluntants containing search term or search code. If search term or search code not provided, returns all values. |  -  |

<a id="restLookupsCwaPollutantsPost"></a>
# **restLookupsCwaPollutantsPost**
> RestLookupsCwaPollutantsGet200Response restLookupsCwaPollutantsPost(output, paramCallback, searchTerm, searchCode)

ECHO CWA Pollutants Lookup Service

Look up Clean Water Act pollutants by name

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
      RestLookupsCwaPollutantsGet200Response result = apiInstance.restLookupsCwaPollutantsPost(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsCwaPollutantsPost");
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

[**RestLookupsCwaPollutantsGet200Response**](RestLookupsCwaPollutantsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of water polluntants containing search term or search code. If search term or search code not provided, returns all values. |  -  |

<a id="restLookupsFederalAgenciesGet"></a>
# **restLookupsFederalAgenciesGet**
> RestLookupsFederalAgenciesGet200Response restLookupsFederalAgenciesGet(output, paramCallback, searchTerm, searchCode)

ECHO Federal Agency Lookup Service

Look up Federal Agency Code

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
      RestLookupsFederalAgenciesGet200Response result = apiInstance.restLookupsFederalAgenciesGet(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsFederalAgenciesGet");
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

[**RestLookupsFederalAgenciesGet200Response**](RestLookupsFederalAgenciesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of federal agency codes and their descriptions. |  -  |

<a id="restLookupsFederalAgenciesPost"></a>
# **restLookupsFederalAgenciesPost**
> RestLookupsFederalAgenciesGet200Response restLookupsFederalAgenciesPost(output, paramCallback, searchTerm, searchCode)

ECHO Federal Agency Lookup Service

Look up Federal Agency Code

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
      RestLookupsFederalAgenciesGet200Response result = apiInstance.restLookupsFederalAgenciesPost(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsFederalAgenciesPost");
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

[**RestLookupsFederalAgenciesGet200Response**](RestLookupsFederalAgenciesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of federal agency codes and their descriptions. |  -  |

<a id="restLookupsIcisInspectionTypesGet"></a>
# **restLookupsIcisInspectionTypesGet**
> RestLookupsIcisInspectionTypesGet200Response restLookupsIcisInspectionTypesGet(output, paramCallback, searchTerm, searchCode)

ECHO ICIS NPDES Inspection Types Lookup Service

Returns the ICIS NPDES Compliance Monitoring Type Code and Description.

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
      RestLookupsIcisInspectionTypesGet200Response result = apiInstance.restLookupsIcisInspectionTypesGet(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsIcisInspectionTypesGet");
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

[**RestLookupsIcisInspectionTypesGet200Response**](RestLookupsIcisInspectionTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of icis_inspection_types codes and their description. If search term or search code is  not provided, all values are returned. |  -  |

<a id="restLookupsIcisInspectionTypesPost"></a>
# **restLookupsIcisInspectionTypesPost**
> RestLookupsIcisInspectionTypesGet200Response restLookupsIcisInspectionTypesPost(output, paramCallback, searchTerm, searchCode)

ECHO ICIS NPDES Inspection Types Lookup Service

Returns the ICIS NPDES Compliance Monitoring Type Code and Description.

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
      RestLookupsIcisInspectionTypesGet200Response result = apiInstance.restLookupsIcisInspectionTypesPost(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsIcisInspectionTypesPost");
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

[**RestLookupsIcisInspectionTypesGet200Response**](RestLookupsIcisInspectionTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of icis_inspection_types codes and their description. If search term or search code is  not provided, all values are returned. |  -  |

<a id="restLookupsIcisLawSectionsGet"></a>
# **restLookupsIcisLawSectionsGet**
> RestLookupsIcisLawSectionsGet200Response restLookupsIcisLawSectionsGet(output, paramCallback, statuteCode, statusFlag, searchTerm, searchCode, sortOrder)

ECHO ICIS NPDES Law Sections Lookup Service

Returns the ICIS NPDES Law Section Descriptions.

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
    String statuteCode = "statuteCode_example"; // String | 
    String statusFlag = "statusFlag_example"; // String | 
    String searchTerm = "searchTerm_example"; // String | Enter a partial or complete search phrase or word.
    String searchCode = "searchCode_example"; // String | Enter a partial or complete code value.
    BigDecimal sortOrder = new BigDecimal(78); // BigDecimal | 
    try {
      RestLookupsIcisLawSectionsGet200Response result = apiInstance.restLookupsIcisLawSectionsGet(output, paramCallback, statuteCode, statusFlag, searchTerm, searchCode, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsIcisLawSectionsGet");
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
| **statuteCode** | **String**|  | [optional] |
| **statusFlag** | **String**|  | [optional] |
| **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] |
| **searchCode** | **String**| Enter a partial or complete code value. | [optional] |
| **sortOrder** | **BigDecimal**|  | [optional] |

### Return type

[**RestLookupsIcisLawSectionsGet200Response**](RestLookupsIcisLawSectionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of icis_inspection_types codes and their description. If search term or search code is  not provided, all values are returned. |  -  |

<a id="restLookupsIcisLawSectionsPost"></a>
# **restLookupsIcisLawSectionsPost**
> RestLookupsIcisLawSectionsGet200Response restLookupsIcisLawSectionsPost(output, paramCallback, statuteCode, statusFlag, searchTerm, searchCode, sortOrder)

ECHO ICIS NPDES Law Sections Lookup Service

Returns the ICIS NPDES Law Section Descriptions.

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
    String statuteCode = "statuteCode_example"; // String | 
    String statusFlag = "statusFlag_example"; // String | 
    String searchTerm = "searchTerm_example"; // String | Enter a partial or complete search phrase or word.
    String searchCode = "searchCode_example"; // String | Enter a partial or complete code value.
    BigDecimal sortOrder = new BigDecimal(78); // BigDecimal | 
    try {
      RestLookupsIcisLawSectionsGet200Response result = apiInstance.restLookupsIcisLawSectionsPost(output, paramCallback, statuteCode, statusFlag, searchTerm, searchCode, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsIcisLawSectionsPost");
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
| **statuteCode** | **String**|  | [optional] |
| **statusFlag** | **String**|  | [optional] |
| **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] |
| **searchCode** | **String**| Enter a partial or complete code value. | [optional] |
| **sortOrder** | **BigDecimal**|  | [optional] |

### Return type

[**RestLookupsIcisLawSectionsGet200Response**](RestLookupsIcisLawSectionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of icis_inspection_types codes and their description. If search term or search code is  not provided, all values are returned. |  -  |

<a id="restLookupsNaicsCodesGet"></a>
# **restLookupsNaicsCodesGet**
> RestLookupsNaicsCodesGet200Response restLookupsNaicsCodesGet(output, paramCallback, searchTerm, searchCode)

ECHO NAICS Codes Lookup Service

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
      RestLookupsNaicsCodesGet200Response result = apiInstance.restLookupsNaicsCodesGet(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsNaicsCodesGet");
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

[**RestLookupsNaicsCodesGet200Response**](RestLookupsNaicsCodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of NAICS codes and descriptions based on search term or search code. If search term or search code not provided, returns all values. |  -  |

<a id="restLookupsNaicsCodesPost"></a>
# **restLookupsNaicsCodesPost**
> RestLookupsNaicsCodesGet200Response restLookupsNaicsCodesPost(output, paramCallback, searchTerm, searchCode)

ECHO NAICS Codes Lookup Service

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
      RestLookupsNaicsCodesGet200Response result = apiInstance.restLookupsNaicsCodesPost(output, paramCallback, searchTerm, searchCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsNaicsCodesPost");
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

[**RestLookupsNaicsCodesGet200Response**](RestLookupsNaicsCodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of NAICS codes and descriptions based on search term or search code. If search term or search code not provided, returns all values. |  -  |

<a id="restLookupsNpdesParametersGet"></a>
# **restLookupsNpdesParametersGet**
> RestLookupsNpdesParametersGet200Response restLookupsNpdesParametersGet(output, paramCallback, searchTerm)

ECHO NPDES Parameters Lookup Service

ICIS Limit Parameter Code and Name lookup based on the supply of a partial parameter name. (NPDES &#x3D; National Pollutant Discharge Elimination System)

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
    try {
      RestLookupsNpdesParametersGet200Response result = apiInstance.restLookupsNpdesParametersGet(output, paramCallback, searchTerm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsNpdesParametersGet");
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

### Return type

[**RestLookupsNpdesParametersGet200Response**](RestLookupsNpdesParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of NPDES Parameter Codes and their description that meet the search term. If the search term is not provided, returns all values. |  -  |

<a id="restLookupsNpdesParametersPost"></a>
# **restLookupsNpdesParametersPost**
> RestLookupsNpdesParametersGet200Response restLookupsNpdesParametersPost(output, paramCallback, searchTerm)

ECHO NPDES Parameters Lookup Service

ICIS Limit Parameter Code and Name lookup based on the supply of a partial parameter name. (NPDES &#x3D; National Pollutant Discharge Elimination System)

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
    try {
      RestLookupsNpdesParametersGet200Response result = apiInstance.restLookupsNpdesParametersPost(output, paramCallback, searchTerm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsNpdesParametersPost");
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

### Return type

[**RestLookupsNpdesParametersGet200Response**](RestLookupsNpdesParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of NPDES Parameter Codes and their description that meet the search term. If the search term is not provided, returns all values. |  -  |

<a id="restLookupsWbdCodeLuGet"></a>
# **restLookupsWbdCodeLuGet**
> RestLookupsWbdCodeLuGet200Response restLookupsWbdCodeLuGet(output, paramCallback, wbdCode, wbdLevel)

ECHO WBD Code Lookup Service

USGS Watershed Boundary Dataset (WBD) Name lookup based on a supplied WBD Code and Watershed Level

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
    String wbdCode = "wbdCode_example"; // String | Two-digit watershed code [Hydrologic Unit Code (HUC)].
    String wbdLevel = "wbdLevel_example"; // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    try {
      RestLookupsWbdCodeLuGet200Response result = apiInstance.restLookupsWbdCodeLuGet(output, paramCallback, wbdCode, wbdLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsWbdCodeLuGet");
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
| **wbdCode** | **String**| Two-digit watershed code [Hydrologic Unit Code (HUC)]. | [optional] |
| **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] |

### Return type

[**RestLookupsWbdCodeLuGet200Response**](RestLookupsWbdCodeLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of WBD names and codes based on the WBD code and WBD level provided. If WBD Code not provided, returns all values. ValueCode is the WBD Code containing the number of digits provided in the WBD level. |  -  |

<a id="restLookupsWbdCodeLuPost"></a>
# **restLookupsWbdCodeLuPost**
> RestLookupsWbdCodeLuGet200Response restLookupsWbdCodeLuPost(output, paramCallback, wbdCode, wbdLevel)

ECHO WBD Code Lookup Service

USGS Watershed Boundary Dataset (WBD) Name lookup based on a supplied WBD Code and Watershed Level

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
    String wbdCode = "wbdCode_example"; // String | Two-digit watershed code [Hydrologic Unit Code (HUC)].
    String wbdLevel = "wbdLevel_example"; // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    try {
      RestLookupsWbdCodeLuGet200Response result = apiInstance.restLookupsWbdCodeLuPost(output, paramCallback, wbdCode, wbdLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsWbdCodeLuPost");
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
| **wbdCode** | **String**| Two-digit watershed code [Hydrologic Unit Code (HUC)]. | [optional] |
| **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] |

### Return type

[**RestLookupsWbdCodeLuGet200Response**](RestLookupsWbdCodeLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of WBD names and codes based on the WBD code and WBD level provided. If WBD Code not provided, returns all values. ValueCode is the WBD Code containing the number of digits provided in the WBD level. |  -  |

<a id="restLookupsWbdNameLuGet"></a>
# **restLookupsWbdNameLuGet**
> RestLookupsWbdNameLuGet200Response restLookupsWbdNameLuGet(wbdName, output, paramCallback, wbdLevel)

ECHO WBD Name Lookup Service

USGS Watershed Boundary Dataset (WBD) Code lookup based on a supplied WBD Name and Watershed Level

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
    String wbdName = "wbdName_example"; // String | Watershed Name Filter.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String wbdLevel = "wbdLevel_example"; // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    try {
      RestLookupsWbdNameLuGet200Response result = apiInstance.restLookupsWbdNameLuGet(wbdName, output, paramCallback, wbdLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsWbdNameLuGet");
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
| **wbdName** | **String**| Watershed Name Filter. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] |

### Return type

[**RestLookupsWbdNameLuGet200Response**](RestLookupsWbdNameLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of WBD names and codes based on the WBD name and WBD level provided. ValueCode is the WBD Code containing the number of digits provided in the WBD level. |  -  |

<a id="restLookupsWbdNameLuPost"></a>
# **restLookupsWbdNameLuPost**
> RestLookupsWbdNameLuGet200Response restLookupsWbdNameLuPost(wbdName, output, paramCallback, wbdLevel)

ECHO WBD Name Lookup Service

USGS Watershed Boundary Dataset (WBD) Code lookup based on a supplied WBD Name and Watershed Level

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
    String wbdName = "wbdName_example"; // String | Watershed Name Filter.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String wbdLevel = "wbdLevel_example"; // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    try {
      RestLookupsWbdNameLuGet200Response result = apiInstance.restLookupsWbdNameLuPost(wbdName, output, paramCallback, wbdLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsApi#restLookupsWbdNameLuPost");
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
| **wbdName** | **String**| Watershed Name Filter. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] |

### Return type

[**RestLookupsWbdNameLuGet200Response**](RestLookupsWbdNameLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of WBD names and codes based on the WBD name and WBD level provided. ValueCode is the WBD Code containing the number of digits provided in the WBD level. |  -  |

