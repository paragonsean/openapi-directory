# ProvincesApi

All URIs are relative to *https://canada-holidays.ca*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**province**](ProvincesApi.md#province) | **GET** /api/v1/provinces/{provinceId} | Get a province or territory by abbreviation |
| [**provinces**](ProvincesApi.md#provinces) | **GET** /api/v1/provinces | Get all provinces |


<a id="province"></a>
# **province**
> Province200Response province(provinceId, year, optional)

Get a province or territory by abbreviation

Returns a Canadian province or territory with its associated holidays. Returns a 404 response for invalid abbreviations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvincesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://canada-holidays.ca");

    ProvincesApi apiInstance = new ProvincesApi(defaultClient);
    String provinceId = "AB"; // String | A Canadian province abbreviation
    Integer year = 2023; // Integer | A calendar year
    String optional = "1"; // String | A boolean parameter (AB and BC only). If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
    try {
      Province200Response result = apiInstance.province(provinceId, year, optional);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvincesApi#province");
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
| **provinceId** | **String**| A Canadian province abbreviation | [enum: AB, BC, MB, NB, NL, NS, NT, NU, true, PE, QC, SK, YT] |
| **year** | **Integer**| A calendar year | [optional] [default to 2023] |
| **optional** | **String**| A boolean parameter (AB and BC only). If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC. | [optional] [default to false] [enum: 1, 0, true, false] |

### Return type

[**Province200Response**](Province200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="provinces"></a>
# **provinces**
> Provinces200Response provinces(year, optional)

Get all provinces

Returns provinces and territories in Canada. Each province or territory lists its associated holidays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvincesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://canada-holidays.ca");

    ProvincesApi apiInstance = new ProvincesApi(defaultClient);
    Integer year = 2023; // Integer | A calendar year
    String optional = "1"; // String | A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
    try {
      Provinces200Response result = apiInstance.provinces(year, optional);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvincesApi#provinces");
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
| **year** | **Integer**| A calendar year | [optional] [default to 2023] |
| **optional** | **String**| A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC. | [optional] [default to false] [enum: 1, 0, true, false] |

### Return type

[**Provinces200Response**](Provinces200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

