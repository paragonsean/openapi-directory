# TemplatesApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRestV1TemplatesAllGet**](TemplatesApi.md#apiRestV1TemplatesAllGet) | **GET** /api/rest/v1/templates/all | all |
| [**apiRestV1TemplatesTemplateIdDelete**](TemplatesApi.md#apiRestV1TemplatesTemplateIdDelete) | **DELETE** /api/rest/v1/templates/{templateId} | delete |
| [**apiRestV1TemplatesTemplateIdGet**](TemplatesApi.md#apiRestV1TemplatesTemplateIdGet) | **GET** /api/rest/v1/templates/{templateId} | get |


<a id="apiRestV1TemplatesAllGet"></a>
# **apiRestV1TemplatesAllGet**
> WebServiceTemplates apiRestV1TemplatesAllGet()

all

Returns all templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    try {
      WebServiceTemplates result = apiInstance.apiRestV1TemplatesAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#apiRestV1TemplatesAllGet");
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

[**WebServiceTemplates**](WebServiceTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1TemplatesTemplateIdDelete"></a>
# **apiRestV1TemplatesTemplateIdDelete**
> apiRestV1TemplatesTemplateIdDelete(templateId)

delete

Deletes a  template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    Long templateId = 56L; // Long | templateId
    try {
      apiInstance.apiRestV1TemplatesTemplateIdDelete(templateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#apiRestV1TemplatesTemplateIdDelete");
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
| **templateId** | **Long**| templateId | |

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
| **200** | Description was not specified |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="apiRestV1TemplatesTemplateIdGet"></a>
# **apiRestV1TemplatesTemplateIdGet**
> WebServiceTemplate apiRestV1TemplatesTemplateIdGet(templateId)

get

Returns details for a single template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    Long templateId = 56L; // Long | templateId
    try {
      WebServiceTemplate result = apiInstance.apiRestV1TemplatesTemplateIdGet(templateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#apiRestV1TemplatesTemplateIdGet");
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
| **templateId** | **Long**| templateId | |

### Return type

[**WebServiceTemplate**](WebServiceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

