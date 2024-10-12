# MeasurementFamilyApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**measurementFamiliesGetList**](MeasurementFamilyApi.md#measurementFamiliesGetList) | **GET** /api/rest/v1/measurement-families | Get list of measurement families |
| [**patchMeasurementFamilies**](MeasurementFamilyApi.md#patchMeasurementFamilies) | **PATCH** /api/rest/v1/measurement-families | Update/create several measurement families |


<a id="measurementFamiliesGetList"></a>
# **measurementFamiliesGetList**
> MeasurementFamiliesGetList200Response measurementFamiliesGetList()

Get list of measurement families

This endpoint allows you to get a list of measurement families.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MeasurementFamilyApi apiInstance = new MeasurementFamilyApi(defaultClient);
    try {
      MeasurementFamiliesGetList200Response result = apiInstance.measurementFamiliesGetList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementFamilyApi#measurementFamiliesGetList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeasurementFamiliesGetList200Response**](MeasurementFamiliesGetList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the measurement families |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="patchMeasurementFamilies"></a>
# **patchMeasurementFamilies**
> List&lt;PatchMeasurementFamilies200ResponseInner&gt; patchMeasurementFamilies(body)

Update/create several measurement families

This endpoint allows you to update and/or create several measurement families at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MeasurementFamilyApi apiInstance = new MeasurementFamilyApi(defaultClient);
    List<MeasurementFamiliesGetList200Response> body = Arrays.asList(); // List<MeasurementFamiliesGetList200Response> | 
    try {
      List<PatchMeasurementFamilies200ResponseInner> result = apiInstance.patchMeasurementFamilies(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementFamilyApi#patchMeasurementFamilies");
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
| **body** | [**List&lt;MeasurementFamiliesGetList200Response&gt;**](MeasurementFamiliesGetList200Response.md)|  | [optional] |

### Return type

[**List&lt;PatchMeasurementFamilies200ResponseInner&gt;**](PatchMeasurementFamilies200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **413** | Request Entity Too Large |  -  |
| **415** | Unsupported Media type |  -  |

