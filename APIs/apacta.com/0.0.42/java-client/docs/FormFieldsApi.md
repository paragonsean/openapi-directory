# FormFieldsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**formFieldsFormFieldIdGet**](FormFieldsApi.md#formFieldsFormFieldIdGet) | **GET** /form_fields/{form_field_id} | Get details about single &#x60;FormField&#x60; |
| [**formFieldsPost**](FormFieldsApi.md#formFieldsPost) | **POST** /form_fields | Add a new field to a &#x60;Form&#x60; |


<a id="formFieldsFormFieldIdGet"></a>
# **formFieldsFormFieldIdGet**
> FormFieldsFormFieldIdGet200Response formFieldsFormFieldIdGet(formFieldId)

Get details about single &#x60;FormField&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldsApi;

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

    FormFieldsApi apiInstance = new FormFieldsApi(defaultClient);
    String formFieldId = "formFieldId_example"; // String | 
    try {
      FormFieldsFormFieldIdGet200Response result = apiInstance.formFieldsFormFieldIdGet(formFieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldsApi#formFieldsFormFieldIdGet");
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
| **formFieldId** | **String**|  | |

### Return type

[**FormFieldsFormFieldIdGet200Response**](FormFieldsFormFieldIdGet200Response.md)

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

<a id="formFieldsPost"></a>
# **formFieldsPost**
> ClockingRecordsPost201Response formFieldsPost(formFieldsPostRequest)

Add a new field to a &#x60;Form&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldsApi;

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

    FormFieldsApi apiInstance = new FormFieldsApi(defaultClient);
    FormFieldsPostRequest formFieldsPostRequest = new FormFieldsPostRequest(); // FormFieldsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.formFieldsPost(formFieldsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldsApi#formFieldsPost");
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
| **formFieldsPostRequest** | [**FormFieldsPostRequest**](FormFieldsPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully added field |  -  |
| **422** | Validation error |  -  |

