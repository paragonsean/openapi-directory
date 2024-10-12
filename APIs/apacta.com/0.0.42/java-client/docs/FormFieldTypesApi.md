# FormFieldTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**formFieldTypesFormFieldTypeIdGet**](FormFieldTypesApi.md#formFieldTypesFormFieldTypeIdGet) | **GET** /form_field_types/{form_field_type_id} | Get details about single &#x60;FormField&#x60; |
| [**formFieldTypesGet**](FormFieldTypesApi.md#formFieldTypesGet) | **GET** /form_field_types | Get list of form field types |


<a id="formFieldTypesFormFieldTypeIdGet"></a>
# **formFieldTypesFormFieldTypeIdGet**
> FormFieldTypesFormFieldTypeIdGet200Response formFieldTypesFormFieldTypeIdGet(formFieldTypeId)

Get details about single &#x60;FormField&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldTypesApi;

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

    FormFieldTypesApi apiInstance = new FormFieldTypesApi(defaultClient);
    String formFieldTypeId = "formFieldTypeId_example"; // String | 
    try {
      FormFieldTypesFormFieldTypeIdGet200Response result = apiInstance.formFieldTypesFormFieldTypeIdGet(formFieldTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldTypesApi#formFieldTypesFormFieldTypeIdGet");
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
| **formFieldTypeId** | **String**|  | |

### Return type

[**FormFieldTypesFormFieldTypeIdGet200Response**](FormFieldTypesFormFieldTypeIdGet200Response.md)

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

<a id="formFieldTypesGet"></a>
# **formFieldTypesGet**
> FormFieldTypesGet200Response formFieldTypesGet(name, identifier)

Get list of form field types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldTypesApi;

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

    FormFieldTypesApi apiInstance = new FormFieldTypesApi(defaultClient);
    String name = "name_example"; // String | Used to filter on the `name` of the form_fields
    String identifier = "identifier_example"; // String | Used to filter on the `identifier` of the form_fields
    try {
      FormFieldTypesGet200Response result = apiInstance.formFieldTypesGet(name, identifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldTypesApi#formFieldTypesGet");
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
| **name** | **String**| Used to filter on the &#x60;name&#x60; of the form_fields | [optional] |
| **identifier** | **String**| Used to filter on the &#x60;identifier&#x60; of the form_fields | [optional] |

### Return type

[**FormFieldTypesGet200Response**](FormFieldTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

