# MeasureFamilyApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**measureFamiliesGet**](MeasureFamilyApi.md#measureFamiliesGet) | **GET** /api/rest/v1/measure-families/{code} | Get a measure family |
| [**measureFamiliesGetList**](MeasureFamilyApi.md#measureFamiliesGetList) | **GET** /api/rest/v1/measure-families | Get list of measure familiy |


<a id="measureFamiliesGet"></a>
# **measureFamiliesGet**
> MeasureFamiliesGet200Response measureFamiliesGet(code)

Get a measure family

This endpoint allows you to get the information about a given measure family.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasureFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MeasureFamilyApi apiInstance = new MeasureFamilyApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      MeasureFamiliesGet200Response result = apiInstance.measureFamiliesGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasureFamilyApi#measureFamiliesGet");
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
| **code** | **String**| Code of the resource | |

### Return type

[**MeasureFamiliesGet200Response**](MeasureFamiliesGet200Response.md)

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
| **403** | Access forbidden |  -  |
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="measureFamiliesGetList"></a>
# **measureFamiliesGetList**
> MeasureFamilies measureFamiliesGetList()

Get list of measure familiy

This endpoint allows you to get a list of measure families. Measure families are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasureFamilyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MeasureFamilyApi apiInstance = new MeasureFamilyApi(defaultClient);
    try {
      MeasureFamilies result = apiInstance.measureFamiliesGetList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasureFamilyApi#measureFamiliesGetList");
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

[**MeasureFamilies**](MeasureFamilies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return measure families paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

