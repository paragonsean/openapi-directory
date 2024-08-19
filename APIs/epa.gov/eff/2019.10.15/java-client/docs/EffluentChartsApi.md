# EffluentChartsApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**effRestServicesDownloadEffluentChartGet**](EffluentChartsApi.md#effRestServicesDownloadEffluentChartGet) | **GET** /eff_rest_services.download_effluent_chart | Effluent Charts Download Service |
| [**effRestServicesDownloadEffluentChartPost**](EffluentChartsApi.md#effRestServicesDownloadEffluentChartPost) | **POST** /eff_rest_services.download_effluent_chart | Effluent Charts Download Service |
| [**effRestServicesGetEffluentChartGet**](EffluentChartsApi.md#effRestServicesGetEffluentChartGet) | **GET** /eff_rest_services.get_effluent_chart | Detailed Effluent Chart Service |
| [**effRestServicesGetEffluentChartPost**](EffluentChartsApi.md#effRestServicesGetEffluentChartPost) | **POST** /eff_rest_services.get_effluent_chart | Detailed Effluent Chart Service |
| [**effRestServicesGetSummaryChartGet**](EffluentChartsApi.md#effRestServicesGetSummaryChartGet) | **GET** /eff_rest_services.get_summary_chart | Summary Effluent Chart Service |
| [**effRestServicesGetSummaryChartPost**](EffluentChartsApi.md#effRestServicesGetSummaryChartPost) | **POST** /eff_rest_services.get_summary_chart | Summary Effluent Chart Service |


<a id="effRestServicesDownloadEffluentChartGet"></a>
# **effRestServicesDownloadEffluentChartGet**
> File effRestServicesDownloadEffluentChartGet(pId, outfall, parameterCode, startDate, endDate)

Effluent Charts Download Service

Downloads tabular Discharge Monitoring Report (DMR) and compliance data for one NPDES permit as a CSV.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffluentChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    EffluentChartsApi apiInstance = new EffluentChartsApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String outfall = "outfall_example"; // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    String parameterCode = "parameterCode_example"; // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    String startDate = "startDate_example"; // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String endDate = "endDate_example"; // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    try {
      File result = apiInstance.effRestServicesDownloadEffluentChartGet(pId, outfall, parameterCode, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffluentChartsApi#effRestServicesDownloadEffluentChartGet");
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
| **pId** | **String**| Identifier for the service. | |
| **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] |
| **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] |
| **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with summary effluent information |  -  |

<a id="effRestServicesDownloadEffluentChartPost"></a>
# **effRestServicesDownloadEffluentChartPost**
> File effRestServicesDownloadEffluentChartPost(pId, outfall, parameterCode, startDate, endDate)

Effluent Charts Download Service

Downloads tabular Discharge Monitoring Report (DMR) and compliance data for one NPDES permit as a CSV.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffluentChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    EffluentChartsApi apiInstance = new EffluentChartsApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String outfall = "outfall_example"; // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    String parameterCode = "parameterCode_example"; // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    String startDate = "startDate_example"; // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String endDate = "endDate_example"; // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    try {
      File result = apiInstance.effRestServicesDownloadEffluentChartPost(pId, outfall, parameterCode, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffluentChartsApi#effRestServicesDownloadEffluentChartPost");
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
| **pId** | **String**| Identifier for the service. | |
| **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] |
| **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] |
| **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with summary effluent information |  -  |

<a id="effRestServicesGetEffluentChartGet"></a>
# **effRestServicesGetEffluentChartGet**
> EffRestServicesGetEffluentChartGet200Response effRestServicesGetEffluentChartGet(pId, outfall, parameterCode, startDate, endDate, output, paramCallback)

Detailed Effluent Chart Service

Discharge Monitoring Report (DMR) data supporting each effluent chart for one NPDES permit. Includes Discharge Monitoring Reports and NPDES Violations.   

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffluentChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    EffluentChartsApi apiInstance = new EffluentChartsApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String outfall = "outfall_example"; // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    String parameterCode = "parameterCode_example"; // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    String startDate = "startDate_example"; // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String endDate = "endDate_example"; // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      EffRestServicesGetEffluentChartGet200Response result = apiInstance.effRestServicesGetEffluentChartGet(pId, outfall, parameterCode, startDate, endDate, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffluentChartsApi#effRestServicesGetEffluentChartGet");
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
| **pId** | **String**| Identifier for the service. | |
| **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] |
| **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] |
| **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**EffRestServicesGetEffluentChartGet200Response**](EffRestServicesGetEffluentChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with detailed effluent information |  -  |

<a id="effRestServicesGetEffluentChartPost"></a>
# **effRestServicesGetEffluentChartPost**
> EffRestServicesGetEffluentChartGet200Response effRestServicesGetEffluentChartPost(pId, outfall, parameterCode, startDate, endDate, output, paramCallback)

Detailed Effluent Chart Service

Discharge Monitoring Report (DMR) data supporting each effluent chart for one NPDES permit. Includes Discharge Monitoring Reports and NPDES Violations.   

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffluentChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    EffluentChartsApi apiInstance = new EffluentChartsApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String outfall = "outfall_example"; // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    String parameterCode = "parameterCode_example"; // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    String startDate = "startDate_example"; // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String endDate = "endDate_example"; // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      EffRestServicesGetEffluentChartGet200Response result = apiInstance.effRestServicesGetEffluentChartPost(pId, outfall, parameterCode, startDate, endDate, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffluentChartsApi#effRestServicesGetEffluentChartPost");
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
| **pId** | **String**| Identifier for the service. | |
| **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] |
| **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] |
| **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**EffRestServicesGetEffluentChartGet200Response**](EffRestServicesGetEffluentChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with detailed effluent information |  -  |

<a id="effRestServicesGetSummaryChartGet"></a>
# **effRestServicesGetSummaryChartGet**
> EffRestServicesGetSummaryChartGet200Response effRestServicesGetSummaryChartGet(pId, output, paramCallback, startDate, endDate)

Summary Effluent Chart Service

Summary of compliance status each outfall and parameter for one NPDES permit. Provides the current compliance status and overall compliance status for the date range of interest. This service supports the Summary Matrix on the Effluent Charts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffluentChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    EffluentChartsApi apiInstance = new EffluentChartsApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String startDate = "startDate_example"; // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String endDate = "endDate_example"; // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    try {
      EffRestServicesGetSummaryChartGet200Response result = apiInstance.effRestServicesGetSummaryChartGet(pId, output, paramCallback, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffluentChartsApi#effRestServicesGetSummaryChartGet");
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
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |

### Return type

[**EffRestServicesGetSummaryChartGet200Response**](EffRestServicesGetSummaryChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with summary effluent information |  -  |

<a id="effRestServicesGetSummaryChartPost"></a>
# **effRestServicesGetSummaryChartPost**
> EffRestServicesGetSummaryChartGet200Response effRestServicesGetSummaryChartPost(pId, output, paramCallback, startDate, endDate)

Summary Effluent Chart Service

Summary of compliance status each outfall and parameter for one NPDES permit. Provides the current compliance status and overall compliance status for the date range of interest. This service supports the Summary Matrix on the Effluent Charts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffluentChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    EffluentChartsApi apiInstance = new EffluentChartsApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String startDate = "startDate_example"; // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    String endDate = "endDate_example"; // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    try {
      EffRestServicesGetSummaryChartGet200Response result = apiInstance.effRestServicesGetSummaryChartPost(pId, output, paramCallback, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffluentChartsApi#effRestServicesGetSummaryChartPost");
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
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |
| **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] |

### Return type

[**EffRestServicesGetSummaryChartGet200Response**](EffRestServicesGetSummaryChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with summary effluent information |  -  |

