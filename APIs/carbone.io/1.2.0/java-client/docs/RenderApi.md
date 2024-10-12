# RenderApi

All URIs are relative to *https://api.carbone.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**renderRenderIdGet**](RenderApi.md#renderRenderIdGet) | **GET** /render/{renderId} | Retreive a generated document from a render ID. |
| [**renderTemplateIdPost**](RenderApi.md#renderTemplateIdPost) | **POST** /render/{templateId} | Generate a document from a template ID, and a JSON data-set |


<a id="renderRenderIdGet"></a>
# **renderRenderIdGet**
> renderRenderIdGet(renderId, carboneVersion)

Retreive a generated document from a render ID.

Documentation: https://carbone.io/api-reference.html#download-rendered-reports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RenderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbone.io");

    RenderApi apiInstance = new RenderApi(defaultClient);
    String renderId = "renderId_example"; // String | Unique identifier of the report
    Integer carboneVersion = 4; // Integer | Carbone version
    try {
      apiInstance.renderRenderIdGet(renderId, carboneVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RenderApi#renderRenderIdGet");
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
| **renderId** | **String**| Unique identifier of the report | |
| **carboneVersion** | **Integer**| Carbone version | [default to 4] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stream of the generated document |  * content-disposition - Template name, for instance: &#39;filename&#x3D;\&quot;{templateid}.docx\&quot;&#39;. <br>  * content-type - File type <br>  |
| **400** | The &#x60;render ID&#x60; is not valid |  -  |
| **401** | Unauthorized, please provide a correct API key on the &#x60;Authorization &#x60; header. The API key is available on your Carbone account: https://account.carbone.io |  -  |
| **404** | The file does not exist. |  -  |

<a id="renderTemplateIdPost"></a>
# **renderTemplateIdPost**
> RenderTemplateIdPost200Response renderTemplateIdPost(templateId, carboneVersion, renderTemplateIdPostRequest)

Generate a document from a template ID, and a JSON data-set

Documentation: https://carbone.io/api-reference.html#render-reports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RenderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbone.io");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RenderApi apiInstance = new RenderApi(defaultClient);
    String templateId = "templateId_example"; // String | Unique identifier of the template
    Integer carboneVersion = 4; // Integer | Carbone version
    RenderTemplateIdPostRequest renderTemplateIdPostRequest = new RenderTemplateIdPostRequest(); // RenderTemplateIdPostRequest | 
    try {
      RenderTemplateIdPost200Response result = apiInstance.renderTemplateIdPost(templateId, carboneVersion, renderTemplateIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RenderApi#renderTemplateIdPost");
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
| **templateId** | **String**| Unique identifier of the template | |
| **carboneVersion** | **Integer**| Carbone version | [default to 4] |
| **renderTemplateIdPostRequest** | [**RenderTemplateIdPostRequest**](RenderTemplateIdPostRequest.md)|  | |

### Return type

[**RenderTemplateIdPost200Response**](RenderTemplateIdPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On success, a &#x60;render ID&#x60; is returned, a unique identifier for the generated document. |  -  |
| **400** | The body request type is not correct, it must be a JSON type and the &#x60;Content-type&#x60; header must be &#x60;application/json&#x60; |  -  |
| **401** | Unauthorized, please provide a correct API key on the &#x60;Authorization &#x60; header. The API key is available on your Carbone account: https://account.carbone.io |  -  |
| **404** | The template is not found |  -  |
| **422** | The &#39;data&#39; property is missing on the body request. |  -  |
| **500** | Something went wrong when merging the JSON data-set into the template. The design of the template has an issue. |  -  |

