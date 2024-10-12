# PdfApi

All URIs are relative to *https://api.truora.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPDF**](PdfApi.md#createPDF) | **POST** /v1/checks/{check_id}/pdf | Create PDF |
| [**getPDF**](PdfApi.md#getPDF) | **GET** /v1/checks/{check_id}/pdf | Get PDF |


<a id="createPDF"></a>
# **createPDF**
> createPDF(checkId)

Create PDF

Creates a PDF containing the background check results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    PdfApi apiInstance = new PdfApi(defaultClient);
    String checkId = "checkId_example"; // String | ID of the check
    try {
      apiInstance.createPDF(checkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#createPDF");
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
| **checkId** | **String**| ID of the check | |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Outputs the link to download the PDF |  -  |
| **404** | This can happen if the check ID doesn&#39;t exist. |  -  |

<a id="getPDF"></a>
# **getPDF**
> getPDF(checkId, lang)

Get PDF

Downloads the PDF in the specified language, Spanish by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    PdfApi apiInstance = new PdfApi(defaultClient);
    String checkId = "checkId_example"; // String | ID of the check
    String lang = "lang_example"; // String | Used to specify the language for the PDF, if not specified the PDF will be downloaded in Spanish.
    try {
      apiInstance.getPDF(checkId, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#getPDF");
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
| **checkId** | **String**| ID of the check | |
| **lang** | **String**| Used to specify the language for the PDF, if not specified the PDF will be downloaded in Spanish. | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: PDF, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Downloads the PDF of the check |  -  |
| **404** | This can happen if the create pdf request has not been finished. |  -  |

