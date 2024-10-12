# ValidationApi

All URIs are relative to *https://mermade.org.uk/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBadge**](ValidationApi.md#getBadge) | **GET** /badge | Return a redirect to a badge svg file depending on a source definition&#39;s validity |
| [**validate**](ValidationApi.md#validate) | **POST** /validate | Validate an OpenAPI 3.0.x definition supplied in the body of the request |
| [**validateUrl**](ValidationApi.md#validateUrl) | **GET** /validate | Validate an OpenAPI 3.0.x definition |


<a id="getBadge"></a>
# **getBadge**
> getBadge(url)

Return a redirect to a badge svg file depending on a source definition&#39;s validity



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mermade.org.uk/api/v1");

    ValidationApi apiInstance = new ValidationApi(defaultClient);
    URI url = new URI(); // URI | The URL to retrieve the OpenAPI 3.0.x definition from
    try {
      apiInstance.getBadge(url);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationApi#getBadge");
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
| **url** | **URI**| The URL to retrieve the OpenAPI 3.0.x definition from | |

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
| **301** | Moved |  -  |

<a id="validate"></a>
# **validate**
> ValidationResult validate(filename, source)

Validate an OpenAPI 3.0.x definition supplied in the body of the request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mermade.org.uk/api/v1");

    ValidationApi apiInstance = new ValidationApi(defaultClient);
    String filename = "filename_example"; // String | The file to upload and validate
    String source = "source_example"; // String | The text of an OpenAPI 3.0.x definition to validate
    try {
      ValidationResult result = apiInstance.validate(filename, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationApi#validate");
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
| **filename** | **String**| The file to upload and validate | [optional] |
| **source** | **String**| The text of an OpenAPI 3.0.x definition to validate | [optional] |

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default |  -  |
| **400** | Invalid request |  -  |

<a id="validateUrl"></a>
# **validateUrl**
> ValidationResult validateUrl(url)

Validate an OpenAPI 3.0.x definition



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mermade.org.uk/api/v1");

    ValidationApi apiInstance = new ValidationApi(defaultClient);
    URI url = new URI(); // URI | The URL to retrieve the OpenAPI 3.0.x definition from
    try {
      ValidationResult result = apiInstance.validateUrl(url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationApi#validateUrl");
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
| **url** | **URI**| The URL to retrieve the OpenAPI 3.0.x definition from | |

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default |  -  |

