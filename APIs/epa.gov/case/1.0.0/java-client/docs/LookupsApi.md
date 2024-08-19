# LookupsApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**restLookupsIcisLawSectionsGet**](LookupsApi.md#restLookupsIcisLawSectionsGet) | **GET** /rest_lookups.icis_law_sections | ECHO ICIS Law Sections Lookup Service |
| [**restLookupsIcisLawSectionsPost**](LookupsApi.md#restLookupsIcisLawSectionsPost) | **POST** /rest_lookups.icis_law_sections | ECHO ICIS Law Sections Lookup Service |


<a id="restLookupsIcisLawSectionsGet"></a>
# **restLookupsIcisLawSectionsGet**
> RestLookupsIcisLawSectionsGet200Response restLookupsIcisLawSectionsGet(output, paramCallback, statuteCode, statusFlag, searchTerm, searchCode, sortOrder)

ECHO ICIS Law Sections Lookup Service

Returns the ICIS Law Section Descriptions.

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

ECHO ICIS Law Sections Lookup Service

Returns the ICIS Law Section Descriptions.

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

