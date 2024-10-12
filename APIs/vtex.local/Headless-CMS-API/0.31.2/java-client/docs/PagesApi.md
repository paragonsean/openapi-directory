# PagesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllContentTypes**](PagesApi.md#getAllContentTypes) | **GET** /_v/cms/api/{builderId}/ | Get all Content Types |
| [**getCMSpage**](PagesApi.md#getCMSpage) | **GET** /_v/cms/api/{builderId}/{content-type}/{document-id}/ | Get CMS page |
| [**getPagesbyContentType**](PagesApi.md#getPagesbyContentType) | **GET** /_v/cms/api/{builderId}/{content-type} | Get all CMS pages by Content Type |


<a id="getAllContentTypes"></a>
# **getAllContentTypes**
> GetAllContentTypes200Response getAllContentTypes(builderId)

Get all Content Types

Gets data from all Content Types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String builderId = "faststore"; // String | Builder ID specified in the settings of the CMS app.
    try {
      GetAllContentTypes200Response result = apiInstance.getAllContentTypes(builderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#getAllContentTypes");
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
| **builderId** | **String**| Builder ID specified in the settings of the CMS app. | |

### Return type

[**GetAllContentTypes200Response**](GetAllContentTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCMSpage"></a>
# **getCMSpage**
> GetCMSpage200Response getCMSpage(builderId, contentType, documentId, versionId, releaseId)

Get CMS page

Gets all data from a given page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String builderId = "faststore"; // String | Builder ID specified in the settings of the CMS app.
    String contentType = "plp"; // String | Content Type ID defined in the FastStore project.
    String documentId = "5af643b5-9a6d-48f2-9b34-919dd762c908"; // String | Document ID presented in the URL path of a CMS preview.
    String versionId = "e7263fc8-bc68-4052-9e25-dd5a2572d3bb"; // String | Version ID presented in the URL path of a CMS preview.
    String releaseId = "6196c277c6dce15f9709a2a7"; // String | Release ID presented in the URL path of a CMS preview.
    try {
      GetCMSpage200Response result = apiInstance.getCMSpage(builderId, contentType, documentId, versionId, releaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#getCMSpage");
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
| **builderId** | **String**| Builder ID specified in the settings of the CMS app. | |
| **contentType** | **String**| Content Type ID defined in the FastStore project. | |
| **documentId** | **String**| Document ID presented in the URL path of a CMS preview. | |
| **versionId** | **String**| Version ID presented in the URL path of a CMS preview. | [optional] |
| **releaseId** | **String**| Release ID presented in the URL path of a CMS preview. | [optional] |

### Return type

[**GetCMSpage200Response**](GetCMSpage200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPagesbyContentType"></a>
# **getPagesbyContentType**
> GetPagesbyContentType200Response getPagesbyContentType(builderId, contentType, versionId, releaseId, filtersLeftCurlyBracketFieldRightCurlyBracket)

Get all CMS pages by Content Type

Gets data from all pages of a given Content Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String builderId = "faststore"; // String | Builder ID specified in the settings of the CMS app.
    String contentType = "plp"; // String | Content Type identifier defined in the FastStore project.
    String versionId = "e7263fc8-bc68-4052-9e25-dd5a2572d3bb"; // String | Version ID presented in the URL path of a CMS preview.
    String releaseId = "6196c277c6dce15f9709a2a7"; // String | Release ID presented in the URL path of a CMS preview.
    String filtersLeftCurlyBracketFieldRightCurlyBracket = "published"; // String | Filter results by a property of the page (e.g., `filters[status]`) or by a nested custom field of the `parameters` object (e.g., `filters[parameters.collection.sort]`). *Replace {field} with the desired property.*
    try {
      GetPagesbyContentType200Response result = apiInstance.getPagesbyContentType(builderId, contentType, versionId, releaseId, filtersLeftCurlyBracketFieldRightCurlyBracket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#getPagesbyContentType");
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
| **builderId** | **String**| Builder ID specified in the settings of the CMS app. | |
| **contentType** | **String**| Content Type identifier defined in the FastStore project. | |
| **versionId** | **String**| Version ID presented in the URL path of a CMS preview. | [optional] |
| **releaseId** | **String**| Release ID presented in the URL path of a CMS preview. | [optional] |
| **filtersLeftCurlyBracketFieldRightCurlyBracket** | **String**| Filter results by a property of the page (e.g., &#x60;filters[status]&#x60;) or by a nested custom field of the &#x60;parameters&#x60; object (e.g., &#x60;filters[parameters.collection.sort]&#x60;). *Replace {field} with the desired property.* | [optional] |

### Return type

[**GetPagesbyContentType200Response**](GetPagesbyContentType200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

