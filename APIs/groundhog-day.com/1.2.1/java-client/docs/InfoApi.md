# InfoApi

All URIs are relative to *https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**root**](InfoApi.md#root) | **GET** /api/v1 | Root |
| [**spec**](InfoApi.md#spec) | **GET** /api/v1/spec | Get JSON schema |


<a id="root"></a>
# **root**
> Root200Response root()

Root

Returns a welcome message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      Root200Response result = apiInstance.root();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#root");
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

[**Root200Response**](Root200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="spec"></a>
# **spec**
> spec()

Get JSON schema

Gets the schema for the JSON API as a yaml file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      apiInstance.spec();
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#spec");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * content-disposition - attachment; filename&#x3D;\&quot;Groundhog-Day-API.v1.yaml\&quot; <br>  * content-type - text/yaml; charset&#x3D;UTF-8 <br>  |

