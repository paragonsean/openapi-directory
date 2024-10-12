# GroundhogsApi

All URIs are relative to *https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groundhog**](GroundhogsApi.md#groundhog) | **GET** /api/v1/groundhogs/{slug} | Get a groundhog by slug |
| [**groundhogs**](GroundhogsApi.md#groundhogs) | **GET** /api/v1/groundhogs | Get all groundhogs |


<a id="groundhog"></a>
# **groundhog**
> Groundhog200Response groundhog(slug)

Get a groundhog by slug

Returns a prognosticating animal and its known predictions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroundhogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1");

    GroundhogsApi apiInstance = new GroundhogsApi(defaultClient);
    String slug = "slug_example"; // String | Groundhog name in kebab-case: (eg, lucy-the-lobster)
    try {
      Groundhog200Response result = apiInstance.groundhog(slug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroundhogsApi#groundhog");
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
| **slug** | **String**| Groundhog name in kebab-case: (eg, lucy-the-lobster) | |

### Return type

[**Groundhog200Response**](Groundhog200Response.md)

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

<a id="groundhogs"></a>
# **groundhogs**
> Groundhogs200Response groundhogs(country, isGroundhog)

Get all groundhogs

Returns all prognosticating animals with their known predictions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroundhogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1");

    GroundhogsApi apiInstance = new GroundhogsApi(defaultClient);
    String country = "Canada or USA"; // String | Filter groundhogs by country of origin (USA or Canada).
    String isGroundhog = "1"; // String | Filter groundhogs by type (actual, alive groundhogs, or other prognosticators)
    try {
      Groundhogs200Response result = apiInstance.groundhogs(country, isGroundhog);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroundhogsApi#groundhogs");
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
| **country** | **String**| Filter groundhogs by country of origin (USA or Canada). | [optional] |
| **isGroundhog** | **String**| Filter groundhogs by type (actual, alive groundhogs, or other prognosticators) | [optional] [enum: 1, 0, true, false] |

### Return type

[**Groundhogs200Response**](Groundhogs200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

