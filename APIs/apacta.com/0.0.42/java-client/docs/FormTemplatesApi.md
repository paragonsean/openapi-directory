# FormTemplatesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**formTemplatesFormTemplateIdGet**](FormTemplatesApi.md#formTemplatesFormTemplateIdGet) | **GET** /form_templates/{form_template_id} | View one form template |
| [**formTemplatesGet**](FormTemplatesApi.md#formTemplatesGet) | **GET** /form_templates | Get array of form_templates for your company |


<a id="formTemplatesFormTemplateIdGet"></a>
# **formTemplatesFormTemplateIdGet**
> FormTemplatesFormTemplateIdGet200Response formTemplatesFormTemplateIdGet(formTemplateId)

View one form template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FormTemplatesApi apiInstance = new FormTemplatesApi(defaultClient);
    String formTemplateId = "formTemplateId_example"; // String | 
    try {
      FormTemplatesFormTemplateIdGet200Response result = apiInstance.formTemplatesFormTemplateIdGet(formTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormTemplatesApi#formTemplatesFormTemplateIdGet");
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
| **formTemplateId** | **String**|  | |

### Return type

[**FormTemplatesFormTemplateIdGet200Response**](FormTemplatesFormTemplateIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="formTemplatesGet"></a>
# **formTemplatesGet**
> FormTemplatesGet200Response formTemplatesGet(name, identifier, pdfTemplateIdentifier, description)

Get array of form_templates for your company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FormTemplatesApi apiInstance = new FormTemplatesApi(defaultClient);
    String name = "name_example"; // String | Used to filter on the `name` of the form_templates
    String identifier = "identifier_example"; // String | Used to filter on the `identifier` of the form_templates
    String pdfTemplateIdentifier = "pdfTemplateIdentifier_example"; // String | Used to filter on the `pdf_template_identifier` of the form_templates
    String description = "description_example"; // String | Used to filter on the `description` of the form_templates
    try {
      FormTemplatesGet200Response result = apiInstance.formTemplatesGet(name, identifier, pdfTemplateIdentifier, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormTemplatesApi#formTemplatesGet");
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
| **name** | **String**| Used to filter on the &#x60;name&#x60; of the form_templates | [optional] |
| **identifier** | **String**| Used to filter on the &#x60;identifier&#x60; of the form_templates | [optional] |
| **pdfTemplateIdentifier** | **String**| Used to filter on the &#x60;pdf_template_identifier&#x60; of the form_templates | [optional] |
| **description** | **String**| Used to filter on the &#x60;description&#x60; of the form_templates | [optional] |

### Return type

[**FormTemplatesGet200Response**](FormTemplatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

