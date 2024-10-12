# TemplateApi

All URIs are relative to *https://api.carbone.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**templatePost**](TemplateApi.md#templatePost) | **POST** /template | Upload a template. |
| [**templateTemplateIdDelete**](TemplateApi.md#templateTemplateIdDelete) | **DELETE** /template/{templateId} | Delete a template from a template ID |
| [**templateTemplateIdGet**](TemplateApi.md#templateTemplateIdGet) | **GET** /template/{templateId} | Download a template from a template ID |


<a id="templatePost"></a>
# **templatePost**
> TemplatePost200Response templatePost(carboneVersion, templatePostRequest)

Upload a template.

Documentation: https://carbone.io/api-reference.html#add-templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbone.io");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TemplateApi apiInstance = new TemplateApi(defaultClient);
    Integer carboneVersion = 4; // Integer | Carbone version
    TemplatePostRequest templatePostRequest = new TemplatePostRequest(); // TemplatePostRequest | Template File to upload, supported formats: DOCX, XLSX, PPTX, ODT, ODS, ODP, ODG, XHTML, IDML, HTML or an XML file
    try {
      TemplatePost200Response result = apiInstance.templatePost(carboneVersion, templatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplateApi#templatePost");
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
| **carboneVersion** | **Integer**| Carbone version | [default to 4] |
| **templatePostRequest** | [**TemplatePostRequest**](TemplatePostRequest.md)| Template File to upload, supported formats: DOCX, XLSX, PPTX, ODT, ODS, ODP, ODG, XHTML, IDML, HTML or an XML file | |

### Return type

[**TemplatePost200Response**](TemplatePost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On success, the &#x60;template ID&#x60; is returned. |  -  |
| **400** | The body request type is not correct, it must be a FormData or a JSON. The &#x60;Content-type&#x60; header must be either &#x60;application/json&#x60; or &#x60;multipart/form-data&#x60; |  -  |
| **401** | Unauthorized, please provide a correct API key on the &#x60;Authorization &#x60; header. The API key is available on your Carbone account: https://account.carbone.io |  -  |
| **415** | Template format not supported, it must be an XML-based document: DOCX, XLSX, PPTX, ODT, ODS, ODP, ODG, XHTML, IDML, HTML or an XML file |  -  |
| **422** | The &#x60;template&#x60; field is empty on the body request |  -  |

<a id="templateTemplateIdDelete"></a>
# **templateTemplateIdDelete**
> TemplateTemplateIdDelete200Response templateTemplateIdDelete(templateId, carboneVersion)

Delete a template from a template ID

Documentation: https://carbone.io/api-reference.html#delete-templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbone.io");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TemplateApi apiInstance = new TemplateApi(defaultClient);
    String templateId = "templateId_example"; // String | Unique identifier of the template
    Integer carboneVersion = 4; // Integer | Carbone version
    try {
      TemplateTemplateIdDelete200Response result = apiInstance.templateTemplateIdDelete(templateId, carboneVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplateApi#templateTemplateIdDelete");
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

### Return type

[**TemplateTemplateIdDelete200Response**](TemplateTemplateIdDelete200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The template is deleted |  -  |
| **400** | The &#x60;template ID&#x60; is not valid |  -  |
| **401** | Unauthorized, please provide a correct API key on the &#x60;Authorization &#x60; header. The API key is available on your Carbone account: https://account.carbone.io |  -  |
| **404** | The template is not found |  -  |

<a id="templateTemplateIdGet"></a>
# **templateTemplateIdGet**
> templateTemplateIdGet(templateId, carboneVersion)

Download a template from a template ID

Documentation: https://carbone.io/api-reference.html#get-templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbone.io");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TemplateApi apiInstance = new TemplateApi(defaultClient);
    String templateId = "templateId_example"; // String | Unique identifier of the template
    Integer carboneVersion = 4; // Integer | Carbone version
    try {
      apiInstance.templateTemplateIdGet(templateId, carboneVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplateApi#templateTemplateIdGet");
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

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | stream of the file content |  * content-disposition - Template name, for instance: &#39;filename&#x3D;\&quot;{templateid}.docx\&quot;&#39;. <br>  * content-type - File type <br>  |
| **400** | The &#x60;template ID&#x60; is not valid |  -  |
| **401** | Unauthorized, please provide a correct API key on the &#x60;Authorization &#x60; header. The API key is available on your Carbone account: https://account.carbone.io |  -  |
| **404** | The template is not found |  -  |

