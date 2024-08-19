# MetadataApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rcraRestServicesMetadataGet**](MetadataApi.md#rcraRestServicesMetadataGet) | **GET** /rcra_rest_services.metadata | Resource Conservation and Recovery Act (RCRA) Metadata Service |
| [**rcraRestServicesMetadataPost**](MetadataApi.md#rcraRestServicesMetadataPost) | **POST** /rcra_rest_services.metadata | Resource Conservation and Recovery Act (RCRA) Metadata Service |


<a id="rcraRestServicesMetadataGet"></a>
# **rcraRestServicesMetadataGet**
> RcraRestServicesMetadataGet200Response rcraRestServicesMetadataGet(output, paramCallback)

Resource Conservation and Recovery Act (RCRA) Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_qid, get_facility_info and other service endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      RcraRestServicesMetadataGet200Response result = apiInstance.rcraRestServicesMetadataGet(output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#rcraRestServicesMetadataGet");
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

### Return type

[**RcraRestServicesMetadataGet200Response**](RcraRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array of columns/objects. |  -  |

<a id="rcraRestServicesMetadataPost"></a>
# **rcraRestServicesMetadataPost**
> RcraRestServicesMetadataGet200Response rcraRestServicesMetadataPost(output, paramCallback)

Resource Conservation and Recovery Act (RCRA) Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_qid, get_facility_info and other service endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      RcraRestServicesMetadataGet200Response result = apiInstance.rcraRestServicesMetadataPost(output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#rcraRestServicesMetadataPost");
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

### Return type

[**RcraRestServicesMetadataGet200Response**](RcraRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array of columns/objects. |  -  |

